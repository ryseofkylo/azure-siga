---
esquema: SIGASC
tabla: CRMPROGRAMA
objeto: SIGASC.CRMPROGRAMA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CRMPROGRAMAID` (único en muestra de 10)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMPROGRAMA

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CRMPROGRAMAID` (único en muestra de 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CRMPROGRAMAID` | varchar | 0% |
| 2 | `CRMPROGRAMANOMBRE` | varchar | 0% |
| 3 | `CRMPROGRAMAOBJETO` | varchar | 0% |
| 4 | `CRMPROGRAMAPARAMETROS` | varchar | 0% |
| 5 | `CRMPROGRAMATIPO` | varchar | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
