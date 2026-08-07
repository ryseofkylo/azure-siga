# -*- coding: utf-8 -*-
import importlib.util, os, re, json, collections, shutil, glob, sys
spec=importlib.util.spec_from_file_location("p",os.path.join(os.path.dirname(os.path.abspath(__file__)),"pipeline.py"))
p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
sys.stdout.reconfigure(encoding='utf-8')

VAULT=p.VAULT
def P(*a): return os.path.join(VAULT,*a)

# ---------- carga ----------
objs=p.load_objs()
canon,ruido,fams=p.classify(objs)
key=p.key
canon_keys=set(key(o) for o in canon)
fam_member_keys=set(key(o) for lst in fams.values() for o in lst)
all_real_ci={ key(o).upper(): key(o) for o in objs }
bare=collections.defaultdict(list)
for o in objs: bare[o['tabla'].upper()].append(key(o))
obj_by_key={key(o):o for o in objs}
is_view=lambda o: o['tipo_objeto']=='VIEW'

# columnas por objeto (tipo/orden reales)
cols_by=collections.defaultdict(list)
for l in open(os.path.join(p.CAT,"columnas.jsonl"),encoding="utf-8"):
    c=json.loads(l); cols_by[(c['esquema'],c['tabla'])].append(c)
for k in cols_by: cols_by[k].sort(key=lambda c:c['orden'])

def resolver(tbl):
    t=tbl.upper()
    if t in all_real_ci: return all_real_ci[t]
    if '.' not in t and len(bare.get(t,[]))==1: return bare[t][0]
    return None

# ---------- FASE 1a + 1b: recorrer vistas ----------
relaciones=[]                     # dicts
reglas=[]                         # dicts
view_consumes=collections.defaultdict(set)   # view_key -> {base tables}
consumed_by=collections.defaultdict(set)     # base table -> {views}
filtros_by=collections.defaultdict(list)     # table -> [(expr,flags,vista)]
derivs_by=collections.defaultdict(list)      # table -> [(expr,vista)]
dedup_by=collections.defaultdict(set)        # table -> {vistas}
view_sql={}

for f in glob.glob(os.path.join(p.DEFS,"*.sql")):
    base=os.path.basename(f)[:-4]           # esquema.tabla
    vkey=all_real_ci.get(base.upper(), base)
    if vkey not in canon_keys:               # NO derivar reglas/relaciones de vistas deprecated
        continue
    sql=open(f,encoding='utf-8',errors='replace').read()
    view_sql[vkey]=sql
    r=p.parse_view(sql,resolver)
    # base tables consumidas (excluye la propia vista)
    bts={t for t in r['base_tables'] if t!=vkey}
    view_consumes[vkey]=bts
    for t in bts: consumed_by[t].add(vkey)
    for (rA,cA,rB,cB) in r['joins']:
        relaciones.append(dict(origen=rA,destino=rB,columna_origen=cA,columna_destino=cB,
                               fuente="view_join",vista=vkey,confidence="alta"))
    for (t,e,flags) in r['filtros']:
        reglas.append(dict(tabla_base=t,tipo="filtro",expresion=e,flags=flags,vista_origen=vkey))
        filtros_by[t].append((e,flags,vkey))
    for (t,e) in r['derivs']:
        reglas.append(dict(tabla_base=t,tipo="derivacion",expresion=e,flags=[],vista_origen=vkey))
        derivs_by[t].append((e,vkey))
    for t in r['dedup_tabs']:
        reglas.append(dict(tabla_base=t,tipo="dedup",expresion="usa DISTINCT/ROW_NUMBER",flags=["dedup"],vista_origen=vkey))
        dedup_by[t].add(vkey)

# relaciones por columna homonima -> HUBS de clave (no N^2)
CURADAS={'EMPRESAID','CLIENTENRO','CONTRATONRO','PRODUCTOID','PKCLIENTENRO','PKCONTRATONRO',
         'PKPRODUCTOID','PKPOLITICAID','CONTRATO','CLIENTE','SUCURSAL','CENTROOPERATIVOID','TECNICOID'}
