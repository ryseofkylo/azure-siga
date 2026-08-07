---
esquema: dbo
tabla: v_LeadsTotales
objeto: dbo.v_LeadsTotales
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 16
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_LeadsTotales

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[LEADS.UNB_leads_rango]]
- [[LEADSMKT.leads]]
- [[dbo.LEADS_202010_WEB]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `FUENTE` | varchar | 0% |
| 2 | `periodo` | int | 0% |
| 3 | `fecha` | datetime2 | 0% |
| 4 | `form_name` | nvarchar | 0% |
| 5 | `provincia` | nvarchar | 0% |
| 6 | `Telfonodecontacto` | nvarchar | 10% |
| 7 | `email` | nvarchar | 0% |
| 8 | `nombre_y_apellido` | nvarchar | 0% |
| 9 | `utm_campaign` | nvarchar | 1% |
| 10 | `utm_medium` | nvarchar | 1% |
| 11 | `utm_source` | nvarchar | 1% |
| 12 | `campo_clave` | nvarchar | 0% |
| 13 | `producto` | nvarchar | 100% |
| 14 | `lead_id` | nvarchar | 100% |
| 15 | `LandingID` | nvarchar | 0% |
| 16 | `URL` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_LeadsTotales
-- Extraida: 2026-08-07T15:28:00.126814+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_LeadsTotales]
AS with leads_Unbounce
as(
	Select 
		DATEADD(HH,-3, CONVERT(datetime, left(date_submitted,11) + replace(time_submitted,'UTC',''))) FECHA
		, page_name form_name
		, provincia
		, telefono_de_contacto Telfonodecontacto
		, email
		, nombre_y_apellido
		, utm_campaign
		, utm_medium
		, utm_source
		, r.producto
		, r.lead_id
		, r.page_uuid LandingID
		, r.page_url + '/' page_url
	from [LEADS].[UNB_leads_20201001_20201031] r
		where page_uuid not in ('d735856d-2c32-42e2-8160-458f7daee89e',	'b2332372-c1fa-4585-87f9-865821d19ca7')
),
leads_Unbounce12
as(
	Select 
		DATEADD(HH,-3, CONVERT(datetime, left(date_submitted,11) + replace(time_submitted,'UTC',''))) FECHA
		, page_name form_name
		, provincia
		, telefono_de_contacto Telfonodecontacto
		, email
		, nombre_y_apellido
		, utm_campaign
		, utm_medium
		, utm_source
		, r.producto
		, r.lead_id
		, r.page_uuid LandingID
		, r.page_url  + '/' page_url
	from [LEADS].[UNB_leads_20201201_20201231] r
		where page_uuid not in ('d735856d-2c32-42e2-8160-458f7daee89e',	'b2332372-c1fa-4585-87f9-865821d19ca7')
),
leads_Unbounce2021_01
as(
	Select 
		DATEADD(HH,-3, CONVERT(datetime, left(date_submitted,11) + replace(time_submitted,'UTC',''))) FECHA
		, page_name form_name
		, provincia
		, replace(isnull(telefono_de_contacto,'')
			+'|'+ isnull(r.nro_celular,'')
			,'|', '') Telfonodecontacto
		--, teléfono_de_contacto Telfonodecontacto
		, email
		, replace(isnull(nombre_cliente,'')
			+'|'+ isnull(r.nombre_y_apellido,'')
			,'|', '')  nombre_y_apellido
		, utm_campaign
		, utm_medium
		, utm_source
		, r.producto
		, r.lead_id
		, r.page_uuid LandingID
		, r.page_url  + '/' page_url
	from [LEADS].[UNB_leads_20210101_20210131] r
		where page_uuid not in ('d735856d-2c32-42e2-8160-458f7daee89e',	'b2332372-c1fa-4585-87f9-865821d19ca7')
),
leads_unbounce09 as
(	Select 
		DATEADD(HH,-3, CONVERT(datetime, left(date_submitted,11) + replace(time_submitted,'UTC',''))) FECHA
		, page_name form_name
		, provincia
		, telefono_de_contacto Telfonodecontacto
		, email
		, nombre_y_apellido
		, utm_campaign
		, utm_medium
		, utm_source
		, '' Producto
		, null lead_id
		, r.page_uuid LandingID
		, r.page_url + '/' page_url
	from [LEADS].[UNB_leads_20200901_20200930] r
		where page_uuid not in ('d735856d-2c32-42e2-8160-458f7daee89e',	'b2332372-c1fa-4585-87f9-865821d19ca7')
	union all 
	Select 
		DATEADD(HH,-3, CONVERT(datetime, left(date_submitted,11) + replace(time_submitted,'UTC',''))) FECHA
		, page_name form_name
		, provincia
		, replace(isnull(telefono_de_contacto,'')
			+'|'+ isnull(r.numero_de_contacto,'')
			+'|'+ isnull(r.telefono_de_contacto,'')
			+'|'+ isnull(r.nro_celular,'')
			,'|', '') Telfonodecontacto
		, replace(isnull(r.email,'')
			+'|'+ isnull(r.correo_electrónico,'')
			,'|', '') email
		, replace(isnull(nombre_y_apellido,'')
			+'|'+ isnull(r.nombre_cliente,'')
			,'|', '')  nombre_y_apellido
		, utm_campaign
		, utm_medium
		, utm_source
		, r.producto
		, r.lead_id
		, r.page_uuid LandingID
		, r.page_url + '/' page_url
	from [LEADS].[UNB_leads_20201101_20201130] r
		where page_uuid not in ('d735856d-2c32-42e2-8160-458f7daee89e',	'b2332372-c1fa-4585-87f9-865821d19ca7')
	)
