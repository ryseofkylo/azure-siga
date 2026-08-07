---
esquema: dbo
tabla: SG_OC_Tag
objeto: dbo.SG_OC_Tag
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

# dbo.SG_OC_Tag

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `IdTag` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `IdTag` | bigint | 0% |
| 2 | `Id` | bigint | 0% |
| 3 | `Name` | nvarchar | 0% |
| 4 | `Context` | nvarchar | 0% |
| 5 | `Date` | datetime2 | 0% |
| 6 | `OC_CasoId` | bigint | 0% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `OC_CasoId` (bigint) → [[clave-OC_CASOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.SG_OC_Caso]] · `SG_OC_Tag.OC_CASOID = SG_OC_Caso.ID` — view_join (v_OC_Leads), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `NOT EXISTS ( SELECT 1 FROM SG_oc_Tag t WHERE t.OC_CasoId = c.id AND LTRIM(RTRIM(t.Name)) IN ('Chat2Whatsapp Deflection', 'Ventas Widget') )` — _de_ [[dbo.v_OC_Leads]]
- `LTRIM(RTRIM(t.Name)) IN ('Chat2Whatsapp Deflection', 'Ventas Widget')` — _de_ [[dbo.v_OC_Leads]]
- `t.Name = 'Ventas Widget'` — _de_ [[dbo.v_OC_Leads]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.v_OC_Leads]], [[dbo.v_OC_Leads_v2]]

## Vistas que la consumen (referencia)
- [[dbo.v_OC_Leads]]
- [[dbo.v_OC_Leads_v2]]