join_cols=set()
for r in relaciones: join_cols.add(r['columna_origen']); join_cols.add(r['columna_destino'])

col_tables=collections.defaultdict(list)   # COL -> [(key, tipo)]
col_types=collections.defaultdict(set)
for o in canon:
    for c in cols_by[(o['esquema'],o['tabla'])]:
        cu=c['columna'].upper()
        col_tables[cu].append(key(o)); col_types[cu].add(c['tipo_dato'])

def es_clave(col):
    if col in CURADAS or col in join_cols: return True
    if re.match(r'^PK', col): return True
    if re.search(r'(ID|NRO|NUMERO|CODIGO)$', col):
        return len(col_tables[col])>=4
    return False

hubs={}  # COL -> [keys]
for col,tabs in col_tables.items():
    if len(tabs)<2: continue
    if es_clave(col): hubs[col]=sorted(set(tabs))

# ---------- salida _data ----------
def wipe(d):
    if os.path.isdir(d): shutil.rmtree(d)
    os.makedirs(d,exist_ok=True)
for d in ["Tablas","Vistas","Familias","Claves","MOCs","_deprecated","_data"]:
    wipe(P(d))

def jl(path,rows):
    with open(path,"w",encoding="utf-8") as fh:
        for r in rows: fh.write(json.dumps(r,ensure_ascii=False)+"\n")
jl(P("_data","relaciones.jsonl"),relaciones)
jl(P("_data","reglas.jsonl"),reglas)
jl(P("_data","claves.jsonl"),[{"columna":c,"tipos":sorted(col_types[c]),"n_tablas":len(t),"tablas":t} for c,t in sorted(hubs.items())])

# ---------- helpers notas ----------
def slug(s): return re.sub(r'[^\w.-]','_',s)
def esc(s):
    s=str(s).replace("|","\\|").replace("\n"," ").replace("\r"," ")
    return s[:60]+("…" if len(s)>60 else "")

# nombre de nota = mismo slug para archivo y wikilink (consistencia)
def notename(k): return slug(k)
# miembro de familia -> nombre de la nota-familia
member2fam={ key(m): fn for fn,ms in fams.items() for m in ms }
def corpus_link(k):
    """Devuelve el basename de nota corpus para k, o None si es deprecated/inexistente."""
    if k in canon_keys: return notename(k)
    if k in member2fam: return notename(member2fam[k])
    return None

def profile_map(o):
    pr=p.load_profile(o['esquema'],o['tabla'],is_view(o))
    m={}
    if pr and 'profile' in pr:
        for c in pr['profile'].get('columns',[]):
            m[c['columna'].upper()]=c
    return m

def col_table(o, prof):
    rows=["| # | Columna | Tipo | %null (m) | Ejemplos |","|--:|---|---|--:|---|"]
    for c in cols_by[(o['esquema'],o['tabla'])]:
        cu=c['columna'].upper(); pc=prof.get(cu)
        null=f"{pc['null_pct_sample']:.0f}%" if pc and pc.get('null_pct_sample') is not None else ""
        ex=""
        if pc and pc.get('top_values'):
            ex=", ".join(esc(v['value']) for v in pc['top_values'][:3])
        rows.append(f"| {c['orden']} | `{c['columna']}` | {c['tipo_dato']} | {null} | {ex} |")
    return "\n".join(rows)

def fm(d):
    out=["---"]
    for k,v in d.items():
        if isinstance(v,list):
            out.append(f"{k}:")
            for it in v: out.append(f"  - {it}")
        elif isinstance(v,bool):
            out.append(f"{k}: {'true' if v else 'false'}")
        else:
            out.append(f"{k}: {v}")
    out.append("---")
    return "\n".join(out)

def dom_tag(o): return slug(p.dominio(o).lower().replace(' / ','-').replace(' ','-'))

