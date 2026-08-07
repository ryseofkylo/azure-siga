---
esquema: dbo
tabla: V_PROMOCION
objeto: dbo.V_PROMOCION
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 20
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_PROMOCION

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.PROMOCION]]
- [[SIGASC.PROMOCIONMES]]
- [[dbo.V_INDICEPROMOCIONMES]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PROMOCIONID` | varchar | 0% |
| 3 | `PROMOCIONNOMBRE` | varchar | 0% |
| 4 | `PROMOCIONSTS` | varchar | 0% |
| 5 | `CPTOFACID` | int | 0% |
| 6 | `PROMOCIONCOMBO` | int | 0% |
| 7 | `PROMOCIONTPODTO` | varchar | 0% |
| 8 | `PROMOCIONPERMANENTE` | int | 0% |
| 9 | `PROMOCIONSIMULTANEA` | int | 0% |
| 10 | `PROMOCIONCLASE` | varchar | 0% |
| 11 | `CANTCUOTAS` | int | 0% |
| 12 | `PROMOCIONDTOPRJ` | real | 1% |
| 13 | `PROMOCIONDTOPRC` | real | 1% |
| 14 | `PROMOCIONPRC` | real | 1% |
| 15 | `PROMOCIONDEBPRC` | real | 1% |
| 16 | `PROMOCIONDEBDTOPRJ` | real | 1% |
| 17 | `DESCPORCENTAJE` | real | 0% |
| 18 | `DESCMONTO` | real | 0% |
| 19 | `DESIMPORTE` | real | 0% |
| 20 | `TIPODESCUENTO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_PROMOCION
-- Extraida: 2026-08-07T15:28:14.069992+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_PROMOCION]
AS SELECT p.EMPRESAID,
	   ( p.pkpromocionid ) AS PROMOCIONID,
	   p.PROMOCIONNOMBRE,
	   p.PROMOCIONSTS,
	   p.CPTOFACID,
	   p.PROMOCIONCOMBO,
	   p.PROMOCIONTPODTO,
	   p.PROMOCIONPERMANENTE,
	   p.PROMOCIONSIMULTANEA,
	   p.PROMOCIONCLASE,
	   m.CANTCUOTAS,
	   x.PROMOCIONDTOPRJ,
	   x.PROMOCIONDTOPRC,
	   x.PROMOCIONPRC,
	   x.PROMOCIONDEBPRC,
	   x.PROMOCIONDEBDTOPRJ,
	   CASE WHEN x.PROMOCIONDTOPRJ > 0 OR x.PROMOCIONDEBDTOPRJ > 0
	        THEN ( CASE WHEN x.PROMOCIONDTOPRJ > x.PROMOCIONDEBDTOPRJ THEN x.PROMOCIONDTOPRJ ELSE x.PROMOCIONDEBDTOPRJ END )
		    ELSE 0 
	   END AS DESCPORCENTAJE,
	   CASE WHEN x.PROMOCIONPRC	  > 0 THEN x.PROMOCIONPRC	  ELSE 0 END AS DESCMONTO,
	   CASE WHEN x.PROMOCIONDTOPRC   > 0 THEN x.PROMOCIONDTOPRC  ELSE 0 END AS DESIMPORTE,
	   /*
	   CASE WHEN x.PROMOCIONDTOPRJ   > 0 OR x.PROMOCIONDEBDTOPRJ > 0 THEN 'Porcentaje' 
		    WHEN x.PROMOCIONPRC	  > 0 THEN 'Monto Fijo'
			WHEN x.PROMOCIONDTOPRC   > 0 THEN 'Importe' 
		END AS TIPODESCUENTO
		*/
		CASE p.PROMOCIONTPODTO 
			WHEN 'F' THEN 'Monto Fijo'
			WHEN 'I' THEN 'Importe'
			WHEN 'P' THEN 'Porcentaje'
		END AS TIPODESCUENTO
FROM SIGASC.PROMOCION p
INNER JOIN 
( SELECT PKPROMOCIONID, --MAX(SUBSTRING(a.pkpromocionmes,CHARINDEX('_',a.pkpromocionmes)+1,LEN(a.pkpromocionmes))) AS CANTCUOTAS,
		 MAX( promocionmes ) AS CANTCUOTAS
  FROM SIGASC.PROMOCIONMES a GROUP BY PKPROMOCIONID
) m
ON ( p.pkpromocionid = m.pkpromocionid )
LEFT JOIN
( SELECT  a.* FROM SIGASC.PROMOCIONMES a
  INNER JOIN V_INDICEPROMOCIONMES b
  ON ( ( a.pkpromocionid = b.pkpromocionid ) AND ( a.pkpromocionmes = CONCAT( b.empresaid, CONCAT('_', b.promocionmes ) )  ) ) 
) x
ON ( p.pkpromocionid = x.pkpromocionid );
```
