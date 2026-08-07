---
esquema: SIGASC
tabla: REFINANCIAFACTURA
objeto: SIGASC.REFINANCIAFACTURA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKFACTURANRO` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.REFINANCIAFACTURA

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKFACTURANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKREFINANCIAFACTURA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `REFINANCIANRO` | int | 0% |
| 4 | `FACTURATPO` | varchar | 0% |
| 5 | `FACTURANRO` | int | 0% |
| 6 | `REFINANCIAFACSDO` | real | 0% |
| 7 | `REFINANCIAFACATRASODIA` | int | 0% |
| 8 | `REFINANCIAFACATRASOINT` | real | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKREFINANCIANRO` | varchar | 0% |
| 11 | `PKFACTURATPO` | varchar | 0% |
| 12 | `PKFACTURANRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `REFINANCIANRO` (int) → [[clave-REFINANCIANRO]]
- `FACTURATPO` (varchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (int) → [[clave-FACTURANRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKREFINANCIANRO` (varchar) → [[clave-PKREFINANCIANRO]]
- `PKFACTURATPO` (varchar) → [[clave-PKFACTURATPO]]
- `PKFACTURANRO` (varchar) → [[clave-PKFACTURANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
