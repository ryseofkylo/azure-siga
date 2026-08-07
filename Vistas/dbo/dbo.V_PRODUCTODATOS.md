---
esquema: dbo
tabla: V_PRODUCTODATOS
objeto: dbo.V_PRODUCTODATOS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 7
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_PRODUCTODATOS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_CONTRATO_CLIENTE]]
- [[dbo.V_CLIENTESPRODDATOS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PKCLIENTENRO` | nvarchar | 0% |
| 3 | `BDMODIFIEDDATE` | date | 0% |
| 4 | `NEGOCIOSEGMENTO` | int | 0% |
| 5 | `NEGOCIOSEGMENTOTIPOID` | int | 12% |
| 6 | `CLIENTESTS` | nvarchar | 0% |
| 7 | `CLIENTETPO` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_PRODUCTODATOS
-- Extraida: 2026-08-07T15:28:13.410750+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_PRODUCTODATOS]
AS SELECT DISTINCT e.EMPRESAID, e.PKCLIENTENRO, CAST( e.BDMODIFIEDDATE AS DATE ) AS BDMODIFIEDDATE,
				e.NEGOCIOSEGMENTO, e.NEGOCIOSEGMENTOTIPOID, e.CLIENTESTS, e.CLIENTETPO
FROM (
		SELECT *
		FROM SIGASC.H_CONTRATO_CLIENTE c
		WHERE pkclientenro IN ( SELECT DISTINCT PKCLIENTENRO FROM SIGASC.H_CONTRATO_CLIENTE
								WHERE negociosegmento = '3' AND negociosegmentotipoid = '1' )
	 ) e
LEFT JOIN V_CLIENTESPRODDATOS v ON ( e.pkclientenro = v.pkclientenro ) 
WHERE v.pkclientenro IS NULL;
```
