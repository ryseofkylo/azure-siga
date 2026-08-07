---
esquema: dbo
tabla: V_SOLUCIONORDEN
objeto: dbo.V_SOLUCIONORDEN
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 2
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_SOLUCIONORDEN

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.ORDENSRV]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ORDENSOL` | varchar | 0% |
| 2 | `SOLUCIONORDEN` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_SOLUCIONORDEN
-- Extraida: 2026-08-07T15:28:21.256976+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_SOLUCIONORDEN]
AS SELECT DISTINCT
		   ORDENSOL, 
		   CASE WHEN ordensol = 'D' THEN 'DOMICILIO'
				WHEN ordensol = 'T' THEN 'TELEFONICO'
				WHEN ordensol = 'O' THEN 'OFICINA'
				WHEN ordensol = 'R' THEN 'RED'
				WHEN ordensol = 'M' THEN 'MDU (EDIFICIOS)'
				WHEN ordensol = 'C' THEN 'CABECERA'
				WHEN ordensol = 'N' THEN 'NINGUNO'
		   END AS SOLUCIONORDEN
	FROM SIGASC.ORDENSRV
	WHERE ordensol <> '';
```
