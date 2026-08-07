---
esquema: SIGASC
tabla: FACTURAESTADOCLIENTE
objeto: SIGASC.FACTURAESTADOCLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)
n_columnas: 3
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURAESTADOCLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PKCLIENTENRO` | varchar | 0% |
| 2 | `FACTURAFCH` | date | 0% |
| 3 | `BDMODIFIEDDATE` | date | 0% |

## Claves de join presentes
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
