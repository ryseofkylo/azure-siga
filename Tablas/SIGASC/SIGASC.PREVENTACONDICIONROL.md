---
esquema: SIGASC
tabla: PREVENTACONDICIONROL
objeto: SIGASC.PREVENTACONDICIONROL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPREVENTACONDICIONROL` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTACONDICIONROL

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPREVENTACONDICIONROL` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTACONDICIONROL` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTACONDID` | int | 0% |
| 4 | `APLICACIONID` | varchar | 0% |
| 5 | `ROLID` | varchar | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKPREVENTACONDID` | varchar | 0% |
| 8 | `PKAPLICACIONID` | varchar | 0% |
| 9 | `PKROLID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTACONDID` (int) → [[clave-PREVENTACONDID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTACONDID` (varchar) → [[clave-PKPREVENTACONDID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
