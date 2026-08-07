---
esquema: dbo
tabla: V_MAPPINGCALLS_2021
objeto: dbo.V_MAPPINGCALLS_2021
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

# dbo.V_MAPPINGCALLS_2021

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[MAPPING.CALLS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ID` | bigint | 0% |
| 2 | `FECHA` | date | 0% |
| 3 | `HORA` | nvarchar | 0% |
| 4 | `DISCADO` | nvarchar | 0% |
| 5 | `ORIGEN` | nvarchar | 0% |
| 6 | `DESTINO` | nvarchar | 0% |
| 7 | `RESULTADO` | nvarchar | 0% |
| 8 | `DURACION` | nvarchar | 0% |
| 9 | `PERIODO` | nvarchar | 0% |
| 10 | `TOTALSEGUNDOS` | int | 0% |
| 11 | `TOTALHORAS` | float | 0% |
| 12 | `TOTALMINUTOS` | float | 0% |
| 13 | `PROVINCIA_ORIGEN` | nvarchar | 0% |
| 14 | `LOCALIDAD_ORIGEN` | nvarchar | 0% |
| 15 | `PROVINCIA_DESTINO` | nvarchar | 0% |
| 16 | `LOCALIDAD_DESTINO` | nvarchar | 0% |
| 17 | `GESTION` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_MAPPINGCALLS_2021
-- Extraida: 2026-08-07T15:28:01.141484+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_MAPPINGCALLS_2021]
AS SELECT 
    IDEVENTOS AS ID,
    CONVERT(DATE, FECHA) AS FECHA,
    HORA,
    DISCADO,
    ORIGEN,
    DESTINO,
    NOMBRE AS RESULTADO,
    DURACION,
    PERIODO,
    TOTALSEGUNDOS,
    TOTALHORAS,
    TOTALMINUTOS,
    PROVINCIA_ORIGEN,
    LOCALIDAD_ORIGEN,
    PROVINCIA_DESTINO,
    LOCALIDAD_DESTINO,
    GESTION
FROM MAPPING.CALLS
WHERE FECHA >= '2021-01-01';
```
