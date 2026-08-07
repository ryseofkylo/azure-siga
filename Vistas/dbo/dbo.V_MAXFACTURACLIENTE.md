---
esquema: dbo
tabla: V_MAXFACTURACLIENTE
objeto: dbo.V_MAXFACTURACLIENTE
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

# dbo.V_MAXFACTURACLIENTE

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_FACTURACLIENTE]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int |  |
| 2 | `CLIENTENRO` | varchar |  |
| 3 | `MAXFACTURAFCH` | date |  |
| 4 | `PERIODO` | nvarchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_MAXFACTURACLIENTE
-- Extraida: 2026-08-07T15:28:01.470227+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_MAXFACTURACLIENTE]
AS SELECT EMPRESAID, CLIENTENRO, 
		   MAX(facturafch) AS MAXFACTURAFCH, 
		   --MAX(PRIMERFECHA) AS MAXFACTURAFCH,
		   MAX(periodo) AS PERIODO
	FROM V_FACTURACLIENTE GROUP BY EMPRESAID, CLIENTENRO;
```
