---
esquema: dbo
tabla: V_FACTURACLIENTE
objeto: dbo.V_FACTURACLIENTE
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 11
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_FACTURACLIENTE

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.PRODUCTO]]
- [[dbo.V_FACTURACION_PERIODO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `FACTURAFCH` | date | 0% |
| 4 | `PERIODO` | int | 0% |
| 5 | `CONTRATOS` | int | 0% |
| 6 | `SUMA_CONTRATOS` | bigint | 0% |
| 7 | `SUMA_POLITICAS` | bigint | 0% |
| 8 | `SUMA_PROMOCIONES` | bigint | 0% |
| 9 | `CLASEPRODUCTO` | int | 0% |
| 10 | `FACTURACION` | float | 0% |
| 11 | `PERIODOANTERIOR` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_FACTURACLIENTE
-- Extraida: 2026-08-07T15:27:55.750097+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_FACTURACLIENTE]
AS SELECT EMPRESAID,
		  CLIENTENRO,
		  CONVERT( DATE,FACTURAFCH )						   AS FACTURAFCH,
		  --FORMAT( FACTURAFCH, 'yyyyMM' )					   AS PERIODO,
		  FACTURAPERIODO									   AS PERIODO,
		  COUNT( DISTINCT FACTURALINCOD )					   AS CONTRATOS,
		  SUM( DISTINCT CAST(FACTURALINCOD AS BIGINT))		   AS SUMA_CONTRATOS,
		  SUM( DISTINCT CAST(FACTURAPOL	   AS BIGINT))		   AS SUMA_POLITICAS,
		  SUM(			CAST(FACTURAPRM	   AS BIGINT))		   AS SUMA_PROMOCIONES,
		  MAX( ISNULL(CLASEPRODUCTO,0) )					   AS CLASEPRODUCTO,
		  ROUND(SUM( FACTURALINIMP),2,1)					   AS FACTURACION,
		  FORMAT( 
			DATEADD( 
				MONTH, -1, CONVERT(DATE,CONCAT(SUBSTRING(STR(FACTURAPERIODO,6),0,5),CONCAT('/',CONCAT(SUBSTRING(STR(FACTURAPERIODO,6),5,2),'/01'))))
				), 'yyyyMM' ) AS PERIODOANTERIOR 
	FROM V_FACTURACION_PERIODO f
	INNER JOIN ( SELECT PRODUCTOID, 
						CASE WHEN PRODUCTONOMBRE LIKE '%CLASICO%'  THEN 1
						     WHEN PRODUCTONOMBRE LIKE '%PLUS%'	   THEN 2
							 WHEN PRODUCTONOMBRE LIKE '%FAMILIAR%' THEN 3
						END AS CLASEPRODUCTO
				FROM SIGASC.PRODUCTO 
			  ) p
	ON ( f.productoid = p.productoid )
	WHERE facturatpo = 'F'
	AND empresaid <> '23'
	AND facturaperiodo <> 0
	AND FACTURALINCOD <> 0 
	AND FORMAT(DATEADD(MONTH, 1, FACTURAFCH),'yyyyMM') <= FACTURAPERIODO
	AND DAY(FACTURAFCH) <= 20 
	AND clientenro = '26_2420404'
	GROUP BY EMPRESAID, CLIENTENRO, 
			 CONVERT( DATE,FACTURAFCH ),
			 --FORMAT( FACTURAFCH, 'YYYYMM' ), 
			 FACTURAPERIODO,
			 CONVERT(DATE, FACTURAFCH), 
			 FORMAT( 
				DATEADD( 
					MONTH, -1, CONVERT(DATE,CONCAT(SUBSTRING(STR(FACTURAPERIODO,6),0,5),CONCAT('/',CONCAT(SUBSTRING(STR(FACTURAPERIODO,6),5,2),'/01'))))
					), 'yyyyMM' );
```
