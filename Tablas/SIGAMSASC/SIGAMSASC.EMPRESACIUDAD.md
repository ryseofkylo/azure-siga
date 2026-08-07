---
esquema: SIGAMSASC
tabla: EMPRESACIUDAD
objeto: SIGAMSASC.EMPRESACIUDAD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`CIUDADID`) — compuesto, tentativo (muestra 10)
n_columnas: 5
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.EMPRESACIUDAD

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CIUDADID`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CIUDADID` | int | 0% |
| 3 | `EMPRESADIRTPO` | varchar | 0% |
| 4 | `EMPRESADIRTPOMODIFICABLE` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
