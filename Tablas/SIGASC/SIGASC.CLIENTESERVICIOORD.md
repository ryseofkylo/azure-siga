---
esquema: SIGASC
tabla: CLIENTESERVICIOORD
objeto: SIGASC.CLIENTESERVICIOORD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTESRVNRO` (único en muestra de 200)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTESERVICIOORD

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTESRVNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCLIENTESERVICIOORD` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTESRVNRO` | int | 0% |
| 4 | `CLIENTESRVGENORDEN` | int | 0% |
| 5 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKCLIENTESRVNRO` | varchar | 0% |
| 8 | `PKCLIENTESRVGENORDEN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTESRVNRO` (int) → [[clave-CLIENTESRVNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTESRVNRO` (varchar) → [[clave-PKCLIENTESRVNRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
