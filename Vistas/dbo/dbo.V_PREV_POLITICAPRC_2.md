---
esquema: dbo
tabla: V_PREV_POLITICAPRC_2
objeto: dbo.V_PREV_POLITICAPRC_2
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 21
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_PREV_POLITICAPRC_2

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.POLITICACPTO]]
- [[dbo.V_PREVENTAS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PREVENTANRO` | int | 0% |
| 3 | `PKPREVENTANRO` | varchar | 0% |
| 4 | `PREVENTASTS` | varchar | 0% |
| 5 | `PREVENTATPO` | varchar | 0% |
| 6 | `CLIENTENROPREVENTA` | int | 2% |
| 7 | `NEGOCIOSEGMENTO` | int | 0% |
| 8 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 9 | `PREVENTAFCHING` | datetime2 | 0% |
| 10 | `PREVENTAUSR` | varchar | 0% |
| 11 | `PROMOTORID` | int | 0% |
| 12 | `PREVENTAMEDCOBROID` | int | 0% |
| 13 | `PREVENTAFCHFIN` | datetime2 | 2% |
| 14 | `PREVENTAPRODLIN` | int | 0% |
| 15 | `PRODUCTOID` | int | 0% |
| 16 | `POLITICAID` | int | 0% |
| 17 | `PROMOCIONID` | int | 23% |
| 18 | `PREVENTAPRODSTS` | varchar | 0% |
| 19 | `PREVENTAPRODCONGEN` | int | 6% |
| 20 | `PREVENTAPRODCANTIDAD` | int | 0% |
| 21 | `POLITICAPRC` | real | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_PREV_POLITICAPRC_2
-- Extraida: 2026-08-07T15:28:12.123504+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_PREV_POLITICAPRC_2]
AS SELECT DISTINCT p.*, r.POLITICAPRC
	FROM V_PREVENTAS p
	LEFT JOIN 
		( SELECT DISTINCT s.PkPREVENTANRO, s.EMPRESAID, c.POLITICAID, MAX(c.politicafch) AS MAXIMA
		  FROM /*SIGASC.POLITICAPRC*/ SIGASC.POLITICAPRC_BACKUP200923 c
		  LEFT JOIN SIGASC.POLITICACPTO p
		  ON ( ( c.pkpoliticaid = p.pkpoliticaid ) AND ( c.pkpoliticalin = p.pkpoliticalin ) )
		  LEFT JOIN V_PREVENTAS s 
		  ON ( CONCAT( c.empresaid, CONCAT( '_', c.politicaid ) ) = CONCAT( s.empresaid, CONCAT( '_', s.politicaid ) ) 
			   AND c.politicafch <= s.preventafching
			  )
		  WHERE politicacptotpo = 'C'
		  GROUP BY s.pkpreventanro, s.empresaid, c.politicaid
		) a
	ON (  
		( a.pkpreventanro = p.pkpreventanro )
		AND CONCAT( a.empresaid, CONCAT( '_', a.politicaid ) ) = CONCAT( p.empresaid, CONCAT( '_', p.politicaid ) )
	   )
	LEFT JOIN /*SIGASC.POLITICAPRC*/ SIGASC.POLITICAPRC_BACKUP200923 r
	ON ( CONCAT( r.empresaid, CONCAT( '_', r.politicaid ) ) = CONCAT( p.empresaid, CONCAT( '_', p.politicaid ) )
		 AND r.politicafch = a.maxima 
	   )
	LEFT JOIN SIGASC.POLITICACPTO t
	ON ( ( r.pkpoliticaid = t.pkpoliticaid ) AND ( r.pkpoliticalin = t.pkpoliticalin ) )
	WHERE politicacptotpo = 'C';
```
