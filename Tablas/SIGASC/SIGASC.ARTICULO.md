---
esquema: SIGASC
tabla: ARTICULO
objeto: SIGASC.ARTICULO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `ARTICULOID` (único en muestra de 200)
n_columnas: 20
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ARTICULO

> **BASE TABLE** · Dominio: **Core SIGA** · 20 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ARTICULOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ARTICULOID` | int | 0% |
| 2 | `ARTICULONOMBRE` | varchar | 0% |
| 3 | `ARTICULOUNIDAD` | varchar | 0% |
| 4 | `ARTICULOUSASERIE` | int | 0% |
| 5 | `ARTICULOAPROVISIONAR` | varchar | 0% |
| 6 | `ARTICULOUSAMETRAJE` | int | 0% |
| 7 | `ARTICULOSERIELARGO` | int | 0% |
| 8 | `ARTICULOSERIECONTROL` | varchar | 0% |
| 9 | `ARTICULOCLASE` | varchar | 0% |
| 10 | `ARTICULOUSAEMPAREJAR` | int | 0% |
| 11 | `ARTICULOTECID` | int | 86% |
| 12 | `ARTICULOCODEXT` | varchar | 12% |
| 13 | `ARTICULOTIPOVALORACION` | varchar | 90% |
| 14 | `ARTICULOCLASEENUM` | varchar | 0% |
| 15 | `ARTICULOUSALOTE` | int | 100% |
| 16 | `ARTICULOCONTROL` | varchar | 0% |
| 17 | `ARTICULODIVISOR` | real | 0% |
| 18 | `ARTICULONOUSAPAIRING` | int | 100% |
| 19 | `ARTICULOORDEN` | int | 1% |
| 20 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `ARTICULOID` (int) → [[clave-ARTICULOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
