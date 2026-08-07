---
esquema: SIGASC
tabla: CRMAVISO
objeto: SIGASC.CRMAVISO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKAVISONRO` (único en muestra de 9)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMAVISO

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKAVISONRO` (único en muestra de 9)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `AVISONRO` | int | 0% |
| 3 | `AVISONOMBRE` | varchar | 0% |
| 4 | `AVISOTPO` | varchar | 0% |
| 5 | `AVISOFCHING` | datetime2 | 0% |
| 6 | `AVISOUSR` | varchar | 0% |
| 7 | `AVISOFHINI` | datetime2 | 0% |
| 8 | `AVISOFHFIN` | datetime2 | 11% |
| 9 | `AVISOSTS` | varchar | 0% |
| 10 | `AVISOOBS` | varchar | 0% |
| 11 | `CLIENTENRO` | int | 56% |
| 12 | `AVISOPOPUP` | int | 22% |
| 13 | `PIPELINERUNID` | varchar | 0% |
| 14 | `PKAVISONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
