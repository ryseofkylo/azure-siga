---
esquema: SIGASC
tabla: CRMCARGOPROCESO
objeto: SIGASC.CRMCARGOPROCESO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCRMCARGOPROCESO` (único en muestra de 20)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMCARGOPROCESO

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCRMCARGOPROCESO` (único en muestra de 20)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCRMCARGOPROCESO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CRMCARGOID` | int | 0% |
| 4 | `CRMCARGOFINI` | datetime2 | 0% |
| 5 | `CRMCARGOFFIN` | datetime2 | 0% |
| 6 | `CRMCARGOUSR` | varchar | 0% |
| 7 | `CRMCARGOFHORA` | datetime2 | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKCRMCARGOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMCARGOID` (varchar) → [[clave-PKCRMCARGOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
