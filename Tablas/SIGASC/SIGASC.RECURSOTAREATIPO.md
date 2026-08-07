---
esquema: SIGASC
tabla: RECURSOTAREATIPO
objeto: SIGASC.RECURSOTAREATIPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKRECURSOTAREATIPO` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.RECURSOTAREATIPO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKRECURSOTAREATIPO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKRECURSOTAREATIPO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `RECURSOID` | int | 0% |
| 4 | `TAREATIPOID` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKRECURSOID` | varchar | 0% |
| 7 | `PKTAREATIPOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `RECURSOID` (int) → [[clave-RECURSOID]]
- `TAREATIPOID` (int) → [[clave-TAREATIPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKRECURSOID` (varchar) → [[clave-PKRECURSOID]]
- `PKTAREATIPOID` (varchar) → [[clave-PKTAREATIPOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
