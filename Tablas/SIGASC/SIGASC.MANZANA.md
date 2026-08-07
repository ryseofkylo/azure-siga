---
esquema: SIGASC
tabla: MANZANA
objeto: SIGASC.MANZANA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `MANZANAGISID` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MANZANA

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `MANZANAGISID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKMANZANA` | varchar | 0% |
| 2 | `PAISID` | int | 0% |
| 3 | `CIUDADID` | int | 0% |
| 4 | `GEODIV1ID` | int | 0% |
| 5 | `GEODIV2ID` | int | 0% |
| 6 | `GEOMANID` | int | 0% |
| 7 | `GEOMANNOMBRE` | varchar | 0% |
| 8 | `GEOMANHOG` | int | 0% |
| 9 | `GEOMANCORDX` | varchar | 0% |
| 10 | `GEOMANCORDY` | varchar | 0% |
| 11 | `MANZANAFCHACTUALIZACION` | datetime2 | 0% |
| 12 | `MANZANAGISID` | int | 0% |
| 13 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 14 | `MANZANAESGENERICO` | int | 0% |
| 15 | `MANZANASTS` | varchar | 0% |
| 16 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PAISID` (int) → [[clave-PAISID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]
- `GEOMANID` (int) → [[clave-GEOMANID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
