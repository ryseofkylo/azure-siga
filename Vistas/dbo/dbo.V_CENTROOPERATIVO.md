---
esquema: dbo
tabla: V_CENTROOPERATIVO
objeto: dbo.V_CENTROOPERATIVO
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

# dbo.V_CENTROOPERATIVO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CENTROOPERATIVO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CENTROOPERATIVOID` | int | 0% |
| 2 | `PKCENTROOPERATIVOID` | varchar | 0% |
| 3 | `CENTROOPERATIVOORIGEN` | varchar | 0% |
| 4 | `CENTROOPERATIVONOMBRE` | varchar | 0% |
| 5 | `CENTROOPERATIVOCRITERIO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CENTROOPERATIVO
-- Extraida: 2026-08-07T15:27:43.174049+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_CENTROOPERATIVO]
AS SELECT EMPRESAID
			  CENTROOPERATIVOID,
			  PKCENTROOPERATIVOID,
			  centrooperativonombre AS CENTROOPERATIVOORIGEN,
			  CASE WHEN ( empresaid = 1 )
				   THEN CASE WHEN ( centrooperativoid = 3 ) 
							 THEN 'CP. SAN MARTIN MZA'
							 ELSE 'CP. MENDOZA'
						END
				   WHEN ( empresaid = 16 )
				   THEN CASE WHEN ( centrooperativoid = 2 )
							 THEN 'CP. CHILECITO'
							 ELSE 'CP. LA RIOJA'
						END
				   WHEN ( empresaid = 3  ) THEN 'CP. TUCUMAN'
				   WHEN ( empresaid = 21 ) THEN 'CP. CATAMARCA'
			       ELSE REPLACE( REPLACE (centrooperativonombre, 'C.O.', 'CP.'), 'C.O', 'CP.')
			  END AS CENTROOPERATIVONOMBRE,
			  CENTROOPERATIVOCRITERIO
	   FROM SIGASC.CENTROOPERATIVO c;
```
