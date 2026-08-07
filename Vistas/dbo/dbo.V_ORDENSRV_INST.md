---
esquema: dbo
tabla: V_ORDENSRV_INST
objeto: dbo.V_ORDENSRV_INST
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

# dbo.V_ORDENSRV_INST

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.ORDENSRV]]
- [[SIGASC.PRODUCTO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ORDENNRO` | varchar | 0% |
| 3 | `CLIENTENROORD` | int | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `ORDENSTS` | varchar | 0% |
| 6 | `PRODUCTOID` | int | 0% |
| 7 | `ORDENFING` | datetime2 | 0% |
| 8 | `ORDENFFIN` | datetime2 | 2% |
| 9 | `ORDENFPROCESO` | datetime2 | 18% |
| 10 | `ORDENSOL` | varchar | 0% |
| 11 | `ORDENTRBRED` | int | 0% |
| 12 | `TECNICOID` | int | 0% |
| 13 | `ORDENUSRING` | varchar | 0% |
| 14 | `MOTIVOORDID` | int | 0% |
| 15 | `MOTIVOORDINGID` | int | 0% |
| 16 | `ORDENGEN` | varchar | 0% |
| 17 | `PKPRODUCTOID` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ORDENSRV_INST
-- Extraida: 2026-08-07T15:28:09.495612+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_ORDENSRV_INST]
AS SELECT 
	 O.EMPRESAID, CONCAT(O.EMPRESAID,CONCAT('_',ORDENNRO)) AS ORDENNRO,
	   CLIENTENROORD, O.CONTRATONRO, o.ORDENSTS, P.PRODUCTOID, ORDENFING, ORDENFFIN, o.ORDENFPROCESO,
	   ORDENSOL, ORDENTRBRED, o.TECNICOID, ORDENUSRING, MOTIVOORDID, MOTIVOORDINGID,  O.ORDENGEN ,
	   CONCAT(O.EMPRESAID,CONCAT('_',P.PRODUCTOID)) AS PKPRODUCTOID
FROM SIGASC.ORDENSRV O
LEFT JOIN SIGASC.CONTRATO C
ON O.CONTRATONRO=C.CONTRATONRO
AND O.EMPRESAID=C.EMPRESAID
LEFT JOIN SIGASC.PRODUCTO P
ON P.EMPRESAID = C.EMPRESAID
AND P.PRODUCTOID = C. PRODUCTOID

WHERE ordentpo = 'I'
AND ordenfing >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES
AND ordenfing <  GETDATE();
```
