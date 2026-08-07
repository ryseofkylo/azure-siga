---
objeto: FASE3-diseno-retrieval
tipo_objeto: diseño
estado: implementado (deterministas) — wiring a LLM pendiente
tags: [tipo/diseño, retrieval]
---

# FASE 3 — Diseño de recuperación

## Tamaño del corpus canónico (resultante)
- Tablas base: **389** · Vistas (referencia): **188** · Familias: **7** · Hubs de clave: **182**
- Reglas de negocio: **967** · Relaciones (view_join): **299**
- `_data/catalogo_compacto.md`: **~33 KB** (389 líneas `tabla | dominio | claves`).

## Recuperación en dos niveles

**Nivel 1 — Catálogo compacto (SIEMPRE en contexto).**
Se inyecta `_data/catalogo_compacto.md` entero en el system prompt: una línea por
tabla base `esquema.tabla | dominio | columnas_clave`. ~33 KB ≈ 8–11k tokens: entra
holgado en cualquier ventana moderna. Con esto el LLM ya "ve" todo el universo de
tablas y sus claves.

**Nivel 2 — Notas completas bajo demanda (schema-linking).**
1. El LLM lee el catálogo y **nombra** las tablas relevantes para la pregunta.
2. `armar_contexto.py` trae SOLO esas notas `.md` completas (columnas + %null +
   ejemplos + grain + reglas + relaciones) más sus vecinos 1-hop por `relaciones.jsonl`.
3. Se adjuntan las `reglas.jsonl` de esas tablas (tombstone, estado, dedup).
4. Recién ahí el LLM genera el SQL **tabla-first**.

## Por qué schema-linking y NO vector puro (en este caso)
- Las claves son **nombres convencionales** (`CLIENTENRO`, `PKCONTRATONRO`,
  `EMPRESAID`): matcheo léxico exacto > similitud semántica.
- Hay **decenas de variantes `H_*` casi homónimas** (`H_CONTRATO_CLIENTE`,
  `H_BAJASMOROSAS`, …) que un embedding colapsaría y confundiría. El nombre exacto
  desambigua; el vector no.
- El corpus canónico **entra en contexto** (nivel 1): el recall del nivel 1 es 100%
  por construcción — no hace falta índice aproximado.
- Las **reglas de negocio** (tombstone `1900-01-01`, filtros de estado) son
  determinísticas y ya están adjuntas por tabla: se recuperan por clave, no por
  semántica.

**Conclusión:** vector DB **no se justifica** con este tamaño. Si el corpus creciera
~10× o entraran descripciones NL largas, se reevalúa un índice híbrido (BM25 +
embeddings) — no antes.

## Implementación (ver `_retrieval/`)
- `_retrieval/system_prompt.md` → system prompt tabla-first.
- `_data/catalogo_compacto.md` → contexto nivel 1 (siempre en contexto).
- `_retrieval/armar_contexto.py` → nivel 2 determinista: materializa notas + reglas
  + relaciones + vecinos 1-hop para las tablas que el LLM nombra.
- `_data/relaciones.jsonl` / `reglas.jsonl` / `claves.jsonl` → fuentes del ensamblador.

**Único pendiente:** wiring a un LLM concreto (proveedor a elección) — afuera a propósito.