# ---------- inferencia de grain (organica, desde la muestra) ----------
DATE_TYPES={'datetime','datetime2','date','smalldatetime','datetimeoffset'}
def type_of(o,col):
    for c in cols_by[(o['esquema'],o['tabla'])]:
        if c['columna']==col: return c['tipo_dato']
    return ''
def is_idlike(name):
    u=name.upper()
    return bool(re.match(r'^PK',u) or re.search(r'(ID|NRO|NUMERO|CODIGO|CUIT|DNI)$',u))

def infer_grain(o):
    pr=p.load_profile(o['esquema'],o['tabla'],False)
    if not pr or 'profile' not in pr: return "TODO (sin perfil de muestreo)"
    N=pr.get('rows_sampled') or 0
    cols=pr['profile'].get('columns',[])
    if not N or not cols: return "TODO (muestra vacía)"
    meta={c['columna']:c for c in cols}
    def dist(c): return meta[c].get('distinct_in_sample')
    def nul(c):  return meta[c].get('null_pct_sample') or 0
    names=[c['columna'] for c in cols]
    uniques=[c for c in names if dist(c)==N and nul(c)<1]
    id_uniques=sorted([c for c in uniques if is_idlike(c)],
                      key=lambda c:(0 if re.match(r'^PK',c.upper()) else 1, len(c)))
    datecols=[c for c in names if type_of(o,c).lower() in DATE_TYPES]
    mod_date=None
    for c in datecols:
        u=c.upper()
        if 'MODIFIED' in u or u.startswith('BD') or 'FECHA' in u or 'ALTA' in u:
            mod_date=c; break
    if not mod_date and datecols: mod_date=datecols[0]
    # mejor clave de entidad (unica id-like, si no la id-like de mayor distinct)
    best_key = id_uniques[0] if id_uniques else None
    if not best_key:
        idcands=[c for c in names if is_idlike(c) and nul(c)<50]
        if idcands: best_key=max(idcands,key=lambda c:dist(c) or 0)

    # histórica/versionada: nombre H_ + fecha de modificación + clave de entidad
    if o['tabla'].upper().startswith('H_') and mod_date and best_key:
        return f"1 fila = 1 versión de `{best_key}` por `{mod_date}` — histórica/versionada (inferido de muestra)"
    if id_uniques:
        return f"1 fila = 1 `{id_uniques[0]}` (único en muestra de {N})"
    if uniques:
        return f"1 fila = 1 `{uniques[0]}` (único en muestra de {N})"
    # sin clave única: intento compuesto sobre sample_rows (pocas filas → tentativo)
    sr=pr['profile'].get('sample_rows') or []
    idcols=sorted([c for c in names if is_idlike(c) and nul(c)<50],
                  key=lambda c:-(dist(c) or 0))[:4]
    if sr and idcols:
        combo=[]
        for c in idcols:
            combo.append(c)
            seen=set(); uniq=True
            for row in sr:
                kv=tuple(str(row.get(k)) for k in combo)
                if kv in seen: uniq=False; break
                seen.add(kv)
            if uniq and len(sr)>=3:
                return f"1 fila ≈ 1 combinación de ({', '.join('`'+x+'`' for x in combo)}) — compuesto, tentativo (muestra {len(sr)})"
    top=sorted(names,key=lambda c:-(dist(c) or 0))[:3]
    return f"grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: {', '.join('`'+c+'`' for c in top)}"

# ---------- notas de TABLA base ----------
def rels_for(k):
    seen=set(); out=[]
    for r in relaciones:
        if r['origen']==k: other,cs,cd=r['destino'],r['columna_origen'],r['columna_destino']
        elif r['destino']==k: other,cs,cd=r['origen'],r['columna_destino'],r['columna_origen']
        else: continue
        link=corpus_link(other)
        if not link: continue          # no enlazar a deprecated/inexistente
        sig=(link,cs,cd)
        if sig in seen: continue
        seen.add(sig)
        out.append(f"- [[{link}]] · `{k.split('.')[-1]}.{cs} = {other.split('.')[-1]}.{cd}` — view_join ({r['vista'].split('.')[-1]}), alta")
    return out

