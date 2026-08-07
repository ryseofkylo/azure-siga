---
esquema: SIGASC
tabla: CRMCAMPANAGRUPO
objeto: SIGASC.CRMCAMPANAGRUPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMCAMNRO` (único en muestra de 5)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMCAMPANAGRUPO

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMCAMNRO` (único en muestra de 5)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCRMCAMPANAGRUPO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CRMCAMNRO` | int | 0% |
| 4 | `CRMGPOUSR` | int | 0% |
| 5 | `CRMCAMGPOINCEXC` | varchar | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKCRMCAMNRO` | varchar | 0% |
| 8 | `PKCRMGPOUSR` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CRMCAMNRO` (int) → [[clave-CRMCAMNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMCAMNRO` (varchar) → [[clave-PKCRMCAMNRO]]
- `PKCRMGPOUSR` (varchar) → [[clave-PKCRMGPOUSR]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
