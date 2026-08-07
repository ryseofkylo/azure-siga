---
esquema: dbo
tabla: SG_ClientMessage
objeto: dbo.SG_ClientMessage
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `Id` (único en muestra de 200)
n_columnas: 4
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.SG_ClientMessage

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Date` | datetime2 | 0% |
| 3 | `Text` | nvarchar | 0% |
| 4 | `CasoId` | bigint | 0% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `CasoId` (bigint) → [[clave-CASOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.SG_Caso]] · `SG_ClientMessage.CASOID = SG_Caso.ID` — view_join (vLeads), alta
- [[dbo.V_LEADS_360]] · `SG_ClientMessage.CASOID = V_LEADS_360.ID` — view_join (V_MESSAGELEADS_360), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `exists ( select 1 from SG_ClientMessage m where m.Text = 'Hola, me gustaría contratar un servicio ¿Me pueden ayudar?' and m.CasoId = c.Id )` — _de_ [[dbo.vLeads]]
- `m.Text = 'Hola, me gustaría contratar un servicio ¿Me pueden ayudar?'` — _de_ [[dbo.vLeads]]
- 🚦 `not exists ( select 1 from SG_ClientMessage m2 where m2.Text = 'Hola, me gustaría contratar un servicio ¿Me pueden ayudar?' and m2.CasoId = c.Id )` — _de_ [[dbo.vLeads]]
- `m2.Text = 'Hola, me gustaría contratar un servicio ¿Me pueden ayudar?'` — _de_ [[dbo.vLeads]]
- `m.casoid IN ( SELECT DISTINCT c.id FROM SG_CASO c WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) )` — _de_ [[dbo.V_SG_MENSAJE]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_MESSAGELEADS_360]], [[dbo.V_SG_MENSAJE]], [[dbo.vLeads12meses]]

## Vistas que la consumen (referencia)
- [[dbo.V_MESSAGELEADS_360]]
- [[dbo.V_SG_CASO]]
- [[dbo.V_SG_MENSAJE]]
- [[dbo.vLeads]]
- [[dbo.vLeads12meses]]
- [[dbo.vLeads_Boton_de_WhatsApp]]
- [[dbo.vLeads_Click_to_WhatsApp]]
- [[dbo.vLeadsnuevo]]
