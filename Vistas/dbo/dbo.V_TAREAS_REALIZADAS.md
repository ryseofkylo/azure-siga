---
esquema: dbo
tabla: V_TAREAS_REALIZADAS
objeto: dbo.V_TAREAS_REALIZADAS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 42
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_TAREAS_REALIZADAS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.ORDENES_REALIZADAS]]
- [[SIGASC.PRODUCTOTPO]]
- [[dbo.V_ORD_REALIZADAS_INDICADORES]]
- [[dbo.V_ORD_REALIZADAS_INDIC_2]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int |  |
| 2 | `SUCURSALID` | int |  |
| 3 | `TAREAID` | varchar |  |
| 4 | `PRODUCTOCATV` | varchar |  |
| 5 | `PRODUCTOINTERNET` | varchar |  |
| 6 | `DERIVADOS` | int |  |
| 7 | `DECODERS` | int |  |
| 8 | `TIPOORDEN` | varchar |  |
| 9 | `ESTADOORDEN` | varchar |  |
| 10 | `MOTIVOINGRESO` | int |  |
| 11 | `MOTIVOID` | int |  |
| 12 | `FORMAGENERADA` | varchar |  |
| 13 | `CENTROOPERATIVOID` | varchar |  |
| 14 | `CLIENTENRO` | varchar |  |
| 15 | `ESTADOCLIENTE` | varchar |  |
| 16 | `FECHAINGRESO` | datetime2 |  |
| 17 | `HORAINGRESO` | datetime2 |  |
| 18 | `FECHAFINALIZADA` | datetime2 |  |
| 19 | `HORAFINALIZADA` | datetime2 |  |
| 20 | `FECHAPROCESADA` | datetime2 |  |
| 21 | `HORAPROCESADA` | datetime2 |  |
| 22 | `FECHAAGENDADA` | datetime2 |  |
| 23 | `TURNOID` | varchar |  |
| 24 | `TECNICOID` | int |  |
| 25 | `DEMORATOTAL` | int |  |
| 26 | `TECNICOEMPLEADONRO` | int |  |
| 27 | `ORDENTRBRED` | int |  |
| 28 | `MOTIVOSOLUCION` | varchar |  |
| 29 | `ZONAHABID` | varchar |  |
| 30 | `ZONAPELID` | varchar |  |
| 31 | `CONTRATOS` | varchar |  |
| 32 | `ORDENFCHCONEXIONFUTURA` | datetime2 |  |
| 33 | `ORDENTIPOCONEXION` | varchar |  |
| 34 | `COD_MZN` | varchar |  |
| 35 | `FACTURATOTAL` | float |  |
| 36 | `TENICOID2` | int |  |
| 37 | `MOVILES` | varchar |  |
| 38 | `PRODUCTOTPOLISTA` | varchar |  |
| 39 | `DERIVADOS_ACTUAL` | int |  |
| 40 | `DECODERS_ACTUAL` | int |  |
| 41 | `EXTENSORES_ACTUAL` | int |  |
| 42 | `CATEGORIAAGRUPACION` | varchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_TAREAS_REALIZADAS
-- Extraida: 2026-08-07T15:28:22.238373+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_TAREAS_REALIZADAS]
AS SELECT DISTINCT --top 10
	   p.empresaid			AS EMPRESAID,
	   p.sucursalid			AS SUCURSALID,
	   p.tareaid			AS TAREAID,
	   a.productotponombre	AS PRODUCTOCATV,
	   b.productotponombre	AS PRODUCTOINTERNET,
	   ad.derivados			AS DERIVADOS,
	   deco.decoders		AS DECODERS,
	   p.tipoorden			AS TIPOORDEN,
	   p.estadoorden		AS ESTADOORDEN,
	   FIRST_VALUE(p.motivoingreso) OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, motivoingreso ) AS MOTIVOINGRESO,
	   FIRST_VALUE(p.motivoid)		OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, motivoid )	  AS MOTIVOID,
	   p.formagenerada		AS FORMAGENERADA,
	   p.centrooperativoid	AS CENTROOPERATIVOID, 
	   p.clientenro			AS CLIENTENRO,
	   p.estadocliente		AS ESTADOCLIENTE,
	   ind.fechaingreso		AS FECHAINGRESO,
	   ind.horaingreso		AS HORAINGRESO,
	   ind.fechafinalizada	AS FECHAFINALIZADA,
	   ind.horafinalizada	AS HORAFINALIZADA,
	   ind.fechaprocesada	AS FECHAPROCESADA,
	   ind.horaprocesada	AS HORAPROCESADA,
	   ind.fechaagendada	AS FECHAAGENDADA,
	   FIRST_VALUE(tur.turnoid)				OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, tur.turnoid )	  AS TURNOID,
	   indic.tecnicoid		AS TECNICOID,
	   ind.demoratotal		AS DEMORATOTAL,
	   FIRST_VALUE(tec.tecnicoempleadonro)	OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, tec.tecnicoempleadonro ) AS TECNICOEMPLEADONRO,
	   FIRST_VALUE(p.ordentrbred)			OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, ordentrbred )	  AS ORDENTRBRED,
	   indic.motivosolucion	AS MOTIVOSOLUCION,
	   p.zonahabid			AS ZONAHABID,
	   p.zonapelid			AS ZONAPELID,
	   ct.contratos			AS CONTRATOS,
	   MAX( p.ordenfchconexionfutura )      OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid ) AS ORDENFCHCONEXIONFUTURA,
	   TRIM(p.ordentipoconexion)	AS ORDENTIPOCONEXION,
	   p.cod_mzn			AS COD_MZN,
	   p.facturatotal		AS FACTURATOTAL,
	   indic.tecnicoid2		AS TENICOID2,
	   indic.moviles		AS MOVILES,
	   p.productotpolista	AS PRODUCTOTPOLISTA,
	   p.derivados			AS DERIVADOS_ACTUAL,
	   p.decoders			AS DECODERS_ACTUAL,
	   p.extensores			AS EXTENSORES_ACTUAL,
	   p.categoriaagrupacion AS CATEGORIAAGRUPACION	   
