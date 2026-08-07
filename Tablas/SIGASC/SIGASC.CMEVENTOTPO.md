---
esquema: SIGASC
tabla: CMEVENTOTPO
objeto: SIGASC.CMEVENTOTPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CMEVETPO` (único en muestra de 7)
n_columnas: 4
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMEVENTOTPO

> **BASE TABLE** · Dominio: **Core SIGA** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CMEVETPO` (único en muestra de 7)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CMEVETPO` | int | 0% |
| 2 | `CMEVETPONOMBRE` | varchar | 0% |
| 3 | `CMEVETPOPRI` | int | 0% |
| 4 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
