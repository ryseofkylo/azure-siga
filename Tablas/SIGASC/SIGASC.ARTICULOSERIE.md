---
esquema: SIGASC
tabla: ARTICULOSERIE
objeto: SIGASC.ARTICULOSERIE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKARTICULOSERIE` (único en muestra de 200)
n_columnas: 24
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ARTICULOSERIE

> **BASE TABLE** · Dominio: **Core SIGA** · 24 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKARTICULOSERIE` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKARTICULOSERIE` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `ARTICULOID` | int | 0% |
| 4 | `ARTICULOSERIE` | varchar | 0% |
| 5 | `ARTICULOFCHING` | datetime2 | 0% |
| 6 | `ARTICULOUSRING` | varchar | 0% |
| 7 | `ARTICULOSTS` | varchar | 0% |
| 8 | `CENTROSTKID` | int | 0% |
| 9 | `CLIENTENRO` | int | 0% |
| 10 | `CONTRATONROART` | int | 1% |
| 11 | `ARTICULOOBS` | varchar | 1% |
| 12 | `ARTICULOPROPIEDAD` | varchar | 0% |
| 13 | `ARTICULOFCHASI` | datetime2 | 2% |
| 14 | `ARTICULOUSRASI` | varchar | 0% |
| 15 | `ARTICULOCND` | varchar | 0% |
| 16 | `ARTICULONROACTIVO` | int | 6% |
| 17 | `GPONNAPID` | int | 15% |
| 18 | `ARTICULOESNUEVO` | int | 0% |
| 19 | `ARTICULOESREFUNCIONALIZADO` | int | 6% |
| 20 | `DESPACHOVENTANRO` | varchar | 100% |
| 21 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 22 | `PIPELINERUNID` | varchar | 0% |
| 23 | `PKARTICULOSERIE` | varchar | 0% |
| 24 | `PKARTICULOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ARTICULOID` (int) → [[clave-ARTICULOID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKARTICULOSERIE` (varchar) → [[clave-PKARTICULOSERIE]]
- `PKARTICULOID` (varchar) → [[clave-PKARTICULOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
