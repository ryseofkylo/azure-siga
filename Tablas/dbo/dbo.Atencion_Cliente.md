---
esquema: dbo
tabla: Atencion_Cliente
objeto: dbo.Atencion_Cliente
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `ID_conversacion` (único en muestra de 200)
n_columnas: 17
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.Atencion_Cliente

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 17 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ID_conversacion` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Exportacion` | nvarchar | 0% |
| 2 | `Filtros` | nvarchar | 96% |
| 3 | `Tipo_de_medios` | nvarchar | 0% |
| 4 | `Usuarios` | nvarchar | 46% |
| 5 | `Fecha` | datetime2 | 0% |
| 6 | `Duracion` | time | 0% |
| 7 | `Cola` | nvarchar | 40% |
| 8 | `Conclusion` | nvarchar | 46% |
| 9 | `Etiqueta_externa` | nvarchar | 33% |
| 10 | `ANI` | nvarchar | 0% |
| 11 | `DNIS` | nvarchar | 0% |
| 12 | `ID_conversacion` | nvarchar | 0% |
| 13 | `Transferidas` | nvarchar | 0% |
| 14 | `Abandonadas` | nvarchar | 0% |
| 15 | `Retencion_total` | nvarchar | 90% |
| 16 | `Manejo_total` | nvarchar | 46% |
| 17 | `Flujo` | nvarchar | 4% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
