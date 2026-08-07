---
esquema: SIGASC
tabla: DECOSISTEMAPRDGRUPODECOSISTEMA
objeto: SIGASC.DECOSISTEMAPRDGRUPODECOSISTEMA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKDECOSISTEMAPRDGRUPODECOSISTEMA` (único en muestra de 87)
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECOSISTEMAPRDGRUPODECOSISTEMA

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKDECOSISTEMAPRDGRUPODECOSISTEMA` (único en muestra de 87)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKDECOSISTEMAPRDGRUPODECOSISTEMA` | varchar | 0% |
| 2 | `DECOSISID` | int | 0% |
| 3 | `DECOGRUPOCLAVE` | varchar | 0% |
| 4 | `DECOGRUPOPRDID` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `DECOSISID` (int) → [[clave-DECOSISID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
