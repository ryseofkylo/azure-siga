---
esquema: dbo
tabla: v_SGParameters
objeto: dbo.v_SGParameters
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 11
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_SGParameters

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_Parameter]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Nro` | bigint | 0% |
| 2 | `utm_source` | varchar | 0% |
| 3 | `utm_medium` | varchar | 0% |
| 4 | `utm_campaign` | varchar | 0% |
| 5 | `provincia` | varchar | 0% |
| 6 | `page_name` | varchar | 0% |
| 7 | `date_lead` | datetime | 0% |
| 8 | `Source` | nvarchar | 0% |
| 9 | `Campaign` | nvarchar | 0% |
| 10 | `producto` | varchar | 0% |
| 11 | `CasoId` | bigint | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_SGParameters
-- Extraida: 2026-08-07T15:28:20.932705+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_SGParameters]
AS with datos as(
       SELECT distinct Casoid
             FROM SG_Parameter
), leadsSG as (
SELECT Casoid,[producto],[adgroup_id],[dia_del_mes_actual],[leadgen_id],[subject],[utm_medium],[fromEmail],[page_id],[fromPhone],[fromName],[extId],[provincia_desde_donde_consulta],[leadgen_utm_medium],[email],[leadgen_utm_campaign],[created_time],[utm_campaign],[form_id],[leadgen_full_name],[leadgen_phone_number],[leadgen_utm_source],[leadgen_email],[ad_id],[full_name],[minuto_del_dia_actual],[phone_number],[leadgen_provincia_desde_donde_consulta],[utm_source],[provincia]
FROM   
       (SELECT Casoid, [Key], cast([value] as varchar(1000)) as valor
             FROM SG_Parameter
                    where casoid in (select casoid from datos)
             ) p  
       PIVOT  
       (  
             max (valor)  
             FOR [Key] IN  
             ([adgroup_id],[producto],[dia_del_mes_actual],[leadgen_id],[subject],[utm_medium],[fromEmail],[page_id],[fromPhone],[fromName],[extId],[provincia_desde_donde_consulta],[leadgen_utm_medium],[email],[leadgen_utm_campaign],[created_time],[utm_campaign],[form_id],[leadgen_full_name],[leadgen_phone_number],[leadgen_utm_source],[leadgen_email],[ad_id],[full_name],[minuto_del_dia_actual],[phone_number],[leadgen_provincia_desde_donde_consulta],[utm_source],[provincia]
             )  
       ) AS pvt  )
	   ,LeadsAds as (
Select 
 L.utm_source
, L.utm_medium
, L.utm_campaign
, dbo.[InitCap](Replace(L.provincia,'_',' ')) as provincia
--, L.provincia_desde_donde_consulta as provincia
, L.[subject] as page_name
, CONVERT(datetime, SWITCHOFFSET(DATEADD(s,cast( L.created_time as bigint), '1970-01-01'),DATENAME(TzOffset, SYSDATETIMEOFFSET()))) as date_lead
, c.Source
, c.Campaign
,l.producto
, L.CasoId
from leadsSG L
       inner join SG_Caso c
             on l.CasoId = c.Id
)
Select 
ROW_NUMBER ( ) OVER(ORDER BY date_lead desc) AS Nro, * from LeadsAds;
```
