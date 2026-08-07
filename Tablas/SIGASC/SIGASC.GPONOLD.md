---
esquema: SIGASC
tabla: GPONOLD
objeto: SIGASC.GPONOLD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKGPONOLDID` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.GPONOLD

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKGPONOLDID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `GPONOLDID` | int | 0% |
| 3 | `GPONOLDNOMBRE` | varchar | 0% |
| 4 | `GPONOLTID` | int | 0% |
| 5 | `GPONOLDZONAID` | int | 8% |
| 6 | `GPONOLDFCHACTUALIZACION` | datetime2 | 0% |
| 7 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKGPONOLDID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
