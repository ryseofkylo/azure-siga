---
esquema: SIGASC
tabla: COBRANZAS_ANTES
objeto: SIGASC.COBRANZAS_ANTES
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`PKRECIBONRO`) — compuesto, tentativo (muestra 10)
n_columnas: 24
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COBRANZAS_ANTES

> **BASE TABLE** · Dominio: **Core SIGA** · 24 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`PKRECIBONRO`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PKRECIBONRO` | varchar | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `RECIBOFCH` | datetime2 | 0% |
| 5 | `RECIBOSTS` | varchar | 0% |
| 6 | `MEDCOBRBO` | int | 0% |
| 7 | `RECIBOIMP` | real | 0% |
| 8 | `RECIBOUSR` | varchar | 0% |
| 9 | `RECIBOGEN` | varchar | 0% |
| 10 | `RECIBOFCHCOB` | datetime2 | 0% |
| 11 | `RECIBOTPO` | varchar | 0% |
| 12 | `PKFACTURATPO` | varchar | 0% |
| 13 | `PKFACTURANRO` | varchar | 0% |
| 14 | `RECIBOFACIMPRBO` | real | 0% |
| 15 | `FACTURAFCH` | datetime2 | 0% |
| 16 | `FACTURAPERIODO` | int | 0% |
| 17 | `PKFACTURALIN` | nvarchar | 0% |
| 18 | `CPTOFACID` | int | 0% |
| 19 | `CPTOFACGRUPOID` | int | 0% |
| 20 | `PKPRODUCTOID` | varchar | 2% |
| 21 | `PRODUCTOTPO` | varchar | 2% |
| 22 | `MONTOLINEA` | real | 0% |
| 23 | `CONTRIBUCION` | real | 0% |
| 24 | `COBRANZALINEA` | real | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PKRECIBONRO` (varchar) → [[clave-PKRECIBONRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PKFACTURATPO` (varchar) → [[clave-PKFACTURATPO]]
- `PKFACTURANRO` (varchar) → [[clave-PKFACTURANRO]]
- `PKFACTURALIN` (nvarchar) → [[clave-PKFACTURALIN]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `CPTOFACGRUPOID` (int) → [[clave-CPTOFACGRUPOID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]
- `PRODUCTOTPO` (varchar) → [[clave-PRODUCTOTPO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_COBRANZAS_ANTES]]
