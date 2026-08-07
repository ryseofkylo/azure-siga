---
esquema: SIGASC
tabla: MOROSIDADCONTRATO
objeto: SIGASC.MOROSIDADCONTRATO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKMOROSIDADMESCONTRATO` (único en muestra de 200)
n_columnas: 20
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MOROSIDADCONTRATO

> **BASE TABLE** · Dominio: **Core SIGA** · 20 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKMOROSIDADMESCONTRATO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKMOROSIDADCONTRATO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `MOROSIDADMES` | int | 0% |
| 4 | `CLIENTENRO` | int | 0% |
| 5 | `MOROSIDADMESCONTRATO` | int | 0% |
| 6 | `MOROSIDADMESORDEN` | int | 0% |
| 7 | `MOROSIDADMESCONCORTERNX` | datetime2 | 100% |
| 8 | `MOROSIDADMESCONCORTEFCH` | datetime2 | 100% |
| 9 | `MOROSIDADMESCONCORTEUSR` | varchar | 0% |
| 10 | `MOROSIDADMESCONCORTESTS` | varchar | 0% |
| 11 | `MOROSIDADMESCONCORTE` | int | 0% |
| 12 | `MOROSIDADMESCONTRATOFCH` | datetime2 | 0% |
| 13 | `MOROSIDADMESCONTRATOTPO` | varchar | 0% |
| 14 | `MOROSIDADMESCONCORTERNXUSR` | varchar | 0% |
| 15 | `MOROSIDADMESGEN` | varchar | 0% |
| 16 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 17 | `PIPELINERUNID` | varchar | 0% |
| 18 | `PKMOROSIDADMES` | varchar | 0% |
| 19 | `PKCLIENTENRO` | varchar | 0% |
| 20 | `PKMOROSIDADMESCONTRATO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKMOROSIDADMES` (varchar) → [[clave-PKMOROSIDADMES]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
