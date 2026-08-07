---
esquema: SIGASC
tabla: CENTROOPERATIVO_OPT
objeto: SIGASC.CENTROOPERATIVO_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CENTROOPERATIVOID` (único en muestra de 36)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CENTROOPERATIVO_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CENTROOPERATIVOID` (único en muestra de 36)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CENTROOPERATIVOID` | nvarchar | 0% |
| 3 | `CENTROOPERATIVONOMBRE` | nvarchar | 0% |
| 4 | `GEOCENTROOPERATIVOCORDY2` | nvarchar | 78% |
| 5 | `GEOCENTROOPERATIVOCORDX2` | nvarchar | 78% |
| 6 | `GEOCENTROOPERATIVOCORDY1` | nvarchar | 78% |
| 7 | `GEOCENTROOPERATIVOCORDX1` | nvarchar | 78% |
| 8 | `CENTROOPERATIVOCRITERIO` | nvarchar | 0% |
| 9 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CENTROOPERATIVOID` (nvarchar) → [[clave-CENTROOPERATIVOID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
