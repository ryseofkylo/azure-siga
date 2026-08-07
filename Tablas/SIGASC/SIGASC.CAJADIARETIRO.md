---
esquema: SIGASC
tabla: CAJADIARETIRO
objeto: SIGASC.CAJADIARETIRO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCAJADIARETIRO` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAJADIARETIRO

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCAJADIARETIRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCAJADIARETIRO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CAJADIAFCH` | datetime2 | 0% |
| 4 | `CAJANRO` | int | 0% |
| 5 | `CAJADIARETIRONRO` | int | 0% |
| 6 | `CPGOTIPOID` | int | 0% |
| 7 | `MONEDAID` | int | 0% |
| 8 | `CAJADIARETIROIMP` | real | 0% |
| 9 | `CAJADIARETIROENTREGA` | varchar | 0% |
| 10 | `CAJADIARETIROOBS` | varchar | 0% |
| 11 | `CAJADIARETIROFCH` | datetime2 | 0% |
| 12 | `CAJADIARETIROUSR` | varchar | 0% |
| 13 | `CAJARETIROTIPO` | int | 0% |
| 14 | `PIPELINERUNID` | varchar | 0% |
| 15 | `PKCAJANRO` | varchar | 0% |
| 16 | `PKCAJADIARETIRONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CAJANRO` (int) → [[clave-CAJANRO]]
- `CPGOTIPOID` (int) → [[clave-CPGOTIPOID]]
- `MONEDAID` (int) → [[clave-MONEDAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAJANRO` (varchar) → [[clave-PKCAJANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
