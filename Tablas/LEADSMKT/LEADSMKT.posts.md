---
esquema: LEADSMKT
tabla: posts
objeto: LEADSMKT.posts
tipo_objeto: BASE TABLE
dominio: Marketing / Leads
canonico: true
grain: TODO (muestra vacía)
n_columnas: 3
tags:
  - esquema/LEADSMKT
  - dominio/marketing-leads
  - tipo/tabla-base
  - canonico
---

# LEADSMKT.posts

> **BASE TABLE** · Dominio: **Marketing / Leads** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** TODO (muestra vacía)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `id` | bigint | 0% |
| 2 | `created_at` | datetime2 | 0% |
| 3 | `updated_at` | datetime2 | 0% |

## Claves de join presentes
- `id` (bigint) → [[clave-ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
