---
esquema: dbo
tabla: V_TAGLEADS_360
objeto: dbo.V_TAGLEADS_360
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

# dbo.V_TAGLEADS_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Tag]]
- [[dbo.V_LEADS_360]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Name` | nvarchar | 0% |
| 3 | `Context` | nvarchar | 0% |
| 4 | `Date` | datetime2 | 0% |
| 5 | `CasoId` | bigint | 0% |
| 6 | `IdTag` | bigint | 0% |
| 7 | `CREATION_DATE` | datetime2 | 0% |
| 8 | `CLOSE_DATE` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_TAGLEADS_360
-- Extraida: 2026-08-07T15:28:21.576853+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_TAGLEADS_360]
AS SELECT t.*, e.CREATION_DATE, e.CLOSE_DATE
FROM dbo.SG_TAG t
INNER JOIN V_LEADS_360 e ON ( e.id = t.casoid );
```
