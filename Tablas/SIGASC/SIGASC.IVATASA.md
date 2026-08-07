---
esquema: SIGASC
tabla: IVATASA
objeto: SIGASC.IVATASA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKIVATASA` (único en muestra de 45)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.IVATASA

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKIVATASA` (único en muestra de 45)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKIVATASA` | varchar | 0% |
| 2 | `IVAID` | int | 0% |
| 3 | `CONDICIONIVA` | int | 0% |
| 4 | `IVAFCH` | datetime2 | 0% |
| 5 | `IVAPRJ` | real | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `IVAID` (int) → [[clave-IVAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
