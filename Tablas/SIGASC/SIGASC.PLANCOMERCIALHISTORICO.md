---
esquema: SIGASC
tabla: PLANCOMERCIALHISTORICO
objeto: SIGASC.PLANCOMERCIALHISTORICO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPLANCOMERCIALHISTORICO` (único en muestra de 35)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PLANCOMERCIALHISTORICO

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPLANCOMERCIALHISTORICO` (único en muestra de 35)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPLANCOMERCIALHISTORICO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PLANCOMERCIALID` | int | 0% |
| 4 | `PLANCOMERCIALHSTFCH` | datetime2 | 0% |
| 5 | `PLANCOMERCIALHSTTPO` | varchar | 0% |
| 6 | `PLANCOMERCIALHSTUSR` | varchar | 0% |
| 7 | `PLANCOMERCIALHSTCOD` | int | 0% |
| 8 | `PLANCOMERCIALHSTVAL` | varchar | 0% |
| 9 | `PLANCOMERCIALHSTNEWCOD` | int | 0% |
| 10 | `PLANCOMERCIALHSTNEWVAL` | varchar | 0% |
| 11 | `PIPELINERUNID` | varchar | 0% |
| 12 | `PKPLANCOMERCIALID` | varchar | 0% |

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
