---
esquema: dbo
tabla: V_BAJASPERIODO_23
objeto: dbo.V_BAJASPERIODO_23
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 13
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_BAJASPERIODO_23

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.FACTURACLIENTE_23]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `PERIODO` | nvarchar | 0% |
| 4 | `CONTRATOS` | int | 0% |
| 5 | `SUMA_CONTRATOS` | int | 0% |
| 6 | `SUMA_POLITICAS` | int | 0% |
| 7 | `SUMA_PROMOCIONES` | int | 0% |
| 8 | `CLASEPRODUCTO` | int | 0% |
| 9 | `FACTURACION` | int | 0% |
| 10 | `PERIODOANTERIOR` | int | 0% |
| 11 | `IMPORTE_POL` | int | 0% |
| 12 | `IMPORTE_PRM` | int | 0% |
| 13 | `ESCALON` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_BAJASPERIODO_23
-- Extraida: 2026-08-07T15:27:39.798814+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_BAJASPERIODO_23]
AS SELECT EMPRESAID, CLIENTENRO,
		   FORMAT( 
				DATEADD( MONTH, 1, CONVERT(DATE,CONCAT(SUBSTRING(STR(PERIODO,6),0,5),CONCAT('/',CONCAT(SUBSTRING(STR(PERIODO,6),5,2),'/01'))))
				  ), 'yyyyMM' ) AS PERIODO,
		   0 AS CONTRATOS,
		   0 AS SUMA_CONTRATOS,
		   0 AS SUMA_POLITICAS,
		   0 AS SUMA_PROMOCIONES,
		   0 AS CLASEPRODUCTO,
		   0 AS FACTURACION,
		   ( periodo ) AS PERIODOANTERIOR,
		   0 AS IMPORTE_POL,
		   0 AS IMPORTE_PRM,
		   0 AS ESCALON
	FROM SIGASC.FACTURACLIENTE_23 c
	WHERE periodo NOT IN ( SELECT DISTINCT PERIODOANTERIOR from SIGASC.FACTURACLIENTE_23 f where f.clientenro = c.clientenro );
```
