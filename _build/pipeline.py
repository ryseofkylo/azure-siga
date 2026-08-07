# -*- coding: utf-8 -*-
"""
Pipeline determinista e idempotente: catalogo SIGA -> vault Obsidian.
FASE 0 (clasificacion) + 1a (relaciones) + 1b (reglas) + 2 (notas).
Escribe SOLO en el vault Azure.
"""
import json, re, os, collections, glob, sys, io

SRC   = r"C:\Users\Matias\Documents\catalogo siga"
VAULT = r"C:\Users\Matias\Documents\azure\azure"

CAT   = os.path.join(SRC, "01_catalogo")
PROF_T= os.path.join(SRC, "02_perfiles", "tablas")
PROF_V= os.path.join(SRC, "02_perfiles", "vistas")
DEFS  = os.path.join(SRC, "05_definiciones_vistas")

# ---------------------------------------------------------------- carga base
def load_objs():
    return [json.loads(l) for l in open(os.path.join(CAT,"tablas.jsonl"),encoding="utf-8")]

def key(o): return f"{o['esquema']}.{o['tabla']}"

# ---------------------------------------------------------------- clasificacion
RX_BACKUP = re.compile(r'(_BKP|_BACKUP|\bBACKUP\b|\bRespaldo)', re.I)
RX_PRUEBA = re.compile(r'(_PRUEBA|\bPRUEBA_|\bPRUEBA\b|Analytics_prueba)', re.I)
RX_MISC   = re.compile(r'(_PyCG|_CONVERT|_VIEJO\b|_VIEJA\b|_test\b|\bCONTRATO_TEST\b|_old\b)', re.I)
RX_STAGING= re.compile(r'registros_insertar', re.I)
RX_DAYDATE= re.compile(r'_\d{6}\b|_\d{8}\b')
RX_DERIV  = re.compile(r'(SUMARIZAD[OA]S?|_FINAL\b|Analytics_agrupada\d*|Analytics_\d+)', re.I)

def fam_of(o):
    n=o['tabla']
    if re.match(r'^NPS_\d{6}$',n,re.I) or re.match(r'^NPS_\d{8}$',n,re.I): return 'MKT.NPS_YYYYMM'
    if re.match(r'^WP_.+_202010$',n,re.I):                                 return 'LEADS.WP_landing_202010'
    if re.match(r'^UNB_leads_\d{8}_\d{8}$',n,re.I):                        return 'LEADS.UNB_leads_rango'
    if re.match(r'^BI_FACTURA_DETALLE_\d{6}$',n,re.I):                     return 'dbo.BI_FACTURA_DETALLE_YYYYMM'
    if re.match(r'^BI_FACTURA_ENCABEZADO_\d{6}$',n,re.I):                  return 'dbo.BI_FACTURA_ENCABEZADO_YYYYMM'
    if re.match(r'^vFACTURACION_DETALLE_\d{6}$',n,re.I):                   return 'dbo.vFACTURACION_DETALLE_YYYYMM'
    if re.match(r'^vRETENCIONES_\d{6}$',n,re.I):                           return 'dbo.vRETENCIONES_YYYYMM'
    return None

def noise_tag(o):
    n=o['tabla']
    if o['esquema'].upper()=='TEMP': return 'temp'
    if RX_BACKUP.search(n):  return 'backup'
    if RX_STAGING.search(n): return 'staging'
    if RX_PRUEBA.search(n):  return 'prueba'
    if RX_DERIV.search(n):   return 'derivada'
    if RX_MISC.search(n):    return 'misc'
    if RX_DAYDATE.search(n): return 'daydate'
    return None

def classify(objs):
    canon=[]; ruido=[]; fams=collections.defaultdict(list)
    for o in objs:
        f=fam_of(o)
        if f: fams[f].append(o); continue
        t=noise_tag(o)
        if t: o=dict(o); o['_tag']=t; ruido.append(o)
        else: canon.append(o)
    return canon, ruido, fams

