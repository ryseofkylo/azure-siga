---
esquema: SIGASC
tabla: POLITICAPRC_MENSUAL
objeto: SIGASC.POLITICAPRC_MENSUAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`PKPOLITICAID`) — compuesto, tentativo (muestra 10)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.POLITICAPRC_MENSUAL

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`PKPOLITICAID`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `POLITICAPERIODO` | nvarchar | 0% |
| 2 | `FECHAPERIODO` | date | 0% |
| 3 | `FACTURAPERIODO` | nvarchar | 0% |
| 4 | `EMPRESAID` | int | 0% |
| 5 | `PKPOLITICAID` | varchar | 0% |
| 6 | `POLITICAFCH` | datetime2 | 0% |
| 7 | `POLITICALIN` | int | 0% |
| 8 | `CPTOFACID` | int | 0% |
| 9 | `POLITICAPRC` | real | 0% |
| 10 | `POLITICAPRCVTO2` | real | 0% |
| 11 | `POLITICAPRCVTO3` | real | 0% |
| 12 | `ACTUALIZACION` | datetime | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PKPOLITICAID` (varchar) → [[clave-PKPOLITICAID]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
