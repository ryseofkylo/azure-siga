---
esquema: dbo
tabla: V_RECLAMOS_360
objeto: dbo.V_RECLAMOS_360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 28
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_RECLAMOS_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.ORDENSRV]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ORDENNRO` | int | 0% |
| 3 | `PKORDENNRO` | varchar | 0% |
| 4 | `CLIENTENROORD` | int | 0% |
| 5 | `CONTRATONRO` | int | 0% |
| 6 | `ORDENSTS` | varchar | 0% |
| 7 | `ORDENFING` | datetime2 | 0% |
| 8 | `ORDENFFIN` | datetime2 | 1% |
| 9 | `ORDENFPROCESO` | datetime2 | 0% |
| 10 | `ORDENSOL` | varchar | 0% |
| 11 | `TECNICOID` | int | 0% |
| 12 | `ORDENTRBRED` | int | 0% |
| 13 | `ORDENUSRING` | varchar | 0% |
| 14 | `MOTIVOORDID` | int | 0% |
| 15 | `MOTIVOORDINGID` | int | 0% |
| 16 | `PKPREVENTANRO` | varchar | 0% |
| 17 | `PREVENTATPO` | varchar | 0% |
| 18 | `NEGOCIOSEGMENTO` | int | 0% |
| 19 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 20 | `PREVENTAUSR` | varchar | 0% |
| 21 | `PROMOTORID` | int | 0% |
| 22 | `PREVENTAMEDCOBROID` | int | 0% |
| 23 | `PRODUCTOID` | int | 0% |
| 24 | `POLITICAID` | int | 0% |
| 25 | `PROMOCIONID` | int | 30% |
| 26 | `POLITICAPRC` | float | 0% |
| 27 | `PREVENTAFCHING` | datetime2 | 0% |
| 28 | `PREVENTAFCHFIN` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_RECLAMOS_360
-- Extraida: 2026-08-07T15:28:15.678301+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_RECLAMOS_360]
AS SELECT o.EMPRESAID, o.ORDENNRO, o.PKORDENNRO,
		   o.CLIENTENROORD, o.CONTRATONRO, o.ORDENSTS, o.ORDENFING, o.ORDENFFIN, 
		   o.ORDENFPROCESO, o.ORDENSOL, o.TECNICOID, o.ORDENTRBRED, o.ORDENUSRING, o.MOTIVOORDID, o.MOTIVOORDINGID,
		   p.PKPREVENTANRO, p.PREVENTATPO, p.NEGOCIOSEGMENTO, p.NEGOCIOSEGMENTOTIPOID, p.PREVENTAUSR, 
		   p.PROMOTORID, p.PREVENTAMEDCOBROID, p.PRODUCTOID, p.POLITICAID, p.PROMOCIONID,
		   p.POLITICAPRC, p.PREVENTAFCHING, p.PREVENTAFCHFIN
	FROM SIGASC.ORDENSRV o
	INNER JOIN ( SELECT * FROM V_PREVENTAS_FINAL WHERE PREVENTASTS = 'F' ) p 
	ON (     ( o.empresaid = p.empresaid ) AND ( o.clientenroord =  p.clientenropreventa ) AND ( o.contratonro = p.preventaprodcongen ) )
	WHERE ordentpo = 'R'
	AND ordenfing >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES
	AND ordenfing <  GETDATE();
```
