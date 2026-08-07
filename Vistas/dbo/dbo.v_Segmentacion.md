---
esquema: dbo
tabla: v_Segmentacion
objeto: dbo.v_Segmentacion
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 19
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_Segmentacion

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.CRMREGISTRO]]
- [[SIGASC.FACTURA]]
- [[SIGASC.FACTURALINEA]]
- [[SIGASC.H_VM_CLIENTE]]
- [[SIGASC.ORDENSRV]]
- [[SIGASC.PRODUCTO]]
- [[SIGASC.VM_CLIENTE]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `clientenro` | int | 0% |
| 3 | `clienteci` | varchar | 0% |
| 4 | `PERIODO` | int | 0% |
| 5 | `FACTURACION` | float | 0% |
| 6 | `CantMesesAdeudados` | int | 0% |
| 7 | `CANT_CRM_bajas_3M` | int | 0% |
| 8 | `CANT_CRM_bajas_M` | int | 0% |
| 9 | `CANT_CRM_otros_3M` | int | 0% |
| 10 | `CANT_CRM_otros_M` | int | 0% |
| 11 | `CANT_ORD_RECONEXIONES_3M` | int | 0% |
| 12 | `CANT_ORD_RECONEXIONES_M` | int | 0% |
| 13 | `CANT_ORD_RECLAMOS_3M` | int | 0% |
| 14 | `CANT_ORD_RECLAMOS_M` | int | 0% |
| 15 | `TieneAsistenciaIntegral` | int | 0% |
| 16 | `clientests` | varchar | 0% |
| 17 | `CLIENTENATURALEZAID` | int | 0% |
| 18 | `NEGOCIOSEGMENTO` | int | 0% |
| 19 | `antigüedad` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_Segmentacion
-- Extraida: 2026-08-07T15:28:18.297083+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_Segmentacion]
AS WITH clientes_fixeados AS (
  SELECT C.[EMPRESAID]
      ,C.[CLIENTENRO]
      ,C.[CLIENTESTS]
	  ,C.[PKCLIENTENRO]
      ,CASE
		when C.[BDMODIFIEDDATE] > '1990-01-01' THEN C.[BDMODIFIEDDATE] 
        WHEN C.[BDMODIFIEDDATE] < '1990-01-01' and C.[CLIENTESTS] = 'C' THEN '2022-09-01'
        ELSE null
    END AS BDMODIFIEDDATE
  FROM [SIGASC].[H_VM_CLIENTE] C
  where (C.[CLIENTESTS] = 'C' or C.[BDMODIFIEDDATE] > '1900-01-01')
),
Antiguedad_min as (
SELECT clientenro, empresaid, MIN(bdmodifieddate) AS ultimo_estado
FROM clientes_fixeados
WHERE clientenro IN (
  SELECT DISTINCT clientenro
  FROM sigasc.factura
  WHERE (facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM')
  or facturaperiodo = FORMAT(DATEADD(month,12,DATEADD(year, -1,GETDATE())),'yyyyMM')
  or facturaperiodo = FORMAT(DATEADD(month,11,DATEADD(year, -1,GETDATE())),'yyyyMM'))
)
and clientests = 'C'
GROUP BY clientenro, empresaid),
Antiguedad_max as (
SELECT clientenro, empresaid, MAX(bdmodifieddate) AS ultimo_estado
FROM clientes_fixeados
WHERE clientenro IN (
  SELECT DISTINCT clientenro
  FROM sigasc.factura
  WHERE facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM')
)
and clientests = 'C'
GROUP BY clientenro, empresaid)
,
Logica_fechas as (
select FORMAT(DATEADD(month,10,DATEADD(year, -1,GETDATE())),'yyyyMM') as periodo union all 
select FORMAT(DATEADD(month,11,DATEADD(year, -1,GETDATE())),'yyyyMM') as periodo union all 
select FORMAT(DATEADD(month,12,DATEADD(year, -1,GETDATE())),'yyyyMM') as periodo
),
Logica_fechas_anteriores as (
select FORMAT(DATEADD(month,10,DATEADD(year, -1,GETDATE())),'yyyyMM') as periodo union all 
select FORMAT(DATEADD(month,11,DATEADD(year, -1,GETDATE())),'yyyyMM') as periodo
),
Logica_fechas_actual as (
select FORMAT(DATEADD(month,12,DATEADD(year, -1,GETDATE())),'yyyyMM') as periodo
)
---------------------------------------------------------------------------------

