---
esquema: dbo
tabla: ABT_PROPENSION_RIESGO
objeto: dbo.ABT_PROPENSION_RIESGO
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)
n_columnas: 30
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.ABT_PROPENSION_RIESGO

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 30 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `FECHA_CORTE` | date | 0% |
| 4 | `target` | int | 0% |
| 5 | `CLIENTENATURALEZAID` | int | 2% |
| 6 | `MEDCOBROID` | int | 2% |
| 7 | `CICLOID` | int | 2% |
| 8 | `NEGOCIOSEGMENTOTIPOID` | int | 40% |
| 9 | `NEGOCIOSEGMENTO` | int | 2% |
| 10 | `CLIENTETPO` | int | 2% |
| 11 | `CLICALID` | int | 2% |
| 12 | `GEOMANID` | int | 2% |
| 13 | `GEODIV1ID` | int | 2% |
| 14 | `GEODIV2ID` | int | 2% |
| 15 | `FECHA_ING_SOSPECHOSA` | int | 2% |
| 16 | `ANTIGUEDAD_MESES` | int | 2% |
| 17 | `CANT_RECLAMOS_6M` | int | 0% |
| 18 | `CANT_MOTIVOS_DISTINTOS` | int | 0% |
| 19 | `RECLAMOS_REINCIDENTES` | int | 0% |
| 20 | `DIAS_RESOLUCION_PROM` | numeric | 80% |
| 21 | `RECLAMOS_ABIERTOS_AL_CORTE` | int | 0% |
| 22 | `CANT_FACTURAS_6M` | int | 0% |
| 23 | `DIAS_ATRASO_PROM` | numeric | 10% |
| 24 | `DIAS_ATRASO_MAX` | int | 0% |
| 25 | `CANT_FACTURAS_ATRASADAS` | int | 0% |
| 26 | `FACTURAS_IMPAGAS_AL_CORTE` | int | 0% |
| 27 | `TIENE_PROMO_ACTIVA_AL_CORTE` | int | 0% |
| 28 | `DIAS_PARA_VENC_PROMO` | int | 78% |
| 29 | `TUVO_RETENCION_PREVIA` | int | 0% |
| 30 | `CANT_RETENCIONES_PREVIAS` | int | 0% |

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
