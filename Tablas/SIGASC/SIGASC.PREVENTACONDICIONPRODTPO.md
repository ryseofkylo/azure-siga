---
esquema: SIGASC
tabla: PREVENTACONDICIONPRODTPO
objeto: SIGASC.PREVENTACONDICIONPRODTPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPRODUCTOTPO` (único en muestra de 48)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTACONDICIONPRODTPO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPRODUCTOTPO` (único en muestra de 48)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTACONDICIONPRODTPO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTACONDID` | int | 0% |
| 4 | `PRODUCTOTPO` | varchar | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKPREVENTACONDID` | varchar | 0% |
| 7 | `PKPRODUCTOTPO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTACONDID` (int) → [[clave-PREVENTACONDID]]
- `PRODUCTOTPO` (varchar) → [[clave-PRODUCTOTPO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTACONDID` (varchar) → [[clave-PKPREVENTACONDID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