SELECT
f.EMPRESAID,
cl.clientenro,
cl.clienteci,
f.facturaperiodo as PERIODO,
sum(d.facturalinimp) AS FACTURACION,
--LOC.GEODIV1NOMBRE AS LOCALIDAD,
-- sum(
-- case when d.facturaprm = 0 and D.facturapol > 0 and D.facturacmb =0
-- and d.cptofacid not in
-- ( 9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_POLITICA,
--     sum(
-- case when d.facturaprm > 0 and d.cptofacid not in
-- (9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_DESCUENTOS,
--     sum(
-- case when D.facturacmb > 0 and d.cptofacid not in
-- (9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_COMBO,
--         sum(
-- case when d.cptofacid in
-- (
--     9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_CARGOS,
(select count(*)
                from ( select distinct clientenro,facturaperiodo 
                          from sigasc.factura f 
                          where 
                          facturasts in ('I','E') 
                          and f.facturatpo='F'
                         ) d
    where d.clientenro = cl.clientenro) as CantMesesAdeudados,
    (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_anteriores
) and CRMMOTIVO1 <> 2) as CANT_CRM_bajas_3M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_actual
) and CRMMOTIVO1 <> 2) as CANT_CRM_bajas_M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 not in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_anteriores
) and CRMMOTIVO1 <> 2) as CANT_CRM_otros_3M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 not in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_actual
) and CRMMOTIVO1 <> 2) as CANT_CRM_otros_M,
(select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'U'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_anteriores
))
AS CANT_ORD_RECONEXIONES_3M,
(select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'U'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_actual
))
AS CANT_ORD_RECONEXIONES_M,
 (select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'R'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_anteriores
))
as CANT_ORD_RECLAMOS_3M,
 (select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'R'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_actual
))
as CANT_ORD_RECLAMOS_M,
MAX(case
      when p.productotpo = 'Q' then 1 else 0
    end) as TieneAsistenciaIntegral,
    cl.clientests,
    cl.CLIENTENATURALEZAID,
    cl.NEGOCIOSEGMENTO,
    -- MCOB.MEDCOBRONOMBRE as MEDIOCOBRO_CLI,
   -- MCOBF.MEDCOBRONOMBRE as MEDIOCOBRO_FAC,
    -- rep.repartonombre,
   -- ct.CLIENTETPONOM,
	DATEDIFF ( month , a.ultimo_estado , getdate() )  as antigüedad
--	,DATEDIFF ( month , b.ultimo_estado , getdate() )  as antigüedad_max
FROM sigasc.factura f
INNER JOIN sigasc.facturalinea d ON F.facturanro = D.facturanro AND F.empresaid = D.empresaid AND f.FACTURATPO = d.FACTURATPO
left join SIGASC.VM_CLIENTE cl on CL.clientenro = f.clientenro and cl.empresaid = f.empresaid
LEFT JOIN sigasc.contrato c
  ON D.empresaid = C.empresaid
  AND F.clientenro = C.clientenro
  AND D.facturalincod = C.contratonro
          LEFT JOIN sigasc.producto p
             ON F.empresaid = P.empresaid 
             AND C.productoid = P.productoid
