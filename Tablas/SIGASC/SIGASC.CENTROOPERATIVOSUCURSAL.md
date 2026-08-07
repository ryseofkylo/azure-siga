---
esquema: SIGASC
tabla: CENTROOPERATIVOSUCURSAL
objeto: SIGASC.CENTROOPERATIVOSUCURSAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCENTROOPESUCURSALID` (único en muestra de 188)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CENTROOPERATIVOSUCURSAL

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCENTROOPESUCURSALID` (único en muestra de 188)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCENTROOPERATIVOSUCURSAL` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CENTROOPERATIVOID` | int | 0% |
| 4 | `CENTROOPESUCURSALID` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKCENTROOPERATIVOID` | varchar | 0% |
| 7 | `PKCENTROOPESUCURSALID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CENTROOPERATIVOID` (int) → [[clave-CENTROOPERATIVOID]]
- `CENTROOPESUCURSALID` (int) → [[clave-CENTROOPESUCURSALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCENTROOPERATIVOID` (varchar) → [[clave-PKCENTROOPERATIVOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.ORDENTRB]] · `CENTROOPERATIVOSUCURSAL.EMPRESAID = ORDENTRB.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.ORDENTRB]] · `CENTROOPERATIVOSUCURSAL.CENTROOPERATIVOID = ORDENTRB.CENTROOPERATIVOID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.VM_CLIENTE]] · `CENTROOPERATIVOSUCURSAL.CENTROOPESUCURSALID = VM_CLIENTE.SUCURSALID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.VM_CLIENTE]] · `CENTROOPERATIVOSUCURSAL.EMPRESAID = VM_CLIENTE.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
