---
esquema: dbo
tabla: v_promomes
objeto: dbo.v_promomes
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 13
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_promomes

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.CONTRATOPROMOCION]]
- [[SIGASC.PROMOCION]]
- [[SIGASC.PROMOCIONMES]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPROMOCIONMES` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PROMOCIONID` | int | 0% |
| 4 | `PROMOCIONMES` | int | 0% |
| 5 | `PROMOCIONDTOPRJ` | float | 0% |
| 6 | `PROMOCIONPRC` | float | 0% |
| 7 | `PROMOCIONDEBDTOPRJ` | float | 0% |
| 8 | `PROMOCIONDEBDTOPRC` | float | 0% |
| 9 | `PKPROMOCIONID` | varchar | 0% |
| 10 | `PKPROMOCIONMES` | varchar | 0% |
| 11 | `CUOTAHASTA` | int | 0% |
| 12 | `PROMOCIONNOMBRE` | varchar | 0% |
| 13 | `PROMOCIONTPODTO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_promomes
-- Extraida: 2026-08-07T15:28:14.387808+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_promomes]
AS WITH contratos_conectados AS (
    SELECT cp.EMPRESAID, cp.PROMOCIONID
    FROM sigasc.contrato c
    left join sigasc.contratopromocion cp
    on c.empresaid = cp.empresaid
    and c.contratonro = cp.contratonro
    WHERE c.contratosts <> 'X'
    GROUP BY cp.EMPRESAID, cp.PROMOCIONID
)
SELECT PM.[SKPROMOCIONMES]
    ,PM.[EMPRESAID]
    ,PM.[PROMOCIONID]
    ,PM.[PROMOCIONMES]
    ,FLOOR(PM.[PROMOCIONDTOPRJ]) AS PROMOCIONDTOPRJ
    ,FLOOR(PM.[PROMOCIONPRC]) AS PROMOCIONPRC
    ,FLOOR(PM.[PROMOCIONDEBDTOPRJ]) AS PROMOCIONDEBDTOPRJ
    ,FLOOR(PM.[PROMOCIONDEBDTOPRC]) AS PROMOCIONDEBDTOPRC
    ,PM.[PKPROMOCIONID]
    ,PM.[PKPROMOCIONMES]
    ,MAX(PM.[PROMOCIONMES]) OVER (PARTITION BY PM.[PKPROMOCIONID]) AS CUOTAHASTA
    ,P.[PROMOCIONNOMBRE]
    ,P.[PROMOCIONTPODTO]
FROM [SIGASC].[PROMOCIONMES] PM
LEFT JOIN [SIGASC].[PROMOCION] P ON P.[PKPROMOCIONID] = PM.[PKPROMOCIONID]
-- Agregar INNER JOIN con la CTE para hacer el cruce
INNER JOIN contratos_conectados CC ON PM.[EMPRESAID] = CC.[EMPRESAID] AND PM.[PROMOCIONID] = CC.[PROMOCIONID]
where PM.[EMPRESAID] <100 and PM.[EMPRESAID] not in (15,19,23,0);
```
