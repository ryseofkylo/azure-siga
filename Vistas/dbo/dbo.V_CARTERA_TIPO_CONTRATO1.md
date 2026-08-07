---
esquema: dbo
tabla: V_CARTERA_TIPO_CONTRATO1
objeto: dbo.V_CARTERA_TIPO_CONTRATO1
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

# dbo.V_CARTERA_TIPO_CONTRATO1

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_CONTRATO]]
- [[SIGASC.PRODUCTO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `contratonro` | int | 0% |
| 2 | `contratosts` | nvarchar | 0% |
| 3 | `empresaid` | int | 0% |
| 4 | `Fecha` | date | 0% |
| 5 | `PRODUCTOTPO` | varchar | 0% |
| 6 | `pkproductoid` | varchar | 0% |
| 7 | `PRODUCTONOMBRE` | varchar | 0% |
| 8 | `CLIENTENRO` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CARTERA_TIPO_CONTRATO1
-- Extraida: 2026-08-07T15:27:42.509603+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_CARTERA_TIPO_CONTRATO1]
AS with contratos_fixeados as
(
SELECT  
hc.[EMPRESAID]
,hc.[CONTRATONRO]
,hc.[CLIENTENRO]
,hc.[POLITICAID]
,hc.[PRODUCTOID]
,hc.[CONTRATOSTS]
,P.PRODUCTOTPO
,p.pkproductoid
,p.PRODUCTONOMBRE
      ,CASE
		when hc.[BDMODIFIEDDATE] > '1990-01-01' THEN hc.[BDMODIFIEDDATE] 
        WHEN hc.[BDMODIFIEDDATE] < '1990-01-01' and hc.[CONTRATOSTS] = 'C' THEN '2022-09-01'
        ELSE null
    END AS BDMODIFIEDDATE
  FROM [SIGASC].[H_CONTRATO] hc
 left join sigasc.producto p
on hc.pkproductoid = p.pkproductoid
and hc.empresaid = p.empresaid
),

contratos_con_lag as(
SELECT contratonro, empresaid, contratosts, bdmodifieddate, PRODUCTOTPO, pkproductoid, PRODUCTONOMBRE, [CLIENTENRO]
FROM (
  SELECT 
    contratonro, 
    empresaid, 
    contratosts, 
    bdmodifieddate, 
    PRODUCTOTPO  ,
    pkproductoid,
    PRODUCTONOMBRE,
    [CLIENTENRO],
    LAG(contratosts) OVER (PARTITION BY contratonro, empresaid ORDER BY bdmodifieddate) AS prev_contratosts
  FROM contratos_fixeados
  where BDMODIFIEDDATE is not null
) t
WHERE (contratosts != prev_contratosts OR prev_contratosts IS NULL))
-----------------------------------------------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid, PRODUCTONOMBRE, [CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE, [CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid, PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid, PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
  SELECT contratonro, contratosts,empresaid,DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha, PRODUCTOTPO, pkproductoid,PRODUCTONOMBRE,[CLIENTENRO]
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,PRODUCTOTPO,pkproductoid,PRODUCTONOMBRE,[CLIENTENRO],
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1;
```
