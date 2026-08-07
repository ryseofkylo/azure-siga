---
esquema: dbo
tabla: V_ANALISISFAC_CONBAJAS_COMPLE
objeto: dbo.V_ANALISISFAC_CONBAJAS_COMPLE
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

# dbo.V_ANALISISFAC_CONBAJAS_COMPLE

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.FACTURARESUMENCOMPLE]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `PERIODO` | int | 0% |
| 4 | `CONTRATOS` | int | 0% |
| 5 | `SUMA_CONTRATOS` | bigint | 0% |
| 6 | `SUMA_POLITICAS` | bigint | 0% |
| 7 | `SUMA_PROMOCIONES` | bigint | 0% |
| 8 | `CLASEPRODUCTO` | int | 0% |
| 9 | `FACTURACION` | float | 0% |
| 10 | `PERIODOANTERIOR` | int | 0% |
| 11 | `IMPORTE_POL` | float | 0% |
| 12 | `IMPORTE_PRM` | float | 0% |
| 13 | `ESCALON` | int | 0% |
| 14 | `ESBAJA` | varchar | 0% |
| 15 | `CONTRATOS_PM` | int | 3% |
| 16 | `SUMA_CON_PM` | bigint | 3% |
| 17 | `SUMA_POL_PM` | bigint | 3% |
| 18 | `SUMA_PRM_PM` | bigint | 3% |
| 19 | `CLASEPROD_PM` | int | 3% |
| 20 | `FACTURACION_PM` | float | 3% |
| 21 | `VARIA_COMPOSICION` | varchar | 0% |
| 22 | `VARIA_FACTURACION` | varchar | 0% |
| 23 | `FACT_EN_CERO` | varchar | 98% |
| 24 | `VARIA_POLITICA` | varchar | 0% |
| 25 | `ESTADO` | varchar | 97% |
| 26 | `IMPORTE_POL_PM` | float | 3% |
| 27 | `IMPORTE_PRM_PM` | float | 3% |
| 28 | `ESCALON_PM` | int | 3% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ANALISISFAC_CONBAJAS_COMPLE
-- Extraida: 2026-08-07T15:27:36.371520+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_ANALISISFAC_CONBAJAS_COMPLE]
AS SELECT f.*,
			c.contratos			AS CONTRATOS_PM,
			c.suma_contratos	AS SUMA_CON_PM,
			c.suma_politicas	AS SUMA_POL_PM,
			c.suma_promociones	AS SUMA_PRM_PM,
			c.claseproducto		AS CLASEPROD_PM,
			c.facturacion		AS FACTURACION_PM,
			CASE WHEN ( f.suma_contratos <> c.suma_contratos ) THEN 'Y' ELSE 'N' END AS VARIA_COMPOSICION,
			CASE WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) > ROUND(ISNULL(c.facturacion,0),0,1) ) THEN 'Aumenta' 
				 WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) < ROUND(ISNULL(c.facturacion,0),0,1) ) THEN 'Disminuye'
				ELSE 'No varia' 
		   END AS VARIA_FACTURACION,
		   CASE WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) = 0 )	THEN 'Facturacion en cero' END AS FACT_EN_CERO,
			CASE WHEN ( f.suma_politicas <> c.suma_politicas ) THEN 'Y' ELSE 'N' END AS VARIA_POLITICA,
			CASE WHEN ( ( c.clientenro IS NULL ) OR ( c.esbaja = 'Y' ) ) THEN 'Alta'
				 WHEN ( f.esbaja = 'Y' )								 THEN 'Baja'
			END AS ESTADO,
		   c.importe_pol         AS IMPORTE_POL_PM,
		   c.importe_prm		 AS IMPORTE_PRM_PM,
		   c.escalon			AS ESCALON_PM
	FROM SIGASC.FACTURARESUMENCOMPLE f
	LEFT JOIN SIGASC.FACTURARESUMENCOMPLE c ON ( ( f.clientenro = c.clientenro ) AND ( f.periodoanterior = c.periodo ) );
```
