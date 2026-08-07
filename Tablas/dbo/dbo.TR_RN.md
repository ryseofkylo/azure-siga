---
esquema: dbo
tabla: TR_RN
objeto: dbo.TR_RN
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)
n_columnas: 15
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.TR_RN

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESA` | varchar | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `TAREAID_I` | varchar | 0% |
| 4 | `TAREAID_R` | varchar | 0% |
| 5 | `FECHAPROCESADA_I` | datetime2 | 0% |
| 6 | `FECHAINGRESO_R` | datetime2 | 0% |
| 7 | `FECHAPROCESADA_R` | datetime2 | 0% |
| 8 | `CONTRATO_R` | varchar | 0% |
| 9 | `CONTRATO` | varchar | 0% |
| 10 | `GARANTIA_INSTALACION` | int | 0% |
| 11 | `TECNICO_REINCIDENTE_1` | varchar | 0% |
| 12 | `TECNICO_REINCIDENTE_2` | varchar | 0% |
| 13 | `MOTIVOINGRESO_R` | int | 0% |
| 14 | `MOTIVOCUMPLIMIENTO_R` | int | 0% |
| 15 | `RN` | bigint | 0% |

## Claves de join presentes
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]
- `CONTRATO` (varchar) → [[clave-CONTRATO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
