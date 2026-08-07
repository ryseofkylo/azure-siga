---
esquema: SIGASC
tabla: CLIENTETEL
objeto: SIGASC.CLIENTETEL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTETEL

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCLIENTETEL` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `CLIENTETEL` | varchar | 0% |
| 5 | `CLIENTETELTPO` | varchar | 0% |
| 6 | `CLIENTETELREF` | int | 0% |
| 7 | `CLIENTETELPERS` | varchar | 0% |
| 8 | `CLIENTETELCONT` | varchar | 2% |
| 9 | `CLIENTETELNUM` | int | 2% |
| 10 | `CLIENTETELWHATSAPP` | int | 0% |
| 11 | `CLIENTETELCARACT` | int | 2% |
| 12 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 13 | `PIPELINERUNID` | varchar | 0% |
| 14 | `PKCLIENTENRO` | varchar | 0% |
| 15 | `PKCLIENTETEL` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
