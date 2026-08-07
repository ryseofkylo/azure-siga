---
esquema: LEADSMKT
tabla: call_centers
objeto: LEADSMKT.call_centers
tipo_objeto: BASE TABLE
dominio: Marketing / Leads
canonico: true
grain: 1 fila = 1 `id` (único en muestra de 4)
n_columnas: 8
tags:
  - esquema/LEADSMKT
  - dominio/marketing-leads
  - tipo/tabla-base
  - canonico
---

# LEADSMKT.call_centers

> **BASE TABLE** · Dominio: **Marketing / Leads** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `id` (único en muestra de 4)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `id` | bigint | 0% |
| 2 | `name` | nvarchar | 0% |
| 3 | `destination_url` | nvarchar | 0% |
| 4 | `destination_email` | nvarchar | 0% |
| 5 | `assignment` | int | 0% |
| 6 | `active` | bit | 0% |
| 7 | `created_at` | datetime2 | 100% |
| 8 | `updated_at` | datetime2 | 100% |

## Claves de join presentes
- `id` (bigint) → [[clave-ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
