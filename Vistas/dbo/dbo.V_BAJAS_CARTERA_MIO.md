---
esquema: dbo
tabla: V_BAJAS_CARTERA_MIO
objeto: dbo.V_BAJAS_CARTERA_MIO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 4
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_BAJAS_CARTERA_MIO

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

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_BAJAS_CARTERA_MIO
-- Extraida: 2026-08-07T15:27:37.061821+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_BAJAS_CARTERA_MIO]
AS with contratos_fixeados as(
SELECT  hc.[EMPRESAID]
,hc.[CONTRATONRO]
,hc.[CLIENTENRO]
,hc.[POLITICAID]
,hc.[PRODUCTOID]
,hc.[CONTRATOSTS]
,hc.[PLANCOMERCIALCLIENTEITEM]
,hc.[PLANCOMERCIALGESTIONID]
,hc.[PLANCOMERCIALCLIENTEID]
      ,CASE
		when hc.[BDMODIFIEDDATE] > '1990-01-01' THEN hc.[BDMODIFIEDDATE] 
        WHEN hc.[BDMODIFIEDDATE] < '1990-01-01' and hc.[CONTRATOSTS] = 'C' THEN '2022-09-01'
        ELSE null
    END AS BDMODIFIEDDATE
  FROM [SIGASC].[H_CONTRATO] hc
 left join sigasc.producto p
on hc.pkproductoid = p.pkproductoid
and hc.empresaid = p.empresaid
where P.productoid in (6402,6409,6418,70048,70049,70050,70061,70062,70063,70044,70074) or ( P.productoid in (8552,8555,8556) and p.empresaid=23)
and P.PRODUCTOTPO = 'M'
),
contratos_con_lag as(
SELECT contratonro, empresaid, contratosts, bdmodifieddate
FROM (
  SELECT 
    contratonro, 
    empresaid, 
    contratosts, 
    bdmodifieddate, 
    LAG(contratosts) OVER (PARTITION BY contratonro, empresaid ORDER BY bdmodifieddate) AS prev_contratosts
  FROM contratos_fixeados
  where BDMODIFIEDDATE is not null
) t
WHERE (contratosts != prev_contratosts OR prev_contratosts IS NULL))
-----------------------------------------------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
 SELECT contratonro, contratosts,empresaid,DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
--------------------------------------
union
----------------------------------------
  SELECT contratonro, contratosts,empresaid,DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT contratonro, contratosts, bdmodifieddate,empresaid,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1;
```
