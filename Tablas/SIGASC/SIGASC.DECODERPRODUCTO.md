---
esquema: SIGASC
tabla: DECODERPRODUCTO
objeto: SIGASC.DECODERPRODUCTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKDECODERPRODUCTO` (único en muestra de 200)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECODERPRODUCTO

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKDECODERPRODUCTO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKDECODERPRODUCTO` | varchar | 0% |
| 2 | `DECOSISID` | int | 0% |
| 3 | `DECODERID` | varchar | 0% |
| 4 | `DECOPRDID` | int | 0% |
| 5 | `DECOPRDING` | varchar | 0% |
| 6 | `DECOPRDUSR` | varchar | 0% |
| 7 | `DECOPRDOBS` | varchar | 9% |
| 8 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `DECOSISID` (int) → [[clave-DECOSISID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
