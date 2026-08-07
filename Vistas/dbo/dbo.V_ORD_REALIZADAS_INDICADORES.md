---
esquema: dbo
tabla: V_ORD_REALIZADAS_INDICADORES
objeto: dbo.V_ORD_REALIZADAS_INDICADORES
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 9
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_ORD_REALIZADAS_INDICADORES

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.ORDENES_REALIZADAS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `TAREAID` | varchar | 0% |
| 2 | `FECHAINGRESO` | datetime2 | 0% |
| 3 | `HORAINGRESO` | datetime2 | 100% |
| 4 | `FECHAFINALIZADA` | datetime2 | 1% |
| 5 | `HORAFINALIZADA` | datetime2 | 100% |
| 6 | `FECHAPROCESADA` | datetime2 | 0% |
| 7 | `HORAPROCESADA` | datetime2 | 100% |
| 8 | `FECHAAGENDADA` | datetime2 | 28% |
| 9 | `DEMORATOTAL` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ORD_REALIZADAS_INDICADORES
-- Extraida: 2026-08-07T15:28:07.847318+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_ORD_REALIZADAS_INDICADORES]
AS SELECT DISTINCT
	r.TAREAID, 
	CASE WHEN ( a.fchingppl   IS NOT NULL ) THEN a.fchingppl   ELSE b.fchingnoppl   END AS FECHAINGRESO,
	CASE WHEN ( a.horaingppl  IS NOT NULL ) THEN a.horaingppl  ELSE b.horaingnoppl  END AS HORAINGRESO,
	CASE WHEN ( a.fchfinppl   IS NOT NULL ) THEN a.fchfinppl   ELSE b.fchfinnoppl   END AS FECHAFINALIZADA,
	CASE WHEN ( a.horafinppl  IS NOT NULL ) THEN a.horafinppl  ELSE b.horafinnoppl  END AS HORAFINALIZADA,
	CASE WHEN ( a.fchprocppl  IS NOT NULL ) THEN a.fchprocppl  ELSE b.fchprocnoppl  END AS FECHAPROCESADA,
	CASE WHEN ( a.horaprocppl IS NOT NULL ) THEN a.horaprocppl ELSE b.horaprocnoppl END AS HORAPROCESADA,
	CASE WHEN ( a.fchagenppl  IS NOT NULL ) THEN a.fchagenppl  ELSE b.fchagennoppl  END AS FECHAAGENDADA,
	CASE WHEN ( a.demorappl   IS NOT NULL ) THEN a.demorappl   ELSE b.demoranoppl   END AS DEMORATOTAL
FROM SIGASC.ORDENES_REALIZADAS r
LEFT JOIN ( SELECT p.TAREAID, 
				MAX(p.fechaingreso)		AS FCHINGPPL,
				MAX(p.horaingreso)		AS HORAINGPPL,
				MAX(p.fechafinalizada)	AS FCHFINPPL,
				MAX(p.horafinalizada)	AS HORAFINPPL,
				MAX(p.fechaprocesada)	AS FCHPROCPPL,
				MAX(p.horaprocesada)	AS HORAPROCPPL,	
				MAX(p.fechaagendada)	AS FCHAGENPPL,
				AVG(p.demoratotal)		AS DEMORAPPL
		FROM SIGASC.ORDENES_REALIZADAS p 
		WHERE productoppal = 'P'
		GROUP BY p.tareaid
) a
ON ( r.tareaid = a.tareaid )
LEFT JOIN ( SELECT p.TAREAID, 
				MAX(p.fechaingreso)	   AS FCHINGNOPPL,
				MAX(p.horaingreso)	   AS HORAINGNOPPL,
				MAX(p.fechafinalizada) AS FCHFINNOPPL,
				MAX(p.horafinalizada)  AS HORAFINNOPPL,
				MAX(p.fechaprocesada)  AS FCHPROCNOPPL,
				MAX(p.horaprocesada)   AS HORAPROCNOPPL,
				MAX(p.fechaagendada)   AS FCHAGENNOPPL,
				AVG(p.demoratotal)	   AS DEMORANOPPL
			FROM SIGASC.ORDENES_REALIZADAS p 
			WHERE ( productoppal <> 'P' OR productoppal IS NULL ) 
			GROUP BY p.tareaid
) b
ON ( r.tareaid = b.tareaid );
```
