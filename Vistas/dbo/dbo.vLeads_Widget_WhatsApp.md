---
esquema: dbo
tabla: vLeads_Widget_WhatsApp
objeto: dbo.vLeads_Widget_WhatsApp
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

# dbo.vLeads_Widget_WhatsApp

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_Tag]]
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
-- Vista: dbo.vLeads_Widget_WhatsApp
-- Extraida: 2026-08-07T15:28:32.035142+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vLeads_Widget_WhatsApp]
AS SELECT 
    c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File], c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by],p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Widget - WhatsApp' AS TipoLead
FROM sg_caso c
LEFT JOIN v_SGParameters_materializada p 
    ON c.id = p.casoid
WHERE LTRIM(RTRIM(c.Campaign)) = 'Widget - WhatsApp'
  AND EXISTS (
      SELECT 1
      FROM SG_Tag t1
      WHERE t1.CasoId = c.id
  )
  AND NOT EXISTS (
      SELECT 1
      FROM SG_Tag t2
      WHERE t2.CasoId = c.id
        AND LTRIM(RTRIM(t2.Name)) IN ('Chat2Whatsapp Deflection', 'Ventas Widget')
  )
 AND c.Creation_date >= DATEADD(month, -13, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1));
```
