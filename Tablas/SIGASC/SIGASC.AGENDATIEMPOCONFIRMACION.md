---
esquema: SIGASC
tabla: AGENDATIEMPOCONFIRMACION
objeto: SIGASC.AGENDATIEMPOCONFIRMACION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKATCCOLOR` (único en muestra de 44)
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.AGENDATIEMPOCONFIRMACION

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKATCCOLOR` (único en muestra de 44)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ATCCOLOR` | int | 0% |
| 3 | `ATCTIEMPO` | int | 0% |
| 4 | `PIPELINERUNID` | varchar | 0% |
| 5 | `PKATCCOLOR` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
