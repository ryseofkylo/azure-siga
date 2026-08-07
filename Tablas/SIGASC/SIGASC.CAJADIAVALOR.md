---
esquema: SIGASC
tabla: CAJADIAVALOR
objeto: SIGASC.CAJADIAVALOR
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCAJADIAVALOR` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAJADIAVALOR

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCAJADIAVALOR` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCAJADIAVALOR` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CAJADIAFCH` | datetime2 | 0% |
| 4 | `CAJANRO` | int | 0% |
| 5 | `CAJADIAVALORTPO` | int | 0% |
| 6 | `CPGOTIPOID` | int | 0% |
| 7 | `MONEDAID` | int | 0% |
| 8 | `CAJADIAVALORIMP` | real | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCAJANRO` | varchar | 0% |
| 11 | `PKCAJADIAVALORTPO` | varchar | 0% |
| 12 | `PKCPGOTIPOID` | varchar | 0% |
| 13 | `PKMONEDAID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CAJANRO` (int) → [[clave-CAJANRO]]
- `CPGOTIPOID` (int) → [[clave-CPGOTIPOID]]
- `MONEDAID` (int) → [[clave-MONEDAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAJANRO` (varchar) → [[clave-PKCAJANRO]]
- `PKCPGOTIPOID` (varchar) → [[clave-PKCPGOTIPOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
