---
esquema: SIGASC
tabla: CMSISTEMAEMP
objeto: SIGASC.CMSISTEMAEMP
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKARTICULOIDCM` (único en muestra de 190)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMSISTEMAEMP

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKARTICULOIDCM` (único en muestra de 190)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCMSISTEMAEMP` | varchar | 0% |
| 2 | `CMSISTEMAID` | int | 0% |
| 3 | `EMPRESAID` | int | 0% |
| 4 | `ARTICULOIDCM` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKCMSISTEMAID` | varchar | 0% |
| 7 | `PKARTICULOIDCM` | varchar | 0% |

## Claves de join presentes
- `CMSISTEMAID` (int) → [[clave-CMSISTEMAID]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCMSISTEMAID` (varchar) → [[clave-PKCMSISTEMAID]]
- `PKARTICULOIDCM` (varchar) → [[clave-PKARTICULOIDCM]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
