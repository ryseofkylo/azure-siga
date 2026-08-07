---
esquema: SIGASC
tabla: MANZANACALLE
objeto: SIGASC.MANZANACALLE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `MANZANACALLEGISID` (único en muestra de 200)
n_columnas: 22
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MANZANACALLE

> **BASE TABLE** · Dominio: **Core SIGA** · 22 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `MANZANACALLEGISID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKMANZANACALLE` | varchar | 0% |
| 2 | `PAISID` | int | 0% |
| 3 | `CIUDADID` | int | 0% |
| 4 | `GEODIV1ID` | int | 0% |
| 5 | `GEODIV2ID` | int | 0% |
| 6 | `GEOMANID` | int | 0% |
| 7 | `CALLEID` | int | 0% |
| 8 | `GEOMANINI` | varchar | 0% |
| 9 | `GEOMANFIN` | varchar | 0% |
| 10 | `GEOMANPARIDAD` | varchar | 0% |
| 11 | `GEOMANCALLECORDX1` | varchar | 0% |
| 12 | `GEOMANCALLECORDY1` | varchar | 0% |
| 13 | `GEOMANCALLECORDX2` | varchar | 0% |
| 14 | `GEOMANCALLECORDY2` | varchar | 0% |
| 15 | `GEOMANHOMEPASS` | int | 100% |
| 16 | `GEOMANCANTHOG` | int | 88% |
| 17 | `MANZANACALLEFCHACTUALIZACION` | datetime2 | 0% |
| 18 | `MANZANACALLEGISID` | int | 0% |
| 19 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 20 | `MANZANACALLEESGENERICO` | int | 98% |
| 21 | `MANZANACALLESTS` | varchar | 0% |
| 22 | `PIPELINERUNID` | varchar | 0% |

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
