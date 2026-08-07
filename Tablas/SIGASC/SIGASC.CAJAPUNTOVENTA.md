---
esquema: SIGASC
tabla: CAJAPUNTOVENTA
objeto: SIGASC.CAJAPUNTOVENTA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCAJAPUNTOVENTA` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAJAPUNTOVENTA

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCAJAPUNTOVENTA` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCAJAPUNTOVENTA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CAJANRO` | int | 0% |
| 4 | `EMPRESAFISCALID` | int | 0% |
| 5 | `PUNTOVTAID` | int | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKCAJANRO` | varchar | 0% |
| 8 | `PKEMPRESAFISCALID` | varchar | 0% |
| 9 | `PKPUNTOVTAID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CAJANRO` (int) → [[clave-CAJANRO]]
- `EMPRESAFISCALID` (int) → [[clave-EMPRESAFISCALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAJANRO` (varchar) → [[clave-PKCAJANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
