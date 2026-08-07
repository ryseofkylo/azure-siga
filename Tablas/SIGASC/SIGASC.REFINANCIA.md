---
esquema: SIGASC
tabla: REFINANCIA
objeto: SIGASC.REFINANCIA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKREFINANCIANRO` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.REFINANCIA

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKREFINANCIANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `REFINANCIANRO` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `REFINANCIAFCH` | datetime2 | 0% |
| 5 | `REFINANCIAUSR` | varchar | 0% |
| 6 | `CUOTAID` | int | 0% |
| 7 | `MONEDAID` | int | 0% |
| 8 | `REFINANCIAIMP` | real | 0% |
| 9 | `REFINANCIAINTREFI` | real | 0% |
| 10 | `REFINANCIAINTPAGO` | real | 0% |
| 11 | `REFINANCIASTS` | varchar | 0% |
| 12 | `REFINANCIARECIBONRO` | int | 0% |
| 13 | `REFINANCIAENTREGA` | real | 0% |
| 14 | `REFINANCIAQUITAINTERES` | real | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |
| 16 | `PKREFINANCIANRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `REFINANCIANRO` (int) → [[clave-REFINANCIANRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `CUOTAID` (int) → [[clave-CUOTAID]]
- `MONEDAID` (int) → [[clave-MONEDAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKREFINANCIANRO` (varchar) → [[clave-PKREFINANCIANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
