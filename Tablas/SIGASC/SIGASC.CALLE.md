---
esquema: SIGASC
tabla: CALLE
objeto: SIGASC.CALLE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CALLEID` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CALLE

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CALLEID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCALLE` | varchar | 0% |
| 2 | `PAISID` | int | 0% |
| 3 | `CIUDADID` | int | 0% |
| 4 | `CALLEID` | int | 0% |
| 5 | `CALLENOMBRE` | varchar | 0% |
| 6 | `CALLEGEONOMBRE` | varchar | 0% |
| 7 | `CALLEVIA` | varchar | 0% |
| 8 | `CALLEFCHACTUALIZACION` | datetime2 | 0% |
| 9 | `CALLEGISID` | int | 0% |
| 10 | `CALLESTS` | varchar | 0% |
| 11 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PAISID` (int) → [[clave-PAISID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
