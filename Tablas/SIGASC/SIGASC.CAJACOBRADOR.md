---
esquema: SIGASC
tabla: CAJACOBRADOR
objeto: SIGASC.CAJACOBRADOR
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCOBRADORID` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAJACOBRADOR

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCOBRADORID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCAJACOBRADOR` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CAJANRO` | int | 0% |
| 4 | `COBRADORID` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKCAJANRO` | varchar | 0% |
| 7 | `PKCOBRADORID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CAJANRO` (int) → [[clave-CAJANRO]]
- `COBRADORID` (int) → [[clave-COBRADORID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAJANRO` (varchar) → [[clave-PKCAJANRO]]
- `PKCOBRADORID` (varchar) → [[clave-PKCOBRADORID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
