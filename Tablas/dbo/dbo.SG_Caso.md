---
esquema: dbo
tabla: SG_Caso
objeto: dbo.SG_Caso
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `Id` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.SG_Caso

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Source` | nvarchar | 0% |
| 3 | `Creation_date` | datetime2 | 0% |
| 4 | `Close_date` | datetime2 | 0% |
| 5 | `Client_id` | bigint | 0% |
| 6 | `Client_crm_id` | nvarchar | 40% |
| 7 | `Client_name` | nvarchar | 0% |
| 8 | `Client_ext_id` | nvarchar | 0% |
| 9 | `File` | nvarchar | 0% |
| 10 | `FechaProcesado` | datetime2 | 0% |
| 11 | `NroCliente` | nvarchar | 40% |
| 12 | `Campaign` | nvarchar | 0% |
| 13 | `Closed_by` | varchar | 96% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `Client_id` (bigint) → [[clave-CLIENT_ID]]
- `Client_crm_id` (nvarchar) → [[clave-CLIENT_CRM_ID]]
- `Client_ext_id` (nvarchar) → [[clave-CLIENT_EXT_ID]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.v_SGParameters_materializada]] · `SG_Caso.ID = v_SGParameters_materializada.CASOID` — view_join (vLeads), alta
- [[dbo.SG_ClientMessage]] · `SG_Caso.ID = SG_ClientMessage.CASOID` — view_join (vLeads), alta
- [[dbo.SG_Tag]] · `SG_Caso.ID = SG_Tag.CASOID` — view_join (vLeads), alta

## Reglas de negocio conocidas
**Filtros**
- `(c.Campaign <> 'Widget - WhatsApp' )` — _de_ [[dbo.vLeads]]
- `(c.Campaign <> 'Widget - WhatsApp')` — _de_ [[dbo.vLeads]]
- `c.Campaign = 'Redes Sociales'` — _de_ [[dbo.vLeads]]
- `c.Campaign = 'Redes Sociales 2'` — _de_ [[dbo.vLeads]]
- `c.Campaign = 'RRSS Leads 2'` — _de_ [[dbo.vLeads]]
- `c.Campaign = 'WP Leads'` — _de_ [[dbo.vLeads]]
- `c.Campaign='Whatsapp'` — _de_ [[dbo.vLeads]]
- 🚦 `exists ( select 1 from SG_ClientMessage m where m.Text = 'Hola, me gustaría contratar un servicio ¿Me pueden ayudar?' and m.CasoId = c.Id )` — _de_ [[dbo.vLeads]]
- `c.Campaign = 'Forms Google Ads'` — _de_ [[dbo.vLeads]]
- `c.Campaign = 'WhatsApp Meta'` — _de_ [[dbo.vLeads]]
- 🚦 `not exists ( select 1 from SG_ClientMessage m2 where m2.Text = 'Hola, me gustaría contratar un servicio ¿Me pueden ayudar?' and m2.CasoId = c.Id )` — _de_ [[dbo.vLeads]]
- `LTRIM(RTRIM(c.Campaign)) = 'Widget - WhatsApp'` — _de_ [[dbo.vLeads]]
- 🚦 `EXISTS ( SELECT 1 FROM SG_Tag t1 WHERE t1.CasoId = c.id )` — _de_ [[dbo.vLeads]]
- 🚦 `NOT EXISTS ( SELECT 1 FROM SG_Tag t2 WHERE t2.CasoId = c.id AND LTRIM(RTRIM(t2.Name)) IN ('Chat2Whatsapp Deflection', 'Ventas Widget') )` — _de_ [[dbo.vLeads]]
- `c.Campaign = 'Widget - WhatsApp'` — _de_ [[dbo.vLeads]]
- `c.Creation_date >= DATEADD(month, -13, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))` — _de_ [[dbo.vLeads_Boton_de_WhatsApp]]
- `c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101)` — _de_ [[dbo.V_SG_CASO]]
- `m.casoid IN ( SELECT DISTINCT c.id FROM SG_CASO c WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) )` — _de_ [[dbo.V_SG_MENSAJE]]
- `t.casoid IN ( SELECT DISTINCT c.id FROM SG_CASO c WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) )` — _de_ [[dbo.V_SG_TAG]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_SG_MENSAJE]], [[dbo.V_SG_TAG]], [[dbo.V_SG_TAG_ENCUESTA_TECNICA]], [[dbo.V_SG_TAG_TOTAL]], [[dbo.vLeads12meses]], [[dbo.v_OC_Leads]], [[dbo.v_OC_Leads_v2]], [[dbo.v_SGParameters]]

## Vistas que la consumen (referencia)
- [[dbo.V_LEADS_360]]
- [[dbo.V_SG_CASO]]
- [[dbo.V_SG_CASO_TOTAL]]
- [[dbo.V_SG_MENSAJE]]
- [[dbo.V_SG_TAG]]
- [[dbo.V_SG_TAG_ENCUESTA_TECNICA]]
- [[dbo.V_SG_TAG_TOTAL]]
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
- [[dbo.v_OC_Leads]]
- [[dbo.v_OC_Leads_v2]]
- [[dbo.v_SGParameters]]
