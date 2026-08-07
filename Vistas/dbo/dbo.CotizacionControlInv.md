---
esquema: dbo
tabla: CotizacionControlInv
objeto: dbo.CotizacionControlInv
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

# dbo.CotizacionControlInv

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SAP_COMPRAS.Moneda]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CotizacionClave` | varchar | 0% |
| 2 | `CotizacionKey` | nvarchar | 0% |
| 3 | `CotizacionFecha` | date | 0% |
| 4 | `CotizacionValor` | decimal | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.CotizacionControlInv
-- Extraida: 2026-08-07T15:27:31.995020+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[CotizacionControlInv]
AS WITH Base AS (
    SELECT
        CONCAT(FCURR, '-', TCURR) AS MonedaUsdKey,
        CONVERT(date, STUFF(STUFF(GDATU, 5, 0, '-'), 8, 0, '-')) AS CotizacionFecha,
        UKURS AS Cotizacion
    FROM SAP_COMPRAS.Moneda
    WHERE CONCAT(FCURR, '-', TCURR) = 'ARS-USD'
),

RangoFechas AS (
    SELECT
        MIN(CotizacionFecha) AS FechaMin,
        MAX(CotizacionFecha) AS FechaMax
    FROM Base
),

-- Generador de números (0...N)
Nums AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) - 1 AS n
    FROM sys.objects
),

Calendario AS (
    SELECT
        DATEADD(DAY, n, rf.FechaMin) AS CotizacionFecha
    FROM RangoFechas rf
    JOIN Nums n
        ON DATEADD(DAY, n.n, rf.FechaMin) <= rf.FechaMax
),

Serie AS (
    SELECT
        'ARS-USD' AS MonedaUsdKey,
        c.CotizacionFecha,
        b.Cotizacion
    FROM Calendario c
    LEFT JOIN Base b
        ON b.CotizacionFecha = c.CotizacionFecha
),

Grupo AS (
    SELECT
        MonedaUsdKey,
        CotizacionFecha,
        Cotizacion,
        SUM(CASE WHEN Cotizacion IS NOT NULL THEN 1 ELSE 0 END)
            OVER (ORDER BY CotizacionFecha) AS Grupo
    FROM Serie
)

SELECT
    MonedaUsdKey AS CotizacionClave,
    CONCAT(
        MonedaUsdKey, '-',
        FORMAT(CotizacionFecha, 'yyyyMMdd')
    ) AS CotizacionKey,
    CotizacionFecha,
    MAX(Cotizacion) OVER (PARTITION BY Grupo) AS CotizacionValor
FROM Grupo;
```
