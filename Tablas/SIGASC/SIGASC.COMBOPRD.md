---
esquema: SIGASC
tabla: COMBOPRD
objeto: SIGASC.COMBOPRD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCOMBOPRD` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COMBOPRD

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCOMBOPRD` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCOMBOPRD` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `COMBOID` | int | 0% |
| 4 | `PRODUCTOID` | int | 0% |
| 5 | `COMBOPRDPRIORIDAD` | int | 0% |
| 6 | `COMBOPRDDTO` | real | 0% |
| 7 | `COMBOPRDPRC` | real | 0% |
| 8 | `COMBOPRDCPTOFACID` | int | 100% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCOMBOID` | varchar | 0% |
| 11 | `PKPRODUCTOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `COMBOID` (int) → [[clave-COMBOID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCOMBOID` (varchar) → [[clave-PKCOMBOID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
