---
esquema: SIGASC
tabla: CLIENTETEL_OPT
objeto: SIGASC.CLIENTETEL_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PK_CLIENTETEL` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTETEL_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PK_CLIENTETEL` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PK_CLIENTETEL` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | varchar | 0% |
| 4 | `CLIENTETEL` | varchar | 0% |
| 5 | `CLIENTETELTPO` | varchar | 0% |
| 6 | `CLIENTETELREF` | int | 0% |
| 7 | `CLIENTETELPERS` | varchar | 0% |
| 8 | `CLIENTETELCONT` | varchar | 96% |
| 9 | `CLIENTETELNUM` | int | 94% |
| 10 | `CLIENTETELWHATSAPP` | int | 0% |
| 11 | `CLIENTETELCARACT` | int | 94% |
| 12 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 13 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
