---
esquema: dbo
tabla: V_ANALISIS_FAC360
objeto: dbo.V_ANALISIS_FAC360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 31
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_ANALISIS_FAC360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.FACTURARESUMEN360]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `CONTRATONRO` | int | 0% |
| 4 | `PREVENTAFCHING` | datetime2 | 0% |
| 5 | `PREVENTAFCHFIN` | datetime2 | 0% |
| 6 | `PREVENTAPRODUCTO` | int | 0% |
| 7 | `PERIODO` | int | 0% |
| 8 | `CONTRATOS` | int | 0% |
| 9 | `SUMA_CONTRATOS` | bigint | 0% |
| 10 | `SUMA_POLITICAS` | bigint | 0% |
| 11 | `SUMA_PROMOCIONES` | bigint | 0% |
| 12 | `CLASEPRODUCTO` | int | 0% |
| 13 | `FACTURACION` | float | 0% |
| 14 | `PERIODOANTERIOR` | int | 0% |
| 15 | `IMPORTE_POL` | float | 0% |
| 16 | `IMPORTE_PRM` | float | 0% |
| 17 | `ESCALON` | int | 0% |
| 18 | `ESBAJA` | varchar | 0% |
| 19 | `CONTRATOS_PM` | int | 20% |
| 20 | `SUMA_CON_PM` | bigint | 20% |
| 21 | `SUMA_POL_PM` | bigint | 20% |
| 22 | `SUMA_PRM_PM` | bigint | 20% |
| 23 | `CLASEPROD_PM` | int | 20% |
| 24 | `FACTURACION_PM` | float | 20% |
| 25 | `VARIA_COMPOSICION` | varchar | 0% |
| 26 | `VARIA_FACTURACION` | varchar | 0% |
| 27 | `VARIA_POLITICA` | varchar | 0% |
| 28 | `ESTADO` | varchar | 80% |
| 29 | `IMPORTE_POL_PM` | float | 20% |
| 30 | `IMPORTE_PRM_PM` | float | 20% |
| 31 | `ESCALON_PM` | int | 20% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ANALISIS_FAC360
-- Extraida: 2026-08-07T15:27:35.387594+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_ANALISIS_FAC360]
AS SELECT f.*,
		   c.contratos			AS CONTRATOS_PM,
		   c.suma_contratos		AS SUMA_CON_PM,
		   c.suma_politicas		AS SUMA_POL_PM,
		   c.suma_promociones	AS SUMA_PRM_PM,
		   c.claseproducto		AS CLASEPROD_PM,
		   c.facturacion		AS FACTURACION_PM,
		   CASE WHEN ( f.suma_contratos <> c.suma_contratos ) THEN 'Y' ELSE 'N' END AS VARIA_COMPOSICION,
		   CASE WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) > ROUND(ISNULL(c.facturacion,0),0,1) ) THEN 'Aumenta' 
	   			WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) < ROUND(ISNULL(c.facturacion,0),0,1) ) THEN 'Disminuye'
				WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) = 0 )									 THEN 'Facturacion en cero' 
				ELSE 'No varia' 
		   END AS VARIA_FACTURACION,
		   CASE WHEN ( f.suma_politicas <> c.suma_politicas ) THEN 'Y' ELSE 'N' END AS VARIA_POLITICA,
		   CASE WHEN ( ( c.clientenro IS NULL ) OR ( c.esbaja = 'Y' ) ) THEN 'Alta'
				WHEN ( f.esbaja = 'Y' )									THEN 'Baja'
		   END AS ESTADO,
		   c.importe_pol         AS IMPORTE_POL_PM,
		   c.importe_prm		 AS IMPORTE_PRM_PM,
		   c.escalon			 AS ESCALON_PM
	FROM SIGASC.FACTURARESUMEN360 f
	LEFT JOIN SIGASC.FACTURARESUMEN360 c 
	ON ( ( f.clientenro = c.clientenro ) AND ( f.contratonro = c.contratonro ) AND ( f.periodoanterior = c.periodo ) );
```
