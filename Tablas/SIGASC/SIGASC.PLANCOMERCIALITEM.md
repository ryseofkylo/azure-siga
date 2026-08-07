---
esquema: SIGASC
tabla: PLANCOMERCIALITEM
objeto: SIGASC.PLANCOMERCIALITEM
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPLANCOMERCIALITEM` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PLANCOMERCIALITEM

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPLANCOMERCIALITEM` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPLANCOMERCIALITEM` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PLANCOMERCIALID` | int | 0% |
| 4 | `PLANCOMERCIALITEM` | int | 0% |
| 5 | `PLANCOMERCIALITEMDESCRIPCION` | varchar | 0% |
| 6 | `PLANCOMERCIALITEMORDEN` | int | 0% |
| 7 | `PLANCOMERCIALITEMMAXIMO` | int | 0% |
| 8 | `PLANCOMERCIALITEMMINIMO` | int | 0% |
| 9 | `PLANCOMERCIALITEMOBLIGATORIO` | int | 0% |
| 10 | `PLANCOMERCIALITEMESADICIONAL` | int | 0% |
| 11 | `PLANCOMERCIALITEMPADRE` | int | 0% |
| 12 | `PIPELINERUNID` | varchar | 0% |
| 13 | `PKPLANCOMERCIALID` | varchar | 0% |
| 14 | `PKPLANCOMERCIALITEM` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PLANCOMERCIALID` (int) → [[clave-PLANCOMERCIALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPLANCOMERCIALID` (varchar) → [[clave-PKPLANCOMERCIALID]]
- `PKPLANCOMERCIALITEM` (varchar) → [[clave-PKPLANCOMERCIALITEM]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
