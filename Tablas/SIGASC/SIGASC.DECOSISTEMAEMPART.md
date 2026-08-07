---
esquema: SIGASC
tabla: DECOSISTEMAEMPART
objeto: SIGASC.DECOSISTEMAEMPART
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKARTICULOIDDECO` (único en muestra de 49)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECOSISTEMAEMPART

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKARTICULOIDDECO` (único en muestra de 49)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKDECOSISTEMAEMPART` | varchar | 0% |
| 2 | `DECOSISID` | int | 0% |
| 3 | `EMPRESAID` | int | 0% |
| 4 | `ARTICULOIDDECO` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKDECOSISID` | varchar | 0% |
| 7 | `PKARTICULOIDDECO` | varchar | 0% |

## Claves de join presentes
- `DECOSISID` (int) → [[clave-DECOSISID]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKDECOSISID` (varchar) → [[clave-PKDECOSISID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
