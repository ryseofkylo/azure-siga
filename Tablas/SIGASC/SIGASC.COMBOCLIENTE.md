---
esquema: SIGASC
tabla: COMBOCLIENTE
objeto: SIGASC.COMBOCLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCOMBOCLIENTENRO` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COMBOCLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCOMBOCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCOMBOCLIENTE` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `COMBOCLIENTENRO` | int | 0% |
| 5 | `COMBOID` | int | 0% |
| 6 | `COMBOCLIENTEFCHING` | datetime2 | 0% |
| 7 | `COMBOCLIENTEFCHFIN` | datetime2 | 8% |
| 8 | `COMBOCLIENTEUSR` | varchar | 0% |
| 9 | `COMBOCLIENTESTS` | varchar | 0% |
| 10 | `COMBOCLIENTEFAC` | int | 0% |
| 11 | `PIPELINERUNID` | varchar | 0% |
| 12 | `PKCLIENTENRO` | varchar | 0% |
| 13 | `PKCOMBOCLIENTENRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `COMBOID` (int) → [[clave-COMBOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]
- `PKCOMBOCLIENTENRO` (varchar) → [[clave-PKCOMBOCLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
