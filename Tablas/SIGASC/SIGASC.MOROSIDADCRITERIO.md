---
esquema: SIGASC
tabla: MOROSIDADCRITERIO
objeto: SIGASC.MOROSIDADCRITERIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKMOROSIDADCRITERIOID` (único en muestra de 195)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MOROSIDADCRITERIO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKMOROSIDADCRITERIOID` (único en muestra de 195)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `MOROSIDADCRITERIOID` | int | 0% |
| 3 | `MOROSIDADCRITERIONOMBRE` | varchar | 0% |
| 4 | `MOROSIDADCRITERIOMES` | int | 0% |
| 5 | `MOROSIDADCRITERIOPRIODIDAD` | int | 2% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKMOROSIDADCRITERIOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
