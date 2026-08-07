---
esquema: dbo
tabla: V_CONTRATOS_BDDD
objeto: dbo.V_CONTRATOS_BDDD
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 24
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_CONTRATOS_BDDD

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.H_CONTRATO]]
- [[SIGASC.PRODUCTO]]
- [[SIGASC.PROMOTOR]]
- [[SIGASC.PROMOTORGRUPO]]
- [[SIGASC.VM_CLIENTE]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CONTRATONRO` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `PRODUCTOID` | int | 0% |
| 5 | `CONTRATOSTS` | nvarchar | 0% |
| 6 | `BDMODIFIEDDATE` | date | 0% |
| 7 | `PKCONTRATONRO` | nvarchar | 0% |
| 8 | `PKPRODUCTOID` | nvarchar | 0% |
| 9 | `PRODUCTOTPO` | varchar | 0% |
| 10 | `PRODUCTOPPL` | varchar | 0% |
| 11 | `CONTRATOFINS` | date | 4% |
| 12 | `CONTRATOFDES` | date | 28% |
| 13 | `CONTRATOUSR` | varchar | 0% |
| 14 | `PROMOTORID` | int | 0% |
| 15 | `CONTRATOGEN` | varchar | 0% |
| 16 | `PROMOTORGRUPOID` | int | 8% |
| 17 | `PROMOTORGRUPONOMBRE` | varchar | 8% |
| 18 | `CLIENTEFCHING` | date | 0% |
| 19 | `CLIENTECP` | varchar | 0% |
| 20 | `LOCALIDADID` | int | 0% |
| 21 | `DPTOID` | int | 0% |
| 22 | `CLIENTESTS` | varchar | 0% |
| 23 | `CLIENTEUSRING` | varchar | 0% |
| 24 | `MEDCOBROID` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CONTRATOS_BDDD
-- Extraida: 2026-08-07T15:27:50.431840+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_CONTRATOS_BDDD]
AS SELECT  
    c.[EMPRESAID],
    c.[CONTRATONRO],
    c.[CLIENTENRO],
    c.[PRODUCTOID],
    c.[CONTRATOSTS],
    CONVERT(date,c.[BDMODIFIEDDATE]) as BDMODIFIEDDATE ,
    c.[PKCONTRATONRO],
    c.[PKPRODUCTOID],
    p.[PRODUCTOTPO],
    p.[PRODUCTOPPL],
    -- CASE 
    --     WHEN p.[PRODUCTOTPO] IN ('b','z','w') THEN 'TV'
    --     WHEN p.[PRODUCTOTPO] IN ('c','i','l','e') THEN 'INT'
    --     WHEN p.[PRODUCTOTPO] = 'N' THEN 'CORPO'
    --     WHEN p.[PRODUCTOTPO] = 'Y' THEN 'SKEELO'
    --     WHEN p.[PRODUCTOTPO] = 'M' THEN 'MIO'
    --     WHEN p.[PRODUCTOTPO] = 'D' THEN 'DIGITAL'
    --     WHEN p.[PRODUCTOTPO] = 'A' THEN 'PREMIUM'
    --     WHEN p.[PRODUCTOTPO] = 'O' THEN 'BOCAS'
    --     WHEN p.[PRODUCTOTPO] = 'Q' THEN 'MTI'
    --     ELSE 'OTRO'
    -- END AS NEGOCIO,
    CONVERT(date,CON.[CONTRATOFINS]) as CONTRATOFINS,
    CONVERT(date,CON.[CONTRATOFDES]) as CONTRATOFDES,
    CON.[CONTRATOUSR],
    CON.[PROMOTORID],
    CON.CONTRATOGEN,
    PG.[PROMOTORGRUPOID],
    PG.[PROMOTORGRUPONOMBRE],
    CONVERT(date,CL.CLIENTEFCHING) as CLIENTEFCHING,
    CL.CLIENTECP,
    CL.[GEODIV1ID] as LOCALIDADID,
    CL.[GEODIV2ID] AS DPTOID,
    CL.CLIENTESTS,
    CL.CLIENTEUSRING,
    CL.MEDCOBROID

FROM [SIGASC].[H_CONTRATO] c
LEFT JOIN [SIGASC].[PRODUCTO] p
    ON c.[PKPRODUCTOID] = p.[PKPRODUCTOID]
LEFT JOIN  [SIGASC].[CONTRATO] CON
    ON C.[PKCONTRATONRO] = CON.[PKCONTRATONRO]
LEFT JOIN  [SIGASC].[PROMOTOR] pro
    ON CON.[PROMOTORID] = PRO.[PROMOTORID]
    and c.empresaid = PRO.empresaid
  LEFT JOIN  [SIGASC].[PROMOTORGRUPO] PG
    ON PRO.[PROMOTORGRUPOID] = PG.[PROMOTORGRUPOID]  
     and c.empresaid = Pg.empresaid

LEFT JOIN  [SIGASC].[VM_CLIENTE] CL    
    ON c.[EMPRESAID]= CL.EMPRESAID
      AND  c.[CLIENTENRO] = CL.CLIENTENRO

WHERE 
    (CON.[CONTRATOFDES] IS NULL 
     OR CON.[CONTRATOFDES] >= '2024-01-01') 
AND C.EMPRESAID NOT IN (15,19);
```
