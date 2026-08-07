---
esquema: SIGASC
tabla: CMSISTEMA
objeto: SIGASC.CMSISTEMA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CMSISTEMAID` (único en muestra de 8)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMSISTEMA

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CMSISTEMAID` (único en muestra de 8)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CMSISTEMAID` | int | 0% |
| 2 | `CMSISTEMANOMBRE` | varchar | 0% |
| 3 | `CMSISTEMAIP` | varchar | 0% |
| 4 | `CMSISTEMAPORT` | varchar | 0% |
| 5 | `CMSISTEMAUSR` | varchar | 0% |
| 6 | `CMSISTEMAPSW` | varchar | 0% |
| 7 | `CMEVEULT` | int | 0% |
| 8 | `CMSISTEMAAPROVEMI` | int | 0% |
| 9 | `CMSISTEMAUSAPRIORIDAD` | int | 38% |
| 10 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `CMSISTEMAID` (int) → [[clave-CMSISTEMAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
