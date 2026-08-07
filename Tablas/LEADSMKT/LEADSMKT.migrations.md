---
esquema: LEADSMKT
tabla: migrations
objeto: LEADSMKT.migrations
tipo_objeto: BASE TABLE
dominio: Marketing / Leads
canonico: true
grain: 1 fila = 1 `id` (único en muestra de 7)
n_columnas: 3
tags:
  - esquema/LEADSMKT
  - dominio/marketing-leads
  - tipo/tabla-base
  - canonico
---

# LEADSMKT.migrations

> **BASE TABLE** · Dominio: **Marketing / Leads** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `id` (único en muestra de 7)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `id` | int | 0% |
| 2 | `migration` | nvarchar | 0% |
| 3 | `batch` | int | 0% |

## Claves de join presentes
- `id` (int) → [[clave-ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
