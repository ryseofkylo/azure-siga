---
esquema: SIGASC
tabla: PREVENTAPRODCONDICION
objeto: SIGASC.PREVENTAPRODCONDICION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPREVENTAPRODCONDICION` (único en muestra de 200)
n_columnas: 20
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTAPRODCONDICION

> **BASE TABLE** · Dominio: **Core SIGA** · 20 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPREVENTAPRODCONDICION` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTAPRODCONDICION` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTANRO` | int | 0% |
| 4 | `PREVENTAPRODLIN` | int | 0% |
| 5 | `PREVENTACONDID` | int | 0% |
| 6 | `PREVENTAPRODCONDFCHENV` | datetime2 | 100% |
| 7 | `PREVENTAPRODCONDUSRENV` | varchar | 0% |
| 8 | `PREVENTAPRODCONDFCHCUMP` | datetime2 | 2% |
| 9 | `PREVENTAPRODCONDUSRACE` | varchar | 0% |
| 10 | `PREVENTAPRODCONDFCHNOACE` | datetime2 | 100% |
| 11 | `PREVENTAPRODCONDUSRNOACE` | varchar | 0% |
| 12 | `PREVENTAPRODCONDFCHAGE` | datetime2 | 100% |
| 13 | `PREVENTAPRODCONDUSRAGE` | varchar | 0% |
| 14 | `PREVENTAPRODCONDSTS` | varchar | 0% |
| 15 | `PREVENTAPRODCONDOBS` | varchar | 0% |
| 16 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 17 | `PIPELINERUNID` | varchar | 0% |
| 18 | `PKPREVENTANRO` | varchar | 0% |
| 19 | `PKPREVENTAPRODLIN` | varchar | 0% |
| 20 | `PKPREVENTACONDID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `PREVENTACONDID` (int) → [[clave-PREVENTACONDID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (varchar) → [[clave-PKPREVENTANRO]]
- `PKPREVENTAPRODLIN` (varchar) → [[clave-PKPREVENTAPRODLIN]]
- `PKPREVENTACONDID` (varchar) → [[clave-PKPREVENTACONDID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