-- left join (select g.GEODIV1ID,g.GEODIV1NOMBRE
-- from sigamsasc.geodiv1 g
-- group by g.GEODIV1ID,g.GEODIV1NOMBRE
-- ) loc on loc.GEODIV1ID = CL.GEODIV1ID
-- LEFT JOIN sigasc.mediocobro mcob ON mcob.medcobroid = cl.medcobroid
--LEFT JOIN sigasc.mediocobro mcobf ON mcobf.medcobroid = f.MEDCOBFAC
-- LEFT JOIN sigasc.reparto rep ON rep.repartoid = cl.repartocliid AND rep.empresaid = f.EMPRESAID 
--left join SIGASC.CLIENTETPO ct on ct.CLIENTETPO = cl.CLIENTETPO
left join antiguedad_min a on a.clientenro = cl.clientenro
--left join antiguedad_max b on b.clientenro = cl.clientenro
where F.facturatpo = 'F'
and f.facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM')
--and f.empresaid = 25
group by f.EMPRESAID,cl.clientenro,f.facturaperiodo,
    cl.CLIENTESTS, 
    cl.CLIENTENATURALEZAID,
    cl.NEGOCIOSEGMENTO,
    cl.clienteci,
    --LOC.GEODIV1NOMBRE,
    -- MCOB.MEDCOBRONOMBRE,
   -- MCOBF.MEDCOBRONOMBRE ,
    -- rep.repartonombre,
   -- ct.CLIENTETPONOM,
    DATEDIFF(month , a.ultimo_estado , getdate())
union all
SELECT
f.EMPRESAID,
cl.clientenro,
cl.clienteci,
f.facturaperiodo as PERIODO,
sum(d.facturalinimp) AS FACTURACION,
--LOC.GEODIV1NOMBRE AS LOCALIDAD,
-- sum(
-- case when d.facturaprm = 0 and D.facturapol > 0 and D.facturacmb =0
-- and d.cptofacid not in
-- ( 9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_POLITICA,
--     sum(
-- case when d.facturaprm > 0 and d.cptofacid not in
-- (9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_DESCUENTOS,
--     sum(
-- case when D.facturacmb > 0 and d.cptofacid not in
-- (9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_COMBO,
--         sum(
-- case when d.cptofacid in
-- (
--     9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_CARGOS,
(select count(*)
                from ( select distinct clientenro,facturaperiodo 
                          from sigasc.factura f 
                          where 
                          facturasts in ('I','E') 
                          and f.facturatpo='F'
                         ) d
    where d.clientenro = cl.clientenro) as CantMesesAdeudados,
     (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_anteriores
) and CRMMOTIVO1 <> 2) as CANT_CRM_bajas_3M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_actual
) and CRMMOTIVO1 <> 2) as CANT_CRM_bajas_M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 not in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_anteriores
) and CRMMOTIVO1 <> 2) as CANT_CRM_otros_3M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 not in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_actual
) and CRMMOTIVO1 <> 2) as CANT_CRM_otros_M,
(select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'U'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_anteriores
))
AS CANT_ORD_RECONEXIONES_3M,
(select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'U'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_actual
))
AS CANT_ORD_RECONEXIONES_M,
 (select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'R'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_anteriores
))
as CANT_ORD_RECLAMOS_3M,
 (select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'R'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_actual
))
as CANT_ORD_RECLAMOS_M,
MAX(case
      when p.productotpo = 'Q' then 1 else 0
    end) as TieneAsistenciaIntegral,
    cl.clientests,
    cl.CLIENTENATURALEZAID,
    cl.NEGOCIOSEGMENTO,
    -- MCOB.MEDCOBRONOMBRE as MEDIOCOBRO_CLI,
  --  MCOBF.MEDCOBRONOMBRE as MEDIOCOBRO_FAC,
    -- rep.repartonombre,
   -- ct.CLIENTETPONOM,
	DATEDIFF ( month , a.ultimo_estado , getdate() )  as antigüedad
--	,DATEDIFF ( month , b.ultimo_estado , getdate() )  as antigüedad_max
FROM sigasc.factura f
INNER JOIN sigasc.facturalinea d ON F.facturanro = D.facturanro AND F.empresaid = D.empresaid AND f.FACTURATPO = d.FACTURATPO
left join SIGASC.VM_CLIENTE cl on CL.clientenro = f.clientenro and cl.empresaid = f.empresaid
LEFT JOIN sigasc.contrato c
  ON D.empresaid = C.empresaid
  AND F.clientenro = C.clientenro
  AND D.facturalincod = C.contratonro
          LEFT JOIN sigasc.producto p
             ON F.empresaid = P.empresaid 
             AND C.productoid = P.productoid
