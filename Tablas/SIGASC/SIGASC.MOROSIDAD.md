---
esquema: SIGASC
tabla: MOROSIDAD
objeto: SIGASC.MOROSIDAD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)
n_columnas: 23
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MOROSIDAD

> **BASE TABLE** · Dominio: **Core SIGA** · 23 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKMOROSIDAD` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `MOROSIDADMES` | int | 0% |
| 4 | `CLIENTENRO` | int | 0% |
| 5 | `MOROSIDADSTS` | varchar | 0% |
| 6 | `MOROSIDADUSR` | varchar | 0% |
| 7 | `MOROSIDADTPO` | varchar | 0% |
| 8 | `MOROSIDADCXLFCH` | datetime2 | 0% |
| 9 | `MOROSIDADCXLUSR` | varchar | 0% |
| 10 | `MOROSIDADCXLTPO` | varchar | 0% |
| 11 | `MOROSIDADCLASE` | varchar | 0% |
| 12 | `MOROSIDADCORTERNX` | datetime2 | 100% |
| 13 | `MOROSIDADCORTEFCH` | datetime2 | 100% |
| 14 | `MOROSIDADCORTESTS` | varchar | 0% |
| 15 | `MOROSIDADFCH` | datetime2 | 0% |
| 16 | `MOROSIDADGEN` | varchar | 0% |
| 17 | `MOROSIDADORDRECONEXION1` | int | 100% |
| 18 | `MOROSIDADORDCORTE2` | int | 100% |
| 19 | `MOROSIDADORDCORTE1` | int | 100% |
| 20 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 21 | `PIPELINERUNID` | varchar | 0% |
| 22 | `PKCLIENTENRO` | varchar | 0% |
| 23 | `PKMOROSIDADMES` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]
- `PKMOROSIDADMES` (varchar) → [[clave-PKMOROSIDADMES]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
