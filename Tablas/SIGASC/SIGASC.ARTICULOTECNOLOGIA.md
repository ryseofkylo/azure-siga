---
esquema: SIGASC
tabla: ARTICULOTECNOLOGIA
objeto: SIGASC.ARTICULOTECNOLOGIA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `ARTICULOTECID` (único en muestra de 8)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ARTICULOTECNOLOGIA

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ARTICULOTECID` (único en muestra de 8)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ARTICULOTECID` | int | 0% |
| 2 | `ARTICULOTECNOMBRE` | varchar | 0% |
| 3 | `ARTICULOHD` | int | 0% |
| 4 | `ARTICULOSD` | int | 0% |
| 5 | `ARTICULOANALOGICO` | int | 0% |
| 6 | `ARTICULOWIFI` | int | 0% |
| 7 | `ARTICULOTECCLASE` | varchar | 0% |
| 8 | `ARTICULOGPON` | int | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
