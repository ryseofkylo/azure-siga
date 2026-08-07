---
esquema: dbo
tabla: V_FACT_PERIODO_TOTAL
objeto: dbo.V_FACT_PERIODO_TOTAL
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

# dbo.V_FACT_PERIODO_TOTAL

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_FACTURACION_PERIODO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `FACTURAPERIODO` | int | 0% |
| 3 | `FACTURACION` | float | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_FACT_PERIODO_TOTAL
-- Extraida: 2026-08-07T15:27:53.062913+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_FACT_PERIODO_TOTAL]
AS SELECT EMPRESAID,
		   FACTURAPERIODO,
		   SUM(facturalinimp) AS FACTURACION
	FROM V_FACTURACION_PERIODO 
	WHERE FORMAT( DATEADD(MONTH, -1, CONVERT(DATE,CONCAT(CAST(FACTURAPERIODO AS VARCHAR),'01'))), 'yyyyMM' ) <= FORMAT( GETDATE(), 'yyyyMM' )
	GROUP BY empresaid, facturaperiodo;
```