FROM SIGASC.ORDENES_REALIZADAS p
LEFT JOIN (
	SELECT a.TAREAID, STRING_AGG( productotponombre, ' | ') WITHIN GROUP ( ORDER BY productotponombre ) AS PRODUCTOTPONOMBRE
	FROM (
			SELECT p.TAREAID, o.PRODUCTOTPONOMBRE
			FROM SIGASC.ORDENES_REALIZADAS p INNER JOIN SIGASC.PRODUCTOTPO o ON ( p.tipoproducto = o.productotpo ) 
			WHERE o.productotpo IN ('B','W','Z') -- PRODUCTOS CABLE
			GROUP BY p.tareaid, o.productotponombre
		 ) a
	GROUP BY tareaid
	) a 
ON ( a.tareaid = p.tareaid )
LEFT JOIN (
	SELECT TAREAID, STRING_AGG( productotponombre, ' | ') WITHIN GROUP ( ORDER BY productotponombre ) AS PRODUCTOTPONOMBRE
	FROM (
			SELECT p.TAREAID, o.PRODUCTOTPONOMBRE
			FROM SIGASC.ORDENES_REALIZADAS p INNER JOIN SIGASC.PRODUCTOTPO o ON ( p.tipoproducto = o.productotpo )
			WHERE o.productotpo IN ('E','C','I','N','L') -- PRODUCTOS INTERNET
			GROUP BY p.tareaid, o.productotponombre
		 ) a
	GROUP BY tareaid
	) b
ON ( b.tareaid = p.tareaid )
LEFT JOIN (
	SELECT p.TAREAID, COUNT( DISTINCT p.productoid ) AS DERIVADOS
	FROM SIGASC.ORDENES_REALIZADAS p 
	WHERE p.tipoproducto = 'R'
	GROUP BY p.tareaid
	) ad
ON ( ad.tareaid = p.tareaid )
LEFT JOIN (
	SELECT p.TAREAID, COUNT( DISTINCT p.productoid ) AS DECODERS
	FROM SIGASC.ORDENES_REALIZADAS p
	WHERE p.tipoproducto = 'D'
	GROUP BY p.tareaid
	) deco
ON ( deco.tareaid = p.tareaid )
LEFT JOIN V_ORD_REALIZADAS_INDICADORES ind ON ( ind.tareaid = p.tareaid )
LEFT JOIN ( SELECT TAREAID, FECHAAGENDADA, TURNOID FROM SIGASC.ORDENES_REALIZADAS GROUP BY TAREAID, FECHAAGENDADA, TURNOID ) tur
ON ( ( tur.tareaid = p.tareaid ) AND ( tur.fechaagendada = ind.fechaagendada ) )
LEFT JOIN V_ORD_REALIZADAS_INDIC_2 indic ON ( indic.tareaid = p.tareaid )
LEFT JOIN ( SELECT TAREAID, TECNICOID, TECNICOEMPLEADONRO FROM SIGASC.ORDENES_REALIZADAS GROUP BY TAREAID, TECNICOID, TECNICOEMPLEADONRO ) tec
ON ( ( tec.tareaid = p.tareaid ) AND ( tec.tecnicoid = indic.tecnicoid ) )
LEFT JOIN ( SELECT TAREAID, STRING_AGG( pkcontratonro, ' | ') WITHIN GROUP ( ORDER BY pkcontratonro ) AS CONTRATOS
		    FROM SIGASC.ORDENES_REALIZADAS GROUP BY TAREAID ) ct
ON ( p.tareaid = ct.tareaid )
WHERE p.tareaid <> '-I-C'
	AND (
		(p.tipoorden = 'I' AND p.tipoproducto IN ('R', 'D', 'C', 'B', 'L', 'Z', 'E', 'W'))
		OR
		(p.tipoorden = 'D' AND p.tipoproducto IN ('B', 'W'))
		OR
		(p.tipoorden = 'R')
		)
		AND
		p.clientenro IS NOT NULL
		AND 
		p.estadoorden IN ('F','C');
```
