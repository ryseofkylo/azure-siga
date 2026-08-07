---
esquema: SIGASC
tabla: TAREA
objeto: SIGASC.TAREA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `TAREAID` (único en muestra de 200)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.TAREA

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `TAREAID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `TAREAID` | int | 0% |
| 2 | `TAREANOMBRE` | varchar | 0% |
| 3 | `TAREATIPOID` | int | 0% |
| 4 | `TAREACAPACIDADEST` | real | 0% |
| 5 | `TAREACAPACIDADSIM` | real | 0% |
| 6 | `TAREAENTIDAD` | varchar | 0% |
| 7 | `TAREAPONDERACION` | int | 5% |
| 8 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `TAREAID` (int) → [[clave-TAREAID]]
- `TAREATIPOID` (int) → [[clave-TAREATIPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
