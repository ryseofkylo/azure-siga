---
objeto: Home
tipo_objeto: portada
tags: [home]
---

# Catálogo SIGA — Portada

Base de conocimiento del warehouse **SIGA** (SQL Server / Synapse) para consulta
**TABLA-FIRST** y generación de SQL asistida por LLM.

## Empezá acá
- 🗂️ **[[MOC-INDICE]]** — índice general (MOCs por esquema, conteos).
- 🧭 Navegá por esquema: `MOCs/` · tablas en `Tablas/{esquema}/` · vistas (referencia) en `Vistas/{esquema}/`.

## Cómo está organizado
- **Tablas/** — tablas base canónicas. **Son el target de consulta.** Cada nota trae
  columnas (con %null y ejemplos), **grain** inferido, relaciones (JOINs), claves y
  **reglas de negocio** (tombstone `1900-01-01`, filtros de estado, dedup).
- **Vistas/** — vistas como **referencia** ("esto se armó así"), con su `CREATE VIEW`.
  No son target de consulta.
- **Familias/** — series particionadas por período (NPS mensual, etc.), colapsadas.
- **Claves/** — hubs `clave-*`: qué tablas comparten una columna de JOIN.
- **_deprecated/** — ruido (backups/pruebas/snapshots). **Fuera del corpus. No consultar.**
- **_retrieval/** — kit text-to-SQL (system prompt + ensamblador de contexto). Ver su `README.md`.
- **_build/** — pipeline reproducible que genera este vault. Ver su `README.md`.
- **_data/** — datos derivados (`relaciones.jsonl`, `reglas.jsonl`, `claves.jsonl`,
  `catalogo_compacto.md`).
