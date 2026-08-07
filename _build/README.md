# _build — Pipeline reproducible

Scripts deterministas e idempotentes que **generan este vault** desde el catálogo
fuente. Regenerar no duplica nada: borra y reescribe solo las carpetas gestionadas
(`Tablas/ Vistas/ Familias/ Claves/ MOCs/ _deprecated/ _data/`). **No toca**
`.obsidian/`, `_retrieval/`, `_build/`, ni `Home.md`.

## Fuente de datos
`pipeline.py` apunta a:
- `SRC   = C:\Users\Matias\Documents\catalogo siga`  (export del warehouse)
- `VAULT = C:\Users\Matias\Documents\azure\azure`     (este vault)

Si movés cualquiera de las dos, editá esas dos constantes al inicio de `pipeline.py`.

## Uso
```
python _build/driver.py     # regenera todo el corpus
python _build/validar.py    # audita wikilinks (debe dar 0 rotos / 0 a deprecated)
```

## Qué hace cada script
- `pipeline.py` — librería: clasifica CANONICO/RUIDO, parsea las vistas (JOINs,
  WHERE/CASE), infiere dominio.
- `driver.py` — genera notas `.md`, MOCs, hubs de clave, familias, deprecated, y los
  `.jsonl` de `_data/` (relaciones, reglas, claves) + catálogo compacto.
- `validar.py` — chequeo de integridad de wikilinks.
