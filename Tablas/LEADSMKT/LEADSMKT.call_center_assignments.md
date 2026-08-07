---
esquema: LEADSMKT
tabla: call_center_assignments
objeto: LEADSMKT.call_center_assignments
tipo_objeto: BASE TABLE
dominio: Marketing / Leads
canonico: true
grain: 1 fila = 1 `id` (único en muestra de 1)
n_columnas: 6
tags:
  - esquema/LEADSMKT
  - dominio/marketing-leads
  - tipo/tabla-base
  - canonico
---

# LEADSMKT.call_center_assignments

> **BASE TABLE** · Dominio: **Marketing / Leads** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `id` (único en muestra de 1)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `id` | bigint | 0% |
| 2 | `call_center_id` | int | 0% |
| 3 | `quantity_assignment` | int | 0% |
| 4 | `quantity_sent` | int | 0% |
| 5 | `created_at` | datetime2 | 100% |
| 6 | `updated_at` | datetime2 | 0% |

## Claves de join presentes
- `id` (bigint) → [[clave-ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
