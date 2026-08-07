---
esquema: SIGASC
tabla: PRESUPUESTO
objeto: SIGASC.PRESUPUESTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPRESUPUESTO` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRESUPUESTO

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPRESUPUESTO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPRESUPUESTO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PERIODO` | int | 0% |
| 4 | `ANIO` | int | 0% |
| 5 | `MES` | int | 0% |
| 6 | `INDICADOR` | varchar | 0% |
| 7 | `VALOR` | int | 0% |
| 8 | `ZONAGEOGRAFICA` | varchar | 64% |
| 9 | `BDMODIFIEDDATE` | datetime2 | 90% |
| 10 | `PIPELINERUNID` | varchar | 0% |
| 11 | `PKPERIODO` | varchar | 0% |
| 12 | `PKINDICADOR` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
