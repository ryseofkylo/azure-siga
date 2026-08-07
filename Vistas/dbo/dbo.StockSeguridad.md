---
esquema: dbo
tabla: StockSeguridad
objeto: dbo.StockSeguridad
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 4
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.StockSeguridad

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SAP_COMPRAS.MaterialesCentro]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MATNR` | nvarchar | 0% |
| 2 | `WERKS` | nvarchar | 0% |
| 3 | `EISBE` | decimal | 0% |
| 4 | `MINBE` | decimal | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.StockSeguridad
-- Extraida: 2026-08-07T15:27:35.049045+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[StockSeguridad]
AS SELECT
    MATNR,
    WERKS,
    EISBE,
    MINBE
FROM SAP_COMPRAS.MaterialesCentro;
```
