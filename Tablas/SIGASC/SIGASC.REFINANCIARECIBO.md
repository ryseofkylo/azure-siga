---
esquema: SIGASC
tabla: REFINANCIARECIBO
objeto: SIGASC.REFINANCIARECIBO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.REFINANCIARECIBO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKREFINANCIARECIBO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `REFINANCIANRO` | int | 0% |
| 4 | `RECIBONRO` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKREFINANCIANRO` | varchar | 0% |
| 7 | `PKRECIBONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `REFINANCIANRO` (int) → [[clave-REFINANCIANRO]]
- `RECIBONRO` (int) → [[clave-RECIBONRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKREFINANCIANRO` (varchar) → [[clave-PKREFINANCIANRO]]
- `PKRECIBONRO` (varchar) → [[clave-PKRECIBONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
