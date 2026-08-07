---
esquema: dbo
tabla: V_MOTIVOFACTURA
objeto: dbo.V_MOTIVOFACTURA
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 3
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_MOTIVOFACTURA

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.MOTIVOFACTURA]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MOTIVOFACID` | int | 0% |
| 2 | `MOTIVOFACNOMBRE` | varchar | 0% |
| 3 | `MOTIVOFACTPO` | varchar | 4% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_MOTIVOFACTURA
-- Extraida: 2026-08-07T15:28:02.457343+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_MOTIVOFACTURA]
AS SELECT MOTIVOFACID, MOTIVOFACNOMBRE, MOTIVOFACTPO FROM SIGASC.MOTIVOFACTURA WHERE motivofacid > 0
UNION ALL
SELECT 0, 'ABONO ADICIONAL', NULL;
```
