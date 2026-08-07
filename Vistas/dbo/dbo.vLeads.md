---
esquema: dbo
tabla: vLeads
objeto: dbo.vLeads
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

# dbo.vLeads

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_ClientMessage]]
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
-- Vista: dbo.vLeads
-- Extraida: 2026-08-07T15:28:26.795715+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vLeads]
AS select c.*, p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Unbounce BANNER WEB' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where p.utm_source in ('Sup-WP')
  and p.utm_medium in ('Bnr')
 AND (c.Campaign <> 'Widget - WhatsApp'
)


union all

-- Unbounce PREMIUM
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File], c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Unbounce PREMIUM' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where p.utm_source in ('Sup-emb')
  and p.utm_medium in ('MIO','Pack_Futbol','Premium')
  AND (c.Campaign <> 'Widget - WhatsApp')

union all

-- PAID MEDIA
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Unbounce PAID MEDIA' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where p.utm_source in ('Zet-FB','Zet-GL')
  and p.utm_medium in ('Con','Dvy','Srh')
  AND (c.Campaign <> 'Widget - WhatsApp')

union all

-- EMBEBIDAS
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Unbounce EMBEBIDAS' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where p.utm_source in ('Sup-emb')
  and p.utm_medium not in ('MIO','Pack_Futbol','Premium', 'Ayuda', 'Denuncia')
  AND (c.Campaign <> 'Widget - WhatsApp')

union all

-- PBU
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Unbounce PBU' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where p.utm_source in ('web')
  and (p.utm_campaign is null or p.utm_campaign <> 'Widget - WhatsApp')

union all

-- Comentarios Redes
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Comentarios Redes' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where c.Campaign = 'Redes Sociales'

union all

-- Comentarios Anuncios
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Comentarios Anuncios' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where c.Campaign = 'Redes Sociales 2'

union all

-- Lead Ads
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Lead Ads' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where c.Campaign = 'RRSS Leads 2'

union all

-- Email Marketing
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File], c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by],p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Email Marketing' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where p.utm_source in ('Sup-MC')

union all

-- WordPress
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'WordPress' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where c.Campaign = 'WP Leads'

union all

-- Botón de WhatsApp
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Botón de WhatsApp' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
WHERE c.Campaign='Whatsapp' 
AND exists (
	select 1 
	from SG_ClientMessage m
	where m.Text = 'Hola, me gustaría contratar un servicio ¿Me pueden ayudar?'
	  and m.CasoId = c.Id
)

union all

-- Forms Google Ads
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File], c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by],p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Forms Google Ads' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where c.Campaign = 'Forms Google Ads'

union all

-- WhatsApp Meta
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'WhatsApp Meta' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where c.Campaign = 'WhatsApp Meta'

union all

-- Click to WhatsApp
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Click to WhatsApp' as TipoLead
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

union all

-- Widget WhatsApp
SELECT 
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

union all

-- Ventas Widget (corregido: sin columna extra)
SELECT c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Ventas Widget' AS TipoLead
FROM sg_caso AS c
LEFT JOIN v_SGParameters_materializada AS p ON c.id = p.casoid
OUTER APPLY (
    SELECT TOP 1 *
    FROM SG_Tag AS t
    WHERE t.CasoId = c.id
      AND t.Name = 'Ventas Widget'
    ORDER BY t.Id
) AS t
WHERE c.Campaign = 'Widget - WhatsApp'
  AND t.Name = 'Ventas Widget'


union all


 -- UNBOUNCE TIKTOK
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, p.utm_source, p.utm_medium, p.utm_campaign, p.provincia, 'Unbounce TIKTOK' as TipoLead
from sg_caso c
left join v_SGParameters_materializada p on c.id = p.casoid
where p.utm_source in ('AG-TT')
  AND (c.Campaign <> 'Widget - WhatsApp');
```
