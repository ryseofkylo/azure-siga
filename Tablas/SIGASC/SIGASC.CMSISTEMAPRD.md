---
esquema: SIGASC
tabla: CMSISTEMAPRD
objeto: SIGASC.CMSISTEMAPRD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`CMPRDID`, `CMSISTEMAID`) — compuesto, tentativo (muestra 10)
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMSISTEMAPRD

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CMPRDID`, `CMSISTEMAID`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CMSISTEMAID` | int | 0% |
| 2 | `CMPRDID` | int | 0% |
| 3 | `CMPRDNOM` | varchar | 0% |
| 4 | `CMPRDCLAVE` | varchar | 3% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `CMSISTEMAID` (int) → [[clave-CMSISTEMAID]]
- `CMPRDID` (int) → [[clave-CMPRDID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
