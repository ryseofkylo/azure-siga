---
esquema: dbo
tabla: V_CLIENTEDATOS_SINFILTRO
objeto: dbo.V_CLIENTEDATOS_SINFILTRO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 8
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_CLIENTEDATOS_SINFILTRO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_CONTRATO_CLIENTE]]
- [[SIGASC.PRODUCTO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PKCLIENTENRO` | nvarchar | 0% |
| 3 | `BDMODIFIEDDATE` | date | 0% |
| 4 | `NEGOCIOSEGMENTO` | int | 0% |
| 5 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 6 | `CLIENTESTS` | nvarchar | 0% |
| 7 | `CLIENTETPO` | int | 0% |
| 8 | `PRODUCTOTPO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CLIENTEDATOS_SINFILTRO
-- Extraida: 2026-08-07T15:27:44.148338+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_CLIENTEDATOS_SINFILTRO]
AS SELECT DISTINCT c.EMPRESAID, PKCLIENTENRO, CAST( c.BDMODIFIEDDATE AS DATE ) BDMODIFIEDDATE,
						NEGOCIOSEGMENTO, NEGOCIOSEGMENTOTIPOID, CLIENTESTS, CLIENTETPO, p.PRODUCTOTPO
		FROM SIGASC.H_CONTRATO_CLIENTE c
		INNER JOIN SIGASC.PRODUCTO p ON ( c.PKPRODUCTOID = p.PKPRODUCTOID )
		WHERE negociosegmento = '3' 
		AND negociosegmentotipoid = '1';
```
