---
esquema: SIGASC
tabla: CAJAGRUPO
objeto: SIGASC.CAJAGRUPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCAJAGRUPOID` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAJAGRUPO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCAJAGRUPOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CAJAGRUPOID` | int | 0% |
| 3 | `CAJAGRUPONOMBRE` | varchar | 0% |
| 4 | `CAJAGRUPOUNIDAD` | int | 0% |
| 5 | `CAJAGRUPOUNIDADCONTABLE` | int | 22% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKCAJAGRUPOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CAJAGRUPOID` (int) → [[clave-CAJAGRUPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAJAGRUPOID` (varchar) → [[clave-PKCAJAGRUPOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
