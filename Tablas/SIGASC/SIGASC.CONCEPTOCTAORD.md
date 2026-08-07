---
esquema: SIGASC
tabla: CONCEPTOCTAORD
objeto: SIGASC.CONCEPTOCTAORD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCPTOFACGRUPOID` (único en muestra de 12)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CONCEPTOCTAORD

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCPTOFACGRUPOID` (único en muestra de 12)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAFISCALID` | int | 0% |
| 2 | `CPTOFACGRUPOID` | int | 0% |
| 3 | `CONCEPTOACTAORDENID` | int | 0% |
| 4 | `CONCEPTOACTAORDENSKEELO` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKCPTOFACGRUPOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAFISCALID` (int) → [[clave-EMPRESAFISCALID]]
- `CPTOFACGRUPOID` (int) → [[clave-CPTOFACGRUPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
