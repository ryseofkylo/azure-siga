---
esquema: dbo
tabla: V_FACTURACLIENTE_CONBAJAS
objeto: dbo.V_FACTURACLIENTE_CONBAJAS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 12
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_FACTURACLIENTE_CONBAJAS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_BAJASPERIODO]]
- [[dbo.V_FACTURACLIENTE]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int |  |
| 2 | `CLIENTENRO` | varchar |  |
| 3 | `FACTURAFCH` | date |  |
| 4 | `PERIODO` | int |  |
| 5 | `CONTRATOS` | int |  |
| 6 | `SUMA_CONTRATOS` | bigint |  |
| 7 | `SUMA_POLITICAS` | bigint |  |
| 8 | `SUMA_PROMOCIONES` | bigint |  |
| 9 | `CLASEPRODUCTO` | int |  |
| 10 | `FACTURACION` | float |  |
| 11 | `PERIODOANTERIOR` | int |  |
| 12 | `ESBAJA` | varchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_FACTURACLIENTE_CONBAJAS
-- Extraida: 2026-08-07T15:27:56.111722+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_FACTURACLIENTE_CONBAJAS]
AS SELECT c.*, 'N' ESBAJA FROM V_FACTURACLIENTE c
	UNION ALL
	SELECT p.*, 'Y' FROM V_BAJASPERIODO p;
```
