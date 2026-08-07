---
esquema: SIGASC
tabla: HISTORICOENTIDAD
objeto: SIGASC.HISTORICOENTIDAD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`EMPRESAID`, `HSTENTIDADID`) — compuesto, tentativo (muestra 10)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.HISTORICOENTIDAD

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`EMPRESAID`, `HSTENTIDADID`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `HSTENTIDADID` | varchar | 0% |
| 3 | `HSTENTIDADPKATT` | varchar | 0% |
| 4 | `HSTENTIDADSTS` | varchar | 0% |
| 5 | `HSTENTIDADFCHALTA` | datetime2 | 0% |
| 6 | `HSTENTIDADUSRALTA` | varchar | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
