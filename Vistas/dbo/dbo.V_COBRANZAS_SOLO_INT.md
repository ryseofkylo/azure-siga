---
esquema: dbo
tabla: V_COBRANZAS_SOLO_INT
objeto: dbo.V_COBRANZAS_SOLO_INT
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

# dbo.V_COBRANZAS_SOLO_INT

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.COBRANZAS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PKRECIBONRO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_COBRANZAS_SOLO_INT
-- Extraida: 2026-08-07T15:27:49.463439+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_COBRANZAS_SOLO_INT]
AS SELECT PKRECIBONRO
	  FROM SIGASC.COBRANZAS c
	  WHERE pkrecibonro IN ( SELECT DISTINCT PKRECIBONRO FROM SIGASC.COBRANZAS WHERE facturanegocio = 'INT' )
	  GROUP BY pkrecibonro
	  HAVING COUNT( DISTINCT facturanegocio ) = 1;
```
