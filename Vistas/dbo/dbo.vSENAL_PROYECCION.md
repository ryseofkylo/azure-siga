---
esquema: dbo
tabla: vSENAL_PROYECCION
objeto: dbo.vSENAL_PROYECCION
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

# dbo.vSENAL_PROYECCION

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.PRODUCTOSENAL]]
- [[SIGASC.SENAL]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int |  |
| 2 | `PRODUCTOID` | int |  |
| 3 | `SENALID` | varchar |  |
| 4 | `SENALNOMBRE` | varchar |  |
| 5 | `SENALSUBTIPO` | varchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.vSENAL_PROYECCION
-- Extraida: 2026-08-07T15:28:35.833068+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vSENAL_PROYECCION]
AS SELECT T2.EMPRESAID, T2.PRODUCTOID , T3. SENALID, T3.SENALNOMBRE, T3.SENALSUBTIPO
FROM (
            SELECT T1.EMPRESAID, T1.PRODUCTOID, MIN(T1.SENALID) AS MINSENALID
            FROM (
            SELECT EMPRESAID, productoid ,  CONVERT(VARCHAR, senalid) AS SENALID
	        FROM SIGASC.PRODUCTOSENAL 
		    WHERE senalid IN ('4','6','25','80','83','1073','1075','46','75','1077',
		    '2','3','15','42','72','1016','1019','1054','1069','10','11','32','43','73','1018','1056','1070','1071')
            ) AS T1
            GROUP BY T1.EMPRESAID, T1.PRODUCTOID
            ) AS T2

LEFT JOIN (
SELECT p.EMPRESAID, p.productoid AS PRODUCTOID,  CONVERT(VARCHAR, p.senalid) AS SENALID, s.SENALNOMBRE,
			  CASE
			   WHEN p.senalid IN ('4','25','80', '1073') THEN 'HBO'
               WHEN p.senalid IN ('6','83','1075') THEN 'ADULTOS'			   
			   WHEN ( p.senalid IN ('46','75','1077') )THEN 'FUTBOL'
			   WHEN ( p.senalid IN ('2','3','15','42','72','1016','1019','1054','1069') )	THEN 'DIGITALES'
			   WHEN ( p.senalid IN ('10','11','32','43','73','1018','1056','1070','1071') )		THEN 'D. ADICIONALES'
			  END AS SENALSUBTIPO
        FROM SIGASC.PRODUCTOSENAL p 
        LEFT JOIN SIGASC.SENAL s 
        ON ( p.senalid = s.senalid )
        ) AS T3

	ON T2.EMPRESAID = T3.EMPRESAID AND
		T2.PRODUCTOID = T3.PRODUCTOID  AND
		T2.MINSENALID = T3.SENALID;
```
