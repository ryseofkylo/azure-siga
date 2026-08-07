---
esquema: SIGASC
tabla: DECOEVENTOTPO
objeto: SIGASC.DECOEVENTOTPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `DECOEVETPO` (único en muestra de 10)
n_columnas: 4
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECOEVENTOTPO

> **BASE TABLE** · Dominio: **Core SIGA** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `DECOEVETPO` (único en muestra de 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `DECOEVETPO` | int | 0% |
| 2 | `DECOEVETPONOMBRE` | varchar | 0% |
| 3 | `DECOEVETPOPRI` | int | 0% |
| 4 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
