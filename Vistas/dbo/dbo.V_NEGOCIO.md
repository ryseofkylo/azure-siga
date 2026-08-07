---
esquema: dbo
tabla: V_NEGOCIO
objeto: dbo.V_NEGOCIO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 3
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_NEGOCIO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.NEGOCIO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `NEGOCIOID` | varchar | 0% |
| 2 | `NEGOCIOORIGEN` | varchar | 0% |
| 3 | `NEGOCIONOMBRE` | varchar | 11% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_NEGOCIO
-- Extraida: 2026-08-07T15:28:02.786825+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_NEGOCIO]
AS SELECT 
	NEGOCIOID,
	NEGOCIONOMBRE AS NEGOCIOORIGEN,
	CASE negocioid
		WHEN 'TVC' THEN 'CABLE'
		WHEN 'INT' THEN 'INTERNET'
		WHEN 'CEL' THEN 'CABLE'
		WHEN 'TEL' THEN 'CABLE'
		WHEN 'TVM' THEN 'CABLE'
		WHEN 'TVU' THEN 'CABLE'
		WHEN 'COR' THEN 'INTERNET'
		WHEN 'MIO' THEN 'MIO'
	END AS NEGOCIONOMBRE
FROM SIGASC.NEGOCIO;
```
