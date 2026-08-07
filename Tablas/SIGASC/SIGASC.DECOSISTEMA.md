---
esquema: SIGASC
tabla: DECOSISTEMA
objeto: SIGASC.DECOSISTEMA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `DECOSISID` (único en muestra de 18)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECOSISTEMA

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `DECOSISID` (único en muestra de 18)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `DECOSISID` | int | 0% |
| 2 | `DECOSISNOMBRE` | varchar | 0% |
| 3 | `DECOSISTPO` | varchar | 0% |
| 4 | `DECOSISINI` | int | 0% |
| 5 | `DECOSISMSJ` | int | 0% |
| 6 | `DECOSISPPV` | int | 0% |
| 7 | `DECOSISIP` | varchar | 17% |
| 8 | `DECOSISPORT` | varchar | 17% |
| 9 | `DECOSISUSR` | varchar | 39% |
| 10 | `DECOSISPSW` | varchar | 44% |
| 11 | `DECOEVEULT` | int | 6% |
| 12 | `DECOSISNACION` | varchar | 94% |
| 13 | `DECOSISREGION` | varchar | 94% |
| 14 | `DECOSISEMPAREJAR` | int | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `DECOSISID` (int) → [[clave-DECOSISID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
