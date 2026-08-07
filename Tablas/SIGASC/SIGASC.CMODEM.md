---
esquema: SIGASC
tabla: CMODEM
objeto: SIGASC.CMODEM
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CMODEMID` (único en muestra de 200)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMODEM

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CMODEMID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CMSISTEMAID` | int | 0% |
| 2 | `CMODEMID` | varchar | 0% |
| 3 | `CMODEMHAB` | int | 0% |
| 4 | `CMODEMSTS` | varchar | 0% |
| 5 | `CMODEMFING` | datetime2 | 0% |
| 6 | `CMODEMFHAB` | datetime2 | 66% |
| 7 | `CMODEMSERIE` | varchar | 0% |
| 8 | `EMPRESAID` | int | 0% |
| 9 | `ARTICULOID` | int | 0% |
| 10 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `CMSISTEMAID` (int) → [[clave-CMSISTEMAID]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ARTICULOID` (int) → [[clave-ARTICULOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
