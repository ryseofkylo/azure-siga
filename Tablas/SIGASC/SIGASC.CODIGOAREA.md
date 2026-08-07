---
esquema: SIGASC
tabla: CODIGOAREA
objeto: SIGASC.CODIGOAREA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCODIGOAREA` (único en muestra de 46)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CODIGOAREA

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCODIGOAREA` (único en muestra de 46)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCODIGOAREA` | varchar | 0% |
| 2 | `PAISID` | int | 0% |
| 3 | `CIUDADID` | int | 0% |
| 4 | `GEODIV1ID` | int | 0% |
| 5 | `CODIGOAREAID` | varchar | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PAISID` (int) → [[clave-PAISID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
