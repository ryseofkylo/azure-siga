---
esquema: SIGASC
tabla: CRMREGISTRO_CAPTACION
objeto: SIGASC.CRMREGISTRO_CAPTACION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMNRO` (único en muestra de 200)
n_columnas: 28
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMREGISTRO_CAPTACION

> **BASE TABLE** · Dominio: **Core SIGA** · 28 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CRMNRO` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `CRMFCHINI` | datetime2 | 0% |
| 5 | `CRMFCHFIN` | datetime2 | 4% |
| 6 | `CRMUSRING` | varchar | 0% |
| 7 | `CRMUSRACT` | varchar | 4% |
| 8 | `CRMTIPO` | varchar | 0% |
| 9 | `CRMMEDIO` | varchar | 0% |
| 10 | `CRMNIVELINI` | varchar | 0% |
| 11 | `CRMNIVELFIN` | varchar | 0% |
| 12 | `CRMRESULTADO` | int | 0% |
| 13 | `CRMSTS` | varchar | 0% |
| 14 | `CRMOBS` | varchar | 0% |
| 15 | `CRMMOTIVO1` | int | 0% |
| 16 | `CRMMOTIVO2` | int | 2% |
| 17 | `CRMMOTIVO3` | int | 3% |
| 18 | `CRMMOTIVO4` | int | 4% |
| 19 | `CRMDOCTPO` | varchar | 0% |
| 20 | `CRMDOCCOD` | varchar | 0% |
| 21 | `CRMLUGARID` | varchar | 0% |
| 22 | `CRMFCHAUX` | datetime2 | 100% |
| 23 | `CRMARCAUDIO` | varchar | 0% |
| 24 | `CRMCAMNRO` | int | 0% |
| 25 | `CRMFLGINGIVR` | int | 0% |
| 26 | `CRMCLASE` | varchar | 0% |
| 27 | `PIPELINERUNID` | varchar | 0% |
| 28 | `PKCRMNRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CRMNRO` (int) → [[clave-CRMNRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `CRMLUGARID` (varchar) → [[clave-CRMLUGARID]]
- `CRMCAMNRO` (int) → [[clave-CRMCAMNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMNRO` (varchar) → [[clave-PKCRMNRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
