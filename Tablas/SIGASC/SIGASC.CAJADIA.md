---
esquema: SIGASC
tabla: CAJADIA
objeto: SIGASC.CAJADIA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCAJADIA` (único en muestra de 200)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAJADIA

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCAJADIA` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCAJADIA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CAJADIAFCH` | datetime2 | 0% |
| 4 | `CAJANRO` | int | 0% |
| 5 | `CAJADIASTS` | varchar | 0% |
| 6 | `CAJADIAFCHCIERRE` | datetime2 | 0% |
| 7 | `CAJADIAUSRCIERRE` | varchar | 0% |
| 8 | `CAJADIARETIROULT` | int | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCAJANRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CAJANRO` (int) → [[clave-CAJANRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAJANRO` (varchar) → [[clave-PKCAJANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
