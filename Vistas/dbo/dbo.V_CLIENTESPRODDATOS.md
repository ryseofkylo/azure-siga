---
esquema: dbo
tabla: V_CLIENTESPRODDATOS
objeto: dbo.V_CLIENTESPRODDATOS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 2
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_CLIENTESPRODDATOS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_CONTRATO_CLIENTE]]
- [[SIGASC.PRODUCTO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PKCLIENTENRO` | nvarchar | 0% |
| 2 | `BDMODIFIEDDATE` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CLIENTESPRODDATOS
-- Extraida: 2026-08-07T15:27:44.488054+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_CLIENTESPRODDATOS]
AS SELECT c.PKCLIENTENRO, c.BDMODIFIEDDATE
FROM SIGASC.H_CONTRATO_CLIENTE c
INNER JOIN SIGASC.PRODUCTO p ON ( c.pkproductoid = p.pkproductoid )
WHERE p.productotpo = 'T';
```
