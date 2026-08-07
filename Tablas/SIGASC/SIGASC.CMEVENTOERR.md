---
esquema: SIGASC
tabla: CMEVENTOERR
objeto: SIGASC.CMEVENTOERR
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CMEVEID` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMEVENTOERR

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CMEVEID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCMEVENTOERR` | varchar | 0% |
| 2 | `CMSISTEMAID` | int | 0% |
| 3 | `CMEVEID` | int | 0% |
| 4 | `CMERRFCH` | datetime2 | 0% |
| 5 | `CMERRCMD` | varchar | 0% |
| 6 | `CMERRENV` | varchar | 0% |
| 7 | `CMERRRET` | varchar | 0% |
| 8 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `CMSISTEMAID` (int) → [[clave-CMSISTEMAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