-- left join (select g.GEODIV1ID,g.GEODIV1NOMBRE
-- from sigamsasc.geodiv1 g
-- group by g.GEODIV1ID,g.GEODIV1NOMBRE
-- ) loc on loc.GEODIV1ID = CL.GEODIV1ID
-- LEFT JOIN sigasc.mediocobro mcob ON mcob.medcobroid = cl.medcobroid
--LEFT JOIN sigasc.mediocobro mcobf ON mcobf.medcobroid = f.MEDCOBFAC
-- LEFT JOIN sigasc.reparto rep ON rep.repartoid = cl.repartocliid AND rep.empresaid = f.EMPRESAID 
--left join SIGASC.CLIENTETPO ct on ct.CLIENTETPO = cl.CLIENTETPO
left join antiguedad_min a on a.clientenro = cl.clientenro
--left join antiguedad_max b on b.clientenro = cl.clientenro
where F.facturatpo = 'F'
and f.facturaperiodo = FORMAT(DATEADD(month,12,DATEADD(year, -1,GETDATE())),'yyyyMM')
and f.clientenro not in (
    SELECT
distinct clientenro
FROM sigasc.factura f
where F.facturatpo = 'F'
and f.facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM')
)
--and f.empresaid = 25
group by f.EMPRESAID,cl.clientenro,f.facturaperiodo,
    cl.CLIENTESTS, 
    cl.CLIENTENATURALEZAID,
    cl.NEGOCIOSEGMENTO,
    cl.clienteci,
    --LOC.GEODIV1NOMBRE,
    -- MCOB.MEDCOBRONOMBRE,
  --  MCOBF.MEDCOBRONOMBRE ,
    -- rep.repartonombre,
   -- ct.CLIENTETPONOM,
    DATEDIFF(month , a.ultimo_estado , getdate())  
union all
SELECT
f.EMPRESAID,
cl.clientenro,
cl.clienteci,
f.facturaperiodo as PERIODO,
sum(d.facturalinimp) AS FACTURACION,
--LOC.GEODIV1NOMBRE AS LOCALIDAD,
-- sum(
-- case when d.facturaprm = 0 and D.facturapol > 0 and D.facturacmb =0
-- and d.cptofacid not in
-- ( 9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_POLITICA,
--     sum(
-- case when d.facturaprm > 0 and d.cptofacid not in
-- (9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_DESCUENTOS,
--     sum(
-- case when D.facturacmb > 0 and d.cptofacid not in
-- (9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_COMBO,
--         sum(
-- case when d.cptofacid in
-- (
--     9341,9342,9343,9344,12,23,36,37,70,255,434,3076,9097,
-- 9246,9308,9460,2,22,64,136,431,442,683,685,970,980,1434,3050,15,49,80,138,
-- 436,701,903,9085,9087,9276,9478,1,5,637,1436,9064,9164,9204,9464,9466,9474
-- ) 
--     then d.facturalinimp
--     else 0
--     end
--     ) as MONTO_CARGOS,
(select count(*)
                from ( select distinct clientenro,facturaperiodo 
                          from sigasc.factura f 
                          where 
                          facturasts in ('I','E') 
                          and f.facturatpo='F'
                         ) d
    where d.clientenro = cl.clientenro) as CantMesesAdeudados,
     (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_anteriores
) and CRMMOTIVO1 <> 2) as CANT_CRM_bajas_3M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_actual
) and CRMMOTIVO1 <> 2) as CANT_CRM_bajas_M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 not in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_anteriores
) and CRMMOTIVO1 <> 2) as CANT_CRM_otros_3M,
 (SELECT COUNT(*) FROM SIGASC.CRMREGISTRO CRM  
    WHERE CRM.CLIENTENRO = CL.CLIENTENRO
    and CRM.CRMMOTIVO1 not in (37,45,38,27)
 AND FORMAT(CRM.CRMFCHINI,'yyyyMM')  in 
(
 select periodo
 from Logica_fechas_actual
) and CRMMOTIVO1 <> 2) as CANT_CRM_otros_M,
(select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'U'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_anteriores
))
AS CANT_ORD_RECONEXIONES_3M,
(select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'U'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_actual
))
AS CANT_ORD_RECONEXIONES_M,
 (select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'R'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_anteriores
))
as CANT_ORD_RECLAMOS_3M,
 (select COUNT(distinct OS.ORDENNRO)
from SIGASC.ORDENSRV os 
where  ORDENTPO = 'R'
AND os.CLIENTENROORD = CL.CLIENTENRO 
AND FORMAT(os.ORDENFING,'yyyyMM')  in 
(
select periodo
 from Logica_fechas_actual
))
as CANT_ORD_RECLAMOS_M,
MAX(case
      when p.productotpo = 'Q' then 1 else 0
    end) as TieneAsistenciaIntegral,
    cl.clientests,
    cl.CLIENTENATURALEZAID,
    cl.NEGOCIOSEGMENTO,
    -- MCOB.MEDCOBRONOMBRE as MEDIOCOBRO_CLI,
  --  MCOBF.MEDCOBRONOMBRE as MEDIOCOBRO_FAC,
    -- rep.repartonombre,
   -- ct.CLIENTETPONOM,
	DATEDIFF ( month , a.ultimo_estado , getdate() )  as antigüedad
