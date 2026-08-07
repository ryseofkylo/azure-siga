---
esquema: dbo
tabla: V_CATEGORIACLIENTE
objeto: dbo.V_CATEGORIACLIENTE
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

# dbo.V_CATEGORIACLIENTE

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CLIENTENATURALEZA]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENATURALEZAID` | int | 0% |
| 2 | `CATEGORIA` | varchar | 0% |
| 3 | `CATEGORIAAGRUPACION` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CATEGORIACLIENTE
-- Extraida: 2026-08-07T15:27:42.837148+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_CATEGORIACLIENTE]
AS SELECT c.CLIENTENATURALEZAID,
	   c.CLIENTENATURALEZANOM AS CATEGORIA,
	   CASE WHEN c.clientenaturalezaid IN ('1','2','6') THEN 'CATV'
			WHEN c.clientenaturalezaid IN ('4','5','7') THEN 'DUPLO'
			WHEN c.clientenaturalezaid IN ('3')		  THEN 'INTERNET'
	   ELSE 'SIN CATEGORIA'
	   END AS CATEGORIAAGRUPACION
FROM SIGASC.CLIENTENATURALEZA c;
```
