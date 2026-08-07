---
esquema: SIGASC
tabla: RECURSO
objeto: SIGASC.RECURSO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKRECURSOID` (único en muestra de 200)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.RECURSO

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKRECURSOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `RECURSOID` | int | 0% |
| 3 | `RECURSONOMBRE` | varchar | 0% |
| 4 | `RECURSOENZONA` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKRECURSOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `RECURSOID` (int) → [[clave-RECURSOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKRECURSOID` (varchar) → [[clave-PKRECURSOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
