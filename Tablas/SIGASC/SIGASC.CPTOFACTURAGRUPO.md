---
esquema: SIGASC
tabla: CPTOFACTURAGRUPO
objeto: SIGASC.CPTOFACTURAGRUPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CPTOFACGRUPOID` (único en muestra de 10)
n_columnas: 4
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CPTOFACTURAGRUPO

> **BASE TABLE** · Dominio: **Core SIGA** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CPTOFACGRUPOID` (único en muestra de 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CPTOFACGRUPOID` | int | 0% |
| 2 | `CPTOFACGRUPONOMBRE` | varchar | 0% |
| 3 | `CPTOFACGRUPOINTERNO` | varchar | 0% |
| 4 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `CPTOFACGRUPOID` (int) → [[clave-CPTOFACGRUPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.CPTOFACTURA]] · `CPTOFACTURAGRUPO.CPTOFACGRUPOID = CPTOFACTURA.CPTOFACGRUPOID` — view_join (V_CONCEPTOFACTURA), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_CONCEPTOFACTURA]]
