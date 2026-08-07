---
esquema: SIGASC
tabla: PREVENTACONDICION
objeto: SIGASC.PREVENTACONDICION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPREVENTACONDID` (único en muestra de 129)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTACONDICION

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPREVENTACONDID` (único en muestra de 129)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PREVENTACONDID` | int | 0% |
| 3 | `PREVENTACONDNOM` | varchar | 0% |
| 4 | `PREVENTACONDTPO` | varchar | 0% |
| 5 | `PREVENTACONDVALIDA` | varchar | 0% |
| 6 | `PREVENTACONDPGM` | varchar | 0% |
| 7 | `PREVENTACONDRESTRINGE` | int | 0% |
| 8 | `PREVENTACONDPGMDIR` | varchar | 0% |
| 9 | `PREVENTACONDSTS` | varchar | 0% |
| 10 | `PREVENTACONDSTSCLI` | varchar | 0% |
| 11 | `PIPELINERUNID` | varchar | 0% |
| 12 | `PKPREVENTACONDID` | varchar | 0% |

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
