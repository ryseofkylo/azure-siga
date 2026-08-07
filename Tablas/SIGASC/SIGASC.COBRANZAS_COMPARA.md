---
esquema: SIGASC
tabla: COBRANZAS_COMPARA
objeto: SIGASC.COBRANZAS_COMPARA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`FACTURANRO`) — compuesto, tentativo (muestra 10)
n_columnas: 20
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COBRANZAS_COMPARA

> **BASE TABLE** · Dominio: **Core SIGA** · 20 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`FACTURANRO`) — compuesto, tentativo (muestra 10)

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
| 12 | `FACTURATPO` | varchar | 0% |
| 13 | `FACTURANRO` | varchar | 0% |
| 14 | `FACTURANRONC` | int | 0% |
| 15 | `RECIBOFACIMP` | real | 0% |
| 16 | `RECIBOFACIMPRBO` | real | 0% |
| 17 | `FACTURAFCH` | datetime2 | 0% |
| 18 | `FACTURAPERIODO` | int | 0% |
| 19 | `FACTURANEGOCIO` | varchar | 0% |
| 20 | `MONTOLINEA` | float | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PKRECIBONRO` (varchar) → [[clave-PKRECIBONRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `FACTURATPO` (varchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (varchar) → [[clave-FACTURANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
