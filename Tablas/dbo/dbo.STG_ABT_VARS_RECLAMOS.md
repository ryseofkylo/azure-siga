---
esquema: dbo
tabla: STG_ABT_VARS_RECLAMOS
objeto: dbo.STG_ABT_VARS_RECLAMOS
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)
n_columnas: 8
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.STG_ABT_VARS_RECLAMOS

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `FECHA_CORTE` | date | 0% |
| 4 | `CANT_RECLAMOS_6M` | int | 0% |
| 5 | `CANT_MOTIVOS_DISTINTOS` | int | 0% |
| 6 | `RECLAMOS_REINCIDENTES` | int | 0% |
| 7 | `DIAS_RESOLUCION_PROM` | numeric | 0% |
| 8 | `RECLAMOS_ABIERTOS_AL_CORTE` | int | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
