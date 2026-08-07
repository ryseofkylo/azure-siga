---
esquema: dbo
tabla: TablaExclusion
objeto: dbo.TablaExclusion
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `CLIENTENRO` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.TablaExclusion

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `CLIENTENOM` | varchar | 0% |
| 4 | `CLIENTEAPE` | varchar | 0% |
| 5 | `CLIENTESTS` | varchar | 0% |
| 6 | `Exclusion` | int | 0% |
| 7 | `Push` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
**Filtros**
- `c.clientenro not in( select t.clientenro from tablaexclusion t )` — _de_ [[dbo.PushMTI]]

## Vistas que la consumen (referencia)
- [[dbo.PushMTI]]
