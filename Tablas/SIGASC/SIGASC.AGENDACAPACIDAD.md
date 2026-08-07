---
esquema: SIGASC
tabla: AGENDACAPACIDAD
objeto: SIGASC.AGENDACAPACIDAD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKAGENDACAPACIDAD` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.AGENDACAPACIDAD

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKAGENDACAPACIDAD` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKAGENDACAPACIDAD` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `AGENDAFECHA` | datetime2 | 0% |
| 4 | `TAREATIPOID` | int | 0% |
| 5 | `RECURSOID` | int | 0% |
| 6 | `TURNOID` | int | 0% |
| 7 | `AGENDACAPDISPO` | real | 0% |
| 8 | `AGENDACAPOCUPA` | real | 0% |
| 9 | `AGENDACAPINICIO` | real | 0% |
| 10 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 11 | `PIPELINERUNID` | varchar | 0% |
| 12 | `PKTAREATIPOID` | varchar | 0% |
| 13 | `PKRECURSOID` | varchar | 0% |
| 14 | `PKTURNOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TAREATIPOID` (int) → [[clave-TAREATIPOID]]
- `RECURSOID` (int) → [[clave-RECURSOID]]
- `TURNOID` (int) → [[clave-TURNOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKTAREATIPOID` (varchar) → [[clave-PKTAREATIPOID]]
- `PKRECURSOID` (varchar) → [[clave-PKRECURSOID]]
- `PKTURNOID` (varchar) → [[clave-PKTURNOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
