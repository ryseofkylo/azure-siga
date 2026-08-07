---
esquema: SIGASC
tabla: PLANCOMERCIALITEMDEFAULT
objeto: SIGASC.PLANCOMERCIALITEMDEFAULT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPLANCOMERCIALITEMDEFAULT` (único en muestra de 200)
n_columnas: 18
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PLANCOMERCIALITEMDEFAULT

> **BASE TABLE** · Dominio: **Core SIGA** · 18 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPLANCOMERCIALITEMDEFAULT` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPLANCOMERCIALITEMDEFAULT` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PLANCOMERCIALID` | int | 0% |
| 4 | `PLANCOMERCIALITEM` | int | 0% |
| 5 | `PLANCOMERCIALPRODALTERNATIVA` | int | 0% |
| 6 | `PRODUCTOID` | int | 0% |
| 7 | `POLITICAPLANDEFAULTID` | int | 0% |
| 8 | `POLITICAID` | int | 0% |
| 9 | `PROMOCIONID` | int | 28% |
| 10 | `PLANCOMERCIALPRODDEFAULT` | int | 0% |
| 11 | `PLANCOMERCIALPRODCONNUEVO` | int | 0% |
| 12 | `PLANCOMERCIALPRODCONUPG` | int | 0% |
| 13 | `PLANCOMERCIALPRODCONDNWGRADE` | int | 0% |
| 14 | `PLANCOMERCIALPRODSTS` | varchar | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |
| 16 | `PKPLANCOMERCIALID` | varchar | 0% |
| 17 | `PKPLANCOMERCIALITEM` | varchar | 0% |
| 18 | `PKPLANCOMERCIALPRODALTERNATIVA` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PLANCOMERCIALID` (int) → [[clave-PLANCOMERCIALID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PROMOCIONID` (int) → [[clave-PROMOCIONID]]
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
