---
esquema: SIGASC
tabla: RECIBOOBS
objeto: SIGASC.RECIBOOBS
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.RECIBOOBS

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKRECIBOOBS` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `RECIBONRO` | int | 0% |
| 4 | `RECIBOOBSLIN` | int | 0% |
| 5 | `RECIBOOBSDSC` | varchar | 0% |
| 6 | `RECIBOOBSFCH` | datetime2 | 0% |
| 7 | `RECIBOOBSUSR` | varchar | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKRECIBONRO` | varchar | 0% |
| 10 | `PKRECIBOOBSLIN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `RECIBONRO` (int) → [[clave-RECIBONRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKRECIBONRO` (varchar) → [[clave-PKRECIBONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
