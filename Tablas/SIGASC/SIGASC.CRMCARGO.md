---
esquema: SIGASC
tabla: CRMCARGO
objeto: SIGASC.CRMCARGO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMCARGOID` (único en muestra de 48)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMCARGO

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMCARGOID` (único en muestra de 48)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CRMCARGOID` | int | 0% |
| 3 | `CRMCARGONOMBRE` | varchar | 0% |
| 4 | `CRMMOTIVO1` | int | 0% |
| 5 | `CRMMOTIVO2` | int | 0% |
| 6 | `CRMMOTIVO3` | int | 0% |
| 7 | `CRMMOTIVO4` | int | 100% |
| 8 | `CRMRESULTADO` | int | 0% |
| 9 | `CPTOFACID` | int | 0% |
| 10 | `CRMCARGOCANTIDAD` | int | 0% |
| 11 | `MONEDAID` | int | 0% |
| 12 | `CRMCARGOPRECIO` | real | 0% |
| 13 | `PIPELINERUNID` | varchar | 0% |
| 14 | `PKCRMCARGOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `MONEDAID` (int) → [[clave-MONEDAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMCARGOID` (varchar) → [[clave-PKCRMCARGOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
