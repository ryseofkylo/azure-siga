# Catálogo SIGA — Diccionario de datos (Obsidian)

Base de conocimiento del **warehouse SIGA** (SQL Server / Azure Synapse) pensada para
consulta **TABLA-FIRST** y generación de SQL asistida por LLM (text-to-SQL).

> **Versión pública sanitizada.** Se removieron los valores de ejemplo del perfilado
> (columna *Ejemplos*) para no exponer datos personales de clientes. El resto del
> diccionario —esquema, tipos, %null, relaciones, reglas de negocio y grain— está intacto.

## Estructura
- **`Tablas/{esquema}/`** — tablas base canónicas. **Son el target de consulta.** Cada
  nota trae columnas (tipo y %null), **grain** inferido, relaciones (JOINs derivados de
  vistas), claves y **reglas de negocio** (tombstone `1900-01-01`, filtros de estado, dedup).
- **`Vistas/{esquema}/`** — vistas como **referencia** ("esto se armó así"), con su
  `CREATE VIEW`. No son target de consulta.
- **`Familias/`** — series particionadas por período (p.ej. NPS mensual), colapsadas.
- **`Claves/`** — hubs `clave-*`: qué tablas comparten una columna de JOIN.
- **`_deprecated/`** — objetos ruido (backups/pruebas/snapshots). Fuera del corpus.
- **`_retrieval/`** — kit text-to-SQL: `system_prompt.md` + `armar_contexto.py`
  (ensamblador de contexto por schema-linking). Ver su `README.md`.
- **`_build/`** — pipeline determinista/idempotente que genera este vault desde el
  export del catálogo. Ver su `README.md`.
- **`_data/`** — datos derivados: `relaciones.jsonl`, `reglas.jsonl`, `claves.jsonl`,
  `catalogo_compacto.md`.

## Cómo empezar
Abrí la carpeta como **vault de Obsidian** y arrancá por `Home.md` → `MOCs/MOC-INDICE`.

## Números
389 tablas base · 188 vistas · 7 familias · 182 hubs de clave · 285 relaciones · 934 reglas.
