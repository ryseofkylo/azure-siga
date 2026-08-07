---
esquema: SIGASC
tabla: CODIGOPOSTAL
objeto: SIGASC.CODIGOPOSTAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCODIGOPOSTAL` (único en muestra de 200)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CODIGOPOSTAL

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCODIGOPOSTAL` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCODIGOPOSTAL` | varchar | 0% |
| 2 | `PAISID` | int | 0% |
| 3 | `CIUDADID` | int | 0% |
| 4 | `CODIGOPOSTAL` | varchar | 0% |
| 5 | `GEODIV1ID` | int | 0% |
| 6 | `GEODIV2ID` | int | 0% |
| 7 | `CODIGOPOSTALNOMBRE` | varchar | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PAISID` (int) → [[clave-PAISID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
