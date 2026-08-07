---
esquema: dbo
tabla: V_PROMOTOR
objeto: dbo.V_PROMOTOR
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 7
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_PROMOTOR

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.PROMOTOR]]
- [[SIGASC.PROMOTORGRUPO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PROMOTORID` | int | 0% |
| 3 | `PKPROMOTORID` | varchar | 0% |
| 4 | `PROMOTORNOMBRE` | varchar | 0% |
| 5 | `PROMOTORSTS` | varchar | 0% |
| 6 | `PKPROMOTORGRUPOID` | varchar | 5% |
| 7 | `PROMOTORGRUPONOMBRE` | varchar | 5% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_PROMOTOR
-- Extraida: 2026-08-07T15:28:15.030096+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_PROMOTOR]
AS SELECT p.EMPRESAID, p.PROMOTORID, p.PKPROMOTORID, p.PROMOTORNOMBRE, p.PROMOTORSTS, 
	   g.PKPROMOTORGRUPOID, g.PROMOTORGRUPONOMBRE
FROM SIGASC.PROMOTOR p
LEFT JOIN SIGASC.PROMOTORGRUPO g ON ( CONCAT( p.empresaid, CONCAT( '_', p.promotorgrupoid ) ) = g.pkpromotorgrupoid );
```
