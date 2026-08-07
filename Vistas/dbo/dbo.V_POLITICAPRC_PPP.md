---
esquema: dbo
tabla: V_POLITICAPRC_PPP
objeto: dbo.V_POLITICAPRC_PPP
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 12
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_POLITICAPRC_PPP

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.POLITICACPTO]]
- [[SIGASC.POLITICAPRC]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPOLITICAPRC` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `POLITICAID` | int | 0% |
| 4 | `POLITICALIN` | int | 0% |
| 5 | `POLITICAFCH` | datetime2 | 0% |
| 6 | `POLITICAPRC` | real | 0% |
| 7 | `POLITICAPRCVTO2` | real | 0% |
| 8 | `POLITICAPRCVTO3` | real | 0% |
| 9 | `POLITICAPRCACTIVACARTELERA` | int | 0% |
| 10 | `PIPELINERUNID` | varchar | 0% |
| 11 | `PKPOLITICAID` | varchar | 0% |
| 12 | `PKPOLITICALIN` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_POLITICAPRC_PPP
-- Extraida: 2026-08-07T15:28:11.461353+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_POLITICAPRC_PPP]
AS SELECT p.* FROM SIGASC.POLITICAPRC p
	LEFT JOIN SIGASC.POLITICACPTO c 
	ON ( ( p.pkpoliticaid = c.pkpoliticaid ) AND ( p.pkpoliticalin = c.pkpoliticalin ) );
```
