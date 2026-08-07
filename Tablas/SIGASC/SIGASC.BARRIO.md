---
esquema: SIGASC
tabla: BARRIO
objeto: SIGASC.BARRIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKBARRIO` (único en muestra de 194)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.BARRIO

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKBARRIO` (único en muestra de 194)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKBARRIO` | varchar | 0% |
| 2 | `PAISID` | int | 0% |
| 3 | `CIUDADID` | int | 0% |
| 4 | `BARRIOID` | int | 0% |
| 5 | `BARRIONOMBRE` | varchar | 0% |
| 6 | `BARRIOCORDX` | varchar | 0% |
| 7 | `BARRIOCORDY` | varchar | 0% |
| 8 | `BARRIOCALLEREFERENCIAID` | int | 0% |
| 9 | `BARRIOGEODIV2ID` | int | 1% |
| 10 | `BARRIOGEODIV1ID` | int | 1% |
| 11 | `PIPELINERUNID` | varchar | 0% |

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
