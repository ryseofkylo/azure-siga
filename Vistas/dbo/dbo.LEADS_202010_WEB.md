---
esquema: dbo
tabla: LEADS_202010_WEB
objeto: dbo.LEADS_202010_WEB
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 13
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.LEADS_202010_WEB

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[LEADS.WP_landing_202010]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `g_recaptcha_response` | nvarchar | 0% |
| 2 | `Fecha` | datetime2 | 0% |
| 3 | `Periodo` | int | 0% |
| 4 | `form_name` | nvarchar | 0% |
| 5 | `Provincia` | nvarchar | 0% |
| 6 | `Telfonodecontacto` | nvarchar | 0% |
| 7 | `your_email` | nvarchar | 0% |
| 8 | `your_name` | nvarchar | 0% |
| 9 | `utm_campaign` | nvarchar | 0% |
| 10 | `utm_medium` | nvarchar | 0% |
| 11 | `utm_source` | nvarchar | 0% |
| 12 | `Producto` | nvarchar | 0% |
| 13 | `url` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.LEADS_202010_WEB
-- Extraida: 2026-08-07T15:27:34.016693+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[LEADS_202010_WEB]
AS SELECT 
	
 r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source, 'Fútbol Premium' Producto
, r.url
from LEADS.WP_futbol_202010 r
UNION ALL
Select r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source, 'Internet' Producto
, r.url
from LEADS.WP_ARLINK_202010 r
UNION ALL
Select r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source, 'Internet Corportativo' Producto
, r.url
from LEADS.WP_ARLINK_NEG_202010 r
UNION ALL
Select r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source, 'TV Clasica' Producto
, r.url
from LEADS.WP_Clasico_202010 r
UNION ALL
Select r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source, 'Combo' Producto
, r.url
from LEADS.WP_COMBO_202010 r
UNION ALL
Select r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source, 'n/a' Producto 
, r.post_url url
from LEADS.WP_Contactanos_202010 r
UNION ALL
Select r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source, 'TV HD' Producto
, r.url
from LEADS.WP_HD_202010 r
UNION ALL
Select r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source, 'MIO' Producto
, r.url
from LEADS.WP_MIO_202010 r
UNION ALL
Select r.[g_recaptcha_response], r.Fecha,r.Periodo, r.form_name, r.Provincia, r.Telfonodecontacto, 
r.[your_email], r.[your_name], r.utm_campaign
, r.utm_medium
, r.utm_source , r.PACK Producto
, r.url
from LEADS.WP_Pack_cine_202010 r;
```
