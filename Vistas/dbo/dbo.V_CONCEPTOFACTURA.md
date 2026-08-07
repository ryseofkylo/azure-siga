---
esquema: dbo
tabla: V_CONCEPTOFACTURA
objeto: dbo.V_CONCEPTOFACTURA
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

# dbo.V_CONCEPTOFACTURA

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CPTOFACTURA]]
- [[SIGASC.CPTOFACTURAGRUPO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CPTOFACID` | int | 0% |
| 3 | `CPTOFACNOMBRE` | varchar | 0% |
| 4 | `CPTOFACTPO` | varchar | 0% |
| 5 | `IVAID` | int | 0% |
| 6 | `CPTOFACDTO` | int | 0% |
| 7 | `CPTOPROVEXT` | int | 75% |
| 8 | `CPTOMOROSIDADCRITERIOID` | int | 24% |
| 9 | `CPTOFACUSADSC` | int | 68% |
| 10 | `CPTOFACDSC` | varchar | 68% |
| 11 | `CPTOFACUNICOPRIORIDAD` | int | 14% |
| 12 | `CPTOFACUNICONPLAY` | int | 22% |
| 13 | `CPTOFACUNICO` | int | 22% |
| 14 | `CPTOFACSTS` | varchar | 8% |
| 15 | `CPTOFACGRUPOID` | int | 10% |
| 16 | `CPTOFACGRUPONOMBRE` | varchar | 10% |
| 17 | `CPTOFACGRUPOINTERNO` | varchar | 10% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CONCEPTOFACTURA
-- Extraida: 2026-08-07T15:27:50.101208+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_CONCEPTOFACTURA]
AS SELECT f.EMPRESAID, CPTOFACID,
		f.CPTOFACNOMBRE, f.CPTOFACTPO, f.IVAID, f.CPTOFACDTO, f.CPTOPROVEXT, 
		f.CPTOMOROSIDADCRITERIOID, f.CPTOFACUSADSC, f.CPTOFACDSC, f.CPTOFACUNICOPRIORIDAD, f.CPTOFACUNICONPLAY,
		f.CPTOFACUNICO, f.CPTOFACSTS, g.CPTOFACGRUPOID, g.CPTOFACGRUPONOMBRE, g.CPTOFACGRUPOINTERNO
FROM SIGASC.CPTOFACTURA f
LEFT JOIN SIGASC.CPTOFACTURAGRUPO g ON ( f.cptofacgrupoid = g.cptofacgrupoid );
```
