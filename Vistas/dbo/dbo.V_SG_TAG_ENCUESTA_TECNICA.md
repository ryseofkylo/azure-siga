---
esquema: dbo
tabla: V_SG_TAG_ENCUESTA_TECNICA
objeto: dbo.V_SG_TAG_ENCUESTA_TECNICA
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

# dbo.V_SG_TAG_ENCUESTA_TECNICA

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_Tag]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `IDTAG` | bigint | 0% |
| 2 | `DATE` | datetime2 | 0% |
| 3 | `NAME` | nvarchar | 0% |
| 4 | `CONTEXT` | nvarchar | 0% |
| 5 | `CASOID` | bigint | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_SG_TAG_ENCUESTA_TECNICA
-- Extraida: 2026-08-07T15:28:20.282846+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_SG_TAG_ENCUESTA_TECNICA]
AS SELECT t.IDTAG,
		  t.[DATE],
		   t.NAME,
		   t.CONTEXT,
		   t.CASOID
	FROM SG_TAG t
	WHERE EXISTS (SELECT 1 FROM SG_TAG T2 
	WHERE (CONTEXT LIKE '%ENCUESTA%TECNICA%' or CONTEXT LIKE '%RECLAMO%GENERADO%')AND t.CASOID= t2.CASOID)

	AND t.casoid IN ( SELECT DISTINCT c.id FROM SG_CASO c
					  WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) );
```
