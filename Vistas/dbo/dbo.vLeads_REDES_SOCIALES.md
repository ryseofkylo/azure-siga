---
esquema: dbo
tabla: vLeads_REDES_SOCIALES
objeto: dbo.vLeads_REDES_SOCIALES
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

# dbo.vLeads_REDES_SOCIALES

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
-- Vista: dbo.vLeads_REDES_SOCIALES
-- Extraida: 2026-08-07T15:28:29.076032+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vLeads_REDES_SOCIALES]
AS select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Comentarios Redes' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where c.Campaign = 'Redes Sociales'
 AND c.Creation_date >= DATEADD(month, -13, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1));
```
