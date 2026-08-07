---
esquema: SIGASC
tabla: FACTURAOBS
objeto: SIGASC.FACTURAOBS
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKFACTURANRO` (único en muestra de 200)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURAOBS

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKFACTURANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKFACTURAOBS` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `FACTURATPO` | varchar | 0% |
| 4 | `FACTURANRO` | int | 0% |
| 5 | `FACTURAOBSLIN` | int | 0% |
| 6 | `FACTURAOBSDSC` | varchar | 0% |
| 7 | `FACTURAOBSFCH` | datetime2 | 0% |
| 8 | `FACTURAOBSUSR` | varchar | 0% |
| 9 | `FACTURAOBSENFACTURA` | int | 0% |
| 10 | `MENSAJEFACTURAID` | int | 0% |
| 11 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 12 | `PIPELINERUNID` | varchar | 0% |
| 13 | `PKFACTURATPO` | varchar | 0% |
| 14 | `PKFACTURANRO` | varchar | 0% |
| 15 | `PKFACTURAOBSLIN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `FACTURATPO` (varchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (int) → [[clave-FACTURANRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKFACTURATPO` (varchar) → [[clave-PKFACTURATPO]]
- `PKFACTURANRO` (varchar) → [[clave-PKFACTURANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
