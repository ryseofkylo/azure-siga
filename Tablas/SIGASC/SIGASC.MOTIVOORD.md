---
esquema: SIGASC
tabla: MOTIVOORD
objeto: SIGASC.MOTIVOORD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `MOTIVOORDID` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MOTIVOORD

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `MOTIVOORDID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MOTIVOORDID` | int | 0% |
| 2 | `MOTIVOORDNOMBRE` | varchar | 0% |
| 3 | `MOTIVOORDTPO` | varchar | 0% |
| 4 | `MOTIVOORDSTS` | varchar | 0% |
| 5 | `MOTIVOORDRED` | int | 0% |
| 6 | `MOTIVOORDGRUPOID` | int | 98% |
| 7 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `MOTIVOORDID` (int) → [[clave-MOTIVOORDID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
- [[dbo.V_RECLAMOS_BDDD]]
