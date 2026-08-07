---
esquema: dbo
tabla: vLeads_Unbounce_BANNER_WEB
objeto: dbo.vLeads_Unbounce_BANNER_WEB
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 19
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.vLeads_Unbounce_BANNER_WEB

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.v_SGParameters_materializada]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint |  |
| 2 | `Source` | nvarchar |  |
| 3 | `Creation_date` | datetime2 |  |
| 4 | `Close_date` | datetime2 |  |
| 5 | `Client_id` | bigint |  |
| 6 | `Client_crm_id` | nvarchar |  |
| 7 | `Client_name` | nvarchar |  |
| 8 | `Client_ext_id` | nvarchar |  |
| 9 | `File` | nvarchar |  |
| 10 | `FechaProcesado` | datetime2 |  |
| 11 | `NroCliente` | nvarchar |  |
| 12 | `Campaign` | nvarchar |  |
| 13 | `Closed_by` | varchar |  |
| 14 | `producto` | varchar |  |
| 15 | `utm_source` | varchar |  |
| 16 | `utm_medium` | varchar |  |
| 17 | `utm_campaign` | varchar |  |
| 18 | `provincia` | varchar |  |
| 19 | `TipoLead` | varchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.vLeads_Unbounce_BANNER_WEB
-- Extraida: 2026-08-07T15:28:29.406219+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vLeads_Unbounce_BANNER_WEB]
AS select c.*, p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Unbounce BANNER WEB' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where p.utm_source in ('Sup-WP')
  and p.utm_medium in ('Bnr')
 AND (c.Campaign <> 'Widget - WhatsApp')
 AND c.Creation_date >= DATEADD(month, -13, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1));
```
