---
esquema: LEADSMKT
tabla: users
objeto: LEADSMKT.users
tipo_objeto: BASE TABLE
dominio: Marketing / Leads
canonico: true
grain: TODO (muestra vacía)
n_columnas: 8
tags:
  - esquema/LEADSMKT
  - dominio/marketing-leads
  - tipo/tabla-base
  - canonico
---

# LEADSMKT.users

> **BASE TABLE** · Dominio: **Marketing / Leads** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** TODO (muestra vacía)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `id` | bigint | 0% |
| 2 | `name` | nvarchar | 0% |
| 3 | `email` | nvarchar | 0% |
| 4 | `email_verified_at` | datetime2 | 0% |
| 5 | `password` | nvarchar | 0% |
| 6 | `remember_token` | nvarchar | 0% |
| 7 | `created_at` | datetime2 | 0% |
| 8 | `updated_at` | datetime2 | 0% |

## Claves de join presentes
- `id` (bigint) → [[clave-ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
