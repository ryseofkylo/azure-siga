---
esquema: SIGASC
tabla: ORDENSRVARTICULO
objeto: SIGASC.ORDENSRVARTICULO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKORDENNRO` (único en muestra de 200)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ORDENSRVARTICULO

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKORDENNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKORDENSRVARTICULO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `ORDENNRO` | int | 0% |
| 4 | `ORDENARTLIN` | int | 0% |
| 5 | `ARTICULOID` | int | 0% |
| 6 | `ORDENARTSERIE` | varchar | 0% |
| 7 | `ORDENARTUNIDAD` | varchar | 0% |
| 8 | `ORDENARTVALORINI` | real | 0% |
| 9 | `ORDENARTMODO` | varchar | 0% |
| 10 | `ORDENARTCANTIDAD` | real | 0% |
| 11 | `ORDENARTSAPCONFIRMADO` | int | 100% |
| 12 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 13 | `PIPELINERUNID` | varchar | 0% |
| 14 | `PKORDENNRO` | varchar | 0% |
| 15 | `PKORDENARTLIN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ORDENNRO` (int) → [[clave-ORDENNRO]]
- `ARTICULOID` (int) → [[clave-ARTICULOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKORDENNRO` (varchar) → [[clave-PKORDENNRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