def claves_for(o):
    out=[]
    for c in cols_by[(o['esquema'],o['tabla'])]:
        cu=c['columna'].upper()
        if cu in hubs: out.append(f"- `{c['columna']}` ({c['tipo_dato']}) → [[clave-{slug(cu)}]]")
    return out

def reglas_section(k):
    out=[]
    ff=filtros_by.get(k,[])
    if ff:
        out.append("**Filtros**")
        seen=set()
        for e,flags,v in ff:
            if e in seen: continue
            seen.add(e)
            fl=" ".join(("🪦" if 'tombstone' in flags else "")+("🚦" if 'estado' in flags else "") for _ in [0]).strip()
            out.append(f"- {fl+' ' if fl else ''}`{e}` — _de_ [[{notename(v)}]]")
    if dedup_by.get(k):
        out.append(f"- ♻️ dedup: vistas que deduplican esta tabla → "+", ".join(f"[[{notename(v)}]]" for v in sorted(dedup_by[k])))
    dd=derivs_by.get(k,[])
    if dd:
        out.append("\n**Derivaciones (CASE)**")
        seen=set()
        for e,v in dd:
            if e in seen: continue
            seen.add(e)
            out.append(f"- _de_ [[{notename(v)}]]:\n  ```sql\n  {e}\n  ```")
    return out

n_tab=0
for o in canon:
    if is_view(o): continue
    k=key(o); prof=profile_map(o); g=infer_grain(o)
    front=fm(dict(esquema=o['esquema'],tabla=o['tabla'],objeto=k,tipo_objeto="BASE TABLE",
        dominio=p.dominio(o),canonico=True,grain=g,n_columnas=o['n_columnas'],
        tags=[f"esquema/{o['esquema']}",f"dominio/{dom_tag(o)}","tipo/tabla-base","canonico"]))
    rels=rels_for(k); cl=claves_for(o); rg=reglas_section(k); vs=sorted(consumed_by.get(k,[]))
    body=[front,"",f"# {k}","",
          f"> **BASE TABLE** · Dominio: **{p.dominio(o)}** · {o['n_columnas']} columnas · Consultá esta tabla directamente (**tabla-first**).",
          f"> **Grain (inferido):** {g}","",
          "## Columnas",col_table(o,prof),"",
          "## Claves de join presentes","\n".join(cl) if cl else "_(sin claves detectadas)_","",
          "## Relaciones (derivadas de JOINs de vistas)","\n".join(rels) if rels else "_(ninguna relación explícita hallada en vistas)_","",
          "## Reglas de negocio conocidas","\n".join(rg) if rg else "_(ninguna regla derivada de vistas)_","",
          "## Vistas que la consumen (referencia)","\n".join(f"- [[{notename(v)}]]" for v in vs) if vs else "_(ninguna)_",""]
    d=P("Tablas",o['esquema']); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,f"{slug(k)}.md"),"w",encoding="utf-8").write("\n".join(body))
    n_tab+=1

# ---------- notas de VISTA (referencia) ----------
n_vw=0
for o in canon:
    if not is_view(o): continue
    k=key(o); prof=profile_map(o)
    front=fm(dict(esquema=o['esquema'],tabla=o['tabla'],objeto=k,tipo_objeto="VIEW",
        dominio=p.dominio(o),canonico=True,referencia=True,grain="N/A (vista)",n_columnas=o['n_columnas'],
        tags=[f"esquema/{o['esquema']}",f"dominio/{dom_tag(o)}","tipo/vista","referencia"]))
    bts=sorted({corpus_link(t) for t in view_consumes.get(k,[]) if corpus_link(t)})
    sql=view_sql.get(k,"-- (definición no encontrada)")
    body=[front,"",f"# {k}","",
          "> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.","",
          "## Tablas base que consume","\n".join(f"- [[{t}]]" for t in bts) if bts else "_(no resueltas)_","",
          "## Columnas expuestas",col_table(o,prof),"",
          "## Definición (CREATE VIEW)","```sql",sql.strip(),"```",""]
    d=P("Vistas",o['esquema']); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,f"{slug(k)}.md"),"w",encoding="utf-8").write("\n".join(body))
    n_vw+=1

