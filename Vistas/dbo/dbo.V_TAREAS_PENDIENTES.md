---
esquema: dbo
tabla: V_TAREAS_PENDIENTES
objeto: dbo.V_TAREAS_PENDIENTES
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 41
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_TAREAS_PENDIENTES

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.ORDENES_PENDIENTES]]
- [[SIGASC.PRODUCTOTPO]]
- [[dbo.V_ORD_PENDIENTES_INDICADORES]]
- [[dbo.V_ORD_PENDIENTES_INDIC_2]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `SUCURSALID` | int | 0% |
| 3 | `TAREAID` | varchar | 0% |
| 4 | `ESTADOORDEN` | varchar | 0% |
| 5 | `PRODUCTOCATV` | varchar | 15% |
| 6 | `PRODUCTOINTERNET` | varchar | 84% |
| 7 | `DERIVADOS` | int | 77% |
| 8 | `DECODERS` | int | 92% |
| 9 | `TIPOORDEN` | varchar | 0% |
| 10 | `MOTIVOINGRESO` | int | 0% |
| 11 | `MOTIVOID` | int | 0% |
| 12 | `FORMAGENERADA` | varchar | 0% |
| 13 | `CENTROOPERATIVOID` | varchar | 0% |
| 14 | `CLIENTENRO` | varchar | 0% |
| 15 | `ESTADOCLIENTE` | varchar | 0% |
| 16 | `FECHAINGRESO` | datetime2 | 0% |
| 17 | `HORAINGRESO` | datetime2 | 100% |
| 18 | `FECHAFINALIZADA` | datetime2 | 96% |
| 19 | `HORAFINALIZADA` | datetime2 | 100% |
| 20 | `FECHAPROCESADA` | datetime2 | 80% |
| 21 | `HORAPROCESADA` | datetime2 | 100% |
| 22 | `DEMORAPENDIENTE` | int | 0% |
| 23 | `FECHAAGENDADA` | datetime2 | 78% |
| 24 | `TURNOID` | varchar | 79% |
| 25 | `ORDENTRBRED` | int | 0% |
| 26 | `MOTIVOSOLUCION` | varchar | 15% |
| 27 | `ZONAHABID` | varchar | 8% |
| 28 | `ZONAPELID` | varchar | 94% |
| 29 | `CONTRATOS` | varchar | 0% |
| 30 | `ORDENFCHCONEXIONFUTURA` | datetime2 | 100% |
| 31 | `ORDENTIPOCONEXION` | varchar | 0% |
| 32 | `COD_MZN` | varchar | 0% |
| 33 | `FACTURATOTAL` | float | 14% |
| 34 | `TECNICOID` | int | 15% |
| 35 | `TENICOID2` | int | 15% |
| 36 | `MOVILES` | varchar | 15% |
| 37 | `PRODUCTOTPOLISTA` | varchar | 58% |
| 38 | `DERIVADOS_ACTUAL` | int | 0% |
| 39 | `DECODERS_ACTUAL` | int | 0% |
| 40 | `EXTENSORES_ACTUAL` | int | 0% |
| 41 | `CATEGORIAAGRUPACION` | varchar | 4% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_TAREAS_PENDIENTES
-- Extraida: 2026-08-07T15:28:21.909612+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_TAREAS_PENDIENTES]
AS SELECT DISTINCT
	   p.empresaid				AS EMPRESAID,
	   p.sucursalid				AS SUCURSALID,
	   p.tareaid				AS TAREAID,
	   p.estadoorden			AS ESTADOORDEN,
	   a.productotponombre		AS PRODUCTOCATV,
	   b.productotponombre		AS PRODUCTOINTERNET,
	   ad.derivados				AS DERIVADOS,
	   deco.decoders			AS DECODERS,
	   p.tipoorden				AS TIPOORDEN,
	   FIRST_VALUE(p.motivoingreso) OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, motivoingreso ) AS MOTIVOINGRESO,
	   FIRST_VALUE(p.motivoid)		OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, motivoid )	  AS MOTIVOID,
	   p.formagenerada			AS FORMAGENERADA,
	   p.centrooperativoid		AS CENTROOPERATIVOID,
	   p.clientenro				AS CLIENTENRO,
	   p.estadocliente			AS ESTADOCLIENTE,
	   ind.fechaingreso			AS FECHAINGRESO,
	   ind.horaingreso			AS HORAINGRESO,
	   ind.fechafinalizada		AS FECHAFINALIZADA,
	   ind.horafinalizada		AS HORAFINALIZADA,
	   ind.fechaprocesada		AS FECHAPROCESADA,
	   ind.horaprocesada		AS HORAPROCESADA,
	   ind.demorapendiente		AS DEMORAPENDIENTE,
	   ind.fechaagendada		AS FECHAAGENDADA,
	   FIRST_VALUE(tur.turnoid)				OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, tur.turnoid )	  AS TURNOID,
	   FIRST_VALUE(p.ordentrbred)			OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, ordentrbred )	  AS ORDENTRBRED,
	   indic.motivosolucion		AS MOTIVOSOLUCION,
	   p.zonahabid				AS ZONAHABID,
	   p.zonapelid				AS ZONAPELID,
	   ct.contratos				AS CONTRATOS,
	   MAX( p.ordenfchconexionfutura )      OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid ) AS ORDENFCHCONEXIONFUTURA,
	   CASE 
		WHEN p.ordentipoconexion IS NULL OR p.ordentipoconexion='' OR p.ordentipoconexion=' ' 
		THEN 'P'
		ELSE p.ordentipoconexion
		END						AS ORDENTIPOCONEXION,
	   p.cod_mzn				AS COD_MZN,
	   p.facturatotal			AS FACTURATOTAL,
	   indic.tecnicoid			AS TECNICOID,
	   --FIRST_VALUE(tec.tecnicoempleadonro)	OVER ( PARTITION BY p.tareaid ORDER BY p.tareaid, tec.tecnicoempleadonro ) AS TECNICOEMPLEADONRO,
	   indic.tecnicoid2			AS TENICOID2,
	   indic.moviles			AS MOVILES,
	   p.productotpolista		AS PRODUCTOTPOLISTA,
	   p.derivados				AS DERIVADOS_ACTUAL,
	   p.decoders				AS DECODERS_ACTUAL,
	   p.extensores				AS EXTENSORES_ACTUAL,
	   p.categoriaagrupacion	AS CATEGORIAAGRUPACION	   
