---
esquema: dbo
tabla: V_COBRANZAS_ANTES
objeto: dbo.V_COBRANZAS_ANTES
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 20
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_COBRANZAS_ANTES

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.COBRANZAS_ANTES]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `RECIBONRO` | varchar | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `RECIBOFCH` | datetime2 | 0% |
| 5 | `RECIBOSTS` | varchar | 0% |
| 6 | `MEDCOBRBO` | int | 0% |
| 7 | `RECIBOIMP` | real | 0% |
| 8 | `RECIBOUSR` | varchar | 0% |
| 9 | `RECIBOGEN` | varchar | 0% |
| 10 | `RECIBOFCHCOB` | datetime2 | 0% |
| 11 | `RECIBOTPO` | varchar | 0% |
| 12 | `FACTURATPO` | varchar | 0% |
| 13 | `FACTURANRO` | varchar | 0% |
| 14 | `RECIBOFACIMPRBO` | real | 0% |
| 15 | `FACTURAFCH` | datetime2 | 0% |
| 16 | `FACTURAPERIODO` | int | 0% |
| 17 | `FACTURANEGOCIO` | varchar | 0% |
| 18 | `MONTOORIGEN` | float | 0% |
| 19 | `CONTRIBUCION` | float | 0% |
| 20 | `MONTOCOBRANZA` | float | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_COBRANZAS_ANTES
-- Extraida: 2026-08-07T15:27:47.133466+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_COBRANZAS_ANTES]
AS SELECT EMPRESAID, PKRECIBONRO AS RECIBONRO, CLIENTENRO, RECIBOFCH, RECIBOSTS, MEDCOBRBO,
		   RECIBOIMP, RECIBOUSR, RECIBOGEN, RECIBOFCHCOB,RECIBOTPO,
		   PKFACTURATPO AS FACTURATPO, PKFACTURANRO AS FACTURANRO, RECIBOFACIMPRBO,
		   FACTURAFCH, FACTURAPERIODO, FACTURANEGOCIO, MONTOORIGEN, CONTRIBUCION,
		   CASE WHEN ( pkfacturanro IS NULL ) THEN RECIBOIMP
				WHEN ( montocobranza = 0 AND facturafch IS NULL ) THEN RECIBOFACIMPRBO ELSE MONTOCOBRANZA END AS MONTOCOBRANZA
	FROM (
	    SELECT EMPRESAID, PKRECIBONRO, CLIENTENRO, RECIBOFCH, RECIBOSTS, MEDCOBRBO,
			   RECIBOIMP, RECIBOUSR, RECIBOGEN, RECIBOFCHCOB, RECIBOTPO,
			   PKFACTURATPO, PKFACTURANRO, RECIBOFACIMPRBO,
			   FACTURAFCH, FACTURAPERIODO,
			   CASE --WHEN ( ( CPTOFACID = 9343 ) AND ( PRODUCTOTPO IN ('C','L') ) ) THEN 'INT' -- CABLE MODEM o GPON
				   WHEN ( CPTOFACGRUPOID = 1 ) THEN 'TVC'
				   WHEN ( CPTOFACGRUPOID = 2 ) THEN 'INT'
				   WHEN ( CPTOFACGRUPOID = 3 ) THEN 'TEL'
				   WHEN ( CPTOFACGRUPOID = 8 ) THEN 'INT'
				   ELSE 'TVC' 
			   END AS FACTURANEGOCIO,
			   ROUND(SUM(montolinea),2)		AS MONTOORIGEN,
			   ROUND(SUM(contribucion),2)	AS CONTRIBUCION,
			   ROUND(SUM(cobranzalinea),2)	AS MONTOCOBRANZA
		FROM SIGASC.COBRANZAS_ANTES c
		--WHERE recibofch >= '2022/12/01' and recibofch < '2023/01/01'
		--and recibonro IN ('20_3876172','17_1543106')
		GROUP BY EMPRESAID, PKRECIBONRO, CLIENTENRO, RECIBOFCH, RECIBOSTS, MEDCOBRBO,
				 RECIBOIMP, RECIBOUSR, RECIBOGEN, RECIBOFCHCOB, RECIBOTPO,
				 PKFACTURATPO, PKFACTURANRO, RECIBOFACIMPRBO,
				 FACTURAFCH, FACTURAPERIODO,
				 CASE --WHEN ( ( CPTOFACID = 9343 ) AND ( PRODUCTOTPO IN ('C','L') ) ) THEN 'INT' -- CABLE MODEM o GPON
					WHEN ( CPTOFACGRUPOID = 1 ) THEN 'TVC'
					WHEN ( CPTOFACGRUPOID = 2 ) THEN 'INT'
					WHEN ( CPTOFACGRUPOID = 3 ) THEN 'TEL'
					WHEN ( CPTOFACGRUPOID = 8 ) THEN 'INT'
					ELSE 'TVC'
			     END 
	) a;
```