# ---------------------------------------------------------------- dominio
DOM = {
 'SIGASC':'Core SIGA','SIGAMSASC':'Core SIGA','dbo':'Data Warehouse / BI',
 'MKT':'Marketing','LEADS':'Marketing / Leads','LEADSMKT':'Marketing / Leads',
 'MAILCHIMP':'Email marketing','ACTIVITY':'Actividad y Bajas',
 'SAP':'Compras y Finanzas (SAP)','SAP_COMPRAS':'Compras y Finanzas (SAP)',
 'COMPRAS':'Compras y Finanzas (SAP)','VISMA':'Compras y Finanzas (Visma)',
 'MIO':'MIO','BIGDATA':'Big Data','MAPPING':'Mapping','ACTIVITY':'Actividad y Bajas',
}
def dominio(o): return DOM.get(o['esquema'],'Otros')

# ---------------------------------------------------------------- perfiles
def load_profile(esquema, tabla, is_view):
    base = PROF_V if is_view else PROF_T
    p = os.path.join(base, f"{esquema}.{tabla}.json")
    if not os.path.exists(p): return None
    try: return json.load(open(p,encoding="utf-8"))
    except Exception: return None

# ---------------------------------------------------------------- SQL parsing
def strip_sql_comments(sql):
    sql = re.sub(r'/\*.*?\*/', ' ', sql, flags=re.S)
    sql = re.sub(r'--[^\n]*', ' ', sql)
    return sql

KW_STOP = {'ON','WHERE','AS','LEFT','RIGHT','INNER','OUTER','FULL','CROSS','JOIN',
           'GROUP','ORDER','HAVING','UNION','SELECT','FROM','WITH','APPLY','AND','OR',
           'PIVOT','UNPIVOT','SET','TOP'}

def unbracket(s): return s.replace('[','').replace(']','').strip()

def find_where_blocks(s):
    """WHERE ... acotado por parentesis (corta en ) del subquery contenedor,
    en clausula de nivel superior GROUP/ORDER/HAVING/UNION/SELECT, o ;)."""
    blocks=[]
    for m in re.finditer(r'\bWHERE\b', s, re.I):
        i=m.end(); depth=0; j=i; n=len(s)
        while j<n:
            ch=s[j]
            if ch=='(': depth+=1
            elif ch==')':
                if depth==0: break
                depth-=1
            elif depth==0:
                if ch==';': break
                if re.match(r'(GROUP\s+BY|ORDER\s+BY|HAVING\b|UNION\b|SELECT\b)', s[j:], re.I): break
            j+=1
        blocks.append(s[i:j])
    return blocks

def find_case_blocks(s):
    """CASE ... END balanceado (respeta CASE anidados)."""
    blocks=[]; low=s.upper(); i=0; n=len(s)
    toks=[(m.start(),m.group(0).upper()) for m in re.finditer(r'\bCASE\b|\bEND\b', s, re.I)]
    stack=[]
    for pos,kind in toks:
        if kind=='CASE': stack.append(pos)
        elif kind=='END' and stack:
            start=stack.pop()
            if not stack:  # cerro un CASE de nivel superior
                blocks.append(s[start:pos+3])
    return blocks

