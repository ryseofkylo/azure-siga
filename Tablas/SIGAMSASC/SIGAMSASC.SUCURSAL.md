---
esquema: SIGAMSASC
tabla: SUCURSAL
objeto: SIGAMSASC.SUCURSAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SUCURSALID` (único en muestra de 136)
n_columnas: 5
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.SUCURSAL

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SUCURSALID` (único en muestra de 136)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SUCURSALID` | int | 0% |
| 2 | `SUCURSALNOMBRE` | varchar | 0% |
| 3 | `UNIDADID` | int | 0% |
| 4 | `SUCURSALALTACLIENTE` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