# ---------- notas FAMILIA ----------
for famname,members in fams.items():
    members=sorted(members,key=lambda o:o['tabla'])
    rep=max(members,key=lambda o:o['n_columnas']); prof=profile_map(rep)
    esq=rep['esquema']
    front=fm(dict(objeto=famname,tipo_objeto="FAMILIA (particiones por período)",esquema=esq,
        dominio=p.dominio(rep),canonico=True,familia=True,n_miembros=len(members),
        tags=[f"esquema/{esq}",f"dominio/{dom_tag(rep)}","tipo/familia","canonico"]))
    body=[front,"",f"# Familia: {famname}","",
        f"> Serie de **{len(members)} objetos** con esquema (casi) idéntico, particionados por período. "
        f"Consultá el **miembro del período** que necesites; el esquema común es el de abajo.","",
        "## Esquema común (según "+rep['tabla']+")",col_table(rep,prof),"",
        "## Miembros disponibles"]
    for m in members: body.append(f"- `{key(m)}` ({m['n_columnas']} col)")
    open(P("Familias",f"{slug(famname)}.md"),"w",encoding="utf-8").write("\n".join(body))

# ---------- notas CLAVE (hubs) ----------
for col,tabs in sorted(hubs.items()):
    by_esq=collections.defaultdict(list)
    for t in tabs: by_esq[t.split('.')[0]].append(t)
    front=fm(dict(objeto=f"clave-{col}",tipo_objeto="CLAVE DE JOIN",columna=col,
        tipos=sorted(col_types[col]),n_tablas=len(tabs),confidence="baja",
        tags=["tipo/clave-join",f"clave/{col}"]))
    body=[front,"",f"# Clave de join: `{col}`","",
        f"> Columna homónima (tipo {', '.join(sorted(col_types[col]))}) presente en **{len(tabs)} tablas canónicas**. "
        f"Candidata de JOIN — confidence **baja** (por nombre+tipo, no declarada).",""]
    for esq in sorted(by_esq):
        body.append(f"**{esq}**")
        for t in sorted(by_esq[esq]): body.append(f"- [[{notename(t)}]]")
        body.append("")
    open(P("Claves",f"clave-{slug(col)}.md"),"w",encoding="utf-8").write("\n".join(body))

# ---------- notas DEPRECATED ----------
for o in ruido:
    k=key(o)
    front=fm(dict(esquema=o['esquema'],tabla=o['tabla'],objeto=k,tipo_objeto=o['tipo_objeto'],
        canonico=False,motivo_ruido=o['_tag'],
        tags=["deprecated",f"ruido/{o['_tag']}",f"esquema/{o['esquema']}"]))
    body=[front,"",f"# ⛔ {k}  (DEPRECATED — {o['_tag']})","",
        "> Objeto marcado como **ruido** (backup/staging/prueba/derivada/snapshot). **Fuera del corpus de retrieval.** No consultar.","",
        f"- Esquema: {o['esquema']} · Tipo: {o['tipo_objeto']} · Columnas: {o['n_columnas']}",""]
    open(P("_deprecated",f"{slug(k)}.md"),"w",encoding="utf-8").write("\n".join(body))

