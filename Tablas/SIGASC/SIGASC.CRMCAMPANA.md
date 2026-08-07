---
esquema: SIGASC
tabla: CRMCAMPANA
objeto: SIGASC.CRMCAMPANA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMCAMNRO` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMCAMPANA

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMCAMNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CRMCAMNRO` | int | 0% |
| 3 | `CRMCAMNOMBRE` | varchar | 0% |
| 4 | `CRMCAMACTIVA` | int | 0% |
| 5 | `CRMCAMFHINI` | datetime2 | 0% |
| 6 | `CRMCAMFHFIN` | datetime2 | 0% |
| 7 | `CRMCAMMEDIO` | varchar | 0% |
| 8 | `CRMCAMPRIORIDAD` | int | 8% |
| 9 | `CRMCAMUSRING` | varchar | 0% |
| 10 | `CRMCAMFHING` | datetime2 | 0% |
| 11 | `CRMCAMTPOID` | int | 0% |
| 12 | `PIPELINERUNID` | varchar | 0% |
| 13 | `PKCRMCAMNRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CRMCAMNRO` (int) → [[clave-CRMCAMNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMCAMNRO` (varchar) → [[clave-PKCRMCAMNRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
