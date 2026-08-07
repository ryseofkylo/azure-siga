---
esquema: SIGASC
tabla: FACTURACLIENTECOMPLE
objeto: SIGASC.FACTURACLIENTECOMPLE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTENRO` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURACLIENTECOMPLE

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
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
| 11 | `IMPORTE_POL` | float | 0% |
| 12 | `IMPORTE_PRM` | float | 0% |
| 13 | `ESCALON` | int | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
**Filtros**
- `periodo NOT IN ( SELECT DISTINCT PERIODOANTERIOR FROM SIGASC.FACTURACLIENTECOMPLE f WHERE f.clientenro = c.clientenro )` — _de_ [[dbo.V_BAJASPERIODOCOMPLE]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_BAJASPERIODOCOMPLE]]

## Vistas que la consumen (referencia)
- [[dbo.V_BAJASPERIODOCOMPLE]]
