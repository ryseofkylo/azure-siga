---
esquema: dbo
tabla: TR_GI
objeto: dbo.TR_GI
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)
n_columnas: 21
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.TR_GI

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 21 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CLIENTENRO`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ID` | varchar | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `TAREAID_I` | varchar | 0% |
| 4 | `FECHAPROCESADA_I` | datetime2 | 0% |
| 5 | `TIPOORDEN` | varchar | 0% |
| 6 | `TIPOPRODUCTO` | varchar | 0% |
| 7 | `EMPRESAID` | int | 0% |
| 8 | `TECNICOID` | int | 0% |
| 9 | `TECNICOID2` | int | 0% |
| 10 | `TECNICOR1` | varchar | 0% |
| 11 | `TECNICOR2` | varchar | 0% |
| 12 | `CONTRATO` | varchar | 0% |
| 13 | `TAREAID_R` | varchar | 85% |
| 14 | `CONTRATO_R` | varchar | 85% |
| 15 | `FECHAINGRESO_R` | datetime2 | 85% |
| 16 | `FECHAPROCESADA_R` | datetime2 | 85% |
| 17 | `MOTIVOINGRESO_R` | int | 85% |
| 18 | `MOTIVOCUMPLIMIENTO_R` | int | 85% |
| 19 | `GARANTIA_INSTALACION` | int | 0% |
| 20 | `TECNICO_REINCIDENTE_1` | varchar | 98% |
| 21 | `TECNICO_REINCIDENTE_2` | varchar | 98% |

## Claves de join presentes
- `ID` (varchar) → [[clave-ID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]
- `TIPOPRODUCTO` (varchar) → [[clave-TIPOPRODUCTO]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TECNICOID` (int) → [[clave-TECNICOID]]
- `CONTRATO` (varchar) → [[clave-CONTRATO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
