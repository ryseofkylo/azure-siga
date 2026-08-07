---
esquema: SIGASC
tabla: CONTRATOS_FINMES
objeto: SIGASC.CONTRATOS_FINMES
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`PKPOLITICAID`) — compuesto, tentativo (muestra 10)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CONTRATOS_FINMES

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`PKPOLITICAID`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PERIODO` | nvarchar | 0% |
| 2 | `INICIOPERIODO` | date | 0% |
| 3 | `EMPRESAID` | int | 0% |
| 4 | `PKPOLITICAID` | nvarchar | 0% |
| 5 | `PKPRODUCTOID` | nvarchar | 0% |
| 6 | `CONTRATOS` | int | 0% |
| 7 | `ACTUALIZACION` | datetime | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PKPOLITICAID` (nvarchar) → [[clave-PKPOLITICAID]]
- `PKPRODUCTOID` (nvarchar) → [[clave-PKPRODUCTOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
