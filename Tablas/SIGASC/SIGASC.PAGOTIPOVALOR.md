---
esquema: SIGASC
tabla: PAGOTIPOVALOR
objeto: SIGASC.PAGOTIPOVALOR
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCPGOTIPOVALID` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PAGOTIPOVALOR

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCPGOTIPOVALID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPAGOTIPOVALOR` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CPGOTIPOID` | int | 0% |
| 4 | `CPGOTIPOVALID` | int | 0% |
| 5 | `CPGOTIPOVALNOMBRE` | varchar | 0% |
| 6 | `CPGOTIPOVALHS` | int | 0% |
| 7 | `CPGOTIPOVALSTS` | int | 0% |
| 8 | `CPGOTIPOVALDEBCRED` | varchar | 25% |
| 9 | `CPGOTIPOVALCUOTAS` | int | 76% |
| 10 | `CPGOTIPOVALIMG` | varchar | 100% |
| 11 | `PIPELINERUNID` | varchar | 0% |
| 12 | `PKCPGOTIPOID` | varchar | 0% |
| 13 | `PKCPGOTIPOVALID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CPGOTIPOID` (int) → [[clave-CPGOTIPOID]]
- `CPGOTIPOVALID` (int) → [[clave-CPGOTIPOVALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCPGOTIPOID` (varchar) → [[clave-PKCPGOTIPOID]]
- `PKCPGOTIPOVALID` (varchar) → [[clave-PKCPGOTIPOVALID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
