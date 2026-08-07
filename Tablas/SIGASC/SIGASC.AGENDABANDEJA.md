---
esquema: SIGASC
tabla: AGENDABANDEJA
objeto: SIGASC.AGENDABANDEJA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `AGENDABANDEJAID` (único en muestra de 200)
n_columnas: 19
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.AGENDABANDEJA

> **BASE TABLE** · Dominio: **Core SIGA** · 19 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `AGENDABANDEJAID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `AGENDABANDEJAID` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `AGENDAFECHA` | datetime2 | 0% |
| 4 | `TAREATIPOID` | int | 0% |
| 5 | `TURNOID` | int | 0% |
| 6 | `AGENDANRO` | int | 0% |
| 7 | `AGENDABANDEJASTATUS` | varchar | 0% |
| 8 | `AGENDABANDEJASTATUSFIN` | varchar | 0% |
| 9 | `AGENDABANDEJAFCHINICIO` | datetime2 | 0% |
| 10 | `AGENDABANDEJAFCHFIN` | datetime2 | 62% |
| 11 | `AGENDABANDEJANOM` | varchar | 0% |
| 12 | `AGENDABANDEJADSC` | varchar | 0% |
| 13 | `AGENDABANDEJACONFIRMADA` | int | 0% |
| 14 | `AGENDABANDEJAPENDIENTE` | int | 0% |
| 15 | `AGENDABANDEJAUSRINICIO` | varchar | 0% |
| 16 | `AGENDABANDEJAUSRFIN` | varchar | 0% |
| 17 | `AGENDABANDEJATECNICOID` | int | 0% |
| 18 | `AGENDABANDEJADISPATCHER` | varchar | 0% |
| 19 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TAREATIPOID` (int) → [[clave-TAREATIPOID]]
- `TURNOID` (int) → [[clave-TURNOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
