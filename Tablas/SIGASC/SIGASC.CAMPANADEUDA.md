---
esquema: SIGASC
tabla: CAMPANADEUDA
objeto: SIGASC.CAMPANADEUDA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CAMDEUDAFACTURANRO` (único en muestra de 200)
n_columnas: 28
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAMPANADEUDA

> **BASE TABLE** · Dominio: **Core SIGA** · 28 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CAMDEUDAFACTURANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCAMPANADEUDA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CRMNRO` | int | 0% |
| 4 | `CAMGESID` | int | 0% |
| 5 | `CAMDEUDAFACTURATOT` | real | 0% |
| 6 | `CAMDEUDAFACTURATPO` | varchar | 0% |
| 7 | `CAMDEUDAFACTURANRO` | int | 0% |
| 8 | `CAMDEUDARECARGO` | int | 0% |
| 9 | `CAMDEUDAIMPORTE` | real | 0% |
| 10 | `CAMDEUDACODBARRA` | varchar | 0% |
| 11 | `CAMDEUDAEXCLUIDA` | int | 0% |
| 12 | `CAMDEUDAFACTURATOTV2` | real | 0% |
| 13 | `CAMDEUDAFACTURAVTO` | datetime2 | 0% |
| 14 | `CAMDEUDAID` | int | 0% |
| 15 | `CAMDEUDAIMPORTEV3` | real | 0% |
| 16 | `CAMDEUDAIMPORTEV2` | real | 0% |
| 17 | `CAMDEUDAFACTURAVTO3` | datetime2 | 44% |
| 18 | `CAMDEUDAFACTURAVTO2` | datetime2 | 44% |
| 19 | `CAMDEUDAFACTURATOTV3` | real | 0% |
| 20 | `CAMDEUDAPOSTERIORFCH` | datetime2 | 100% |
| 21 | `CAMDEUDAPOSTERIORUSR` | varchar | 44% |
| 22 | `CAMDEUDAPOSTERIORES` | int | 44% |
| 23 | `CAMDEUDAFACTURAPERIODO` | int | 44% |
| 24 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 25 | `PIPELINERUNID` | varchar | 0% |
| 26 | `PKCAMGESID` | varchar | 0% |
| 27 | `PKCRMNRO` | varchar | 0% |
| 28 | `PKCAMDEUDAID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CRMNRO` (int) → [[clave-CRMNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAMGESID` (varchar) → [[clave-PKCAMGESID]]
- `PKCRMNRO` (varchar) → [[clave-PKCRMNRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
