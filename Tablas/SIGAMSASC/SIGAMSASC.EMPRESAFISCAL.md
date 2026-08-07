---
esquema: SIGAMSASC
tabla: EMPRESAFISCAL
objeto: SIGAMSASC.EMPRESAFISCAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `EMPRESAFISCALID` (único en muestra de 24)
n_columnas: 11
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.EMPRESAFISCAL

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `EMPRESAFISCALID` (único en muestra de 24)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAFISCALID` | int | 0% |
| 2 | `EMPRESAFISCALNOMBRE` | varchar | 0% |
| 3 | `EMPRESAFISCALNOMBREFANTASIA` | varchar | 0% |
| 4 | `EMPRESAFISCALRUT` | varchar | 0% |
| 5 | `EMPRESAFISCALDIRECCION` | varchar | 0% |
| 6 | `EMPRESAFISCALCODIGOPOSTAL` | varchar | 50% |
| 7 | `EMPRESAFISCALCVU` | varchar | 54% |
| 8 | `EMPRESAFISCALMCC` | varchar | 50% |
| 9 | `EMPRESAFISCALLOCALIDAD` | varchar | 54% |
| 10 | `EMPRESAFISCALNOMABV` | varchar | 25% |
| 11 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAFISCALID` (int) → [[clave-EMPRESAFISCALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
