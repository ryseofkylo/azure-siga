---
esquema: dbo
tabla: TR_R
objeto: dbo.TR_R
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `TAREAID_R` (único en muestra de 200)
n_columnas: 36
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.TR_R

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 36 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `TAREAID_R` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | varchar | 0% |
| 2 | `SUCURSALID` | int | 0% |
| 3 | `TAREAID_R` | varchar | 0% |
| 4 | `DERIVADOS` | int | 0% |
| 5 | `DECODERS` | int | 0% |
| 6 | `TIPOORDEN` | varchar | 0% |
| 7 | `ESTADOORDEN` | varchar | 0% |
| 8 | `MOTIVOINGRESO_R` | int | 0% |
| 9 | `MOTIVOCUMPLIMIENTO_R` | int | 0% |
| 10 | `FORMAGENERADA` | varchar | 0% |
| 11 | `CLIENTENRO` | varchar | 0% |
| 12 | `ESTADOCLIENTE` | varchar | 0% |
| 13 | `FECHAINGRESO_R` | datetime2 | 0% |
| 14 | `HORAINGRESO` | datetime2 | 100% |
| 15 | `FECHAFINALIZADA` | datetime2 | 0% |
| 16 | `HORAFINALIZADA` | datetime2 | 100% |
| 17 | `FECHAPROCESADA_R` | datetime2 | 0% |
| 18 | `HORAPROCESADA` | datetime2 | 100% |
| 19 | `FECHAAGENDADA` | datetime2 | 4% |
| 20 | `TURNOID` | varchar | 4% |
| 21 | `TECNICOID` | int | 0% |
| 22 | `DEMORATOTAL` | int | 0% |
| 23 | `TECNICOEMPLEADONRO` | int | 0% |
| 24 | `ORDENTRBRED` | int | 0% |
| 25 | `MOTIVOSOLUCION` | varchar | 0% |
| 26 | `ZONAHABID` | varchar | 6% |
| 27 | `ZONAPELID` | varchar | 100% |
| 28 | `ORDENFCHCONEXIONFUTURA` | datetime2 | 100% |
| 29 | `ORDENTIPOCONEXION` | varchar | 0% |
| 30 | `COD_MZN` | varchar | 0% |
| 31 | `FACTURATOTAL` | float | 4% |
| 32 | `TECNICOID2` | int | 0% |
| 33 | `MOVILES` | varchar | 0% |
| 34 | `PRODUCTOTPOLISTA` | varchar | 2% |
| 35 | `CATEGORIAAGRUPACION` | varchar | 0% |
| 36 | `CONTRATO_R` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (varchar) → [[clave-EMPRESAID]]
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]
- `TURNOID` (varchar) → [[clave-TURNOID]]
- `TECNICOID` (int) → [[clave-TECNICOID]]
- `TECNICOEMPLEADONRO` (int) → [[clave-TECNICOEMPLEADONRO]]
- `ZONAHABID` (varchar) → [[clave-ZONAHABID]]
- `ZONAPELID` (varchar) → [[clave-ZONAPELID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
