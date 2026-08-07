---
esquema: SIGASC
tabla: PRODUCTOCMPRD
objeto: SIGASC.PRODUCTOCMPRD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPRODUCTOCMPRD` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTOCMPRD

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPRODUCTOCMPRD` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPRODUCTOCMPRD` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PRODUCTOID` | int | 0% |
| 4 | `CMSISTEMAID` | int | 0% |
| 5 | `CMPRDID` | int | 0% |
| 6 | `PRODUCTOCMCONTV` | int | 0% |
| 7 | `PRODUCTOCMCONTEL` | int | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKPRODUCTOID` | varchar | 0% |
| 10 | `PKCMSISTEMAID` | varchar | 0% |
| 11 | `PKCMPRDID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `CMSISTEMAID` (int) → [[clave-CMSISTEMAID]]
- `CMPRDID` (int) → [[clave-CMPRDID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]
- `PKCMSISTEMAID` (varchar) → [[clave-PKCMSISTEMAID]]
- `PKCMPRDID` (varchar) → [[clave-PKCMPRDID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
