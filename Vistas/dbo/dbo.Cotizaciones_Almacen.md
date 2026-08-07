---
esquema: dbo
tabla: Cotizaciones_Almacen
objeto: dbo.Cotizaciones_Almacen
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 4
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.Cotizaciones_Almacen

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SAP_COMPRAS.Moneda]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CotizacionClave` | varchar | 0% |
| 2 | `CotizacionKey` | nvarchar | 56% |
| 3 | `CotizacionFecha` | date | 0% |
| 4 | `CotizacionValor` | decimal | 35% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.Cotizaciones_Almacen
-- Extraida: 2026-08-07T15:27:32.325028+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[Cotizaciones_Almacen]
AS WITH Moneda AS (
    SELECT
        FCURR + '-' + TCURR AS MonedaUsdKey,
        FCURR + '-' + TCURR + '-' + GDATU AS CotizacionKey,
        FCURR AS MonedaOrigen,
        TCURR AS MonedaDestino,
        GDATU AS FechaValDesde,
        DATEFROMPARTS(
            SUBSTRING(GDATU, 1, 4),
            SUBSTRING(GDATU, 5, 2),
            SUBSTRING(GDATU, 7, 2)
        ) AS FechaCotizacion,
        UKURS AS Cotizacion
    FROM SAP_COMPRAS.Moneda
    WHERE FCURR + '-' + TCURR = 'ARS-USD'
      AND SUBSTRING(GDATU, 1, 4) >= '2016'
),

MinMaxFecha AS (
    SELECT
        DATEADD(DAY, -1, MIN(FechaCotizacion)) AS MinDate,
        MAX(FechaCotizacion) AS MaxDate
    FROM Moneda
),

Numeros AS (
    SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) - 1 AS n
    FROM sys.objects
),

Calendario AS (
    SELECT
        DATEADD(DAY, n, MinDate) AS FechaCotizacion
    FROM Numeros
    CROSS JOIN MinMaxFecha
    WHERE DATEADD(DAY, n, MinDate) <= MaxDate
),

MonedaExpandida AS (
    SELECT
        'ARS-USD' AS MonedaUsdKey,
        c.FechaCotizacion,
        m.Cotizacion,
        m.CotizacionKey
    FROM Calendario c
    LEFT JOIN Moneda m
        ON c.FechaCotizacion = m.FechaCotizacion
),

Cotizaciones AS (
    SELECT
        MonedaUsdKey,
        CotizacionKey,
        FechaCotizacion AS PrecioFecha,
        COALESCE(
            Cotizacion,
            LAG(Cotizacion) OVER (ORDER BY FechaCotizacion)
        ) AS Cotizacion
    FROM MonedaExpandida
)

SELECT
    MonedaUsdKey  AS CotizacionClave,
    CotizacionKey,
    PrecioFecha   AS CotizacionFecha,
    Cotizacion    AS CotizacionValor
FROM Cotizaciones
WHERE MonedaUsdKey = 'ARS-USD';
```
