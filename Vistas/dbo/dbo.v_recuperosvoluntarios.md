---
esquema: dbo
tabla: v_recuperosvoluntarios
objeto: dbo.v_recuperosvoluntarios
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 29
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_recuperosvoluntarios

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[ACTIVITY.H_RECUPEROSVOLUNTARIOS]]
- [[ACTIVITY.RECUPEROSVOLUNTARIOS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENRO` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODUCTO` | nvarchar | 0% |
| 7 | `TIPOPROD` | nvarchar | 0% |
| 8 | `SUCURSALID` | int | 0% |
| 9 | `CENTROOPERATIVO` | nvarchar | 0% |
| 10 | `NOMBRE` | nvarchar | 0% |
| 11 | `MEDIODECOBRO` | nvarchar | 0% |
| 12 | `CLIENTETST` | nvarchar | 0% |
| 13 | `TELEFONO` | nvarchar | 0% |
| 14 | `DEPARTAMENTO` | nvarchar | 0% |
| 15 | `LOCALIDAD` | nvarchar | 0% |
| 16 | `PRINCIPAL` | nvarchar | 0% |
| 17 | `CONTRATOSTS` | nvarchar | 0% |
| 18 | `FECHAFINALIZACION` | datetime2 | 0% |
| 19 | `SEGMENTO` | nvarchar | 0% |
| 20 | `SINCARGO` | nvarchar | 0% |
| 21 | `PROMOCIONES` | nvarchar | 60% |
| 22 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 23 | `CLIENTETIPO` | nvarchar | 0% |
| 24 | `IDPLANCOMERCIAL` | real | 98% |
| 25 | `PLANCOMERCIAL` | nvarchar | 86% |
| 26 | `CODMZN` | nvarchar | 0% |
| 27 | `IDZONA` | real | 12% |
| 28 | `ZONA` | nvarchar | 12% |
| 29 | `PIPELINERUNID` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_recuperosvoluntarios
-- Extraida: 2026-08-07T15:28:16.977551+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_recuperosvoluntarios]
AS SELECT * FROM ACTIVITY.H_RECUPEROSVOLUNTARIOS
UNION ALL
SELECT * FROM ACTIVITY.RECUPEROSVOLUNTARIOS;
```
