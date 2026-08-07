---
esquema: SIGASC
tabla: CAMPANAGESTION
objeto: SIGASC.CAMPANAGESTION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCAMGESID` (único en muestra de 200)
n_columnas: 21
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAMPANAGESTION

> **BASE TABLE** · Dominio: **Core SIGA** · 21 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCAMGESID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CAMGESID` | int | 0% |
| 3 | `CRMCAMNRO` | int | 0% |
| 4 | `CAMGESTPO` | varchar | 0% |
| 5 | `CAMGESPERIODOINI` | int | 100% |
| 6 | `CAMGESPERIODOFIN` | int | 100% |
| 7 | `CAMGESCLIENTESTS` | varchar | 100% |
| 8 | `CAMGESCANTCUOTAS` | int | 58% |
| 9 | `CAMGESMEDCOBROID` | int | 0% |
| 10 | `CAMGESRECARGO` | int | 100% |
| 11 | `CAMGESEXCLUYEPERIODOANT` | int | 100% |
| 12 | `CAMGESEXCLUYEGESTIONANT` | int | 100% |
| 13 | `CAMGESGENERADESDEARCH` | int | 1% |
| 14 | `CAMGESPERIODOCODBARRA` | int | 0% |
| 15 | `CAMGESESTADO` | varchar | 0% |
| 16 | `CAMGESFECHAFIN` | datetime2 | 18% |
| 17 | `CAMGESFECHAINICIO` | datetime2 | 18% |
| 18 | `CAMGESINCLUYEREFINANCIADOS` | int | 8% |
| 19 | `CAMGESINCLUYEFACSINVENCER` | int | 70% |
| 20 | `PIPELINERUNID` | varchar | 0% |
| 21 | `PKCAMGESID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CRMCAMNRO` (int) → [[clave-CRMCAMNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAMGESID` (varchar) → [[clave-PKCAMGESID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
