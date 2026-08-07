---
esquema: SIGASC
tabla: URN
objeto: SIGASC.URN
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `URNID` (único en muestra de 49)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.URN

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `URNID` (único en muestra de 49)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `URNID` | int | 0% |
| 2 | `URNVAL` | varchar | 0% |
| 3 | `URNDESCRIPCION` | varchar | 0% |
| 4 | `URNTIEMPOLOG` | int | 100% |
| 5 | `URNMENSAJE02` | varchar | 0% |
| 6 | `URNMENSAJE01` | varchar | 0% |
| 7 | `URNVIDEO` | varchar | 94% |
| 8 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