# ---------- MOCs por esquema ----------
esquemas=sorted(set(o['esquema'] for o in objs))
for esq in esquemas:
    ct=[o for o in canon if o['esquema']==esq and not is_view(o)]
    cv=[o for o in canon if o['esquema']==esq and is_view(o)]
    fa=[f for f,ms in fams.items() if ms and ms[0]['esquema']==esq]
    rz=[o for o in ruido if o['esquema']==esq]
    if not (ct or cv or fa or rz): continue
    DOMv=p.DOM.get(esq,'Otros')
    body=[fm(dict(objeto=f"MOC-{esq}",tipo_objeto="MOC",esquema=esq,dominio=DOMv,
        tags=["tipo/moc",f"esquema/{esq}"])),"",
        f"# MOC — Esquema `{esq}`  ·  {DOMv}","",
        f"Tablas base canónicas: **{len(ct)}** · Vistas (referencia): **{len(cv)}** · Familias: **{len(fa)}** · Deprecated: **{len(rz)}**","",
        "## Tablas base (tabla-first)"]
    for o in sorted(ct,key=lambda o:o['tabla']): body.append(f"- [[{notename(key(o))}]]")
    if fa:
        body+=["","## Familias (particiones por período)"]
        for f in sorted(fa): body.append(f"- [[{slug(f)}]]")
    if cv:
        body+=["","## Vistas (referencia, no target)"]
        for o in sorted(cv,key=lambda o:o['tabla']): body.append(f"- [[{notename(key(o))}]]")
    open(P("MOCs",f"MOC-{slug(esq)}.md"),"w",encoding="utf-8").write("\n".join(body))

# indice raiz
tot_c=len([o for o in canon if not is_view(o)]); tot_v=len([o for o in canon if is_view(o)])
idx=[fm(dict(objeto="MOC-INDICE",tipo_objeto="MOC-raiz",tags=["tipo/moc","indice"])),"",
    "# Catálogo SIGA — Índice","",
    f"- Tablas base canónicas: **{tot_c}**",
    f"- Vistas (referencia): **{tot_v}**",
    f"- Familias (particiones): **{len(fams)}**",
    f"- Claves de join (hubs): **{len(hubs)}**",
    f"- Relaciones (view_join): **{len(relaciones)}**",
    f"- Reglas de negocio: **{len(reglas)}**",
    f"- Deprecated (fuera de corpus): **{len(ruido)}**","",
    "## MOCs por esquema"]
for esq in esquemas:
    if any(o['esquema']==esq for o in objs): idx.append(f"- [[MOC-{slug(esq)}]]")
idx+=["","## Cómo usar","- **Tabla-first**: consultá las tablas base; las vistas son *referencia* de cómo se armó cada cosa.",
      "- Las **reglas de negocio** (tombstone 1900-01-01, filtros de estado, dedup) están en cada nota de tabla base.",
      "- **Grain** inferido en cada nota de tabla (qué representa 1 fila).",
      "- Recuperación (FASE 3) en `_retrieval/` (system prompt + ensamblador de contexto)."]
open(P("MOCs","MOC-INDICE.md"),"w",encoding="utf-8").write("\n".join(idx))

# catalogo compacto (para FASE 3 retrieval)
lines=["# Catálogo compacto (schema-linking)","",
       "Formato: `esquema.tabla | dominio | columnas_clave`","```"]
for o in sorted(canon,key=lambda o:(o['esquema'],o['tabla'])):
    if is_view(o): continue
    ks=[c['columna'] for c in cols_by[(o['esquema'],o['tabla'])] if c['columna'].upper() in hubs][:8]
    lines.append(f"{key(o)} | {p.dominio(o)} | {', '.join(ks)}")
lines.append("```")
open(P("_data","catalogo_compacto.md"),"w",encoding="utf-8").write("\n".join(lines))

# manifest
open(P("_data","manifest.json"),"w",encoding="utf-8").write(json.dumps(dict(
    total=len(objs),canon_tablas=tot_c,canon_vistas=tot_v,familias=len(fams),
    miembros_familia=len(fam_member_keys),ruido=len(ruido),hubs=len(hubs),
    relaciones=len(relaciones),reglas=len(reglas)),ensure_ascii=False,indent=2))

print(f"OK  tablas={n_tab} vistas={n_vw} familias={len(fams)} hubs={len(hubs)} "
      f"deprecated={len(ruido)} relaciones={len(relaciones)} reglas={len(reglas)}")
