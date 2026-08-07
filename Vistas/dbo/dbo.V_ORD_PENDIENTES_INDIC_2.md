---
esquema: dbo
tabla: V_ORD_PENDIENTES_INDIC_2
objeto: dbo.V_ORD_PENDIENTES_INDIC_2
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 5
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_ORD_PENDIENTES_INDIC_2

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.ORDENES_PENDIENTES]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `TAREAID` | varchar | 2% |
| 2 | `TECNICOID` | int | 2% |
| 3 | `TECNICOID2` | int | 2% |
| 4 | `MOTIVOSOLUCION` | varchar | 0% |
| 5 | `MOVILES` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ORD_PENDIENTES_INDIC_2
-- Extraida: 2026-08-07T15:28:06.518731+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_ORD_PENDIENTES_INDIC_2]
AS SELECT DISTINCT
	   a.TAREAID, 
	   CASE WHEN b.tecnicoint IS NOT NULL 
			THEN b.tecnicoint WHEN a.tecnicocable IS NOT NULL THEN a.tecnicocable ELSE c.tecniconoppl END AS TECNICOID,
	   CASE WHEN b.tecnicoint2 IS NOT NULL 
			THEN b.tecnicoint2 WHEN a.tecnicocable2 IS NOT NULL THEN a.tecnicocable2 ELSE c.tecniconoppl2 END AS TECNICOID2,
	   CASE WHEN b.motivoint IS NOT NULL 
			THEN b.motivoint WHEN a.motivocable IS NOT NULL THEN a.motivocable ELSE c.motivonoppl END AS MOTIVOSOLUCION,
	   CASE WHEN b.movilesint IS NOT NULL 
			THEN b.movilesint WHEN a.movilescable IS NOT NULL THEN a.movilescable ELSE c.movilesnoppl END AS MOVILES
FROM SIGASC.ORDENES_PENDIENTES p
LEFT JOIN (	
	SELECT p.tareaid, 
		   FIRST_VALUE(tecnicoid)	   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS TECNICOCABLE,
		   FIRST_VALUE(tecnicoid2)	   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS TECNICOCABLE2,
		   FIRST_VALUE(motivosolucion) OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS MOTIVOCABLE,
		   FIRST_VALUE(moviles)		   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS MOVILESCABLE
	FROM SIGASC.ORDENES_PENDIENTES p
	WHERE p.tipoproducto IN ('B','W','Z') AND productoppal = 'P'
) a
ON ( p.tareaid = a.tareaid )
LEFT JOIN (
	SELECT p.tareaid, 
		   FIRST_VALUE(tecnicoid)	   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS TECNICOINT,
		   FIRST_VALUE(tecnicoid2)	   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS TECNICOINT2,
		   FIRST_VALUE(motivosolucion) OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS MOTIVOINT,
		   FIRST_VALUE(moviles)		   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS MOVILESINT
	FROM SIGASC.ORDENES_PENDIENTES p
	WHERE p.tipoproducto IN ('E','C','I','N','L') AND productoppal = 'P'
) b
ON ( p.tareaid = b.tareaid )
LEFT JOIN (
	SELECT p.tareaid, 
		   FIRST_VALUE(tecnicoid)	   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS TECNICONOPPL,
		   FIRST_VALUE(tecnicoid2)	   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS TECNICONOPPL2,
		   FIRST_VALUE(motivosolucion) OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS MOTIVONOPPL,
		   FIRST_VALUE(moviles)		   OVER ( PARTITION BY tareaid ORDER BY tareaid ) AS MOVILESNOPPL
	FROM SIGASC.ORDENES_PENDIENTES p
	WHERE productoppal <> 'P' OR productoppal IS NULL
) c 
ON ( p.tareaid = c.tareaid );
```
