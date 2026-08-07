---
esquema: SIGASC
tabla: COBRANZAMOVDETALLE
objeto: SIGASC.COBRANZAMOVDETALLE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `COBRANZAMOVFACTURANRO` (único en muestra de 200)
n_columnas: 19
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COBRANZAMOVDETALLE

> **BASE TABLE** · Dominio: **Core SIGA** · 19 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `COBRANZAMOVFACTURANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCOBRANZAMOVDETALLE` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `COBRANZAMOVID` | int | 0% |
| 4 | `COBRANZAMOVLINEA` | int | 0% |
| 5 | `COBRANZAMOVCLIENTENRO` | int | 0% |
| 6 | `COBRANZAMOVFACTURATPO` | varchar | 0% |
| 7 | `COBRANZAMOVFACTURANRO` | int | 0% |
| 8 | `COBRANZAMOVRECIBOFCH` | datetime2 | 2% |
| 9 | `COBRANZAMOVRECIBOLETRA` | varchar | 0% |
| 10 | `COBRANZAMOVRECIBOPTOVTA` | int | 0% |
| 11 | `COBRANZAMOVRECIBONRO` | int | 0% |
| 12 | `COBRANZAMOVIMP` | real | 0% |
| 13 | `COBRANZAMOVDETALLE` | varchar | 0% |
| 14 | `COBRANZAMOVSTS` | varchar | 0% |
| 15 | `COBRANZAMOVSTSDSC` | varchar | 0% |
| 16 | `COBRANZAMOVRECIBOGEN` | int | 0% |
| 17 | `PIPELINERUNID` | varchar | 0% |
| 18 | `PKCOBRANZAMOVID` | varchar | 0% |
| 19 | `PKCOBRANZAMOVLINEA` | varchar | 0% |

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
