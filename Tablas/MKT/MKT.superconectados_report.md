---
esquema: MKT
tabla: superconectados_report
objeto: MKT.superconectados_report
tipo_objeto: BASE TABLE
dominio: Marketing
canonico: true
grain: 1 fila = 1 `impresiones` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/MKT
  - dominio/marketing
  - tipo/tabla-base
  - canonico
---

# MKT.superconectados_report

> **BASE TABLE** · Dominio: **Marketing** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `impresiones` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `campania` | nvarchar | 0% |
| 2 | `tipo_de_campania` | nvarchar | 0% |
| 3 | `impresiones` | int | 0% |
| 4 | `clics` | int | 0% |
| 5 | `inversion` | numeric | 20% |
| 6 | `periodo` | nvarchar | 0% |
| 7 | `canal` | nvarchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
