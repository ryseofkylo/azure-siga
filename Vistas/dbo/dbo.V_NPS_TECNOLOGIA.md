---
esquema: dbo
tabla: V_NPS_TECNOLOGIA
objeto: dbo.V_NPS_TECNOLOGIA
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 3
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_NPS_TECNOLOGIA

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[MKT.NPS_YYYYMM]]
- [[SIGASC.H_CONTRATO]]
- [[SIGASC.PRODUCTO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Clientenro` | int | 0% |
| 2 | `Categoria` | varchar | 0% |
| 3 | `PERIODO` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_NPS_TECNOLOGIA
-- Extraida: 2026-08-07T15:28:04.830957+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_NPS_TECNOLOGIA]
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
,p.[PRODUCTONOMBRE]
,p.[PRODUCTOPPL]
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
SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,PRODUCTOPPL,CLIENTENRO
FROM (
  SELECT 
    contratonro, 
    empresaid, 
    contratosts, 
    bdmodifieddate,
    PRODUCTONOMBRE ,
    CLIENTENRO,
    PRODUCTOPPL,
    LAG(contratosts) OVER (PARTITION BY contratonro, empresaid ORDER BY bdmodifieddate) AS prev_contratosts
  FROM contratos_fixeados
  where BDMODIFIEDDATE is not null
) t
WHERE (contratosts != prev_contratosts OR prev_contratosts IS NULL))
-----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
   when  PRODUCTOPPL='P'
 Then '3'  END )
 As 'Categoria',
 202209 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202209)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202209
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    --------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3'  END )
 As 'Categoria',
 202211 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202211)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202211
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    --------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3'  END )
 As 'Categoria',
 202302 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202302)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202302
    ) AS subquery
    WHERE rn = 1
    group by Clientenro   
    --------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3'  END )
 As 'Categoria',
 202304 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202304)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202304
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    --------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' END )
 As 'Categoria',
 202306 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202307)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202306
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
        --------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202308 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202308)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202308
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
            --------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202310 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202310)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202310
    ) AS subquery
    WHERE rn = 1
    group by Clientenro

--------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202402 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202402)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202402
    ) AS subquery
    WHERE rn = 1
    group by Clientenro 
    ---------------------------------------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202404 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202404)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202404
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    ---------------------------------------------------------------------------------
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202406 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202406)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202406
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202408 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202408)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202408
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202410 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202410)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202410
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    
    
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202412 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202412)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202412
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    
    
    union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202502 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202502)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202502
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    

        union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202504 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202504)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202504
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
       

        union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202506 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202506)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202506
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
    
          

        union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202508 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202508)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202508
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
      
          

        union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202510 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202510)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202510
    ) AS subquery
    WHERE rn = 1
    group by Clientenro
          
          

        union all
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202512 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202512)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202512
    ) AS subquery
    WHERE rn = 1
    group by Clientenro        union all
 
 
 
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202602 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202602)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202602
    ) AS subquery
    WHERE rn = 1
    group by Clientenro        union all
     
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202604 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202604)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202604
    ) AS subquery
    WHERE rn = 1
    group by Clientenro         union all
     
    -----------------------------------------------------------------------------
 SELECT 
 Clientenro,
 MIN(case when PRODUCTONOMBRE like '%FTTH%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%GPON%' and PRODUCTOPPL='P'
 Then '1' 
  when PRODUCTONOMBRE  like '%G-PON%' and PRODUCTOPPL='P'
 Then '1' 
 when PRODUCTONOMBRE like '%EOC%' and PRODUCTOPPL='P'
 Then '2'
  when  PRODUCTOPPL='P'
 Then '3' 
 END )
 As 'Categoria',
 202606 as PERIODO
    FROM (
        SELECT contratonro, empresaid, contratosts, bdmodifieddate,PRODUCTONOMBRE,CLIENTENRO,PRODUCTOPPL,
               ROW_NUMBER() OVER (PARTITION BY contratonro,empresaid ORDER BY bdmodifieddate DESC) AS rn
        FROM contratos_con_lag
        WHERE CLIENTENRO IN 
        (SELECT distinct CLIENTENRO
        FROM MKT.NPS_202606)
        AND FORMAT(bdmodifieddate,'yyyyMM') <= 202606
    ) AS subquery
    WHERE rn = 1
    group by Clientenro;
```
