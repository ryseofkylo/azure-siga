---
esquema: dbo
tabla: STG_ABT_VARS_CLIENTE
objeto: dbo.STG_ABT_VARS_CLIENTE
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)
n_columnas: 17
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.STG_ABT_VARS_CLIENTE

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 17 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `FECHA_CORTE` | date | 0% |
| 4 | `target` | int | 0% |
| 5 | `CLIENTENATURALEZAID` | int | 0% |
| 6 | `MEDCOBROID` | int | 0% |
| 7 | `CICLOID` | int | 0% |
| 8 | `NEGOCIOSEGMENTOTIPOID` | int | 40% |
| 9 | `NEGOCIOSEGMENTO` | int | 0% |
| 10 | `CLIENTETPO` | int | 0% |
| 11 | `CLICALID` | int | 0% |
| 12 | `GEOMANID` | int | 0% |
| 13 | `GEODIV1ID` | int | 0% |
| 14 | `GEODIV2ID` | int | 0% |
| 15 | `CLIENTEFCHING` | datetime2 | 0% |
| 16 | `FECHA_ING_SOSPECHOSA` | int | 0% |
| 17 | `ANTIGUEDAD_MESES` | int | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `CLIENTENATURALEZAID` (int) → [[clave-CLIENTENATURALEZAID]]
- `MEDCOBROID` (int) → [[clave-MEDCOBROID]]
- `CICLOID` (int) → [[clave-CICLOID]]
- `NEGOCIOSEGMENTOTIPOID` (int) → [[clave-NEGOCIOSEGMENTOTIPOID]]
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `CLIENTETPO` (int) → [[clave-CLIENTETPO]]
- `CLICALID` (int) → [[clave-CLICALID]]
- `GEOMANID` (int) → [[clave-GEOMANID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