--	,DATEDIFF ( month , b.ultimo_estado , getdate() )  as antigüedad_max
FROM sigasc.factura f
INNER JOIN sigasc.facturalinea d ON F.facturanro = D.facturanro AND F.empresaid = D.empresaid AND f.FACTURATPO = d.FACTURATPO
left join SIGASC.VM_CLIENTE cl on CL.clientenro = f.clientenro and cl.empresaid = f.empresaid
LEFT JOIN sigasc.contrato c
  ON D.empresaid = C.empresaid
  AND F.clientenro = C.clientenro
  AND D.facturalincod = C.contratonro
          LEFT JOIN sigasc.producto p
             ON F.empresaid = P.empresaid 
             AND C.productoid = P.productoid
-- left join (select g.GEODIV1ID,g.GEODIV1NOMBRE
-- from sigamsasc.geodiv1 g
-- group by g.GEODIV1ID,g.GEODIV1NOMBRE
-- ) loc on loc.GEODIV1ID = CL.GEODIV1ID
-- LEFT JOIN sigasc.mediocobro mcob ON mcob.medcobroid = cl.medcobroid
--LEFT JOIN sigasc.mediocobro mcobf ON mcobf.medcobroid = f.MEDCOBFAC
-- LEFT JOIN sigasc.reparto rep ON rep.repartoid = cl.repartocliid AND rep.empresaid = f.EMPRESAID 
--left join SIGASC.CLIENTETPO ct on ct.CLIENTETPO = cl.CLIENTETPO
left join antiguedad_min a on a.clientenro = cl.clientenro
--left join antiguedad_max b on b.clientenro = cl.clientenro
where F.facturatpo = 'F'
and f.facturaperiodo = FORMAT(DATEADD(month,11,DATEADD(year, -1,GETDATE())),'yyyyMM')
and f.clientenro not in (
    SELECT
distinct clientenro
FROM sigasc.factura f
where F.facturatpo = 'F'
and (f.facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM')
or f.facturaperiodo = FORMAT(DATEADD(month,12,DATEADD(year, -1,GETDATE())),'yyyyMM'))
)
--and f.empresaid = 25
group by f.EMPRESAID,cl.clientenro,f.facturaperiodo,
    cl.CLIENTESTS, 
    cl.CLIENTENATURALEZAID,
    cl.NEGOCIOSEGMENTO,
    cl.clienteci,
    --LOC.GEODIV1NOMBRE,
    -- MCOB.MEDCOBRONOMBRE,
 --   MCOBF.MEDCOBRONOMBRE ,
    -- rep.repartonombre,
   -- ct.CLIENTETPONOM,
    DATEDIFF(month , a.ultimo_estado , getdate());
```
