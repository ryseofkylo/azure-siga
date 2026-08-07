---
esquema: SIGASC
tabla: MOROSIDADMES
objeto: SIGASC.MOROSIDADMES
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKMOROSIDADMES` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MOROSIDADMES

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKMOROSIDADMES` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `MOROSIDADMES` | int | 0% |
| 3 | `MOROSIDADMESSTS` | varchar | 0% |
| 4 | `MOROSIDADMESUSR` | varchar | 0% |
| 5 | `MOROSIDADMESFCH` | datetime2 | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKMOROSIDADMES` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKMOROSIDADMES` (varchar) → [[clave-PKMOROSIDADMES]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
