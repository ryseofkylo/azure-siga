---
esquema: LEADSMKT
tabla: leads
objeto: LEADSMKT.leads
tipo_objeto: BASE TABLE
dominio: Marketing / Leads
canonico: true
grain: 1 fila = 1 `id` (único en muestra de 200)
n_columnas: 27
tags:
  - esquema/LEADSMKT
  - dominio/marketing-leads
  - tipo/tabla-base
  - canonico
---

# LEADSMKT.leads

> **BASE TABLE** · Dominio: **Marketing / Leads** · 27 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `id` | bigint | 0% |
| 2 | `date_submitted` | date | 0% |
| 3 | `time_submitted` | datetime2 | 0% |
| 4 | `ip_address` | nvarchar | 0% |
| 5 | `variant` | nvarchar | 0% |
| 6 | `page_uuid` | nvarchar | 0% |
| 7 | `page_url` | nvarchar | 0% |
| 8 | `page_name` | nvarchar | 0% |
| 9 | `page_variant_name` | nvarchar | 100% |
| 10 | `provincia` | nvarchar | 0% |
| 11 | `email` | nvarchar | 0% |
| 12 | `utm_source` | nvarchar | 0% |
| 13 | `date_lead` | datetime2 | 0% |
| 14 | `utm_campaign` | nvarchar | 0% |
| 15 | `utm_medium` | nvarchar | 0% |
| 16 | `dni` | nvarchar | 1% |
| 17 | `nro_celular` | bigint | 0% |
| 18 | `nombre_cliente` | nvarchar | 0% |
| 19 | `nro_fijo` | bigint | 100% |
| 20 | `nro_cliente` | bigint | 0% |
| 21 | `lat` | decimal | 0% |
| 22 | `long` | decimal | 0% |
| 23 | `producto` | nvarchar | 0% |
| 24 | `lead_id` | nvarchar | 0% |
| 25 | `call_center_id` | int | 0% |
| 26 | `created_at` | datetime2 | 0% |
| 27 | `updated_at` | datetime2 | 0% |

## Claves de join presentes
- `id` (bigint) → [[clave-ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
**Filtros**
- `r.date_lead >= '20210201'` — _de_ [[dbo.v_LeadsTotales]]

## Vistas que la consumen (referencia)
- [[dbo.v_LeadsTotales]]
