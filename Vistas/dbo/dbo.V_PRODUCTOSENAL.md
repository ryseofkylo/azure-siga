---
esquema: dbo
tabla: V_PRODUCTOSENAL
objeto: dbo.V_PRODUCTOSENAL
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 8
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_PRODUCTOSENAL

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.PRODUCTOSENAL]]
- [[SIGASC.SENAL]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PRODUCTOID` | varchar | 0% |
| 3 | `SENALID` | varchar | 0% |
| 4 | `SENALNOMBRE` | varchar | 0% |
| 5 | `SENALTIPO` | varchar | 74% |
| 6 | `SENALSUBTIPO` | varchar | 74% |
| 7 | `ORDENSENALTIPO` | int | 74% |
| 8 | `ORDENSENALSUBTIPO` | int | 74% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_PRODUCTOSENAL
-- Extraida: 2026-08-07T15:28:13.745224+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_PRODUCTOSENAL]
AS SELECT EMPRESAID, PRODUCTOID, SENALID, SENALNOMBRE, SENALTIPO, SENALSUBTIPO,
	   CASE SENALTIPO 
			WHEN 'DIGITALES'	  THEN 1
			WHEN 'D. ADICIONALES' THEN 2
			WHEN 'PREMIUM'		  THEN 3
			WHEN 'PLATAFORMA'		  THEN 4
	   END AS ORDENSENALTIPO,
	   CASE SENALSUBTIPO
			WHEN 'HD' THEN 1
			WHEN 'SD' THEN 2
			WHEN 'ADICIONALES' THEN 3
			WHEN 'HBO-ADULTOS' THEN 4
			WHEN 'FUTBOL'	   THEN 5
			WHEN 'UNIVERSAL +' THEN 6
			WHEN 'MAX ESTANDAR' THEN 7
	   END AS ORDENSENALSUBTIPO
FROM (
	   SELECT p.EMPRESAID, 
			  p.pkproductoid AS PRODUCTOID, 
			  CONVERT(VARCHAR, p.senalid) AS SENALID,
	          s.SENALNOMBRE,
			  CASE 
			   WHEN ( p.senalid IN ('2','3','15','42','72','1016','1019','1054','1069') )								THEN 'DIGITALES'
			   WHEN ( p.senalid IN ('10','11','32','43','73','1018','1056','1070','1071') )							    THEN 'D. ADICIONALES'
			   WHEN ( p.senalid IN ('4','6','25','45','46','74','75','80','83','1063','1073','1074','1075','1076','1077') ) THEN 'PREMIUM'
			   WHEN ( p.senalid IN ('1093') ) THEN 'PLATAFORMA'
	          END AS SENALTIPO,
			  CASE 
			   WHEN ( p.senalid IN ('3','15','42','72','1016','1019','1054','1069') )		THEN 'HD'
			   WHEN ( p.senalid IN ('2') )													THEN 'SD'
			   WHEN ( p.senalid IN ('10','11','32','43','73','1018','1056','1070','1071') ) THEN 'ADICIONALES'
			   WHEN ( p.senalid IN ('4','6','25','80','83','1073','1075') )				    THEN 'HBO-ADULTOS'
			   WHEN ( p.senalid IN ('45','46','74','75','1076','1077') )					THEN 'FUTBOL'
			   WHEN ( p.senalid IN ('1063','1074') )										THEN 'UNIVERSAL +'
			   WHEN ( p.senalid IN ('1093') )										THEN 'MAX ESTANDAR'
			  END AS SENALSUBTIPO
		FROM SIGASC.PRODUCTOSENAL p
		LEFT JOIN SIGASC.SENAL s ON ( p.senalid = s.senalid )
	   ) a;
```
