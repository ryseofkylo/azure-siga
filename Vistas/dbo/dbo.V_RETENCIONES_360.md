---
esquema: dbo
tabla: V_RETENCIONES_360
objeto: dbo.V_RETENCIONES_360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 26
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_RETENCIONES_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_RETENCIONES]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CONTRATONRO` | varchar | 0% |
| 3 | `CLIENTENRO` | varchar | 0% |
| 4 | `PROMOCIONID` | varchar | 0% |
| 5 | `PRODUCTOID` | varchar | 0% |
| 6 | `CONTRATOPRMFCH` | date | 0% |
| 7 | `CONTRATOPRMFFIN` | date | 36% |
| 8 | `CONTRATOPRMFCHCXL` | date | 74% |
| 9 | `CONTRATOPRMUSR` | varchar | 0% |
| 10 | `CONTRATOPRMSTS` | varchar | 0% |
| 11 | `CONTRATOPRMMES` | int | 0% |
| 12 | `promocionclase` | varchar | 0% |
| 13 | `PKPREVENTANRO` | varchar | 0% |
| 14 | `PREVENTATPO` | varchar | 0% |
| 15 | `NEGOCIOSEGMENTO` | int | 0% |
| 16 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 17 | `PREVENTAUSR` | varchar | 0% |
| 18 | `PROMOTORID` | int | 0% |
| 19 | `PREVENTAMEDCOBROID` | int | 0% |
| 20 | `PRODUCTO_PREVENTA` | int | 0% |
| 21 | `POLITICAID` | int | 0% |
| 22 | `PROMO_PREVENTA` | int | 0% |
| 23 | `POLITICAPRC` | float | 0% |
| 24 | `PREVENTAFCHING` | date | 0% |
| 25 | `PREVENTAFCHFIN` | date | 0% |
| 26 | `DIASPREVENTA` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_RETENCIONES_360
-- Extraida: 2026-08-07T15:28:17.957303+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_RETENCIONES_360]
AS SELECT o.*,
		   p.PKPREVENTANRO, p.PREVENTATPO, p.NEGOCIOSEGMENTO, p.NEGOCIOSEGMENTOTIPOID, p.PREVENTAUSR, 
		   p.PROMOTORID, p.PREVENTAMEDCOBROID, p.PRODUCTOID AS PRODUCTO_PREVENTA, p.POLITICAID, p.PROMOCIONID AS PROMO_PREVENTA,
		   p.POLITICAPRC, CONVERT(date, p.PREVENTAFCHING) AS PREVENTAFCHING, CONVERT(date, p.PREVENTAFCHFIN) AS PREVENTAFCHFIN,
		   datediff(day,PREVENTAFCHING,contratoprmfch) AS DIASPREVENTA
	FROM V_RETENCIONES o
	INNER JOIN ( SELECT * FROM V_PREVENTAS_FINAL WHERE PREVENTASTS = 'F' ) p 
	ON (     ( o.empresaid = p.empresaid ) 
		 AND ( o.clientenro =  CONCAT( p.empresaid, CONCAT( '_',  p.clientenropreventa ) ) )
		 AND ( o.contratonro = CONCAT( p.empresaid, CONCAT( '_', p.preventaprodcongen  ) ) )
	)	
	WHERE contratoprmfch >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES
	AND contratoprmfch <  GETDATE();
```
