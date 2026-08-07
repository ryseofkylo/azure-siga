---
esquema: SIGASC
tabla: CAJA
objeto: SIGASC.CAJA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCAJANRO` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAJA

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCAJANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CAJANRO` | int | 0% |
| 3 | `CAJANOMBRE` | varchar | 0% |
| 4 | `CAJAFCHULTAPERTURA` | datetime2 | 100% |
| 5 | `CAJAGRUPOID` | int | 0% |
| 6 | `CAJAESTADO` | varchar | 0% |
| 7 | `CAJATIPO` | varchar | 0% |
| 8 | `CAJACOBRADORDEFAULT` | int | 100% |
| 9 | `CAJACIERREAUTO` | int | 0% |
| 10 | `CAJAAPERTURAAUTO` | int | 0% |
| 11 | `PIPELINERUNID` | varchar | 0% |
| 12 | `PKCAJANRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CAJANRO` (int) → [[clave-CAJANRO]]
- `CAJAGRUPOID` (int) → [[clave-CAJAGRUPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAJANRO` (varchar) → [[clave-PKCAJANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
