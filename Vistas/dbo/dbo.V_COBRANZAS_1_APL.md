---
esquema: dbo
tabla: V_COBRANZAS_1_APL
objeto: dbo.V_COBRANZAS_1_APL
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

# dbo.V_COBRANZAS_1_APL

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.RECIBO]]
- [[SIGASC.RECIBOFAC]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PKRECIBONRO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_COBRANZAS_1_APL
-- Extraida: 2026-08-07T15:27:46.135796+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_COBRANZAS_1_APL]
AS SELECT r.PKRECIBONRO FROM SIGASC.RECIBO r
	  LEFT JOIN ( SELECT * FROM SIGASC.RECIBOFAC WHERE FACTURATPO = 'F' ) b ON ( r.pkrecibonro = b.pkrecibonro )
	  WHERE r.recibosts <> 'X'
	  AND r.recibotpo = 'R'	
	  AND r.RECIBOFCH >= DATEADD(MM, -17, GETDATE())
	  GROUP BY r.PKRECIBONRO
	  HAVING COUNT(b.skrecibofac) = 1;
```
