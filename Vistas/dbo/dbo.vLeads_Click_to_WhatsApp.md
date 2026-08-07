---
esquema: dbo
tabla: vLeads_Click_to_WhatsApp
objeto: dbo.vLeads_Click_to_WhatsApp
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

# dbo.vLeads_Click_to_WhatsApp

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_ClientMessage]]
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
-- Vista: dbo.vLeads_Click_to_WhatsApp
-- Extraida: 2026-08-07T15:28:27.444117+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vLeads_Click_to_WhatsApp]
AS select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Click to WhatsApp' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
WHERE c.Campaign='Whatsapp' 
AND exists (
	select 1 
	from SG_ClientMessage m
	where m.Text in (
		'Hola, quiero que me asesoren',
		'Hola, me gustaría que me asesoren',
		'Me interesa la promo Internet en San Juan',
		'Me interesa la promo Internet en Mendoza',
		'Me interesa la promo Combo en San Juan',
		'Me interesa la promo HD en San Juan',
		'Me interesa la promo Combo en Mendoza',
		'Me interesa la promo HD en Mendoza',
		'Me interesa la promo Internet en Comodoro Rivadavia',
		'Me interesa la promo Combo en Comodoro Rivadavia',
		'Me interesa la promo Internet en Tucumán',
		'Me interesa la promo Combo en Tucumán',
		'Me interesa la promo Internet en La Rioja',
		'Me interesa la promo Combo en La Rioja',
		'Me interesa la promo Internet en Villa Mercedes',
		'Me interesa la promo Combo en Villa Mercedes',
		'Me interesa la promo Internet en Catamarca',
		'Me interesa la promo Combo en Catamarca',
		'Me interesa la promo Internet en Puerto Madryn',
		'Me interesa la promo Combo en Puerto Madryn',
		'Me interesa la promo HD en Ushuaia',
		'Me interesa la promo Internet en Ushuaia',
		'Me interesa la promo HD en Trelew',
		'Me interesa la promo Internet en Trelew',
		'Me interesa la promo Combo en Trelew',
		'Me interesa la promo HD en Bariloche',
		'Me interesa la promo Combo Bariloche',
		'Me interesa la promo Internet Bariloche',
		'Me interesa la promo HD en SMDLA',
		'Me interesa la promo Combo en SMDLA',
		'Me interesa la promo Internet en SMDLA'
	)
	  and m.CasoId = c.Id
)
AND not exists (
	select 1
	from SG_ClientMessage m2
	where m2.Text = 'Hola, me gustaría contratar un servicio ¿Me pueden ayudar?'
	  and m2.CasoId = c.Id
)
 AND c.Creation_date >= DATEADD(month, -13, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1));
```
