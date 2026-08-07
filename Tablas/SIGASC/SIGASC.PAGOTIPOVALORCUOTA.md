---
esquema: SIGASC
tabla: PAGOTIPOVALORCUOTA
objeto: SIGASC.PAGOTIPOVALORCUOTA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPAGOTIPOVALORCUOTA` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PAGOTIPOVALORCUOTA

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPAGOTIPOVALORCUOTA` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPAGOTIPOVALORCUOTA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CPGOTIPOID` | int | 0% |
| 4 | `CPGOTIPOVALID` | int | 0% |
| 5 | `CPGOTIPOVALCUOTAID` | int | 0% |
| 6 | `CPGOTIPOVALCUOTANOM` | varchar | 0% |
| 7 | `CPGOTIPOVALCUOTACOEF` | real | 0% |
| 8 | `CPGOTIPOVALCUOTASTS` | varchar | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCPGOTIPOID` | varchar | 0% |
| 11 | `PKCPGOTIPOVALID` | varchar | 0% |
| 12 | `PKCPGOTIPOVALCUOTAID` | varchar | 0% |

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
