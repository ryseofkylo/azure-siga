---
esquema: SIGASC
tabla: PREVENTAPRODUCTOARTICULO
objeto: SIGASC.PREVENTAPRODUCTOARTICULO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPREVENTAPRODUCTOARTICULO` (único en muestra de 42)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTAPRODUCTOARTICULO

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPREVENTAPRODUCTOARTICULO` (único en muestra de 42)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTAPRODUCTOARTICULO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTANRO` | int | 0% |
| 4 | `PREVENTAPRODLIN` | int | 0% |
| 5 | `ARTICULOID` | int | 0% |
| 6 | `ARTICULOSERIE` | varchar | 0% |
| 7 | `MATERIALID` | int | 0% |
| 8 | `PREVENTAPRODARTORDEN` | int | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKPREVENTANRO` | varchar | 0% |
| 11 | `PKPREVENTAPRODLIN` | varchar | 0% |
| 12 | `PKARTICULOID` | varchar | 0% |
| 13 | `PKARTICULOSERIE` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `ARTICULOID` (int) → [[clave-ARTICULOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (varchar) → [[clave-PKPREVENTANRO]]
- `PKPREVENTAPRODLIN` (varchar) → [[clave-PKPREVENTAPRODLIN]]
- `PKARTICULOID` (varchar) → [[clave-PKARTICULOID]]
- `PKARTICULOSERIE` (varchar) → [[clave-PKARTICULOSERIE]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
