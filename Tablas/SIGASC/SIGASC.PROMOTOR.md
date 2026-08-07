---
esquema: SIGASC
tabla: PROMOTOR
objeto: SIGASC.PROMOTOR
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPROMOTORID` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PROMOTOR

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPROMOTORID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PROMOTORID` | int | 0% |
| 3 | `PROMOTORNOMBRE` | varchar | 0% |
| 4 | `PROMOTORSTS` | varchar | 0% |
| 5 | `PROMOTORGRUPOID` | int | 0% |
| 6 | `USUARIOID` | int | 100% |
| 7 | `PROMOTORTECNICOID` | int | 100% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKPROMOTORID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PROMOTORID` (int) → [[clave-PROMOTORID]]
- `PROMOTORGRUPOID` (int) → [[clave-PROMOTORGRUPOID]]
- `USUARIOID` (int) → [[clave-USUARIOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPROMOTORID` (varchar) → [[clave-PKPROMOTORID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_CONTRATOS_BDDD]]
- [[dbo.V_PROMOTOR]]
