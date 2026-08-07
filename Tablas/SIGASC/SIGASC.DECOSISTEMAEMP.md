---
esquema: SIGASC
tabla: DECOSISTEMAEMP
objeto: SIGASC.DECOSISTEMAEMP
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKDECOSISID` (único en muestra de 60)
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECOSISTEMAEMP

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKDECOSISID` (único en muestra de 60)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `DECOSISID` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `DECOSISEMPCODE` | varchar | 95% |
| 4 | `PIPELINERUNID` | varchar | 0% |
| 5 | `PKDECOSISID` | varchar | 0% |

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
