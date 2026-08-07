---
esquema: SIGASC
tabla: COBRANZAMOVIMIENTO
objeto: SIGASC.COBRANZAMOVIMIENTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCOBRANZAMOVID` (único en muestra de 200)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COBRANZAMOVIMIENTO

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCOBRANZAMOVID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `COBRANZAMOVID` | int | 0% |
| 3 | `COBRANZAMOVDSC` | varchar | 0% |
| 4 | `COBRANZAMOVSTATUS` | varchar | 0% |
| 5 | `COBRANZAMOVFCH` | datetime2 | 0% |
| 6 | `COBRANZAMOVUSR` | varchar | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |
| 8 | `PKCOBRANZAMOVID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCOBRANZAMOVID` (varchar) → [[clave-PKCOBRANZAMOVID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
