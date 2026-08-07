---
esquema: SIGASC
tabla: CLIENTESRVCAMBIO
objeto: SIGASC.CLIENTESRVCAMBIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: TODO (muestra vacía)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTESRVCAMBIO

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** TODO (muestra vacía)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCLIENTESRVCAMBIO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTESRVNRO` | int | 0% |
| 4 | `CLIENTESRVCAMBIOOLDCONTRATONRO` | int | 0% |
| 5 | `CLIENTESRVCAMBIONEWCONTRATONRO` | int | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKCLIENTESRVNRO` | varchar | 0% |
| 8 | `PKCLIENTESRVCAMBIOOLDCONTRATONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTESRVNRO` (int) → [[clave-CLIENTESRVNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTESRVNRO` (varchar) → [[clave-PKCLIENTESRVNRO]]
- `PKCLIENTESRVCAMBIOOLDCONTRATONRO` (varchar) → [[clave-PKCLIENTESRVCAMBIOOLDCONTRATONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
