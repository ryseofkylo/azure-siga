---
esquema: SIGAMSASC
tabla: UNIDAD
objeto: SIGAMSASC.UNIDAD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `UNIDADID` (único en muestra de 127)
n_columnas: 23
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.UNIDAD

> **BASE TABLE** · Dominio: **Core SIGA** · 23 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `UNIDADID` (único en muestra de 127)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `UNIDADID` | int | 0% |
| 2 | `UNIDADNOMBRE` | varchar | 0% |
| 3 | `LICENCIAID` | int | 0% |
| 4 | `UNIDADALTACLIENTE` | int | 0% |
| 5 | `UNIDADFUSIONADA` | int | 0% |
| 6 | `UNIDADRAZONSOCIAL` | varchar | 0% |
| 7 | `UNIDADRUT` | varchar | 0% |
| 8 | `UNIDADDIRECCION` | varchar | 0% |
| 9 | `EMPRESAID` | int | 0% |
| 10 | `EMPRESAFISCALID` | int | 0% |
| 11 | `GERENTEID` | int | 2% |
| 12 | `UNIDADENTECODIGORP` | varchar | 0% |
| 13 | `UNIDADENTECODIGOBARRA` | varchar | 0% |
| 14 | `UNIDADTOTALIZASAP` | int | 1% |
| 15 | `UNIDADRESTRINGESERVICIO` | int | 89% |
| 16 | `UNIDADRESTRINGEORDENSRV` | int | 73% |
| 17 | `UNIDADRESTRINGEFACTURA` | int | 81% |
| 18 | `UNIDADRESTRINGERECIBO` | int | 81% |
| 19 | `UNIDADRESTRINGECAMPANIA` | int | 81% |
| 20 | `UNIDADRESTRINGECRM` | int | 81% |
| 21 | `UNIDADRESTRINGEPREVENTA` | int | 78% |
| 22 | `PIPELINERUNID` | varchar | 0% |
| 23 | `UNIDADCONCESIONARIO` | int | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `EMPRESAFISCALID` (int) → [[clave-EMPRESAFISCALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
