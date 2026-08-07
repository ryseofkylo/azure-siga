---
esquema: dbo
tabla: V_INDICEPROMOCIONMES
objeto: dbo.V_INDICEPROMOCIONMES
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

# dbo.V_INDICEPROMOCIONMES

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.PROMOCION]]
- [[SIGASC.PROMOCIONMES]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PKPROMOCIONID` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PROMOCIONMES` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_INDICEPROMOCIONMES
-- Extraida: 2026-08-07T15:27:59.475308+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_INDICEPROMOCIONMES]
AS SELECT PKPROMOCIONID, EMPRESAID, MIN(promocionmes) AS PROMOCIONMES 
FROM SIGASC.PROMOCIONMES 
WHERE pkpromocionid IN ( SELECT DISTINCT pkpromocionid FROM SIGASC.PROMOCION WHERE promociontpodto <>  'F' )
GROUP BY pkpromocionid, empresaid

UNION ALL

SELECT PKPROMOCIONID, EMPRESAID, MIN(promocionmes) AS PKPROMOCIONMES 
FROM SIGASC.PROMOCIONMES 
WHERE pkpromocionid IN ( SELECT DISTINCT pkpromocionid FROM SIGASC.PROMOCION WHERE promociontpodto = 'F' )
AND promocionprc > 0 
GROUP BY pkpromocionid, empresaid;
```
