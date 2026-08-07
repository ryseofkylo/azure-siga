---
esquema: dbo
tabla: V_MEDIOCOBRO
objeto: dbo.V_MEDIOCOBRO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 7
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_MEDIOCOBRO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[BIGDATA.AGRUPACIONMEDCOBROBD]]
- [[SIGASC.MEDIOCOBRO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MEDCOBROID` | int | 0% |
| 2 | `MEDCOBRONOMBRE` | varchar | 0% |
| 3 | `MEDCOBROTPO` | varchar | 0% |
| 4 | `MEDIOCOBRONOMBREBD` | varchar | 70% |
| 5 | `MEDIOCOBROGRUPOBD` | varchar | 70% |
| 6 | `CLASIFICACION` | varchar | 70% |
| 7 | `MEDIOCOBROCANALBD` | varchar | 70% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_MEDIOCOBRO
-- Extraida: 2026-08-07T15:28:01.806450+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_MEDIOCOBRO]
AS SELECT DISTINCT
		   m.MEDCOBROID,
		   m.MEDCOBRONOMBRE,
		   m.MEDCOBROTPO,
		   a.MEDIOCOBRONOMBREBD,
		   a.MEDIOCOBROGRUPOBD,
		   a.CLASIFICACION,
		   a.MEDIOCOBROCANALBD
	FROM SIGASC.MEDIOCOBRO m
	LEFT JOIN BIGDATA.AGRUPACIONMEDCOBROBD a ON ( m.medcobroid = a.mediocobroidbd );
```
