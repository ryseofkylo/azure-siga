---
esquema: dbo
tabla: Precios_Almacen
objeto: dbo.Precios_Almacen
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

# dbo.Precios_Almacen

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SAP_COMPRAS.Movimientos]]
- [[SAP_COMPRAS.Precio]]
- [[SAP_COMPRAS.StockInicial]]
- [[dbo.Cotizaciones_Almacen]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MaterialPrecioKey` | varchar | 0% |
| 2 | `PrecioEstandar` | decimal | 0% |
| 3 | `PrecioFecha` | date | 33% |
| 4 | `Cotizacion` | decimal | 100% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.Precios_Almacen
-- Extraida: 2026-08-07T15:27:34.346075+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[Precios_Almacen]
AS WITH UltimaCompraTmp AS (
    SELECT
        CONCAT(MATNR,'-',WERKS,'-',BWTAR,'-',SOBKZ,'-',PSPNR) AS MaterialPrecioKey,
        MAX(CAST(BLDAT AS date)) AS UltFecha
    FROM SAP_COMPRAS.Movimientos
    GROUP BY
        MATNR, WERKS, BWTAR, SOBKZ, PSPNR

    UNION ALL

    SELECT
        CONCAT(MATNR,'-',WERKS,'-',BWTAR,'-',SOBKZ,'-',PSPNR) AS MaterialPrecioKey,
        CAST('2019-12-31' AS date) AS UltFecha
    FROM SAP_COMPRAS.StockInicial
    GROUP BY
        MATNR, WERKS, BWTAR, SOBKZ, PSPNR
),

UltimaCompra AS (
    SELECT
        MaterialPrecioKey,
        MAX(UltFecha) AS PrecioFecha
    FROM UltimaCompraTmp
    GROUP BY MaterialPrecioKey
),

PreciosTmp AS (
    SELECT
        CONCAT(MATNR,'-',WERKS,'-',BWTAR,'-',SOBKZ,'-',PSPNR) AS MaterialPrecioKey,
        STPRS AS PrecioEstandar
    FROM SAP_COMPRAS.Precio
)

SELECT
    p.MaterialPrecioKey,
    p.PrecioEstandar,
    u.PrecioFecha,
    c.CotizacionValor AS Cotizacion
FROM PreciosTmp p
LEFT JOIN UltimaCompra u
    ON p.MaterialPrecioKey = u.MaterialPrecioKey
LEFT JOIN dbo.Cotizaciones_Almacen c
    ON c.CotizacionFecha = u.PrecioFecha;
```
