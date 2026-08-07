---
esquema: SIGASC
tabla: GPONNAPPUERTO
objeto: SIGASC.GPONNAPPUERTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKGPONNAPPUERTO` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.GPONNAPPUERTO

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKGPONNAPPUERTO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKGPONNAPPUERTO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `GPONNAPID` | int | 0% |
| 4 | `GPONNAPPUERTOID` | int | 0% |
| 5 | `GPONNAPPUERTOARTSERIE` | varchar | 0% |
| 6 | `GPONNAPPUERTOARTID` | int | 0% |
| 7 | `GPONNAPPUERTOCLIENTE` | int | 0% |
| 8 | `GPONNAPPUERTORX` | real | 0% |
| 9 | `GPONNAPPUERTOSTS` | varchar | 0% |
| 10 | `GPONNAPPUERTOFCHACTUALIZACION` | datetime2 | 0% |
| 11 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 12 | `PIPELINERUNID` | varchar | 0% |
| 13 | `PKGPONNAPID` | varchar | 0% |
| 14 | `PKGPONNAPPUERTOID` | varchar | 0% |

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
