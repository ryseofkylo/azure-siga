---
esquema: SIGASC
tabla: CENTROOPERATIVO
objeto: SIGASC.CENTROOPERATIVO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCENTROOPERATIVOID` (único en muestra de 38)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CENTROOPERATIVO

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCENTROOPERATIVOID` (único en muestra de 38)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CENTROOPERATIVOID` | int | 0% |
| 3 | `CENTROOPERATIVONOMBRE` | varchar | 0% |
| 4 | `GEOCENTROOPERATIVOCORDY2` | varchar | 8% |
| 5 | `GEOCENTROOPERATIVOCORDX2` | varchar | 8% |
| 6 | `GEOCENTROOPERATIVOCORDY1` | varchar | 8% |
| 7 | `GEOCENTROOPERATIVOCORDX1` | varchar | 8% |
| 8 | `CENTROOPERATIVOCRITERIO` | varchar | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCENTROOPERATIVOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CENTROOPERATIVOID` (int) → [[clave-CENTROOPERATIVOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCENTROOPERATIVOID` (varchar) → [[clave-PKCENTROOPERATIVOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.EMPRESASMULTI]] · `CENTROOPERATIVO.EMPRESAID = EMPRESASMULTI.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
- [[dbo.V_CENTROOPERATIVO]]
