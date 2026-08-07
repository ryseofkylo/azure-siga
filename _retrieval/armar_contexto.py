# -*- coding: utf-8 -*-
"""
Ensamblador de contexto (FASE 3, nivel 2 del schema-linking).
NO usa LLM: es determinista. Dado un conjunto de tablas nombradas, materializa
el bundle de contexto (notas completas + reglas + relaciones + claves + vecinos).

Uso:
  python armar_contexto.py catalogo
      -> imprime el catálogo compacto (nivel 1, va siempre en contexto).
  python armar_contexto.py sugerir <palabras...>
      -> lista líneas del catálogo que matchean (ayuda al schema-linking).
  python armar_contexto.py contexto ESQUEMA.TABLA [ESQUEMA.TABLA ...] [--vecinos]
      -> arma el bundle para esas tablas. --vecinos incluye notas de vecinos 1-hop.
"""
import os, sys, json, re, glob
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # ...\Azure
DATA  = os.path.join(VAULT, "_data")

def _load_jl(name):
    path=os.path.join(DATA,name)
    if not os.path.exists(path): return []
    return [json.loads(l) for l in open(path,encoding="utf-8")]

def build_index():
    """key canónico (esquema.tabla / familia / clave) -> ruta de nota."""
    idx={}
    for sub in ("Tablas","Vistas","Familias","Claves"):
        for f in glob.glob(os.path.join(VAULT,sub,"**","*.md"),recursive=True):
            base=os.path.basename(f)[:-3]           # sin .md
            idx[base.upper()]=f
    return idx

REL   = _load_jl("relaciones.jsonl")
REGLAS= _load_jl("reglas.jsonl")
IDX   = build_index()

def resolve(name):
    return IDX.get(name.upper())

def read_note(name):
    p=resolve(name)
    if not p: return None
    return open(p,encoding="utf-8").read()

def neighbors(table):
    out=[]
    for r in REL:
        if r["origen"]==table:  out.append((r["destino"], r["columna_origen"], r["columna_destino"], r["vista"]))
        elif r["destino"]==table:out.append((r["origen"],  r["columna_destino"], r["columna_origen"], r["vista"]))
    # dedup
    seen=set(); res=[]
    for t,ca,cb,v in out:
        if (t,ca,cb) in seen: continue
        seen.add((t,ca,cb)); res.append((t,ca,cb,v))
    return res

def reglas_de(table):
    return [r for r in REGLAS if r["tabla_base"]==table]

def cmd_catalogo():
    p=os.path.join(DATA,"catalogo_compacto.md")
    print(open(p,encoding="utf-8").read())

def cmd_sugerir(words):
    p=os.path.join(DATA,"catalogo_compacto.md")
    pat=[w.lower() for w in words]
    for line in open(p,encoding="utf-8"):
        low=line.lower()
        if all(w in low for w in pat) and "|" in line:
            sys.stdout.write(line)

def cmd_contexto(tables, incluir_vecinos=False):
    print("# CONTEXTO ENSAMBLADO (tabla-first)\n")
    print("> Respetá las **reglas de negocio** de cada tabla (tombstone 1900-01-01, filtros de estado, dedup).")
    print("> Las **vistas** son referencia; consultá las **tablas base**.\n")
    vistos=set()
    for t in tables:
        note=read_note(t)
        print("\n" + "="*70)
        if note is None:
            print(f"# {t}\n_(no encontrada en el vault — ¿nombre exacto esquema.tabla?)_")
            continue
        print(note.rstrip())
        vistos.add(t.upper())

    # vecinos 1-hop (compactos o completos)
    vec=[]
    for t in tables:
        for (nb,ca,cb,v) in neighbors(t):
            if nb.upper() in vistos: continue
            if not resolve(nb): continue   # solo vecinos con nota en el corpus
            vec.append((t,nb,ca,cb,v))
    if vec:
        print("\n" + "="*70)
        print("# VECINOS (JOINs conocidos, confidence alta)\n")
        seen=set()
        for (t,nb,ca,cb,v) in vec:
            sig=(t,nb,ca,cb)
            if sig in seen: continue
            seen.add(sig)
            print(f"- `{t}`.`{ca}` = `{nb}`.`{cb}`  → [[{nb}]]  (de {v})")
        if incluir_vecinos:
            print("\n## Notas de vecinos\n")
            for nb in sorted({nb for (_,nb,_,_,_) in vec}):
                n=read_note(nb)
                if n:
                    print("\n" + "-"*60); print(n.rstrip())

if __name__=="__main__":
    a=sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    cmd=a[0]
    if cmd=="catalogo": cmd_catalogo()
    elif cmd=="sugerir": cmd_sugerir(a[1:])
    elif cmd=="contexto":
        args=a[1:]; vec="--vecinos" in args
        tabs=[x for x in args if not x.startswith("--")]
        cmd_contexto(tabs, vec)
    else:
        print(__doc__)
