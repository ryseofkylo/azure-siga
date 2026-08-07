---
esquema: SIGASC
tabla: PRODUCTOURN
objeto: SIGASC.PRODUCTOURN
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPRODUCTOURN` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTOURN

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPRODUCTOURN` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPRODUCTOURN` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PRODUCTOID` | int | 0% |
| 4 | `URNID` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKPRODUCTOID` | varchar | 0% |
| 7 | `PKURNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
