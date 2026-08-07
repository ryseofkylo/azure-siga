---
esquema: SIGAMSASC
tabla: CIUDAD
objeto: SIGAMSASC.CIUDAD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CIUDADID` (único en muestra de 40)
n_columnas: 5
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.CIUDAD

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CIUDADID` (único en muestra de 40)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PAISID` | int | 0% |
| 2 | `CIUDADID` | int | 0% |
| 3 | `CIUDADNOM` | varchar | 0% |
| 4 | `ESTADOID` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PAISID` (int) → [[clave-PAISID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
