---
esquema: dbo
tabla: V_ORGANIZACION
objeto: dbo.V_ORGANIZACION
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

# dbo.V_ORGANIZACION

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.ORGANIZACION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ORGANIZACIONID` | int | 0% |
| 2 | `ORGANIZACIONNOMBRE` | varchar | 0% |
| 3 | `ORGANIZACIONGRUPO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ORGANIZACION
-- Extraida: 2026-08-07T15:28:10.170972+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_ORGANIZACION]
AS SELECT o.ORGANIZACIONID,
		   o.ORGANIZACIONNOMBRE,
		   CASE 
		   WHEN o.organizacionid = '4' THEN 'TELEPERFORMANCE'
		   WHEN o.organizacionid IN ('2','6','7','14','16','17','18','19','52') THEN 'OFICINA'
		   WHEN o.organizacionid IN ('27','36','46','26','28','34','35','41','48',
									 '37','32','42','31','11','33','22','40','49','39','43','15','29','38','47','20','53','55') THEN 'OTROS'
		   ELSE 'OTROS'  END AS ORGANIZACIONGRUPO
	FROM SIGAMSASC.ORGANIZACION o
	UNION ALL
	SELECT 0, 'SISTEMA', 'OTROS';
```
