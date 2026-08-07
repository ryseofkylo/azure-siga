---
esquema: SIGASC
tabla: REFINANCIACUPONFACTURA
objeto: SIGASC.REFINANCIACUPONFACTURA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKREFINANCIACUPONFACTURA` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.REFINANCIACUPONFACTURA

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKREFINANCIACUPONFACTURA` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKREFINANCIACUPONFACTURA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `REFINANCIANRO` | int | 0% |
| 4 | `REFINANCIACUPONID` | int | 0% |
| 5 | `REFINANCIACUPONFACID` | int | 0% |
| 6 | `REFINANCIACUPONFACIMPORTE` | real | 0% |
| 7 | `REFINANCIACUPONFACTPO` | varchar | 0% |
| 8 | `REFINANCIACUPONFACNRO` | int | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKREFINANCIANRO` | varchar | 0% |
| 11 | `PKREFINANCIACUPONID` | varchar | 0% |
| 12 | `PKREFINANCIACUPONFACID` | varchar | 0% |

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
