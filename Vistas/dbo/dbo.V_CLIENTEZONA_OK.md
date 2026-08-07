---
esquema: dbo
tabla: V_CLIENTEZONA_OK
objeto: dbo.V_CLIENTEZONA_OK
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

# dbo.V_CLIENTEZONA_OK

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CLIENTEZONA]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCLIENTEZONA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `CLIZONATPO` | varchar | 0% |
| 5 | `CLIZONAID` | int | 0% |
| 6 | `CLIZONAUSRING` | varchar | 0% |
| 7 | `CLIZONAFCHING` | datetime2 | 0% |
| 8 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCLIENTENRO` | varchar | 0% |
| 11 | `PKCLIZONATPO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CLIENTEZONA_OK
-- Extraida: 2026-08-07T15:27:44.820185+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_CLIENTEZONA_OK]
AS SELECT * FROM SIGASC.CLIENTEZONA
WHERE SKCLIENTEZONA NOT IN (
select distinct skclientezona
from sigasc.clientezona where clientenro in (
select clientenro from sigasc.clientezona where clizonatpo = 'HAB' group by clientenro having count(*) > 1 )
and empresaid = '27'
);
```