def parse_view(sql, resolver, cte_aware=True):
    """resolver(tbl)->key canonico o None. Devuelve dict con joins/filtros/derivaciones/tablas."""
    s = strip_sql_comments(sql)
    cte = set(m.group(1).lower() for m in re.finditer(r'(?:\bWITH\b|,)\s*([A-Za-z_]\w*)\s+AS\s*\(', s, re.I))

    alias2t = {}
    for m in re.finditer(r'\b(?:FROM|JOIN)\s+(\[?[A-Za-z_]\w*\]?(?:\.\[?[A-Za-z_]\w*\]?)?)\s+(?:AS\s+)?(\[?[A-Za-z_]\w*\]?)', s, re.I):
        tbl = unbracket(m.group(1)); al = unbracket(m.group(2))
        if al.upper() in KW_STOP or tbl.upper() in KW_STOP: continue
        alias2t[al] = tbl

    def R(alias_or_tbl):
        tbl = alias2t.get(alias_or_tbl, alias_or_tbl)
        if tbl.lower() in cte: return None
        return resolver(tbl)

    # tablas base consumidas
    base_tables=set()
    for m in re.finditer(r'\b(?:FROM|JOIN)\s+(\[?[A-Za-z_]\w*\]?(?:\.\[?[A-Za-z_]\w*\]?)?)', s, re.I):
        tbl=unbracket(m.group(1))
        if tbl.lower() in cte: continue
        r=resolver(tbl)
        if r: base_tables.add(r)

    # JOIN ... ON
    joins=[]
    for m in re.finditer(r'\bON\b(.*?)(?=\b(?:LEFT|RIGHT|INNER|OUTER|FULL|CROSS|JOIN|WHERE|GROUP|ORDER|HAVING|UNION)\b|\)|$)', s, re.I|re.S):
        for eq in re.finditer(r'\b(\w+)\.(\w+)\s*=\s*(\w+)\.(\w+)', m.group(1)):
            aA,cA,aB,cB=eq.groups()
            rA=R(aA); rB=R(aB)
            if not rA or not rB or rA==rB: continue
            joins.append((rA,cA.upper(),rB,cB.upper()))

    # WHERE -> filtros (y join-eq de coma)
    filtros=[]  # (tabla_base, expr, flags)
    for blk in find_where_blocks(s):
        for conj in split_top_and(blk):
            e=clean_expr(conj)
            if not e or len(e)>500: continue
            eq=re.fullmatch(r'(\w+)\.(\w+)\s*=\s*(\w+)\.(\w+)', e)
            if eq:  # join por coma
                rA=R(eq.group(1)); rB=R(eq.group(3))
                if rA and rB and rA!=rB:
                    joins.append((rA,eq.group(2).upper(),rB,eq.group(4).upper()))
                continue
            als=aliases_in(e)
            tabs={R(a) for a in als}; tabs.discard(None)
            if not tabs: continue
            flags=[]
            if re.search(r'1900-?0?1-?0?1|19000101|1900', e): flags.append('tombstone')
            if re.search(r'\b\w*(STS|ESTADO|STATUS)\w*\b', e, re.I): flags.append('estado')
            for t in tabs:
                filtros.append((t,e,flags))

    # dedup / dedup signals
    dedup_tabs=set()
    if re.search(r'\bDISTINCT\b', s, re.I) or re.search(r'\b(ROW_NUMBER|RANK|DENSE_RANK)\s*\(\s*\)\s*OVER', s, re.I):
        dedup_tabs=set(base_tables)

    # CASE -> derivaciones (cap y dedup)
    derivs=[]  # (tabla_base, expr)
    seen=set()
    for cb in find_case_blocks(s):
        e=clean_expr(cb)
        if len(e)>450: continue
        if e in seen: continue
        seen.add(e)
        als=aliases_in(cb); tabs={R(a) for a in als}; tabs.discard(None)
        for t in tabs:
            derivs.append((t,e))
        if len(seen)>=12: break

    return dict(alias2t=alias2t, cte=cte, joins=joins, base_tables=base_tables,
                filtros=filtros, derivs=derivs, dedup_tabs=dedup_tabs)

def split_top_and(txt):
    """Divide por AND de nivel superior (respeta parentesis)."""
    out=[]; depth=0; cur=''; i=0; U=txt
    tokens=re.split(r'(\(|\)|\bAND\b|\bOR\b)', txt, flags=re.I)
    for tk in tokens:
        if tk=='(' : depth+=1; cur+=tk
        elif tk==')': depth-=1; cur+=tk
        elif tk.upper()=='AND' and depth==0:
            if cur.strip(): out.append(cur.strip()); cur=''
        elif tk.upper()=='OR' and depth==0:
            cur+=' OR '  # mantené OR dentro del mismo predicado
        else: cur+=tk
    if cur.strip(): out.append(cur.strip())
    return [p for p in out if p.strip()]

def aliases_in(expr):
    return set(m.group(1) for m in re.finditer(r'\b([A-Za-z_]\w*)\.\w+', expr))

def clean_expr(e):
    e=re.sub(r'\s+',' ',e).strip()
    return e

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    objs=load_objs()
    canon,ruido,fams=classify(objs)
    print("clasif:",len(canon),"canon /",len(ruido),"ruido /",sum(len(v) for v in fams.values()),"en",len(fams),"familias")
