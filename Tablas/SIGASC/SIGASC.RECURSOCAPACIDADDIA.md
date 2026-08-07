---
esquema: SIGASC
tabla: RECURSOCAPACIDADDIA
objeto: SIGASC.RECURSOCAPACIDADDIA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKRECURSOCAPACIDADDIA` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.RECURSOCAPACIDADDIA

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKRECURSOCAPACIDADDIA` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKRECURSOCAPACIDADDIA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `RECURSOID` | int | 0% |
| 4 | `RECURSODIA` | varchar | 0% |
| 5 | `RECURSOHORAINI` | datetime2 | 100% |
| 6 | `RECURSOHORAFIN` | datetime2 | 100% |
| 7 | `PIPELINERUNID` | varchar | 0% |
| 8 | `PKRECURSOID` | varchar | 0% |
| 9 | `PKRECURSODIA` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `RECURSOID` (int) → [[clave-RECURSOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKRECURSOID` (varchar) → [[clave-PKRECURSOID]]
- `PKRECURSODIA` (varchar) → [[clave-PKRECURSODIA]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
