---
esquema: dbo
tabla: SG_Note
objeto: dbo.SG_Note
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `Id` (único en muestra de 200)
n_columnas: 3
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.SG_Note

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Value` | nvarchar | 0% |
| 3 | `CasoId` | bigint | 0% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `CasoId` (bigint) → [[clave-CASOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
