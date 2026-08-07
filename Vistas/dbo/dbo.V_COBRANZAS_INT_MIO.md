---
esquema: dbo
tabla: V_COBRANZAS_INT_MIO
objeto: dbo.V_COBRANZAS_INT_MIO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 1
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_COBRANZAS_INT_MIO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
_(no resueltas)_

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PKRECIBONRO` | varchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_COBRANZAS_INT_MIO
-- Extraida: 2026-08-07T15:27:48.457260+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_COBRANZAS_INT_MIO]
AS SELECT PKRECIBONRO
	  FROM SIGASC.COBRANZAS_MIO c
	  WHERE pkrecibonro IN ( SELECT DISTINCT PKRECIBONRO FROM SIGASC.COBRANZAS_MIO WHERE facturanegocio = 'INT' )
	  GROUP BY pkrecibonro
	  HAVING COUNT( DISTINCT facturanegocio ) = 1;
```
