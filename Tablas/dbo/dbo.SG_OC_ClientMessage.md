---
esquema: dbo
tabla: SG_OC_ClientMessage
objeto: dbo.SG_OC_ClientMessage
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

# dbo.SG_OC_ClientMessage

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Date` | datetime2 | 0% |
| 3 | `Text` | nvarchar | 2% |
| 4 | `OC_CasoId` | bigint | 0% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `OC_CasoId` (bigint) → [[clave-OC_CASOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.SG_OC_Caso]] · `SG_OC_ClientMessage.OC_CASOID = SG_OC_Caso.ID` — view_join (v_OC_Leads), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `exists ( select 1 from SG_OC_ClientMessage m where m.Text in ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?') and m.OC_CasoId = c.Id )` — _de_ [[dbo.v_OC_Leads]]
- `m.Text in ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?')` — _de_ [[dbo.v_OC_Leads]]
- 🚦 `not exists( select 1 from SG_oc_ClientMessage m2 where m2.Text in ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?') and m2.oc_CasoId = c.Id )` — _de_ [[dbo.v_OC_Leads]]
- `m2.Text in ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?')` — _de_ [[dbo.v_OC_Leads]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.v_OC_Leads]], [[dbo.v_OC_Leads_v2]]

## Vistas que la consumen (referencia)
- [[dbo.v_OC_Leads]]
- [[dbo.v_OC_Leads_v2]]
