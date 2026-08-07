---
esquema: dbo
tabla: SG_Tag
objeto: dbo.SG_Tag
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `IdTag` (único en muestra de 200)
n_columnas: 6
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.SG_Tag

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `IdTag` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Name` | nvarchar | 0% |
| 3 | `Context` | nvarchar | 0% |
| 4 | `Date` | datetime2 | 0% |
| 5 | `CasoId` | bigint | 0% |
| 6 | `IdTag` | bigint | 0% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `CasoId` (bigint) → [[clave-CASOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.SG_Caso]] · `SG_Tag.CASOID = SG_Caso.ID` — view_join (vLeads), alta
- [[dbo.V_LEADS_360]] · `SG_Tag.CASOID = V_LEADS_360.ID` — view_join (V_TAGLEADS_360), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `EXISTS ( SELECT 1 FROM SG_Tag t1 WHERE t1.CasoId = c.id )` — _de_ [[dbo.vLeads]]
- 🚦 `NOT EXISTS ( SELECT 1 FROM SG_Tag t2 WHERE t2.CasoId = c.id AND LTRIM(RTRIM(t2.Name)) IN ('Chat2Whatsapp Deflection', 'Ventas Widget') )` — _de_ [[dbo.vLeads]]
- `LTRIM(RTRIM(t2.Name)) IN ('Chat2Whatsapp Deflection', 'Ventas Widget')` — _de_ [[dbo.vLeads]]
- `t.Name = 'Ventas Widget'` — _de_ [[dbo.vLeads]]
- `(t.Name IS NULL OR LTRIM(RTRIM(t.Name)) NOT IN ('Chat2Whatsapp Deflection', 'Ventas Widget'))` — _de_ [[dbo.vLeads12meses]]
- `t.casoid IN ( SELECT DISTINCT c.id FROM SG_CASO c WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) )` — _de_ [[dbo.V_SG_TAG]]
- 🚦 `EXISTS (SELECT 1 FROM SG_TAG T2 WHERE (CONTEXT LIKE '%ENCUESTA%TECNICA%' or CONTEXT LIKE '%RECLAMO%GENERADO%')AND t.CASOID= t2.CASOID)` — _de_ [[dbo.V_SG_TAG_ENCUESTA_TECNICA]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_SG_TAG]], [[dbo.V_SG_TAG_ENCUESTA_TECNICA]], [[dbo.V_SG_TAG_TOTAL]], [[dbo.vLeads12meses]]

## Vistas que la consumen (referencia)
- [[dbo.V_SG_CASO]]
- [[dbo.V_SG_CASO_TOTAL]]
- [[dbo.V_SG_TAG]]
- [[dbo.V_SG_TAG_ENCUESTA_TECNICA]]
- [[dbo.V_SG_TAG_TOTAL]]
- [[dbo.V_TAGLEADS_360]]
- [[dbo.vLeads]]
- [[dbo.vLeads12meses]]
- [[dbo.vLeads_Ventas_Widget]]
- [[dbo.vLeads_Widget_WhatsApp]]
- [[dbo.vLeadsnuevo]]
