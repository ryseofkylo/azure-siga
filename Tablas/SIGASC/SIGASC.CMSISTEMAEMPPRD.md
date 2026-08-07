---
esquema: SIGASC
tabla: CMSISTEMAEMPPRD
objeto: SIGASC.CMSISTEMAEMPPRD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCMSISTEMAEMPPRD` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMSISTEMAEMPPRD

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCMSISTEMAEMPPRD` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCMSISTEMAEMPPRD` | varchar | 0% |
| 2 | `CMSISTEMAID` | int | 0% |
| 3 | `EMPRESAID` | int | 0% |
| 4 | `ARTICULOIDCM` | int | 0% |
| 5 | `CMPRDID` | int | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKCMSISTEMAID` | varchar | 0% |
| 8 | `PKARTICULOIDCM` | varchar | 0% |
| 9 | `PKCMPRDID` | varchar | 0% |

## Claves de join presentes
- `CMSISTEMAID` (int) → [[clave-CMSISTEMAID]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CMPRDID` (int) → [[clave-CMPRDID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCMSISTEMAID` (varchar) → [[clave-PKCMSISTEMAID]]
- `PKARTICULOIDCM` (varchar) → [[clave-PKARTICULOIDCM]]
- `PKCMPRDID` (varchar) → [[clave-PKCMPRDID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