, leads_anual as (
	Select 
		DATEADD(HH,-3, CONVERT(datetime, left(date_submitted,11) + replace(time_submitted,'UTC',''))) FECHA
		, page_name form_name
		, provincia
		, replace(isnull(telefono_de_contacto,'')
			+'|'+ isnull(r.numero_de_contacto,'')
			+'|'+ isnull(r.numero_de_telefono,'')
			+'|'+ isnull(r.telefono_de_contacto,'')
			+'|'+ isnull(r.telephone,''),'|', '') Telfonodecontacto
		, email
		, replace(isnull(nombre_y_apellido,'')
			+'|'+ isnull(r.name,'')
			+'|'+ isnull(r.nombre,''),'|', '')  nombre_y_apellido
		, utm_campaign
		, utm_medium
		, utm_source
		, r.txt_procucto Producto
		, null lead_id
		, r.page_uuid LandingID
		, r.page_url + '/' page_url
	from LEADS.[UNB_leads_20200101_20200831] r
		where page_uuid not in ('d735856d-2c32-42e2-8160-458f7daee89e',	'b2332372-c1fa-4585-87f9-865821d19ca7')
),
leads_unbounce_new as(
	
	Select 
		date_lead FECHA -- Ya esta convertida a UTC -3 
		, r.page_name form_name
		, r.provincia
		, isnull(cast(r.nro_celular as varchar(100)),'') Telfonodecontacto
		, r.email
		, isnull(r.nombre_cliente,'') nombre_y_apellido
		, r.utm_campaign
		, r.utm_medium
		, r.utm_source
		, r.producto Producto
		, r.lead_id
		, r.page_uuid LandingID
		, r.page_url
	from LEADSMKT.leads r
		where r.date_lead >= '20210201' --filtro por el inicio de producción
		and page_uuid not in ('d735856d-2c32-42e2-8160-458f7daee89e',	'b2332372-c1fa-4585-87f9-865821d19ca7')


)
, leads as(
	Select 'UNBOUNCE' FUENTE, year(fecha)*100 + MONTH(fecha) periodo, 
	fecha, form_name, Provincia, Telfonodecontacto, email, nombre_y_apellido, utm_campaign, utm_medium, utm_source, Producto, lead_id, LandingID, page_url
	from leads_Unbounce
	union all 
	Select 'UNBOUNCE' FUENTE, year(fecha)*100 + MONTH(fecha) periodo, 
	fecha, form_name, Provincia, Telfonodecontacto, email, nombre_y_apellido, utm_campaign, utm_medium, utm_source, Producto, lead_id, LandingID, page_url
	from leads_Unbounce09 l
	union all 
	Select 'UNBOUNCE' FUENTE, year(fecha)*100 + MONTH(fecha) periodo, 
	fecha, form_name, Provincia, Telfonodecontacto, email, nombre_y_apellido, utm_campaign, utm_medium, utm_source, Producto, lead_id, LandingID, page_url
	from leads_anual
	union all 
	Select 'UNBOUNCE' FUENTE, year(fecha)*100 + MONTH(fecha) periodo, 
	fecha, form_name, Provincia, Telfonodecontacto, email, nombre_y_apellido, utm_campaign, utm_medium, utm_source, Producto, lead_id, LandingID, page_url
	from leads_Unbounce12
	union all 
	Select 'UNBOUNCE' FUENTE, year(fecha)*100 + MONTH(fecha) periodo, 
	fecha, form_name, Provincia, Telfonodecontacto, email, nombre_y_apellido, utm_campaign, utm_medium, utm_source, Producto, lead_id, LandingID, page_url
	from leads_Unbounce2021_01
	union all 
	Select 'UNBOUNCE' FUENTE, year(l.FECHA)*100 + MONTH(l.FECHA) periodo, 
		l.fecha, l.form_name, Provincia
		, l.Telfonodecontacto, l.email, l.nombre_y_apellido
		, l.utm_campaign, l.utm_medium, l.utm_source, l.Producto, l.lead_id, LandingID, page_url
	from leads_unbounce_new l

)

Select 'UNBOUNCE' FUENTE, periodo, 	fecha
	--, dbo.fnCorregirNombreFormulario(form_name) form_name
	,  form_name
	, case 
		when provincia like 'Tucum%n' then 'Tucuman'
		when provincia like 'R%o Negro' then 'Rio Negro'
		when provincia like 'C%rdoba' then 'Cordoba'
		when provincia like 'Neuqu%n' then 'Neuquen'
		else provincia 
	end provincia, 
	Telfonodecontacto, email, nombre_y_apellido, utm_campaign, utm_medium, utm_source
	, lower(concat(email,'|',Telfonodecontacto)) campo_clave
	, producto
	, l.lead_id
	, l.LandingID
	, l.page_url as URL
from leads l
--where periodo in(202102)
union all
	Select 'WEB' FUENTE,
		Periodo, fecha, upper(form_name) form_name, 
		case 
			when provincia like 'Tucum%n' then 'Tucuman'
			when provincia like 'R%o Negro' then 'Rio Negro'
			when provincia like 'C%rdoba' then 'Cordoba'
			when provincia like 'Neuqu%n' then 'Neuquen'
			else provincia 
		end provincia
		, Telfonodecontacto, [your_email], [your_name], utm_campaign, utm_medium, utm_source
		, lower(concat([your_email],'|',Telfonodecontacto)) campo_clave
		, F.Producto
		, Telfonodecontacto lead_id
		, f.form_name LandingId
		, f.url
from LEADS_202010_WEB f;
```
