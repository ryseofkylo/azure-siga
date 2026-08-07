---
esquema: dbo
tabla: v_SGParameters_materializada
objeto: dbo.v_SGParameters_materializada
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `Nro` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.v_SGParameters_materializada

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Nro` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Nro` | bigint | 0% |
| 2 | `utm_source` | varchar | 0% |
| 3 | `utm_medium` | varchar | 0% |
| 4 | `utm_campaign` | varchar | 0% |
| 5 | `provincia` | varchar | 5% |
| 6 | `page_name` | varchar | 0% |
| 7 | `date_lead` | datetime | 0% |
| 8 | `Source` | nvarchar | 0% |
| 9 | `Campaign` | nvarchar | 0% |
| 10 | `producto` | varchar | 5% |
| 11 | `CasoId` | bigint | 0% |

## Claves de join presentes
- `CasoId` (bigint) → [[clave-CASOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.SG_Caso]] · `v_SGParameters_materializada.CASOID = SG_Caso.ID` — view_join (vLeads), alta

## Reglas de negocio conocidas
**Filtros**
- `p.utm_source in ('Sup-WP')` — _de_ [[dbo.vLeads]]
- `p.utm_medium in ('Bnr')` — _de_ [[dbo.vLeads]]
- `p.utm_source in ('Sup-emb')` — _de_ [[dbo.vLeads]]
- `p.utm_medium in ('MIO','Pack_Futbol','Premium')` — _de_ [[dbo.vLeads]]
- `p.utm_source in ('Zet-FB','Zet-GL')` — _de_ [[dbo.vLeads]]
- `p.utm_medium in ('Con','Dvy','Srh')` — _de_ [[dbo.vLeads]]
- `p.utm_medium not in ('MIO','Pack_Futbol','Premium', 'Ayuda', 'Denuncia')` — _de_ [[dbo.vLeads]]
- `p.utm_source in ('web')` — _de_ [[dbo.vLeads]]
- `(p.utm_campaign is null or p.utm_campaign <> 'Widget - WhatsApp')` — _de_ [[dbo.vLeads]]
- `p.utm_source in ('Sup-MC')` — _de_ [[dbo.vLeads]]
- `p.utm_source in ('AG-TT')` — _de_ [[dbo.vLeads]]
- `p.utm_source IN ('Sup-WP')` — _de_ [[dbo.vLeads12meses]]
- `p.utm_medium IN ('Bnr')` — _de_ [[dbo.vLeads12meses]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.vLeads12meses]]

## Vistas que la consumen (referencia)
- [[dbo.vLeads]]
- [[dbo.vLeads12meses]]
- [[dbo.vLeads_Boton_de_WhatsApp]]
- [[dbo.vLeads_COMENTARIOS_ANUNCIOS]]
- [[dbo.vLeads_Click_to_WhatsApp]]
- [[dbo.vLeads_EMAIL_MARKETING]]
- [[dbo.vLeads_Forms_Google_Ads]]
- [[dbo.vLeads_LEAD_ADS]]
- [[dbo.vLeads_REDES_SOCIALES]]
- [[dbo.vLeads_Unbounce_BANNER_WEB]]
- [[dbo.vLeads_Unbounce_EMBEBIDAS]]
- [[dbo.vLeads_Unbounce_PAID_MEDIA]]
- [[dbo.vLeads_Unbounce_PBU]]
- [[dbo.vLeads_Unbounce_PREMIUM]]
- [[dbo.vLeads_Unbounce_TIKTOK]]
- [[dbo.vLeads_Ventas_Widget]]
- [[dbo.vLeads_WhatsApp_Meta]]
- [[dbo.vLeads_Widget_WhatsApp]]
- [[dbo.vLeads_WordPress]]
- [[dbo.vLeadsnuevo]]
