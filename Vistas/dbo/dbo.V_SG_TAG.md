---
esquema: dbo
tabla: V_SG_TAG
objeto: dbo.V_SG_TAG
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 4
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_SG_TAG

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_Tag]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `IDTAG` | bigint | 0% |
| 2 | `NAME` | nvarchar | 0% |
| 3 | `CONTEXT` | nvarchar | 0% |
| 4 | `CASOID` | bigint | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_SG_TAG
-- Extraida: 2026-08-07T15:28:19.958170+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_SG_TAG]
AS SELECT t.IDTAG,
		   t.NAME,
		   t.CONTEXT,
		   t.CASOID
	FROM SG_TAG t
	WHERE NAME IN ('Cliente no responde','Cliente retenido','Imposibilidad de contacto','No retenido','No retenidos',
				   'OT Generada','RETENIDO','Solicito prioridad','Solucionado en línea' )
	AND t.casoid IN ( SELECT DISTINCT c.id FROM SG_CASO c
					  WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) );
```
