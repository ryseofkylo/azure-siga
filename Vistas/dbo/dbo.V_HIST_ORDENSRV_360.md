---
esquema: dbo
tabla: V_HIST_ORDENSRV_360
objeto: dbo.V_HIST_ORDENSRV_360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 23
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_HIST_ORDENSRV_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_ORDENSRV]]
- [[dbo.V_ORDENINSTALACION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PKORDENNRO` | varchar | 0% |
| 3 | `CLIENTENROORD` | int | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `ORDENFING` | datetime2 | 0% |
| 6 | `ORDENSOL` | varchar | 0% |
| 7 | `TECNICOID` | int | 0% |
| 8 | `MOTIVOORDID` | int | 0% |
| 9 | `MOTIVOORDINGID` | int | 0% |
| 10 | `PKPREVENTANRO` | varchar | 0% |
| 11 | `PREVENTAFCHING` | date | 0% |
| 12 | `PREVENTAFCHFIN` | date | 0% |
| 13 | `PREVENTATPO` | varchar | 0% |
| 14 | `NEGOCIOSEGMENTO` | int | 0% |
| 15 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 16 | `PROMOTORID` | int | 0% |
| 17 | `PREVENTAMEDCOBROID` | int | 0% |
| 18 | `PRODUCTOID` | int | 0% |
| 19 | `POLITICAID` | int | 0% |
| 20 | `PROMOCIONID` | int | 52% |
| 21 | `RECLAMOENGARANTIA` | varchar | 0% |
| 22 | `ORDENSTS` | nvarchar | 0% |
| 23 | `BDMODIFIEDDATE` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_HIST_ORDENSRV_360
-- Extraida: 2026-08-07T15:27:58.128488+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_HIST_ORDENSRV_360]
AS SELECT o.EMPRESAID, o.PKORDENNRO, o.CLIENTENROORD, o.CONTRATONRO, 
		   o.ORDENFING, o.ORDENSOL, o.TECNICOID, o.MOTIVOORDID, o.MOTIVOORDINGID,
		   o.PKPREVENTANRO, o.PREVENTAFCHING, o.PREVENTAFCHFIN, o.PREVENTATPO, o.NEGOCIOSEGMENTO,
		   o.NEGOCIOSEGMENTOTIPOID, o.PROMOTORID, o.PREVENTAMEDCOBROID, o.PRODUCTOID, 
		   o.POLITICAID, o.PROMOCIONID, o.RECLAMOENGARANTIA,
		   v.ORDENSTS, v.BDMODIFIEDDATE
	FROM V_ORDENINSTALACION o
	INNER JOIN SIGASC.H_ORDENSRV v ON ( o.pkordennro = v.pkordennro )
	WHERE v.bdmodifieddate >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES
	AND v.bdmodifieddate < GETDATE();
```
