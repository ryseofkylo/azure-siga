---
esquema: SIGASC
tabla: CMODEMPRODUCTO
objeto: SIGASC.CMODEMPRODUCTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CMODEMID` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMODEMPRODUCTO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CMODEMID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCMODEMPRODUCTO` | varchar | 0% |
| 2 | `CMSISTEMAID` | int | 0% |
| 3 | `CMODEMID` | varchar | 0% |
| 4 | `CMPRDID` | int | 0% |
| 5 | `CMODEMPRDING` | varchar | 0% |
| 6 | `CMODEMPRDUSR` | varchar | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |

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
