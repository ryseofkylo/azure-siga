---
esquema: dbo
tabla: V_RECLAMOS_BDDD
objeto: dbo.V_RECLAMOS_BDDD
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 14
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_RECLAMOS_BDDD

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.DOMINIOS]]
- [[SIGASC.MOTIVOORD]]
- [[SIGASC.ORDENSRV]]
- [[SIGASC.PRODUCTO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ORDENNRO` | varchar | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `ORDENSTS` | varchar | 0% |
| 6 | `ORDENFING` | datetime2 | 0% |
| 7 | `ORDENFFIN` | datetime2 | 2% |
| 8 | `ORDENFPROCESO` | datetime2 | 0% |
| 9 | `ORDENSOL` | varchar | 0% |
| 10 | `DESCRIPCION` | varchar | 0% |
| 11 | `TECNICOID` | int | 0% |
| 12 | `ORDENUSRING` | varchar | 0% |
| 13 | `MOTIVOORDID` | int | 0% |
| 14 | `MOTIVOORDNOMBRE` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_RECLAMOS_BDDD
-- Extraida: 2026-08-07T15:28:15.999519+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_RECLAMOS_BDDD]
AS SELECT 
	 O.EMPRESAID, CONCAT(O.EMPRESAID,CONCAT('_',ORDENNRO)) AS ORDENNRO,
	   O.CLIENTENROORD as CLIENTENRO, O.CONTRATONRO, o.ORDENSTS, ORDENFING, ORDENFFIN, o.ORDENFPROCESO,
	   o.ORDENSOL, d.DESCRIPCION, o.TECNICOID, O.ORDENUSRING, O.MOTIVOORDID, M.[MOTIVOORDNOMBRE]
FROM SIGASC.ORDENSRV O

LEFT JOIN SIGASC.CONTRATO C
ON O.CONTRATONRO=C.CONTRATONRO
AND O.EMPRESAID=C.EMPRESAID

LEFT JOIN SIGASC.PRODUCTO P
ON P.EMPRESAID = C.EMPRESAID
AND P.PRODUCTOID = C. PRODUCTOID

LEFT JOIN  [SIGASC].[MOTIVOORD] M
ON O.[MOTIVOORDID] = M.[MOTIVOORDID]

 LEFT JOIN  [SIGASC].[DOMINIOS] D
ON O.[ORDENSOL] = d.[valor]
and d.DOMINIONOMBRE='ordensolucion'

WHERE ordentpo = 'R'
AND ordenfing >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-12,GETDATE()))-1),DATEADD(mm,-12,GETDATE())),101) 
AND ordenfing <  GETDATE()
AND C.EMPRESAID NOT IN (15,19);
```
