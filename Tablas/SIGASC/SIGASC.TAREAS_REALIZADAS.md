---
esquema: SIGASC
tabla: TAREAS_REALIZADAS
objeto: SIGASC.TAREAS_REALIZADAS
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: TODO (muestra vacía)
n_columnas: 42
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.TAREAS_REALIZADAS

> **BASE TABLE** · Dominio: **Core SIGA** · 42 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** TODO (muestra vacía)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `SUCURSALID` | int | 0% |
| 3 | `TAREAID` | varchar | 0% |
| 4 | `PRODUCTOCATV` | nvarchar | 0% |
| 5 | `PRODUCTOINTERNET` | nvarchar | 0% |
| 6 | `DERIVADOS` | int | 0% |
| 7 | `DECODERS` | int | 0% |
| 8 | `TIPOORDEN` | char | 0% |
| 9 | `ESTADOORDEN` | char | 0% |
| 10 | `MOTIVOINGRESO` | nvarchar | 0% |
| 11 | `MOTIVOID` | int | 0% |
| 12 | `FORMAGENERADA` | nvarchar | 0% |
| 13 | `CENTROOPERATIVOID` | nvarchar | 0% |
| 14 | `CLIENTENRO` | int | 0% |
| 15 | `ESTADOCLIENTE` | nvarchar | 0% |
| 16 | `FECHAINGRESO` | datetime | 0% |
| 17 | `HORAINGRESO` | nvarchar | 0% |
| 18 | `FECHAFINALIZADA` | datetime | 0% |
| 19 | `HORAFINALIZADA` | nvarchar | 0% |
| 20 | `FECHAPROCESADA` | datetime | 0% |
| 21 | `HORAPROCESADA` | nvarchar | 0% |
| 22 | `FECHAAGENDADA` | datetime | 0% |
| 23 | `TURNOID` | nvarchar | 0% |
| 24 | `TECNICOID` | nvarchar | 0% |
| 25 | `TECNICOEMPLEADONRO` | int | 0% |
| 26 | `ORDENTRBRED` | int | 0% |
| 27 | `MOTIVOSOLUCION` | nvarchar | 0% |
| 28 | `ZONAHABID` | nvarchar | 0% |
| 29 | `ZONAPELID` | nvarchar | 0% |
| 30 | `CONTRATOS` | nvarchar | 0% |
| 31 | `ORDENFCHCONEXIONFUTURA` | datetime | 0% |
| 32 | `ORDENTIPOCONEXION` | nvarchar | 0% |
| 33 | `COD_MZN` | nvarchar | 0% |
| 34 | `FACTURATOTAL` | decimal | 0% |
| 35 | `TENICOID2` | nvarchar | 0% |
| 36 | `MOVILES` | nvarchar | 0% |
| 37 | `PRODUCTOTPOLISTA` | nvarchar | 0% |
| 38 | `DERIVADOS_ACTUAL` | int | 0% |
| 39 | `DECODERS_ACTUAL` | int | 0% |
| 40 | `EXTENSORES_ACTUAL` | int | 0% |
| 41 | `CATEGORIAAGRUPACION` | nvarchar | 0% |
| 42 | `FECHA_CARGA` | datetime | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `TAREAID` (varchar) → [[clave-TAREAID]]
- `MOTIVOID` (int) → [[clave-MOTIVOID]]
- `CENTROOPERATIVOID` (nvarchar) → [[clave-CENTROOPERATIVOID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `TURNOID` (nvarchar) → [[clave-TURNOID]]
- `TECNICOID` (nvarchar) → [[clave-TECNICOID]]
- `TECNICOEMPLEADONRO` (int) → [[clave-TECNICOEMPLEADONRO]]
- `ZONAHABID` (nvarchar) → [[clave-ZONAHABID]]
- `ZONAPELID` (nvarchar) → [[clave-ZONAPELID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
