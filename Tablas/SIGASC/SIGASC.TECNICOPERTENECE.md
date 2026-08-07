---
esquema: SIGASC
tabla: TECNICOPERTENECE
objeto: SIGASC.TECNICOPERTENECE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `TECNICOPERTENECEID` (único en muestra de 6)
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.TECNICOPERTENECE

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `TECNICOPERTENECEID` (único en muestra de 6)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `TECNICOPERTENECEID` | int | 0% |
| 2 | `TECNICOPERTENECENOMBRE` | varchar | 0% |
| 3 | `TECNICOPERTENECEACTIVO` | varchar | 0% |
| 4 | `TECNICOPERTENECECONTRATADO` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
