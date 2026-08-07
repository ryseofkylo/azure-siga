---
esquema: dbo
tabla: V_ORDENINSTALACION
objeto: dbo.V_ORDENINSTALACION
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 32
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_ORDENINSTALACION

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.HISTORICOENTIDADREG]]
- [[SIGASC.ORDENSRV]]
- [[dbo.V_RECLAMOS_360]]

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
| 9 | `ORDENFPROCESO` | datetime2 | 1% |
| 10 | `ORDENSOL` | varchar | 0% |
| 11 | `TECNICOID` | int | 0% |
| 12 | `ORDENTRBRED` | int | 0% |
| 13 | `ORDENUSRING` | varchar | 0% |
| 14 | `MOTIVOORDID` | int | 0% |
| 15 | `MOTIVOORDINGID` | int | 0% |
| 16 | `TIENEPREVENTA` | varchar | 0% |
| 17 | `PKPREVENTANRO` | varchar | 0% |
| 18 | `PREVENTAFCHING` | date | 0% |
| 19 | `PREVENTAFCHFIN` | date | 0% |
| 20 | `PREVENTATPO` | varchar | 0% |
| 21 | `NEGOCIOSEGMENTO` | int | 0% |
| 22 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 23 | `PREVENTAUSR` | varchar | 0% |
| 24 | `PROMOTORID` | int | 0% |
| 25 | `PREVENTAMEDCOBROID` | int | 0% |
| 26 | `PRODUCTOID` | int | 0% |
| 27 | `POLITICAID` | int | 0% |
| 28 | `PROMOCIONID` | int | 48% |
| 29 | `POLITICAPRC` | float | 0% |
| 30 | `RECLAMOENGARANTIA` | varchar | 0% |
| 31 | `AGENDAMIENTOS` | int | 0% |
| 32 | `DEMORACUMPLIMIENTO` | int | 2% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ORDENINSTALACION
-- Extraida: 2026-08-07T15:28:08.498907+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_ORDENINSTALACION]
AS SELECT DISTINCT
		   o.EMPRESAID, o.ORDENNRO, o.PKORDENNRO,
		   o.CLIENTENROORD, o.CONTRATONRO, o.ORDENSTS, o.ORDENFING, o.ORDENFFIN, 
		   o.ORDENFPROCESO, o.ORDENSOL, o.TECNICOID, o.ORDENTRBRED, o.ORDENUSRING, o.MOTIVOORDID, o.MOTIVOORDINGID,
		   CASE WHEN ( p.pkpreventanro IS NOT NULL ) THEN 'SI' ELSE 'NO' END AS TIENEPREVENTA,
		   p.PKPREVENTANRO, CONVERT(date, p.PREVENTAFCHING) AS PREVENTAFCHING, CONVERT(date, p.PREVENTAFCHFIN) AS PREVENTAFCHFIN,
		   p.PREVENTATPO, p.NEGOCIOSEGMENTO, p.NEGOCIOSEGMENTOTIPOID, p.PREVENTAUSR, 
		   p.PROMOTORID, p.PREVENTAMEDCOBROID, p.PRODUCTOID, p.POLITICAID, p.PROMOCIONID, p.POLITICAPRC,
		   CASE WHEN ( r.ordennro IS NOT NULL ) THEN 'SI' ELSE 'NO' END AS RECLAMOENGARANTIA,
		   ISNULL(e.AGENDAMIENTOS,0) AS AGENDAMIENTOS,
		   DATEDIFF( DAY, m.FECHA_EMITIDA , o.ORDENFPROCESO ) AS DEMORACUMPLIMIENTO
	FROM SIGASC.ORDENSRV o
	INNER JOIN ( SELECT * FROM V_PREVENTAS_FINAL WHERE PREVENTASTS = 'F' ) p 
	ON ( ( o.empresaid = p.empresaid ) AND ( o.clientenroord = p.clientenropreventa ) AND ( o.contratonro = p.preventaprodcongen ) )
	LEFT JOIN V_RECLAMOS_360 r
	ON (     ( o.empresaid = r.empresaid ) AND ( o.clientenroord = r.clientenroord ) AND ( o.contratonro = r.contratonro )
		 AND ( r.ordenfing <= ( DATEADD( DAY, 30, o.ordenfing ) ) ) 
		 AND ( r.ordenfing >= o.ordenfing )  
	   )
	LEFT JOIN 
	( SELECT r.EMPRESAID,
			 ( SUBSTRING( HSTENTIDADREGPKVAL, CHARINDEX('|', HSTENTIDADREGPKVAL ) + 1, LEN( HSTENTIDADREGPKVAL ) ) )  AS ORDENNRO,
			 COUNT(*) AS AGENDAMIENTOS			
	  FROM SIGASC.HISTORICOENTIDADREG r
	  WHERE hstentidadregvalnew = 'AGENDADA'
	  GROUP BY r.EMPRESAID, ( SUBSTRING( HSTENTIDADREGPKVAL, CHARINDEX('|', HSTENTIDADREGPKVAL ) + 1, LEN( HSTENTIDADREGPKVAL ) ) )
	) e
	ON ( ( o.empresaid = e.empresaid ) AND ( o.ordennro = e.ordennro ) )
	LEFT JOIN
	( SELECT r.EMPRESAID,
			 ( SUBSTRING( HSTENTIDADREGPKVAL, CHARINDEX('|', HSTENTIDADREGPKVAL ) + 1, LEN( HSTENTIDADREGPKVAL ) ) )  AS ORDENNRO,
			 MAX( hstentidadregfch ) AS FECHA_EMITIDA
	  FROM SIGASC.HISTORICOENTIDADREG r
	  WHERE hstentidadregvalnew = 'EMITIDA'
	  GROUP BY r.EMPRESAID, ( SUBSTRING( HSTENTIDADREGPKVAL, CHARINDEX('|', HSTENTIDADREGPKVAL ) + 1, LEN( HSTENTIDADREGPKVAL ) ) )
	) m
	ON ( ( o.empresaid = m.empresaid ) AND ( o.ordennro = m.ordennro ) )
	WHERE o.ordentpo = 'I' -- Orden de Instalación 
	AND o.ordengen = 'C' -- Orden de Instalación "CONTRATO" ( Excluye Mudanza, Reconexión o Cambio Producto )
	AND o.ordenfing >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES
	AND o.ordenfing <  GETDATE();
```
