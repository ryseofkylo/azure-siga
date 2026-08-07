---
esquema: SIGASC
tabla: PLANCOMERCIALITEMHISTORICO
objeto: SIGASC.PLANCOMERCIALITEMHISTORICO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPLANCOMERCIALITEMHISTORICO` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PLANCOMERCIALITEMHISTORICO

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPLANCOMERCIALITEMHISTORICO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPLANCOMERCIALITEMHISTORICO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PLANCOMERCIALID` | int | 0% |
| 4 | `PLANCOMERCIALITEM` | int | 0% |
| 5 | `PLANCOMERCIALPRODALTERNATIVA` | int | 0% |
| 6 | `PLANCOMERCIALITEMHSTFCH` | datetime2 | 0% |
| 7 | `PLANCOMERCIALITEMHSTTPO` | varchar | 0% |
| 8 | `PLANCOMERCIALITEMHSTUSR` | varchar | 0% |
| 9 | `PLANCOMERCIALITEMHSTCOD` | int | 0% |
| 10 | `PLANCOMERCIALITEMHSTVAL` | varchar | 0% |
| 11 | `PLANCOMERCIALITEMHSTNEWCOD` | int | 0% |
| 12 | `PLANCOMERCIALITEMHSTNEWVAL` | varchar | 0% |
| 13 | `PIPELINERUNID` | varchar | 0% |
| 14 | `PKPLANCOMERCIALID` | varchar | 0% |
| 15 | `PKPLANCOMERCIALITEM` | varchar | 0% |
| 16 | `PKPLANCOMERCIALPRODALTERNATIVA` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PLANCOMERCIALID` (int) → [[clave-PLANCOMERCIALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPLANCOMERCIALID` (varchar) → [[clave-PKPLANCOMERCIALID]]
- `PKPLANCOMERCIALITEM` (varchar) → [[clave-PKPLANCOMERCIALITEM]]
- `PKPLANCOMERCIALPRODALTERNATIVA` (varchar) → [[clave-PKPLANCOMERCIALPRODALTERNATIVA]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
