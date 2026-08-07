---
esquema: SIGASC
tabla: PRODUCTOTPO_OPT
objeto: SIGASC.PRODUCTOTPO_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PRODUCTOTPO` (único en muestra de 23)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTOTPO_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PRODUCTOTPO` (único en muestra de 23)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PRODUCTOTPO` | nvarchar | 0% |
| 2 | `PRODUCTOTPONOMBRE` | nvarchar | 0% |
| 3 | `PRODUCTOGENORDEN` | int | 0% |
| 4 | `PRODUCTOESADICIONAL` | int | 0% |
| 5 | `PRODUCTOTPOPRIORIDAD` | int | 0% |
| 6 | `PRODUCTOTPOVALIDAPPL` | int | 74% |
| 7 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `PRODUCTOTPO` (nvarchar) → [[clave-PRODUCTOTPO]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
