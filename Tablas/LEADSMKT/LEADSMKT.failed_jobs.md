---
esquema: LEADSMKT
tabla: failed_jobs
objeto: LEADSMKT.failed_jobs
tipo_objeto: BASE TABLE
dominio: Marketing / Leads
canonico: true
grain: TODO (muestra vacía)
n_columnas: 7
tags:
  - esquema/LEADSMKT
  - dominio/marketing-leads
  - tipo/tabla-base
  - canonico
---

# LEADSMKT.failed_jobs

> **BASE TABLE** · Dominio: **Marketing / Leads** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** TODO (muestra vacía)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `id` | bigint | 0% |
| 2 | `uuid` | nvarchar | 0% |
| 3 | `connection` | nvarchar | 0% |
| 4 | `queue` | nvarchar | 0% |
| 5 | `payload` | nvarchar | 0% |
| 6 | `exception` | nvarchar | 0% |
| 7 | `failed_at` | datetime2 | 0% |

## Claves de join presentes
- `id` (bigint) → [[clave-ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
