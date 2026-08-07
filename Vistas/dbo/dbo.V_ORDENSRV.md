---
esquema: dbo
tabla: V_ORDENSRV
objeto: dbo.V_ORDENSRV
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 11
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_ORDENSRV

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.ORDENSRV]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ORDENNRO` | varchar | 0% |
| 3 | `CLIENTENROORD` | int | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `ORDENFING` | datetime2 | 0% |
| 6 | `ORDENFFIN` | datetime2 | 1% |
| 7 | `ORDENSOL` | varchar | 0% |
| 8 | `ORDENTRBRED` | int | 0% |
| 9 | `ORDENUSRING` | varchar | 0% |
| 10 | `MOTIVOORDID` | int | 0% |
| 11 | `MOTIVOORDINGID` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ORDENSRV
-- Extraida: 2026-08-07T15:28:08.825326+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_ORDENSRV]
AS SELECT EMPRESAID, CONCAT(EMPRESAID,CONCAT('_',ORDENNRO)) AS ORDENNRO,
	   CLIENTENROORD, CONTRATONRO, ORDENFING, ORDENFFIN, ORDENSOL, ORDENTRBRED, ORDENUSRING, MOTIVOORDID, MOTIVOORDINGID
FROM SIGASC.ORDENSRV 
WHERE ordentpo = 'R'
AND ordenfing >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES
AND ordenfing <  GETDATE();
```
