---
esquema: SIGASC
tabla: PUNTOVENTA
objeto: SIGASC.PUNTOVENTA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PUNTOVTANOMBRE` (único en muestra de 200)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PUNTOVENTA

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PUNTOVTANOMBRE` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAFISCALID` | int | 0% |
| 2 | `PUNTOVTAID` | int | 0% |
| 3 | `PUNTOVTANOMBRE` | varchar | 0% |
| 4 | `PUNTOVTATPO` | varchar | 0% |
| 5 | `PUNTOVTAMODO` | varchar | 0% |
| 6 | `PUNTOVTACAJA` | int | 0% |
| 7 | `PUNTOVTASTS` | varchar | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAFISCALID` (int) → [[clave-EMPRESAFISCALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
