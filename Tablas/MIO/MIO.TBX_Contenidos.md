---
esquema: MIO
tabla: TBX_Contenidos
objeto: MIO.TBX_Contenidos
tipo_objeto: BASE TABLE
dominio: MIO
canonico: true
grain: 1 fila = 1 `Id` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/MIO
  - dominio/mio
  - tipo/tabla-base
  - canonico
---

# MIO.TBX_Contenidos

> **BASE TABLE** · Dominio: **MIO** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | nvarchar | 0% |
| 2 | `ContentType` | nvarchar | 0% |
| 3 | `Title` | nvarchar | 0% |
| 4 | `Episode` | nvarchar | 18% |
| 5 | `SeriesTitle` | nvarchar | 18% |
| 6 | `AlternativeTitle` | nvarchar | 27% |
| 7 | `ReleaseYear` | nvarchar | 6% |
| 8 | `Duration` | nvarchar | 0% |
| 9 | `Season` | nvarchar | 18% |
| 10 | `Genres` | nvarchar | 4% |
| 11 | `description` | nvarchar | 10% |
| 12 | `fecha` | datetime2 | 0% |

## Claves de join presentes
- `Id` (nvarchar) → [[clave-ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
