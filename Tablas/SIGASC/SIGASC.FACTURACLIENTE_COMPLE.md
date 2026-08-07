---
esquema: SIGASC
tabla: FACTURACLIENTE_COMPLE
objeto: SIGASC.FACTURACLIENTE_COMPLE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTENRO` (único en muestra de 200)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURACLIENTE_COMPLE

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `PERIODO` | int | 0% |
| 4 | `CONTRATOS` | int | 0% |
| 5 | `SUMA_CONTRATOS` | bigint | 0% |
| 6 | `SUMA_POLITICAS` | bigint | 0% |
| 7 | `SUMA_PROMOCIONES` | bigint | 0% |
| 8 | `CLASEPRODUCTO` | int | 0% |
| 9 | `FACTURACION` | float | 0% |
| 10 | `PERIODOANTERIOR` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
