---
esquema: dbo
tabla: V_NPS_RECLAMOS
objeto: dbo.V_NPS_RECLAMOS
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

# dbo.V_NPS_RECLAMOS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[MKT.NPS_YYYYMM]]
- [[SIGASC.CRMREGISTRO]]
- [[SIGASC.ORDENSRV]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Clientenro` | bigint | 0% |
| 2 | `PERIODO` | int | 0% |
| 3 | `EMPRESAID` | int | 0% |
| 4 | `Cant_Reclamos` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_NPS_RECLAMOS
-- Extraida: 2026-08-07T15:28:04.483894+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_NPS_RECLAMOS]
AS SELECT n.[Clientenro],202205 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202205]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202203
	AND FORMAT(ordenfing,'yyyyMM')  <=  202205
group by n.[Clientenro]
,o.[EMPRESAID]
union all
SELECT n.[Clientenro],202207 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202207]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202205
	AND FORMAT(ordenfing,'yyyyMM')  <=  202207
group by n.[Clientenro]
,o.[EMPRESAID]
union all
SELECT n.[Clientenro],202209 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202209]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202207
	AND FORMAT(ordenfing,'yyyyMM')  <=  202209
group by n.[Clientenro]
,o.[EMPRESAID]
union all
SELECT n.[Clientenro],202211 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202211]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202209
	AND FORMAT(ordenfing,'yyyyMM')  <=  202211
group by n.[Clientenro]
,o.[EMPRESAID]
union all
SELECT n.[Clientenro],202302 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202302]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202212
	AND FORMAT(ordenfing,'yyyyMM')  <=  202302
group by n.[Clientenro]
,o.[EMPRESAID]
union all
SELECT n.[Clientenro],202304 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202304]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202302
	AND FORMAT(ordenfing,'yyyyMM')  <=  202304
group by n.[Clientenro]
,o.[EMPRESAID]
union all
SELECT n.[Clientenro],202306 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202307]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202304
	AND FORMAT(ordenfing,'yyyyMM')  <=  202306
group by n.[Clientenro]
,o.[EMPRESAID]
union all
SELECT n.[Clientenro],202308 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202308]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202306
	AND FORMAT(ordenfing,'yyyyMM')  <=  202308
group by n.[Clientenro]
,o.[EMPRESAID]
union all
SELECT n.[Clientenro],202310 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202310]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202308
	AND FORMAT(ordenfing,'yyyyMM')  <=  202310
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202402 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202402]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202312
	AND FORMAT(ordenfing,'yyyyMM')  <=  202402
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202404 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202404]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202402
	AND FORMAT(ordenfing,'yyyyMM')  <=  202404
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202406 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202406]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202404
	AND FORMAT(ordenfing,'yyyyMM')  <=  202406
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202408 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202408]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202406
	AND FORMAT(ordenfing,'yyyyMM')  <=  202408
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202410 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202410]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202408
	AND FORMAT(ordenfing,'yyyyMM')  <=  202410
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202412 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202412]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202410
	AND FORMAT(ordenfing,'yyyyMM')  <=  202412
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202502 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202502]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202412
	AND FORMAT(ordenfing,'yyyyMM')  <=  202502
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202504 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202504]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202502
	AND FORMAT(ordenfing,'yyyyMM')  <=  202504
group by n.[Clientenro]
,o.[EMPRESAID]


union all
SELECT n.[Clientenro],202506 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202506]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202504
	AND FORMAT(ordenfing,'yyyyMM')  <=  202506
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202508 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202508]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202506
	AND FORMAT(ordenfing,'yyyyMM')  <=  202508
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202510 as PERIODO
,o.[EMPRESAID],count(distinct o.ORDENNRO) as Cant_Reclamos
	FROM SIGASC.ORDENSRV o
	inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202510]) n
 on o.CLIENTENROORD = n.CLIENTENRO
	WHERE ordentpo = 'R'
	AND FORMAT(ordenfing,'yyyyMM') > 202508
	AND FORMAT(ordenfing,'yyyyMM')  <=  202510
group by n.[Clientenro]
,o.[EMPRESAID]

union all
SELECT n.[Clientenro],202512 as PERIODO
,crm.[EMPRESAID],count(distinct crm.CRMNRO) as Cant_IntBaja
    FROM SIGASC.CRMREGISTRO CRM  
    inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202512]) n
 on crm.CLIENTENRO = n.CLIENTENRO
    WHERE FORMAT(crmfchini,'yyyyMM') > 202510
    AND FORMAT(crmfchini,'yyyyMM')  <=  202512
    and CRM.CRMMOTIVO1 in (37,45,38,27)
group by n.[Clientenro]
,crm.[EMPRESAID]

union all
SELECT n.[Clientenro],202602 as PERIODO
,crm.[EMPRESAID],count(distinct crm.CRMNRO) as Cant_IntBaja
    FROM SIGASC.CRMREGISTRO CRM  
    inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202602]) n
 on crm.CLIENTENRO = n.CLIENTENRO
    WHERE FORMAT(crmfchini,'yyyyMM') > 202512
    AND FORMAT(crmfchini,'yyyyMM')  <=  202602
    and CRM.CRMMOTIVO1 in (37,45,38,27)
group by n.[Clientenro]
,crm.[EMPRESAID]


union all
SELECT n.[Clientenro],202604 as PERIODO
,crm.[EMPRESAID],count(distinct crm.CRMNRO) as Cant_IntBaja
    FROM SIGASC.CRMREGISTRO CRM  
    inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202604]) n
 on crm.CLIENTENRO = n.CLIENTENRO
    WHERE FORMAT(crmfchini,'yyyyMM') > 202602
    AND FORMAT(crmfchini,'yyyyMM')  <=  202604
    and CRM.CRMMOTIVO1 in (37,45,38,27)
group by n.[Clientenro]
,crm.[EMPRESAID]



union all
SELECT n.[Clientenro],202606 as PERIODO
,crm.[EMPRESAID],count(distinct crm.CRMNRO) as Cant_IntBaja
    FROM SIGASC.CRMREGISTRO CRM  
    inner join (SELECT 
[Clientenro]
 FROM [MKT].[NPS_202606]) n
 on crm.CLIENTENRO = n.CLIENTENRO
    WHERE FORMAT(crmfchini,'yyyyMM') > 202604
    AND FORMAT(crmfchini,'yyyyMM')  <=  202606
    and CRM.CRMMOTIVO1 in (37,45,38,27)
group by n.[Clientenro]
,crm.[EMPRESAID];
```
