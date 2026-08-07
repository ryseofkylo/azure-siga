---
esquema: SIGASC
tabla: NEGOCIO
objeto: SIGASC.NEGOCIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `NEGOCIOID` (único en muestra de 9)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.NEGOCIO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `NEGOCIOID` (único en muestra de 9)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `NEGOCIOID` | varchar | 0% |
| 2 | `NEGOCIONOMBRE` | varchar | 0% |
| 3 | `NEGLOGOID` | int | 100% |
| 4 | `NEGOCIOREQHAB` | int | 0% |
| 5 | `NEGOCIOZONATPOID` | varchar | 89% |
| 6 | `NEGOCIOGRUPO` | int | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `NEGOCIOID` (varchar) → [[clave-NEGOCIOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_NEGOCIO]]
