---
esquema: dbo
tabla: V_COBRANZAS_2
objeto: dbo.V_COBRANZAS_2
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

# dbo.V_COBRANZAS_2

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.COBRANZAS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int |  |
| 2 | `RECIBONRO` | varchar |  |
| 3 | `CLIENTENRO` | int |  |
| 4 | `RECIBOFCH` | datetime2 |  |
| 5 | `RECIBOSTS` | varchar |  |
| 6 | `MEDCOBRBO` | int |  |
| 7 | `RECIBOIMP` | float |  |
| 8 | `RECIBOUSR` | varchar |  |
| 9 | `RECIBOGEN` | varchar |  |
| 10 | `RECIBOFCHCOB` | datetime2 |  |
| 11 | `RECIBOTPO` | varchar |  |
| 12 | `FACTURATPO` | varchar |  |
| 13 | `FACTURANRO` | varchar |  |
| 14 | `RECIBOFACIMP` | float |  |
| 15 | `FACTURAFCH` | datetime2 |  |
| 16 | `FACTURAPERIODO` | int |  |
| 17 | `FACTURANEGOCIO` | varchar |  |
| 18 | `MONTOORIGEN` | float |  |
| 19 | `CONTRIBUCION` | float |  |
| 20 | `MONTOCOBRANZA` | float |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_COBRANZAS_2
-- Extraida: 2026-08-07T15:27:46.807755+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_COBRANZAS_2]
AS SELECT EMPRESAID,
RECIBONRO, CLIENTENRO, RECIBOFCH, RECIBOSTS, MEDCOBRBO,
RECIBOIMP, RECIBOUSR, RECIBOGEN, RECIBOFCHCOB,RECIBOTPO,
FACTURATPO, FACTURANRO, RECIBOFACIMP,
FACTURAFCH, FACTURAPERIODO,
CASE --WHEN ( ( CPTOFACID = 9343 ) AND ( PRODUCTOTPO IN ('C','L') ) ) THEN 'INT' -- CABLE MODEM o GPON
	 WHEN ( CPTOFACGRUPOID = 1 ) THEN 'TVC'
	 WHEN ( CPTOFACGRUPOID = 2 ) THEN 'INT'
	 WHEN ( CPTOFACGRUPOID = 3 ) THEN 'TEL'
	 WHEN ( CPTOFACGRUPOID = 8 ) THEN 'INT'
ELSE 'TVC' END AS FACTURANEGOCIO,
ROUND(SUM(montolinea),2) AS MONTOORIGEN,
ROUND(SUM(contribucion),2) AS CONTRIBUCION,
ROUND(SUM(cobranzalinea),2) AS MONTOCOBRANZA
FROM SIGASC.COBRANZAS c
--where recibonro = '2_9623998'--'1_23079248'
GROUP BY EMPRESAID,
RECIBONRO, CLIENTENRO, RECIBOFCH, RECIBOSTS, MEDCOBRBO,
RECIBOIMP, RECIBOUSR, RECIBOGEN, RECIBOFCHCOB, RECIBOTPO,
FACTURATPO, FACTURANRO, RECIBOFACIMP,
FACTURAFCH, FACTURAPERIODO,
CASE --WHEN ( ( CPTOFACID = 9343 ) AND ( PRODUCTOTPO IN ('C','L') ) ) THEN 'INT' -- CABLE MODEM o GPON
	 WHEN ( CPTOFACGRUPOID = 1 ) THEN 'TVC'
	 WHEN ( CPTOFACGRUPOID = 2 ) THEN 'INT'
	 WHEN ( CPTOFACGRUPOID = 3 ) THEN 'TEL'
	 WHEN ( CPTOFACGRUPOID = 8 ) THEN 'INT'
ELSE 'TVC' END;
```
