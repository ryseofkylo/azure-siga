---
esquema: SIGASC
tabla: PREVENTACLIENTEZONA
objeto: SIGASC.PREVENTACLIENTEZONA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPREVENTACLIENTEZONA` (único en muestra de 144)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTACLIENTEZONA

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPREVENTACLIENTEZONA` (único en muestra de 144)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTACLIENTEZONA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTANRO` | int | 0% |
| 4 | `PREVENTAZONATPO` | varchar | 0% |
| 5 | `PREVENTAZONAID` | int | 0% |
| 6 | `PREVENTAUSRING` | varchar | 0% |
| 7 | `PREVENTAZONAFCHING` | datetime2 | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKPREVENTANRO` | varchar | 0% |
| 10 | `PKPREVENTAZONATPO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (varchar) → [[clave-PKPREVENTANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
