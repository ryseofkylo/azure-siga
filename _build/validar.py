import os, re, glob, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
V=r"C:\Users\Matias\Documents\azure\azure"
CORPUS=["Tablas","Vistas","Familias","Claves","MOCs"]
def notes(sub): return glob.glob(os.path.join(V,sub,"**","*.md"),recursive=True)
# targets existentes por basename
targets=set()
folder_of={}
for sub in CORPUS+["_deprecated"]:
    for f in notes(sub):
        b=os.path.basename(f)[:-3]; targets.add(b); folder_of[b]=sub
dep_targets={b for b,s in folder_of.items() if s=="_deprecated"}

link_rx=re.compile(r'\[\[([^\]|#]+)')
broken=collections.Counter()
to_dep=collections.Counter()
total_links=0
per_file_broken=collections.defaultdict(list)
for sub in CORPUS:
    for f in notes(sub):
        txt=open(f,encoding='utf-8').read()
        for m in link_rx.finditer(txt):
            t=m.group(1).strip()
            total_links+=1
            if t not in targets:
                broken[t]+=1; per_file_broken[os.path.basename(f)].append(t)
            elif t in dep_targets:
                to_dep[t]+=1
print(f"notas corpus: {sum(len(notes(s)) for s in CORPUS)} | deprecated: {len(notes('_deprecated'))}")
print(f"wikilinks totales en corpus: {total_links}")
print(f"LINKS ROTOS (target inexistente): {sum(broken.values())} en {len(broken)} destinos distintos")
for t,c in broken.most_common(15): print(f"   [{c}] -> {t}")
print(f"\nLINKS corpus -> DEPRECATED (deberían no existir): {sum(to_dep.values())} en {len(to_dep)} destinos")
for t,c in to_dep.most_common(15): print(f"   [{c}] -> {t}")
