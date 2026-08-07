---
esquema: dbo
tabla: V_ULTIMAFACTURACION
objeto: dbo.V_ULTIMAFACTURACION
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

# dbo.V_ULTIMAFACTURACION

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.FACTURACION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENRO` | varchar |  |
| 2 | `PERIODO` | int |  |
| 3 | `FACTURATOTAL` | float |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ULTIMAFACTURACION
-- Extraida: 2026-08-07T15:28:22.895319+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_ULTIMAFACTURACION]
AS SELECT DISTINCT a.CLIENTENRO, a.PERIODO, SUM(e.FACTURATOTAL) AS FACTURATOTAL 
FROM SIGASC.FACTURACION e
INNER JOIN 
	( SELECT CONCAT( f.empresaid, '_', f.clientenro ) AS CLIENTENRO, MAX(f.facturaperiodo) AS PERIODO
	  FROM SIGASC.FACTURACION f
	  GROUP BY CONCAT( f.empresaid, '_', f.clientenro ) 
	) a
ON ( ( a.clientenro = CONCAT( e.empresaid, '_', e.clientenro ) ) AND ( a.PERIODO = e.facturaperiodo ) )
WHERE e.facturatpo = 'F'
GROUP BY a.clientenro, a.periodo;
```
