---
esquema: dbo
tabla: V_CRM_BDDD
objeto: dbo.V_CRM_BDDD
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 17
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_CRM_BDDD

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CRMREGISTRO]]
- [[dbo.V_CRMMOTIVO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `CRMNRO` | varchar | 0% |
| 4 | `CRMFCHINI` | date | 0% |
| 5 | `CRMSTS` | varchar | 0% |
| 6 | `CRMMEDIO` | varchar | 0% |
| 7 | `CRMUSRACT` | varchar | 0% |
| 8 | `CRMUSRING` | varchar | 0% |
| 9 | `CRMMOTIVO1` | int | 0% |
| 10 | `CRMMOTIVO2` | int | 0% |
| 11 | `CRMMOTIVO3` | int | 0% |
| 12 | `CRMMOTIVO4` | int | 0% |
| 13 | `MOTIVOID` | varchar | 0% |
| 14 | `CRMMOTIVO1NOM` | varchar | 0% |
| 15 | `CRMMOTIVO2NOM` | varchar | 76% |
| 16 | `CRMMOTIVO3NOM` | varchar | 78% |
| 17 | `CRMMOTIVO4NOM` | varchar | 100% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CRM_BDDD
-- Extraida: 2026-08-07T15:27:50.771542+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_CRM_BDDD]
AS SELECT C.EMPRESAID,
	   C.CLIENTENRO,
	   (c.pkcrmnro) AS CRMNRO,
	  -- C.CRMOBS,
	   CONVERT(DATE,C.CRMFCHINI) AS CRMFCHINI,
	   C.CRMSTS,  
       C.CRMMEDIO, 
   	   C.CRMUSRACT,
	   C.CRMUSRING,
       c.CRMMOTIVO1,
       c.CRMMOTIVO2,
       c.CRMMOTIVO3,
       c.CRMMOTIVO4,
	   CONCAT(c.EMPRESAID, '_', ISNULL(c.CRMMOTIVO1,0), '_', ISNULL(c.CRMMOTIVO2,0), '_', ISNULL(c.CRMMOTIVO3,0), '_', ISNULL(c.CRMMOTIVO4,0) ) AS MOTIVOID,
       M.[CRMMOTIVO1NOM], m.[CRMMOTIVO2NOM], m.[CRMMOTIVO3NOM] ,m.[CRMMOTIVO4NOM]
       
FROM SIGASC.CRMREGISTRO C

left join [dbo].[V_CRMMOTIVO] M
on CONCAT(c.EMPRESAID, '_', ISNULL(c.CRMMOTIVO1,0), '_', ISNULL(c.CRMMOTIVO2,0), '_', ISNULL(c.CRMMOTIVO3,0), '_', ISNULL(c.CRMMOTIVO4,0) )  = m.[MOTIVOID]
and c.empresaid= m.empresaid

WHERE c.CRMFCHINI >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-12,GETDATE()))-1),DATEADD(mm,-12,GETDATE())),101)  
and  c.CRMTIPO='E'
AND C.CRMUSRING <> 'ROOT'
AND c.CRMFCHINI <  GETDATE()
AND c.CRMMOTIVO1 not in ( '2','1','16','17','20','21','22','23','24','25','26','27','28','29','30','32',
'33','34','35','36','38','39','40','41','43','46','52','53','55','56','57','58') -- CRM QUE NO SEAN DE "CAMPAÑAS" y otros
AND NOT (
    c.CRMMOTIVO1 = '5'
    AND c.CRMMOTIVO2 = '1'
    AND c.CRMMOTIVO3 = '7'
)
AND NOT (
    c.CRMMOTIVO1 = '14'
    AND c.CRMMOTIVO2 = '1'
)
AND c.CLIENTENRO <> 0			-- CLIENTENRO DEL CRM DIFERENTE DE 0
AND LEN(c.clientenro) >= 4	-- CLIENTENRO DEL CRM MAYOR A 4 DIGITOS
AND c.CRMSTS <> 'A' 
AND c.EMPRESAID NOT IN (15,19);
```
