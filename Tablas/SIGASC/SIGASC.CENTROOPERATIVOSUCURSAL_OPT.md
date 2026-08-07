---
esquema: SIGASC
tabla: CENTROOPERATIVOSUCURSAL_OPT
objeto: SIGASC.CENTROOPERATIVOSUCURSAL_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CENTROOPESUCURSALID` (único en muestra de 186)
n_columnas: 4
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CENTROOPERATIVOSUCURSAL_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CENTROOPESUCURSALID` (único en muestra de 186)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CENTROOPERATIVOID` | nvarchar | 0% |
| 3 | `CENTROOPESUCURSALID` | nvarchar | 0% |
| 4 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CENTROOPERATIVOID` (nvarchar) → [[clave-CENTROOPERATIVOID]]
- `CENTROOPESUCURSALID` (nvarchar) → [[clave-CENTROOPESUCURSALID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
