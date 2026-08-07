---
esquema: SIGASC
tabla: MEDIOCOBRORETORNO
objeto: SIGASC.MEDIOCOBRORETORNO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`MEDCOBRORETID`) — compuesto, tentativo (muestra 10)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MEDIOCOBRORETORNO

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`MEDCOBRORETID`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MEDCOBROID` | int | 0% |
| 2 | `MEDCOBRORETID` | varchar | 0% |
| 3 | `MEDCOBRORETNOMBRE` | varchar | 0% |
| 4 | `MEDCOBRORETSTS` | varchar | 0% |
| 5 | `MEDCOBRORETRESTRINGE` | int | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `MEDCOBROID` (int) → [[clave-MEDCOBROID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
