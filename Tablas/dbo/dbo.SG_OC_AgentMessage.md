---
esquema: dbo
tabla: SG_OC_AgentMessage
objeto: dbo.SG_OC_AgentMessage
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `Id` (único en muestra de 200)
n_columnas: 5
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.SG_OC_AgentMessage

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Date` | datetime2 | 0% |
| 3 | `Context` | nvarchar | 100% |
| 4 | `Name` | nvarchar | 100% |
| 5 | `OC_CasoId` | bigint | 0% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `OC_CasoId` (bigint) → [[clave-OC_CASOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
