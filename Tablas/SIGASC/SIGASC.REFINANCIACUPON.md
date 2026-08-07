---
esquema: SIGASC
tabla: REFINANCIACUPON
objeto: SIGASC.REFINANCIACUPON
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKREFINANCIACUPON` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.REFINANCIACUPON

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKREFINANCIACUPON` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKREFINANCIACUPON` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `REFINANCIANRO` | int | 0% |
| 4 | `REFINANCIACUPONID` | int | 0% |
| 5 | `REFINANCIACUPONCUOTA` | varchar | 0% |
| 6 | `REFINANCIACUPONIMPORTEVTO1` | real | 0% |
| 7 | `REFINANCIACUPONIMPORTEVTO2` | real | 0% |
| 8 | `REFINANCIACUPONFECHAVTO1` | datetime2 | 0% |
| 9 | `REFINANCIACUPONFECHAVTO2` | datetime2 | 0% |
| 10 | `REFINANCIACUPONESTADO` | varchar | 0% |
| 11 | `REFINANCIACUPONRECIBONRO` | int | 0% |
| 12 | `REFINANCIACUPONFACTURATPO` | varchar | 0% |
| 13 | `REFINANCIACUPONFACTURANRO` | int | 0% |
| 14 | `PIPELINERUNID` | varchar | 0% |
| 15 | `PKREFINANCIANRO` | varchar | 0% |
| 16 | `PKREFINANCIACUPONID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `REFINANCIANRO` (int) → [[clave-REFINANCIANRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKREFINANCIANRO` (varchar) → [[clave-PKREFINANCIANRO]]
- `PKREFINANCIACUPONID` (varchar) → [[clave-PKREFINANCIACUPONID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
