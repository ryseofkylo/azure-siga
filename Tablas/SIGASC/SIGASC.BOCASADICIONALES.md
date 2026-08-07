---
esquema: SIGASC
tabla: BOCASADICIONALES
objeto: SIGASC.BOCASADICIONALES
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CONTRATONRO` (único en muestra de 200)
n_columnas: 4
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.BOCASADICIONALES

> **BASE TABLE** · Dominio: **Core SIGA** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CONTRATONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `FECHA` | datetime2 | 0% |
| 2 | `CLIENTENRO` | nvarchar | 0% |
| 3 | `CONTRATONRO` | nvarchar | 0% |
| 4 | `BOCAS_ADICIONALES` | int | 0% |

## Claves de join presentes
- `CLIENTENRO` (nvarchar) → [[clave-CLIENTENRO]]
- `CONTRATONRO` (nvarchar) → [[clave-CONTRATONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
