---
esquema: SIGASC
tabla: TURNO
objeto: SIGASC.TURNO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKTURNOID` (único en muestra de 125)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.TURNO

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKTURNOID` (único en muestra de 125)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `TURNOID` | int | 0% |
| 3 | `TURNONOMBRE` | varchar | 0% |
| 4 | `TURNOHORAINICIO` | datetime2 | 100% |
| 5 | `TURNOHORAFINAL` | datetime2 | 100% |
| 6 | `PRODUCTIVIDADTURNOID` | int | 2% |
| 7 | `TURNOESTADO` | varchar | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKTURNOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TURNOID` (int) → [[clave-TURNOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKTURNOID` (varchar) → [[clave-PKTURNOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
