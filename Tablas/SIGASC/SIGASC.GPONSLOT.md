---
esquema: SIGASC
tabla: GPONSLOT
objeto: SIGASC.GPONSLOT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKGPONSLOTID` (único en muestra de 200)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.GPONSLOT

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKGPONSLOTID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `GPONSLOTID` | int | 0% |
| 3 | `GPONSLOTNOMBRE` | varchar | 0% |
| 4 | `GPONCHASISID` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKGPONSLOTID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
