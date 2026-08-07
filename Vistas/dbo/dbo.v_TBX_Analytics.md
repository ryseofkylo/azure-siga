---
esquema: dbo
tabla: v_TBX_Analytics
objeto: dbo.v_TBX_Analytics
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 7
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_TBX_Analytics

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[MIO.TBX_Analytics]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SubscriberId` | nvarchar |  |
| 2 | `Network` | nvarchar |  |
| 3 | `Id` | nvarchar |  |
| 4 | `ContentProviderShortName` | nvarchar |  |
| 5 | `DeviceType` | nvarchar |  |
| 6 | `Fecha` | datetime |  |
| 7 | `DeviceDescription` | nvarchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_TBX_Analytics
-- Extraida: 2026-08-07T15:28:22.563295+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_TBX_Analytics]
AS select SubscriberId,Network,Id,ContentProviderShortName,DeviceType
,cast(cast(dateadd(HOUR, -3 ,[Date]) as date) as datetime) as Fecha
,[DeviceDescription]
from MIO.TBX_Analytics
group by SubscriberId,Network,Id
,ContentProviderShortName,DeviceType
, cast(cast(dateadd(HOUR, -3 ,[Date]) as date) as datetime),[DeviceDescription];
```
