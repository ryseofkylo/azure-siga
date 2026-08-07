---
esquema: SIGASC
tabla: PAGOTIPO
objeto: SIGASC.PAGOTIPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCPGOTIPOID` (único en muestra de 200)
n_columnas: 21
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PAGOTIPO

> **BASE TABLE** · Dominio: **Core SIGA** · 21 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCPGOTIPOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CPGOTIPOID` | int | 0% |
| 3 | `CPGOTIPONOMBRE` | varchar | 0% |
| 4 | `CPGOTIPOSTS` | int | 0% |
| 5 | `CPGOTIPOABR` | varchar | 0% |
| 6 | `CPGOTIPOUSAVALOR` | int | 0% |
| 7 | `CPGOTIPOUSANRO` | int | 0% |
| 8 | `CPGOTIPOUSAVTO` | int | 0% |
| 9 | `CPGOTIPOUSACP` | int | 0% |
| 10 | `CPGOTIPOUSADIAS` | int | 0% |
| 11 | `CPGOTIPOUSACONTROL` | int | 0% |
| 12 | `CPGOTIPOCAJAAPERTURA` | int | 0% |
| 13 | `CPGOTIPOCAJACIERRE` | int | 0% |
| 14 | `CPGOTIPOUSALOTE` | int | 0% |
| 15 | `CPGOTIPOUSATITULAR` | int | 0% |
| 16 | `CPGOTIPOUSACUPON` | int | 0% |
| 17 | `CPGOTIPOUSACS` | int | 0% |
| 18 | `CPGOTIPOUSAUNIDADCONTABLE` | int | 53% |
| 19 | `CPGOTIPOUSACUIT` | int | 0% |
| 20 | `PIPELINERUNID` | varchar | 0% |
| 21 | `PKCPGOTIPOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CPGOTIPOID` (int) → [[clave-CPGOTIPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCPGOTIPOID` (varchar) → [[clave-PKCPGOTIPOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_PAGOTIPO]]

## Vistas que la consumen (referencia)
- [[dbo.V_PAGOTIPO]]
