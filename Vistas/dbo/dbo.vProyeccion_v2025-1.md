---
esquema: dbo
tabla: vProyeccion_v2025-1
objeto: dbo.vProyeccion_v2025-1
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 9
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.vProyeccion_v2025-1

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.BI_FACTURA_DETALLE_ALL]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `empresaid` | int |  |
| 2 | `clientenro` | int |  |
| 3 | `contratonro` | int |  |
| 4 | `FAC` | float |  |
| 5 | `PROMOID` | int |  |
| 6 | `TIPO_POLITICA` | varchar |  |
| 7 | `TIPO_PROD` | varchar |  |
| 8 | `CUOTA` | varchar |  |
| 9 | `MONTO_POLITICA` | real |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.vProyeccion_v2025-1
-- Extraida: 2026-08-07T15:28:34.829742+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vProyeccion_v2025-1]
AS SELECT 
T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
-----<<INT>>------
SELECT 
[empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC, MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID, MAX([Politica]) AS POLITICA_NOMBRE
,CASE 
            WHEN MAX([PoliticaId]) >= 70000 AND MAX([Politica]) LIKE '%super%' THEN 'LITE SUPER'
            WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
            ELSE 'OLD'
        END AS TIPO_POLITICA
,'INT' AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND PROMOID NOT IN (70000,70001,70002,70003,70004,70005,70006,70007,70008,70009,70010)
AND [PRODUCTOTPO] in ('c','l','e')
AND CPTOFACID NOT IN (9341,9342,9343,9344)
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND CPTOFACID NOT IN (9341,9342,9343,9344) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M' 
AND PROMOID NOT IN (70000,70001,70002,70003,70004,70005,70006,70007,70008,70009,70010)
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by 
empresaid, clientenro, contratonro, promoid ) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea   
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND CPTOFACID NOT IN (9341,9342,9343,9344)
AND [facturatpo]= 'F'
AND [facturagen]= 'M' and 
concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by empresaid, clientenro, contratonro, politicaid ) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID


---<<  TV  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC, MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID , MAX([Politica]) AS POLITICA_NOMBRE
,CASE 
            WHEN MAX([PoliticaId]) >= 70000 AND MAX([Politica]) LIKE '%super%' THEN 'LITE SUPER'
            WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
            ELSE 'OLD'
        END AS TIPO_POLITICA
,'TV' AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND PROMOID NOT IN (70000,70001,70002,70003,70004,70005,70006,70007,70008,70009,70010)
AND [PRODUCTOTPO] in ('B','Z','W')
AND CPTOFACID NOT IN (9341,9342,9343,9344)
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro] ) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota 
 FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND CPTOFACID NOT IN (9341,9342,9343,9344) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M' 
AND PROMOID NOT IN (70000,70001,70002,70003,70004,70005,70006,70007,70008,70009,70010)
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea  
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND CPTOFACID NOT IN (9341,9342,9343,9344)
AND [facturatpo]= 'F'
AND [facturagen]= 'M' 
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by 
empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  DECO  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'DECO' AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('D')
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
AND productonombre NOT like '%adic%'

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID


---<<  DECO ADIC >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'DECO ADIC' AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('D')
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
AND productonombre like '%adic%'

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) as T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID


---<<  MIO ANALOGICO E INTERNET  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'MIO ANALOGICO E INTERNET'  AS TIPO_PROD
FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('M')
AND productoid in (6409,70049,70050,70062,70063)


GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid ) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  MIO DIGITAL  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'MIO DIGITAL'  AS TIPO_PROD
FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('M')
AND productoid in (6402,6418,70048,70061)


GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid ) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID


---<<  MIO STAND ALONE  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'MIO STAND ALONE'  AS TIPO_PROD
FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('M')
AND productoid  = 70044

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid ) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  MIO PREMIUM  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'MIO PREMIUM'  AS TIPO_PROD
FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('M')
AND productoid NOT in (6402, 6409,6418, 70048, 70049,70050,70061, 70062,70063, 70083, 70044, 70074)

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid ) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID


---<<  MIO + PARAMOUNT+ >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'MIO + PARAMOUNT+'  AS TIPO_PROD
FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('M')
AND productoid = 70083

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid ) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID


