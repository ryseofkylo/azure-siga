---
esquema: SIGAMSASC
tabla: EMPRESA_OPT
objeto: SIGAMSASC.EMPRESA_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `EMPRESAID` (único en muestra de 27)
n_columnas: 9
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.EMPRESA_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `EMPRESAID` (único en muestra de 27)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `EMPRESANOM` | nvarchar | 0% |
| 3 | `PAISID` | int | 0% |
| 4 | `EMPLOGOID` | int | 0% |
| 5 | `EMPRESARAZONSOCIAL` | nvarchar | 0% |
| 6 | `EMPRESARUT` | nvarchar | 0% |
| 7 | `EMPRESADIRECCION` | nvarchar | 0% |
| 8 | `EMPRESADEVENGAVTO` | int | 0% |
| 9 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PAISID` (int) → [[clave-PAISID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
