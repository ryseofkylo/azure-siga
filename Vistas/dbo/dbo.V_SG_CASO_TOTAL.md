---
esquema: dbo
tabla: V_SG_CASO_TOTAL
objeto: dbo.V_SG_CASO_TOTAL
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 5
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_SG_CASO_TOTAL

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_Tag]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CASOID` | bigint | 0% |
| 2 | `IDTAG` | bigint | 0% |
| 3 | `CLOSE_DATE` | date | 0% |
| 4 | `NROCLIENTE` | nvarchar | 28% |
| 5 | `CAMPAIGN` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_SG_CASO_TOTAL
-- Extraida: 2026-08-07T15:28:19.295528+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_SG_CASO_TOTAL]
AS SELECT c.id AS CASOID,
		   t.IDTAG,
		   CONVERT(DATE, c.close_date) AS CLOSE_DATE,
		   c.NROCLIENTE,
		   c.CAMPAIGN
	FROM SG_CASO c

	LEFT JOIN ( SELECT * FROM SG_TAG ) t
	ON ( c.id = t.casoid )
	WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101);
```
