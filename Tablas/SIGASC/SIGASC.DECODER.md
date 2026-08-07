---
esquema: SIGASC
tabla: DECODER
objeto: SIGASC.DECODER
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `DECODERID` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECODER

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `DECODERID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `DECOSISID` | int | 0% |
| 2 | `DECODERID` | varchar | 0% |
| 3 | `DECODERHAB` | int | 0% |
| 4 | `DECODERSTS` | varchar | 0% |
| 5 | `DECODERFING` | datetime2 | 0% |
| 6 | `DECODERFHAB` | datetime2 | 84% |
| 7 | `DECODERPIN` | int | 8% |
| 8 | `EMPRESAID` | int | 0% |
| 9 | `ARTICULOID` | int | 0% |
| 10 | `DECODERPAREJASERIE` | varchar | 32% |
| 11 | `DECODERPAREJAARTICULOID` | int | 30% |
| 12 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `DECOSISID` (int) → [[clave-DECOSISID]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ARTICULOID` (int) → [[clave-ARTICULOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
