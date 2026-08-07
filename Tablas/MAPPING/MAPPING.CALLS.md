---
esquema: MAPPING
tabla: CALLS
objeto: MAPPING.CALLS
tipo_objeto: BASE TABLE
dominio: Mapping
canonico: true
grain: 1 fila = 1 `IDEVENTOS` (único en muestra de 200)
n_columnas: 22
tags:
  - esquema/MAPPING
  - dominio/mapping
  - tipo/tabla-base
  - canonico
---

# MAPPING.CALLS

> **BASE TABLE** · Dominio: **Mapping** · 22 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `IDEVENTOS` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `IDEVENTOS` | bigint | 0% |
| 2 | `FECHA` | datetime2 | 0% |
| 3 | `HORA` | nvarchar | 0% |
| 4 | `DISCADO` | nvarchar | 0% |
| 5 | `ORIGEN` | nvarchar | 0% |
| 6 | `DESTINO` | nvarchar | 0% |
| 7 | `NOMBRE` | nvarchar | 0% |
| 8 | `DURACION` | nvarchar | 0% |
| 9 | `ID_LOCU` | int | 0% |
| 10 | `X1X2X3` | int | 0% |
| 11 | `POST_DISCADO` | nvarchar | 100% |
| 12 | `PIPELINERUNID` | nvarchar | 0% |
| 13 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 14 | `PERIODO` | nvarchar | 0% |
| 15 | `TOTALSEGUNDOS` | int | 0% |
| 16 | `TOTALHORAS` | float | 0% |
| 17 | `TOTALMINUTOS` | float | 0% |
| 18 | `PROVINCIA_ORIGEN` | nvarchar | 0% |
| 19 | `LOCALIDAD_ORIGEN` | nvarchar | 0% |
| 20 | `PROVINCIA_DESTINO` | nvarchar | 0% |
| 21 | `LOCALIDAD_DESTINO` | nvarchar | 0% |
| 22 | `GESTION` | nvarchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_MAPPINGCALLS]]
- [[dbo.V_MAPPINGCALLS_2021]]