FROM SIGASC.ORDENES_PENDIENTES p
LEFT JOIN (
	SELECT a.TAREAID, STRING_AGG( productotponombre, ' | ') WITHIN GROUP ( ORDER BY productotponombre ) AS PRODUCTOTPONOMBRE
	FROM (
			SELECT p.TAREAID, o.PRODUCTOTPONOMBRE
			FROM SIGASC.ORDENES_PENDIENTES p INNER JOIN SIGASC.PRODUCTOTPO o ON ( p.tipoproducto = o.productotpo ) 
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
			FROM SIGASC.ORDENES_PENDIENTES p INNER JOIN SIGASC.PRODUCTOTPO o ON ( p.tipoproducto = o.productotpo )
			WHERE o.productotpo IN ('E','C','I','N','L','S','T') -- PRODUCTOS INTERNET
			GROUP BY p.tareaid, o.productotponombre
		 ) a
	GROUP BY tareaid
	) b
ON ( b.tareaid = p.tareaid )
LEFT JOIN (
	SELECT p.TAREAID, COUNT( DISTINCT p.productoid ) AS DERIVADOS
	FROM SIGASC.ORDENES_PENDIENTES p 
	WHERE p.tipoproducto = 'R'
	GROUP BY p.tareaid
	) ad
ON ( ad.tareaid = p.tareaid )
LEFT JOIN (
	SELECT p.TAREAID, COUNT( DISTINCT p.productoid ) AS DECODERS
	FROM SIGASC.ORDENES_PENDIENTES p
	WHERE p.tipoproducto = 'D'
	GROUP BY p.tareaid
	) deco
ON ( deco.tareaid = p.tareaid )
LEFT JOIN V_ORD_PENDIENTES_INDICADORES ind ON ( ind.tareaid = p.tareaid )
LEFT JOIN ( SELECT TAREAID, FECHAAGENDADA, TURNOID FROM SIGASC.ORDENES_PENDIENTES GROUP BY TAREAID, FECHAAGENDADA, TURNOID ) tur
ON ( ( tur.tareaid = p.tareaid ) AND ( tur.fechaagendada = ind.fechaagendada ) )
LEFT JOIN V_ORD_PENDIENTES_INDIC_2 indic ON ( indic.tareaid = p.tareaid )
LEFT JOIN ( SELECT TAREAID, TECNICOID, TECNICOEMPLEADONRO FROM SIGASC.ORDENES_PENDIENTES GROUP BY TAREAID, TECNICOID, TECNICOEMPLEADONRO ) tec
ON ( ( tec.tareaid = p.tareaid ) AND ( tec.tecnicoid = indic.tecnicoid ) )
LEFT JOIN ( SELECT TAREAID, STRING_AGG( pkcontratonro, ' | ') WITHIN GROUP ( ORDER BY pkcontratonro ) AS CONTRATOS
		    FROM SIGASC.ORDENES_PENDIENTES GROUP BY TAREAID ) ct
ON ( p.tareaid = ct.tareaid )
WHERE --p.tareaid <> '-I-C'
	(
    (p.tipoorden = 'I' AND p.tipoproducto IN ('R', 'D', 'C', 'B', 'L', 'Z', 'E', 'W', 'T', 'N', 'I', 'S'))
    OR
    (p.tipoorden = 'D' AND p.tipoproducto IN ('B', 'W', 'T', 'N', 'I', 'S'))
	OR
    (p.tipoorden = 'R')
    )
	AND
	p.clientenro IS NOT NULL;
```
