---
esquema: dbo
tabla: v_fechasprueba
objeto: dbo.v_fechasprueba
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

# dbo.v_fechasprueba

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATOPROMOCION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `fechas` | nvarchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_fechasprueba
-- Extraida: 2026-08-07T15:27:56.454479+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [v_fechasprueba]
AS select SUBSTRING(CONTRATOPRMFCH,CHARINDEX('_',CONTRATOPRMFCH)+1,LEN(CONTRATOPRMFCH))  as fechas from sigasc.contratopromocion;
```
