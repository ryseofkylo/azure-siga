---
esquema: dbo
tabla: SG_OC_Caso
objeto: dbo.SG_OC_Caso
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

# dbo.SG_OC_Caso

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Source` | nvarchar | 0% |
| 3 | `Creation_date` | datetime2 | 0% |
| 4 | `Close_date` | datetime2 | 100% |
| 5 | `Client_id` | bigint | 0% |
| 6 | `Client_crm_id` | nvarchar | 86% |
| 7 | `Client_name` | nvarchar | 0% |
| 8 | `Client_ext_id` | nvarchar | 0% |
| 9 | `File` | nvarchar | 0% |
| 10 | `FechaProcesado` | datetime2 | 0% |
| 11 | `NroCliente` | nvarchar | 84% |
| 12 | `Campaign` | nvarchar | 0% |
| 13 | `Closed_by` | varchar | 100% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `Client_id` (bigint) → [[clave-CLIENT_ID]]
- `Client_crm_id` (nvarchar) → [[clave-CLIENT_CRM_ID]]
- `Client_ext_id` (nvarchar) → [[clave-CLIENT_EXT_ID]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.v_OC_SGParameters]] · `SG_OC_Caso.ID = v_OC_SGParameters.CASOID` — view_join (v_OC_Leads), alta
- [[dbo.SG_OC_ClientMessage]] · `SG_OC_Caso.ID = SG_OC_ClientMessage.OC_CASOID` — view_join (v_OC_Leads), alta
- [[dbo.SG_OC_Tag]] · `SG_OC_Caso.ID = SG_OC_Tag.OC_CASOID` — view_join (v_OC_Leads), alta

## Reglas de negocio conocidas
**Filtros**
- `c.id not in ( select distinct Id from sg_caso )` — _de_ [[dbo.v_OC_Leads]]
- `(c.Campaign <> 'Widget - WhatsApp')` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'Unbounce'` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'Redes Sociales'` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'Redes Sociales 2'` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'RRSS Leads 2'` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'WP Leads'` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'Whatsapp'` — _de_ [[dbo.v_OC_Leads]]
- 🚦 `exists ( select 1 from SG_OC_ClientMessage m where m.Text in ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?') and m.OC_CasoId = c.Id )` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'Forms Google Ads'` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'WhatsApp Meta'` — _de_ [[dbo.v_OC_Leads]]
- 🚦 `not exists( select 1 from SG_oc_ClientMessage m2 where m2.Text in ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?') and m2.oc_CasoId = c.Id )` — _de_ [[dbo.v_OC_Leads]]
- `LTRIM(RTRIM(c.Campaign)) = 'Widget - WhatsApp'` — _de_ [[dbo.v_OC_Leads]]
- 🚦 `NOT EXISTS ( SELECT 1 FROM SG_oc_Tag t WHERE t.OC_CasoId = c.id AND LTRIM(RTRIM(t.Name)) IN ('Chat2Whatsapp Deflection', 'Ventas Widget') )` — _de_ [[dbo.v_OC_Leads]]
- `c.Campaign = 'Widget - WhatsApp'` — _de_ [[dbo.v_OC_Leads]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.v_OC_Leads]], [[dbo.v_OC_Leads_v2]], [[dbo.v_OC_SGParameters]]

## Vistas que la consumen (referencia)
- [[dbo.v_OC_Leads]]
- [[dbo.v_OC_Leads_v2]]
- [[dbo.v_OC_SGParameters]]
