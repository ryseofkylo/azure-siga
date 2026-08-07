---
esquema: SIGASC
tabla: PREVENTACLICONDICION
objeto: SIGASC.PREVENTACLICONDICION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPREVENTACLICONDICION` (único en muestra de 200)
n_columnas: 17
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTACLICONDICION

> **BASE TABLE** · Dominio: **Core SIGA** · 17 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPREVENTACLICONDICION` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTACLICONDICION` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTANRO` | int | 0% |
| 4 | `PREVENTACONDID` | int | 0% |
| 5 | `PREVENTACLICONDFCHENV` | datetime2 | 100% |
| 6 | `PREVENTACLICONDUSRENV` | varchar | 0% |
| 7 | `PREVENTACLICONDFCHCUMP` | datetime2 | 0% |
| 8 | `PREVENTACLICONDUSRACE` | varchar | 0% |
| 9 | `PREVENTACLICONDUSRNOACE` | varchar | 0% |
| 10 | `PREVENTACLICONDFCHAGE` | datetime2 | 100% |
| 11 | `PREVENTACLICONDUSRAGE` | varchar | 0% |
| 12 | `PREVENTACLICONDSTS` | varchar | 0% |
| 13 | `PREVENTACLICONDOBS` | varchar | 0% |
| 14 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |
| 16 | `PKPREVENTANRO` | varchar | 0% |
| 17 | `PKPREVENTACONDID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `PREVENTACONDID` (int) → [[clave-PREVENTACONDID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (varchar) → [[clave-PKPREVENTANRO]]
- `PKPREVENTACONDID` (varchar) → [[clave-PKPREVENTACONDID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
