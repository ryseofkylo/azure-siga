---
esquema: SIGASC
tabla: CRMPREINGRESO
objeto: SIGASC.CRMPREINGRESO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMPREINGRESOCOD` (único en muestra de 200)
n_columnas: 22
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMPREINGRESO

> **BASE TABLE** · Dominio: **Core SIGA** · 22 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMPREINGRESOCOD` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CRMPREINGRESOCOD` | varchar | 0% |
| 3 | `CRMTIPOPREINGRESO` | varchar | 0% |
| 4 | `CRMPREINGRESONOM` | varchar | 0% |
| 5 | `CRMPREINGMEDIO` | varchar | 29% |
| 6 | `CRMPREINGUSR` | varchar | 100% |
| 7 | `CRMDOCTPO` | varchar | 100% |
| 8 | `CRMPREINGSTS` | varchar | 3% |
| 9 | `CRMPREINGTIPO` | varchar | 17% |
| 10 | `CRMPREINGRESOUSR` | varchar | 99% |
| 11 | `CRMMOTIVO1` | int | 0% |
| 12 | `CRMMOTIVO2` | int | 0% |
| 13 | `CRMMOTIVO3` | int | 26% |
| 14 | `CRMMOTIVO4` | int | 62% |
| 15 | `CRMPREINGRESOOBS` | varchar | 78% |
| 16 | `CRMPREINGNIVELINI` | varchar | 20% |
| 17 | `CRMPREINGNIVELFIN` | varchar | 20% |
| 18 | `CRMLUGARID` | varchar | 100% |
| 19 | `CRMRESULTADO` | int | 99% |
| 20 | `CRMPREINGIVR` | int | 96% |
| 21 | `PIPELINERUNID` | varchar | 0% |
| 22 | `PKCRMPREINGRESOCOD` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CRMLUGARID` (varchar) → [[clave-CRMLUGARID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
