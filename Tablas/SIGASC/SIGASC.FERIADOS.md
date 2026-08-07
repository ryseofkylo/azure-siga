---
esquema: SIGASC
tabla: FERIADOS
objeto: SIGASC.FERIADOS
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `FECHA` (único en muestra de 74)
n_columnas: 2
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FERIADOS

> **BASE TABLE** · Dominio: **Core SIGA** · 2 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `FECHA` (único en muestra de 74)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `FECHA` | date | 0% |
| 2 | `DESCRIPCION` | varchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