---<<  skeelo  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'SKEELO'  AS TIPO_PROD
FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, 1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('Y')

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, 1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, 1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid ) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  PARAMOUNT  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'PARAMOUNT'  AS TIPO_PROD
FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND [PRODUCTOTPO] in ('M')
AND productoid in  (6393,6394,6407,70052)

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea  
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  UNIVERSAL  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'UNIVERSAL'  AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND productoid in  (6411,6415,6416,70041,70042,70053,70075)

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea  
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  MAX  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'MAX'  AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND productoid in  (70080)

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  MTI  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'MTI'  AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND productoTPO ='Q'
and politicaid<>70195

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M' 

group by 
empresaid, clientenro, contratonro, promoid
) D

ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea  
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M' 

group by empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  ADULTO  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'ADULTO'  AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND productoTPO IN ('A')
AND (PRODUCTONOMBRE LIKE ('%ADULTO%') or PRODUCTONOMBRE LIKE ('%800-801%'))

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea  
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  HBO  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'HBO'  AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND (PRODUCTONOMBRE LIKE ('%HBO%') or PRODUCTONOMBRE like ('%pack full%'))

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  FUTBOL  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'FUTBOL'  AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND PRODUCTONOMBRE LIKE ('%FUTBOL%')

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
group by empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  BOCAS  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID, MAX([Politica]) AS POLITICA_NOMBRE
,CASE 
            WHEN MAX([Politica]) LIKE '%multiple%' THEN 'MULTIPLE'
            ELSE 'RESIDENCIAL'
        END AS TIPO_POLITICA
,'BOCAS'  AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND PRODUCTOTPO= 'R'
and concepto not LIKE ('%CONEXION%')
and concepto not LIKE ('%INSTAL%')

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota 
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M' 
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M' 
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')

group by empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID

---<<  CORPO  >>---
UNION ALL
SELECT T.[empresaid], T.[clientenro], T.[contratonro], T.FAC, T.PROMOID, T.TIPO_POLITICA, T.TIPO_PROD, 
CASE WHEN D.PROMOID >0 THEN D.CUOTA END AS CUOTA, P.IMPORTE_LINEA AS MONTO_POLITICA
FROM (
SELECT [empresaid],[clientenro],[contratonro],SUM([IMPORTE_LINEA]) AS FAC,MAX([PROMOID]) AS PROMOID
,MAX([PoliticaId]) as POLITICAID
,CASE 
    WHEN MAX([PoliticaId]) >= 70000 THEN 'LITE'
    ELSE 'OLD'
    END AS TIPO_POLITICA
,'CORPO'  AS TIPO_PROD

FROM [dbo].[BI_FACTURA_DETALLE_ALL]
where [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND CPTOFACID NOT IN (9341,9342,9343,9344)
AND PRODUCTOTPO = 'N'
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
AND politica NOT LIKE '%SAP%'
AND politica NOT LIKE '%USD%'

GROUP BY 
[empresaid]
,[clientenro]
,[contratonro]) AS T

LEFT JOIN (SELECT empresaid, clientenro, contratonro, promoid, max(cuota) as cuota
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT) 
AND [facturatpo]= 'F'
AND [facturagen]= 'M'
AND CPTOFACID NOT IN (9341,9342,9343,9344)
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%') 
AND politica NOT LIKE '%SAP%'
AND politica NOT LIKE '%USD%'
group by 
empresaid, clientenro, contratonro, promoid
) D
ON T.empresaid = D.EMPRESAID
AND T.clientenro= D.clientenro
AND T.contratonro= D.contratonro
AND T.PROMOID= D.PROMOID

LEFT JOIN (SELECT empresaid, clientenro, contratonro, politicaid, max(importe_linea) as importe_linea  
FROM [dbo].[BI_FACTURA_DETALLE_ALL] 
WHERE [PERIODO] = CAST(FORMAT(DATEADD(MONTH, -1, GETDATE()), 'yyyyMM') AS INT)
AND PROMOID=0 AND COMBOID=0 
AND [facturatpo]= 'F'
AND [facturagen]= 'M' 
AND CPTOFACID NOT IN (9341,9342,9343,9344)
and concepto not like ('%CONEXION%')
and concepto not like ('%INSTAL%')
AND politica NOT LIKE '%SAP%'
AND politica NOT LIKE '%USD%'
group by empresaid, clientenro, contratonro, politicaid
) P
ON T.empresaid = P.EMPRESAID
AND T.clientenro= P.clientenro
AND T.contratonro= P.contratonro
AND T.POLITICAID= P.POLITICAID;
```
