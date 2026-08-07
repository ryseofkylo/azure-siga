---
esquema: dbo
tabla: Cant_registros_diarios
objeto: dbo.Cant_registros_diarios
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `TableName`, `Cantidad`, `SchemaName`
n_columnas: 5
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.Cant_registros_diarios

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `TableName`, `Cantidad`, `SchemaName`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Cantidad` | int | 0% |
| 2 | `SchemaName` | nvarchar | 0% |
| 3 | `TableName` | nvarchar | 0% |
| 4 | `SourceType` | nvarchar | 0% |
| 5 | `Max_MODIFIEDDATE` | datetime2 | 100% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
