---
esquema: dbo
tabla: v_OC_Leads
objeto: dbo.v_OC_Leads
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 15
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_OC_Leads

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_OC_Caso]]
- [[dbo.SG_OC_ClientMessage]]
- [[dbo.SG_OC_Tag]]
- [[dbo.v_OC_SGParameters]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Source` | nvarchar | 0% |
| 3 | `Creation_date` | datetime2 | 0% |
| 4 | `Close_date` | datetime2 | 100% |
| 5 | `Client_id` | bigint | 0% |
| 6 | `Client_crm_id` | nvarchar | 95% |
| 7 | `Client_name` | nvarchar | 0% |
| 8 | `Client_ext_id` | nvarchar | 0% |
| 9 | `File` | nvarchar | 0% |
| 10 | `FechaProcesado` | datetime2 | 0% |
| 11 | `NroCliente` | nvarchar | 96% |
| 12 | `Campaign` | nvarchar | 0% |
| 13 | `Closed_by` | varchar | 100% |
| 14 | `producto` | varchar | 42% |
| 15 | `TipoLead` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_OC_Leads
-- Extraida: 2026-08-07T15:28:05.520512+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_OC_Leads]
AS select c.*, p.producto ,'Unbounce BANNER WEB' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
p.utm_source in ('Sup-WP')
and p.utm_medium in ('Bnr')
and c.id not in (
    select distinct Id from sg_caso
)


union all

-- Unbounce PREMIUM
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Unbounce PREMIUM' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
p.utm_source in ('Sup-emb')
and p.utm_medium in ('MIO','Pack_Futbol','Premium')
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- PAID MEDIA
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Unbounce PAID MEDIA' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
p.utm_source in ('Zet-FB','Zet-GL')
and p.utm_medium in ('Con','Dvy','Srh')
and (c.Campaign <> 'Widget - WhatsApp')
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- EMBEBIDAS
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Unbounce EMBEBIDAS' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'Unbounce'
and p.utm_source in ('Sup-emb')
and p.utm_medium not in ('MIO','Pack_Futbol','Premium', 'Ayuda', 'Denuncia')
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- PBU
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Unbounce PBU' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'Unbounce'
and p.utm_source in ('web')
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- Comentarios Redes
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Comentarios Redes' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'Redes Sociales'
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- Comentarios Anuncios
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Comentarios Anuncios' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'Redes Sociales 2'
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- Lead Ads
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Lead Ads' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'RRSS Leads 2'
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- Email Marketing
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Email Marketing' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
p.utm_source in ('Sup-MC')
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- WordPress
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'WordPress' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'WP Leads'
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- Botón de WhatsApp
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Botón de WhatsApp' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'Whatsapp'
and exists (
    select 1 
    from SG_OC_ClientMessage m
    where m.Text in ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?')
    and m.OC_CasoId = c.Id
)
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- Forms Google Ads
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Forms Google Ads' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'Forms Google Ads'
and c.id not in (
    select distinct Id from sg_caso
)

union all

-- WhatsApp Meta 
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'WhatsApp Meta' as TipoLead
from sg_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'WhatsApp Meta'
and c.id not in (
    select distinct Id from sg_caso
)

union all


-- Click to WhatsApp
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto ,'Click to WhatsApp' as TipoLead
from sg_oc_caso c
left join v_oc_sgparameters p on c.id = p.casoid
where 
c.Campaign = 'Whatsapp'
and exists (
    select 1 
    from SG_oc_ClientMessage m
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
    and m.oc_CasoId = c.Id
)
and not exists(
    select 1
    from SG_oc_ClientMessage m2
    where m2.Text in ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?')
    and m2.oc_CasoId = c.Id
)
and c.id not in (
    select distinct Id from sg_caso
)

union all


-- Widget WhatsApp
SELECT 
    c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], 
    p.producto, 
    'Widget - WhatsApp' AS TipoLead
FROM sg_oc_caso c
LEFT JOIN v_oc_sgparameters p on c.id = p.casoid
WHERE LTRIM(RTRIM(c.Campaign)) = 'Widget - WhatsApp'
  AND NOT EXISTS (
      SELECT 1
      FROM SG_oc_Tag t
      WHERE t.OC_CasoId = c.id
        AND LTRIM(RTRIM(t.Name)) IN ('Chat2Whatsapp Deflection', 'Ventas Widget')
  )
and c.id not in (
    select distinct Id from sg_caso
)


union all

-- Ventas Widget (corregido: sin columna extra)
SELECT c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, 'Ventas Widget' AS TipoLead
FROM sg_oc_caso AS c
LEFT JOIN v_oc_sgparameters p on c.id = p.casoid
OUTER APPLY (
    SELECT TOP 1 *
    FROM SG_oc_Tag AS t
    WHERE t.OC_CasoId = c.id
      AND t.Name = 'Ventas Widget'
    ORDER BY t.Id
) AS t
WHERE c.Campaign = 'Widget - WhatsApp'
  AND t.Name = 'Ventas Widget'
 and c.id not in (
    select distinct Id from sg_caso
)


union all


-- UNBOUNCE TIKTOK
select c.[Id] ,c.[Source],c.[Creation_date],c.[Close_date],c.[Client_id],c.[Client_crm_id],c.[Client_name],c.[Client_ext_id],c.[File],c.[FechaProcesado],c.[NroCliente],c.[Campaign],c.[Closed_by], p.producto, 'Unbounce TIKTOK' as TipoLead
from sg_oc_caso AS c
left join v_oc_sgparameters p on c.id = p.casoid
where p.utm_source in ('AG-TT')
  AND (c.Campaign <> 'Widget - WhatsApp');
```
