---
esquema: SIGASC
tabla: GPONNAP
objeto: SIGASC.GPONNAP
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKGPONNAPID` (único en muestra de 200)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.GPONNAP

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKGPONNAPID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `GPONNAPID` | int | 0% |
| 3 | `GPONNAPSERIENRO` | varchar | 0% |
| 4 | `GPONNAPGEOX` | varchar | 0% |
| 5 | `GPONNAPGEOY` | varchar | 0% |
| 6 | `GPONNAPPUERTOS` | int | 0% |
| 7 | `GPONNAPDESCRIPCION` | varchar | 0% |
| 8 | `GPONOLDID` | int | 0% |
| 9 | `GPONNAPGEOYNUM` | real | 0% |
| 10 | `GPONNAPGEOXNUM` | real | 0% |
| 11 | `GPONNAPSERIEID` | int | 34% |
| 12 | `GPONNAPFCHACTUALIZACION` | datetime2 | 0% |
| 13 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 14 | `PIPELINERUNID` | varchar | 0% |
| 15 | `PKGPONNAPID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKGPONNAPID` (varchar) → [[clave-PKGPONNAPID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
