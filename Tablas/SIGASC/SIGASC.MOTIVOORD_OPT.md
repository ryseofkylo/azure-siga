---
esquema: SIGASC
tabla: MOTIVOORD_OPT
objeto: SIGASC.MOTIVOORD_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `MOTIVOORDID` (único en muestra de 200)
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MOTIVOORD_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `MOTIVOORDID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MOTIVOORDID` | int | 0% |
| 2 | `MOTIVOORDNOMBRE` | nvarchar | 0% |
| 3 | `MOTIVOORDTPO` | nvarchar | 0% |
| 4 | `MOTIVOORDSTS` | nvarchar | 0% |
| 5 | `MOTIVOORDRED` | int | 0% |
| 6 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `MOTIVOORDID` (int) → [[clave-MOTIVOORDID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
