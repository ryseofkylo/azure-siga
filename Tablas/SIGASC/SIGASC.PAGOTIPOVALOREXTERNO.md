---
esquema: SIGASC
tabla: PAGOTIPOVALOREXTERNO
objeto: SIGASC.PAGOTIPOVALOREXTERNO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPAGOTIPOVALOREXTNRO` (único en muestra de 200)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PAGOTIPOVALOREXTERNO

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPAGOTIPOVALOREXTNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PAGOTIPOVALOREXTNRO` | int | 0% |
| 3 | `CPGOTIPOID` | int | 0% |
| 4 | `CPGOTIPOVALID` | int | 0% |
| 5 | `PAGOTIPOVALOREXTID` | int | 0% |
| 6 | `PAGOTIPOVALOREXTNOMBRE` | varchar | 0% |
| 7 | `PAGOTIPOVALOREXTCOMERCIO` | varchar | 0% |
| 8 | `SUCURSALID` | int | 0% |
| 9 | `PAGOTIPOVALOREXTCUOTAS` | int | 0% |
| 10 | `PAGOTIPOVALOREXTIDSITE` | varchar | 0% |
| 11 | `PAGOTIPOVALOREXTACTIVO` | int | 0% |
| 12 | `PAGOTIPOVALOREXTCONFIG` | varchar | 95% |
| 13 | `PAGOTIPOVALOREXTTIPO` | varchar | 0% |
| 14 | `PIPELINERUNID` | varchar | 0% |
| 15 | `PKPAGOTIPOVALOREXTNRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CPGOTIPOID` (int) → [[clave-CPGOTIPOID]]
- `CPGOTIPOVALID` (int) → [[clave-CPGOTIPOVALID]]
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
