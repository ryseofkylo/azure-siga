---
esquema: SIGASC
tabla: PRODUCTOPOL
objeto: SIGASC.PRODUCTOPOL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPRODUCTOPOL` (único en muestra de 200)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTOPOL

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPRODUCTOPOL` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPRODUCTOPOL` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PRODUCTOID` | int | 0% |
| 4 | `POLITICAID` | int | 0% |
| 5 | `PRODUCTOPOLITICABASE` | int | 0% |
| 6 | `PRODUCTOPOLITICAREDUCIDO` | int | 0% |
| 7 | `POLITICAENPORTAL` | int | 100% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKPRODUCTOID` | varchar | 0% |
| 10 | `PKPOLITICAID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]
- `PKPOLITICAID` (varchar) → [[clave-PKPOLITICAID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
