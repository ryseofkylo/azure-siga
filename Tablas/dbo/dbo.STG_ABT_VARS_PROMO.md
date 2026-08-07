---
esquema: dbo
tabla: STG_ABT_VARS_PROMO
objeto: dbo.STG_ABT_VARS_PROMO
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)
n_columnas: 7
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.STG_ABT_VARS_PROMO

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `FECHA_CORTE` | date | 0% |
| 4 | `TIENE_PROMO_ACTIVA_AL_CORTE` | int | 0% |
| 5 | `DIAS_PARA_VENC_PROMO` | int | 51% |
| 6 | `TUVO_RETENCION_PREVIA` | int | 0% |
| 7 | `CANT_RETENCIONES_PREVIAS` | int | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
