---
esquema: SIGASC
tabla: PLANCOMERCIALVIGENCIA
objeto: SIGASC.PLANCOMERCIALVIGENCIA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPLANCOMERCIALID` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PLANCOMERCIALVIGENCIA

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPLANCOMERCIALID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPLANCOMERCIALVIGENCIA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PLANCOMERCIALID` | int | 0% |
| 4 | `PLANCOMERCIALVIGENCIAFCHINI` | datetime2 | 0% |
| 5 | `PLANCOMERCIALVIGENCIAFCHFIN` | datetime2 | 0% |
| 6 | `PLANCOMERCIALVIGENCIASTS` | varchar | 0% |
| 7 | `PLANCOMERCIALVIGENCIANOM` | varchar | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKPLANCOMERCIALID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PLANCOMERCIALID` (int) → [[clave-PLANCOMERCIALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPLANCOMERCIALID` (varchar) → [[clave-PKPLANCOMERCIALID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
