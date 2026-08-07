---
esquema: SIGASC
tabla: CLIENTESERVICIOORD_OPT_changed
objeto: SIGASC.CLIENTESERVICIOORD_OPT_changed
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PK_CLIENTESERVICIOORD` (único en muestra de 200)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTESERVICIOORD_OPT_changed

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PK_CLIENTESERVICIOORD` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PK_CLIENTESERVICIOORD` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTESRVNRO` | varchar | 0% |
| 4 | `CLIENTESRVGENORDEN` | varchar | 0% |
| 5 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PK_CLIENTESERVICIOORD` (varchar) → [[clave-PK_CLIENTESERVICIOORD]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTESRVNRO` (varchar) → [[clave-CLIENTESRVNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
