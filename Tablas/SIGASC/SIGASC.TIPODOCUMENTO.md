---
esquema: SIGASC
tabla: TIPODOCUMENTO
objeto: SIGASC.TIPODOCUMENTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTECITPO` (único en muestra de 11)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.TIPODOCUMENTO

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTECITPO` (único en muestra de 11)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTECITPO` | varchar | 0% |
| 2 | `CLIENTECITPONOMBRE` | varchar | 0% |
| 3 | `CLIENTECITPOVALPRG` | varchar | 0% |
| 4 | `AFIPCLIENTECITPO` | int | 0% |
| 5 | `CLIENTECITPOEXTRANJERO` | int | 0% |
| 6 | `CLIENTECITPOEXPRESION` | varchar | 0% |
| 7 | `CLIENTECITPOMASCARA` | varchar | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
