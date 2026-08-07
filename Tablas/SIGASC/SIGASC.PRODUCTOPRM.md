---
esquema: SIGASC
tabla: PRODUCTOPRM
objeto: SIGASC.PRODUCTOPRM
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPRODUCTOPRM` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTOPRM

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPRODUCTOPRM` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPRODUCTOPRM` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PRODUCTOID` | int | 0% |
| 4 | `POLITICAID` | int | 0% |
| 5 | `PROMOCIONID` | int | 0% |
| 6 | `PROMOCIONPRIORIDAD` | int | 0% |
| 7 | `PROMOCIONACTIVAENCARTELERA` | int | 96% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKPRODUCTOID` | varchar | 0% |
| 10 | `PKPOLITICAID` | varchar | 0% |
| 11 | `PKPROMOCIONID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PROMOCIONID` (int) → [[clave-PROMOCIONID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]
- `PKPOLITICAID` (varchar) → [[clave-PKPOLITICAID]]
- `PKPROMOCIONID` (varchar) → [[clave-PKPROMOCIONID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
