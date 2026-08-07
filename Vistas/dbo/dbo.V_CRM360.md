---
esquema: dbo
tabla: V_CRM360
objeto: dbo.V_CRM360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 12
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_CRM360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_CRMREGISTRO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `CRMNRO` | varchar | 0% |
| 4 | `CRMFCHINI` | date | 0% |
| 5 | `CRMSTS` | varchar | 0% |
| 6 | `CRMMEDIO` | varchar | 0% |
| 7 | `CRMUSRACT` | varchar | 0% |
| 8 | `CRMUSRING` | varchar | 0% |
| 9 | `MOTIVOID` | varchar | 0% |
| 10 | `PKPREVENTANRO` | varchar | 0% |
| 11 | `PREVENTAFCHING` | datetime2 | 0% |
| 12 | `PREVENTAFCHFIN` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CRM360
-- Extraida: 2026-08-07T15:27:51.110741+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_CRM360]
AS SELECT DISTINCT o.EMPRESAID, o.CLIENTENRO, o.CRMNRO, o.CRMFCHINI, o.CRMSTS, o.CRMMEDIO, o.CRMUSRACT, o.CRMUSRING, o.MOTIVOID,
					p.PKPREVENTANRO, p.PREVENTAFCHING, p.PREVENTAFCHFIN
	FROM V_CRMREGISTRO o
	INNER JOIN ( SELECT * FROM V_PREVENTAS_FINAL WHERE PREVENTASTS = 'F' ) p 
	ON (     ( o.empresaid = p.empresaid ) 
		 AND ( o.clientenro = CONCAT( p.empresaid, CONCAT( '_' , p.clientenropreventa ) ) )
		 AND ( o.CRMFCHINI >= p.PREVENTAFCHING )
	   )
	WHERE crmfchini >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES
--	WHERE crmfchini >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES
	AND crmfchini <  GETDATE();
```
