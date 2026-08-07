---
esquema: SIGASC
tabla: PREVENTAPRODUCTOTEMPORAL
objeto: SIGASC.PREVENTAPRODUCTOTEMPORAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPREVENTANRO` (único en muestra de 47)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTAPRODUCTOTEMPORAL

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPREVENTANRO` (único en muestra de 47)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTAPRODUCTOTEMPORAL` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTANRO` | int | 0% |
| 4 | `PREVENTAPRODLIN` | int | 0% |
| 5 | `PRODUCTOTEMPORALID` | int | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKPREVENTANRO` | varchar | 0% |
| 8 | `PKPREVENTAPRODLIN` | varchar | 0% |
| 9 | `PKPRODUCTOTEMPORALID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (varchar) → [[clave-PKPREVENTANRO]]
- `PKPREVENTAPRODLIN` (varchar) → [[clave-PKPREVENTAPRODLIN]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
