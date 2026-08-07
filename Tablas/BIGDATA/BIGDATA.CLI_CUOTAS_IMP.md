---
esquema: BIGDATA
tabla: CLI_CUOTAS_IMP
objeto: BIGDATA.CLI_CUOTAS_IMP
tipo_objeto: BASE TABLE
dominio: Big Data
canonico: true
grain: 1 fila = 1 `SKCLI_CUOTAS_IMP` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/BIGDATA
  - dominio/big-data
  - tipo/tabla-base
  - canonico
---

# BIGDATA.CLI_CUOTAS_IMP

> **BASE TABLE** · Dominio: **Big Data** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCLI_CUOTAS_IMP` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCLI_CUOTAS_IMP` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `CUOTA_CABLE` | int | 0% |
| 5 | `CUOTA_INT` | int | 0% |
| 6 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |

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
