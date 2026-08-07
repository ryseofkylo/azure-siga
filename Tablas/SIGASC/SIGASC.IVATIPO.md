---
esquema: SIGASC
tabla: IVATIPO
objeto: SIGASC.IVATIPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `IVAID` (único en muestra de 9)
n_columnas: 3
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.IVATIPO

> **BASE TABLE** · Dominio: **Core SIGA** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `IVAID` (único en muestra de 9)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `IVAID` | int | 0% |
| 2 | `IVANOMBRE` | varchar | 0% |
| 3 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `IVAID` (int) → [[clave-IVAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
