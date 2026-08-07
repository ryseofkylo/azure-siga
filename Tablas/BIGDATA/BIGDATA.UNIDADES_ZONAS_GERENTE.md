---
esquema: BIGDATA
tabla: UNIDADES_ZONAS_GERENTE
objeto: BIGDATA.UNIDADES_ZONAS_GERENTE
tipo_objeto: BASE TABLE
dominio: Big Data
canonico: true
grain: 1 fila = 1 `SUCURSAL_ID` (único en muestra de 124)
n_columnas: 10
tags:
  - esquema/BIGDATA
  - dominio/big-data
  - tipo/tabla-base
  - canonico
---

# BIGDATA.UNIDADES_ZONAS_GERENTE

> **BASE TABLE** · Dominio: **Big Data** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SUCURSAL_ID` (único en muestra de 124)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SUCURSAL_ID` | int | 0% |
| 2 | `SUB_UNIDAD` | varchar | 0% |
| 3 | `UNIDAD` | varchar | 0% |
| 4 | `ORDEN` | int | 0% |
| 5 | `GERENTE` | varchar | 0% |
| 6 | `ZONA` | varchar | 0% |
| 7 | `EMPRESA` | varchar | 0% |
| 8 | `UNIDAD2` | varchar | 0% |
| 9 | `CENTRO_OPERATIVO` | varchar | 0% |
| 10 | `EMPRESAID` | int | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
