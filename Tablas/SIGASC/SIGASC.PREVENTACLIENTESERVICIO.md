---
esquema: SIGASC
tabla: PREVENTACLIENTESERVICIO
objeto: SIGASC.PREVENTACLIENTESERVICIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPREVENTACLIENTESERVICIO` (único en muestra de 193)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTACLIENTESERVICIO

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPREVENTACLIENTESERVICIO` (único en muestra de 193)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTACLIENTESERVICIO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTANRO` | int | 0% |
| 4 | `PREVENTASRVLIN` | int | 0% |
| 5 | `SERVICIOID` | int | 0% |
| 6 | `PREVENTASRVORDEN` | int | 72% |
| 7 | `PREVENTACLISRVNRO` | int | 37% |
| 8 | `PREVENTASRVCANTIDAD` | int | 0% |
| 9 | `PREVENTASRVFACTURA` | varchar | 0% |
| 10 | `SERVICIOTARIFAID` | int | 30% |
| 11 | `CUOTAID` | int | 30% |
| 12 | `PIPELINERUNID` | varchar | 0% |
| 13 | `PKPREVENTANRO` | varchar | 0% |
| 14 | `PKPREVENTASRVLIN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `SERVICIOID` (int) → [[clave-SERVICIOID]]
- `SERVICIOTARIFAID` (int) → [[clave-SERVICIOTARIFAID]]
- `CUOTAID` (int) → [[clave-CUOTAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (varchar) → [[clave-PKPREVENTANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
