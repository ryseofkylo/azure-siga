---
esquema: dbo
tabla: v_HistoricoContrato
objeto: dbo.v_HistoricoContrato
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 6
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_HistoricoContrato

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_CONTRATO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `CONTRATONRO` | int | 0% |
| 4 | `PKPRODUCTOID` | nvarchar | 0% |
| 5 | `PERIODO` | date | 0% |
| 6 | `CONTRATOSTS` | nvarchar | 99% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_HistoricoContrato
-- Extraida: 2026-08-07T15:27:59.153794+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_HistoricoContrato]
AS WITH tmp_periodo (PERIODO) AS (
  select DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))) UNION ALL
select DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) UNION ALL
select DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
),
contratos_arreglados as(
SELECT C.[EMPRESAID]
      ,C.[CONTRATONRO]
      ,C.[CLIENTENRO]
      ,C.[CONTRATOSTS]
	  ,C.[PKPRODUCTOID]
      ,CASE
		when C.[BDMODIFIEDDATE] > '1990-01-01' THEN C.[BDMODIFIEDDATE] 
        WHEN C.[BDMODIFIEDDATE] < '1990-01-01' and C.[CONTRATOSTS] = 'C' THEN '2022-09-01'
        ELSE null
    END AS BDMODIFIEDDATE
  FROM [SIGASC].[H_CONTRATO] C
  where (C.[CONTRATOSTS] = 'C' or C.[BDMODIFIEDDATE] > '1900-01-01')
--and clientenro = 5455021
--and contratonro =5775520
),
inicio_contratos as (
select *
from  contratos_arreglados a
where BDMODIFIEDDATE = (select min(b.BDMODIFIEDDATE)
from  contratos_arreglados b
where a.EMPRESAID=b.EMPRESAID
and a.[CONTRATONRO] = b.[CONTRATONRO]
and a.CLIENTENRO = b.CLIENTENRO)
)
,
tabla_periodos as (
SELECT 
--distinct 
v.EMPRESAID,v.CLIENTENRO,v.CONTRATONRO,v.PKPRODUCTOID,PERIODO FROM inicio_contratos v
INNER JOIN tmp_periodo 
ON PERIODO >=  DATEADD(month, DATEDIFF(month, 0, v.BDMODIFIEDDATE), 0)
and PERIODO <= (select
case
	when MAX(c.CONTRATOSTS) = 'X'
	then
	DATEADD(month, DATEDIFF(month, 0, max(c.BDMODIFIEDDATE)), 0)
	else 
	DATEADD(month, DATEDIFF(month, 0,GETDATE()), 0)
END AS modified_date
from contratos_arreglados c
where 
C.[CONTRATONRO] = v.CONTRATONRO
AND C.[CLIENTENRO] = v.CLIENTENRO
AND c.[EMPRESAID] = v.EMPRESAID
)),
status_final_final as(
select EMPRESAID,CLIENTENRO,CONTRATONRO,contratosts,DATEADD(month, DATEDIFF(month, 0, c.BDMODIFIEDDATE), 0)as PERIODO
from contratos_arreglados C
where c.BDMODIFIEDDATE = (
SELECT MAX(A.BDMODIFIEDDATE)
FROM contratos_arreglados a
WHERE 
A.EMPRESAID = c.EMPRESAID
and A.CLIENTENRO = c.CLIENTENRO
and A.CONTRATONRO = c.CONTRATONRO
AND DATEADD(month, DATEDIFF(month, 0, A.BDMODIFIEDDATE), 0) = DATEADD(month, DATEDIFF(month, 0, c.BDMODIFIEDDATE), 0))
GROUP BY EMPRESAID,CLIENTENRO,CONTRATONRO,contratosts,DATEADD(month, DATEDIFF(month, 0, c.BDMODIFIEDDATE), 0)
)
select a.*,b.CONTRATOSTS
from tabla_periodos a
left join status_final_final b
on a.[CONTRATONRO] = b.CONTRATONRO
and a.[CLIENTENRO] = b.CLIENTENRO
and a.[EMPRESAID] = b.EMPRESAID
and a.PERIODO = b.PERIODO;
```
