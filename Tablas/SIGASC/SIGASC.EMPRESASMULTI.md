---
esquema: SIGASC
tabla: EMPRESASMULTI
objeto: SIGASC.EMPRESASMULTI
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `EMPRESAID` (único en muestra de 27)
n_columnas: 3
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.EMPRESASMULTI

> **BASE TABLE** · Dominio: **Core SIGA** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `EMPRESAID` (único en muestra de 27)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `EMPRESANOM` | varchar | 0% |
| 3 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.ORDENTRB]] · `EMPRESASMULTI.EMPRESAID = ORDENTRB.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.ORDENSRV]] · `EMPRESASMULTI.EMPRESAID = ORDENSRV.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.CENTROOPERATIVO]] · `EMPRESASMULTI.EMPRESAID = CENTROOPERATIVO.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
