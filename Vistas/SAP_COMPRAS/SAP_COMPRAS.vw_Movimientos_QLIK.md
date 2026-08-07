---
esquema: SAP_COMPRAS
tabla: vw_Movimientos_QLIK
objeto: SAP_COMPRAS.vw_Movimientos_QLIK
tipo_objeto: VIEW
dominio: Compras y Finanzas (SAP)
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 42
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/vista
  - referencia
---

# SAP_COMPRAS.vw_Movimientos_QLIK

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SAP_COMPRAS.ControlInventario]]
- [[SAP_COMPRAS.Material]]
- [[SAP_COMPRAS.Movimientos]]
- [[SAP_COMPRAS.Precio]]
- [[SAP_COMPRAS.StockInicial]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `TipoMov` | varchar |  |
| 2 | `MaterialId` | nvarchar |  |
| 3 | `Centro` | nvarchar |  |
| 4 | `Almacen` | nvarchar |  |
| 5 | `ClaseValoracion` | nvarchar |  |
| 6 | `StockEspecial` | nvarchar |  |
| 7 | `ElementoPep` | nvarchar |  |
| 8 | `DebeHaber` | nvarchar |  |
| 9 | `Lote` | nvarchar |  |
| 10 | `Documento` | nvarchar |  |
| 11 | `Ejercicio` | nvarchar |  |
| 12 | `PosicionDoc` | nvarchar |  |
| 13 | `ClaseMovimientoId` | nvarchar |  |
| 14 | `ProveedorId` | nvarchar |  |
| 15 | `Moneda` | nvarchar |  |
| 16 | `DivisionId` | nvarchar |  |
| 17 | `CentroCostoId` | nvarchar |  |
| 18 | `EmpresaId` | nvarchar |  |
| 19 | `Fecha` | date |  |
| 20 | `FechaDocumento` | date |  |
| 21 | `FechaEntrada` | date |  |
| 22 | `FechaModificacion` | date |  |
| 23 | `UsuarioUltModif` | nvarchar |  |
| 24 | `CuentaMayor` | nvarchar |  |
| 25 | `MaterialPrecioKey` | nvarchar |  |
| 26 | `ClaseMovimientoKey` | nvarchar |  |
| 27 | `Proyecto` | nvarchar |  |
| 28 | `PeriodoSalId` | bigint |  |
| 29 | `CantidadEntrada` | decimal |  |
| 30 | `CantidadSalida` | decimal |  |
| 31 | `Cantidad` | decimal |  |
| 32 | `DocumentoControl` | nvarchar |  |
| 33 | `ControlPeriodo` | nvarchar |  |
| 34 | `FechaRecuento` | date |  |
| 35 | `CantidadTeorica` | decimal |  |
| 36 | `UnidadMedida` | nvarchar |  |
| 37 | `TipoStockId` | nvarchar |  |
| 38 | `CantxPrecioT` | decimal |  |
| 39 | `CantxPrecioR` | decimal |  |
| 40 | `SaldoAcum` | decimal |  |
| 41 | `SKU` | int |  |
| 42 | `SaldoUSDAcum` | decimal |  |

## Definición (CREATE VIEW)
```sql
-- Vista: SAP_COMPRAS.vw_Movimientos_QLIK
-- Extraida: 2026-08-07T15:28:36.825745+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [SAP_COMPRAS].[vw_Movimientos_QLIK]
AS WITH 
-- =============================================================================
-- CTE 1: Movimientos SAP (igual que QLIK Movimientos.txt líneas 2-36)
-- =============================================================================
MovimientosMOV AS (
    SELECT 
        'MOV' AS TipoMov,
        m.MATNR AS MaterialId,
        m.WERKS AS Centro,
        m.LGORT AS Almacen,
        m.BWTAR AS ClaseValoracion,
        m.SOBKZ AS StockEspecial,
        m.PSPNR AS ElementoPep,
        m.SHKZG AS DebeHaber,
        TRY_CAST(REPLACE(m.MENGE, ',', '.') AS DECIMAL(18,3)) AS MENGE,
        TRY_CAST(REPLACE(m.DMBTR, ',', '.') AS DECIMAL(18,2)) AS DMBTR,
        m.CHARG, m.MBLNR, m.MJAHR, m.ZEILE, m.BWART, m.LIFNR, m.WAERS, m.GSBER, m.KOSTL, m.BUKRS,
        TRY_CAST(m.BLDAT AS DATE) AS BLDAT,
        TRY_CAST(m.BUDAT AS DATE) AS BUDAT,
        TRY_CAST(m.CPUDT AS DATE) AS CPUDT,
        TRY_CAST(m.AEDAT AS DATE) AS AEDAT,
        m.USNAM, m.SAKTO,
        -- Claves
        CONCAT(m.MATNR, '-', m.WERKS, '-', ISNULL(m.BWTAR,''), '-', ISNULL(m.SOBKZ,''), '-', ISNULL(m.PSPNR,'')) AS MaterialPrecioKey,
        CASE WHEN TRY_CAST(LEFT(m.PSPNR, 1) AS INT) <> 1 THEN 'No' ELSE 'Si' END AS Proyecto,
        (YEAR(TRY_CAST(m.BUDAT AS DATE)) - 1) * 12 + MONTH(TRY_CAST(m.BUDAT AS DATE)) AS PeriodoSalId
    FROM SAP_COMPRAS.Movimientos m
    WHERE EXISTS (SELECT 1 FROM SAP_COMPRAS.Material mat WHERE mat.MATNR = m.MATNR)
      AND LEFT(m.LGORT, 1) <> 'M'
      AND m.LGORT <> '0000'
),

-- =============================================================================
-- CTE 2: Stock Inicial (igual que QLIK Movimientos.txt líneas 45-74)
-- =============================================================================
MovimientosSI AS (
    SELECT 
        'S.I' AS TipoMov,
        si.MATNR AS MaterialId,
        si.WERKS AS Centro,
        si.LGORT AS Almacen,
        si.BWTAR AS ClaseValoracion,
        si.SOBKZ AS StockEspecial,
        si.PSPNR AS ElementoPep,
        'S' AS DebeHaber,
        TRY_CAST(REPLACE(si.Cantidad, ',', '.') AS DECIMAL(18,3)) AS MENGE,
        TRY_CAST(REPLACE(si.DMBTR, ',', '.') AS DECIMAL(18,2)) AS DMBTR,
        CAST(NULL AS NVARCHAR(50)) AS CHARG,
        CAST(NULL AS NVARCHAR(50)) AS MBLNR,
        CAST(NULL AS NVARCHAR(50)) AS MJAHR,
        CAST(NULL AS NVARCHAR(50)) AS ZEILE,
        CAST(NULL AS NVARCHAR(50)) AS BWART,
        CAST(NULL AS NVARCHAR(50)) AS LIFNR,
        si.WAERS,
        CAST(NULL AS NVARCHAR(50)) AS GSBER,
        CAST(NULL AS NVARCHAR(50)) AS KOSTL,
        si.BUKRS,
        CAST('2019-12-31' AS DATE) AS BLDAT,
        CAST('2019-12-31' AS DATE) AS BUDAT,
        CAST('2019-12-31' AS DATE) AS CPUDT,
        CAST('2019-12-31' AS DATE) AS AEDAT,
        CAST(NULL AS NVARCHAR(50)) AS USNAM,
        CAST(NULL AS NVARCHAR(50)) AS SAKTO,
        CONCAT(si.MATNR, '-', si.WERKS, '-', ISNULL(si.BWTAR,''), '-', ISNULL(si.SOBKZ,''), '-', ISNULL(si.PSPNR,'')) AS MaterialPrecioKey,
        CASE WHEN TRY_CAST(LEFT(si.PSPNR, 1) AS INT) <> 1 THEN 'No' ELSE 'Si' END AS Proyecto,
        (2019 - 1) * 12 + 12 AS PeriodoSalId  -- Diciembre 2019
    FROM (
        SELECT MATNR, WERKS, LGORT, BWTAR, SOBKZ, PSPNR, WAERS, BUKRS, DMBTR,
               StockEstado, Cantidad
        FROM SAP_COMPRAS.StockInicial
        UNPIVOT (
            Cantidad FOR StockEstado IN (LABST, UMLME, INSME, EINME, SPEME, RETME)
        ) AS unpvt
    ) si
    WHERE EXISTS (SELECT 1 FROM SAP_COMPRAS.Material mat WHERE mat.MATNR = si.MATNR)
      AND LEFT(si.LGORT, 1) <> 'M'
      AND TRY_CAST(REPLACE(si.Cantidad, ',', '.') AS DECIMAL(18,3)) <> 0  -- MENGE <> '0'
      AND si.LGORT <> '0000'
),

-- =============================================================================
-- CTE 3: Movimientos combinados (MOV + S.I)
-- =============================================================================
MovimientosBase AS (
    SELECT * FROM MovimientosMOV
    UNION ALL
    SELECT * FROM MovimientosSI
),

-- =============================================================================
-- CTE 4: Centros Activos (QLIK Movimientos.txt líneas 142-146)
-- Solo centros donde Sum(Cantidad) > 0
-- =============================================================================
CentrosActivos AS (
    SELECT Centro
    FROM MovimientosBase
    GROUP BY Centro
    HAVING SUM(CASE WHEN DebeHaber = 'H' THEN -1 * MENGE ELSE MENGE END) > 0
),

-- =============================================================================
-- CTE 5: Movimientos filtrados por CentrosActivos (QLIK línea 209)
-- =============================================================================
MovimientosFiltrados AS (
    SELECT mb.*
    FROM MovimientosBase mb
    WHERE mb.Centro IN (SELECT Centro FROM CentrosActivos)
),

-- =============================================================================
-- CTE 6: Control Inventario (ControlInventario.txt - NO usa CentrosActivos)
-- =============================================================================
ControlInventario AS (
    SELECT 
        'CIN' AS TipoMov,
        c.MATNR AS MaterialId,
        c.WERKS AS Centro,
        c.LGORT AS Almacen,
        CAST(NULL AS NVARCHAR(50)) AS ClaseValoracion,
        c.SOBK AS StockEspecial,
        CAST(NULL AS NVARCHAR(50)) AS ElementoPep,
        CAST(NULL AS NVARCHAR(50)) AS DebeHaber,
        TRY_CAST(REPLACE(c.MENGE, ',', '.') AS DECIMAL(18,3)) AS MENGE,
        CAST(NULL AS DECIMAL(18,2)) AS DMBTR,
        c.CHARG,
        c.MBLNR,
        c.MJAH AS MJAHR,
        c.ZEILE,
        CAST(NULL AS NVARCHAR(50)) AS BWART,
        CAST(NULL AS NVARCHAR(50)) AS LIFNR,
        CAST(NULL AS NVARCHAR(50)) AS WAERS,
        CAST(NULL AS NVARCHAR(50)) AS GSBER,
        CAST(NULL AS NVARCHAR(50)) AS KOSTL,
        CAST(NULL AS NVARCHAR(50)) AS BUKRS,
        CAST(NULL AS DATE) AS BLDAT,
        TRY_CAST(c.BUDAT AS DATE) AS BUDAT,
        CAST(NULL AS DATE) AS CPUDT,
        CAST(NULL AS DATE) AS AEDAT,
        CAST(NULL AS NVARCHAR(50)) AS USNAM,
        CAST(NULL AS NVARCHAR(50)) AS SAKTO,
        CONCAT(c.MATNR, '-', c.WERKS, '-', '', '-', ISNULL(c.SOBK,''), '-', '') AS MaterialPrecioKey,
        CAST(NULL AS NVARCHAR(10)) AS Proyecto,
        (YEAR(TRY_CAST(c.BUDAT AS DATE)) - 1) * 12 + MONTH(TRY_CAST(c.BUDAT AS DATE)) AS PeriodoSalId,
        -- Campos específicos de CIN
        c.IBLNR AS DocumentoControl,
        c.GJAH AS ControlPeriodo,
        TRY_CAST(c.ZLDAT AS DATE) AS FechaRecuento,
        TRY_CAST(REPLACE(c.BUCHM, ',', '.') AS DECIMAL(18,3)) AS CantidadTeorica,
        c.MEINS AS UnidadMedida,
        c.BSTA AS TipoStockId,
        TRY_CAST(REPLACE(c.WRTZL, ',', '.') AS DECIMAL(18,2)) AS CantxPrecioT,
        TRY_CAST(REPLACE(c.WRTBM, ',', '.') AS DECIMAL(18,2)) AS CantxPrecioR
    FROM SAP_COMPRAS.ControlInventario c
    WHERE TRY_CAST(c.ZLDAT AS DATE) >= '2019-12-31'
),

-- =============================================================================
-- CTE 7: Períodos - todos los períodos desde mínimo hasta máximo
-- (QLIK Saldos Periodo.txt líneas 37-59)
-- =============================================================================
RangoPeriodos AS (
    SELECT 
        MIN(PeriodoSalId) AS MinPer,
        MAX(PeriodoSalId) AS MaxPer
    FROM MovimientosFiltrados
),

-- Generamos todos los períodos
Periodos AS (
    SELECT 
        p.MinPer + n.n AS PeriodoSalId,
        EOMONTH(DATEFROMPARTS(
            ((p.MinPer + n.n - 1) / 12) + 1,  -- Año
            ((p.MinPer + n.n - 1) % 12) + 1,  -- Mes
            1
        )) AS FechaPeriodo
    FROM RangoPeriodos p
    CROSS JOIN (
        -- Generamos números del 0 al máximo de períodos esperados (~100)
        SELECT TOP 120 ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) - 1 AS n
        FROM sys.objects a CROSS JOIN sys.objects b
    ) n
    WHERE (p.MinPer + n.n) <= p.MaxPer
),

-- =============================================================================
-- CTE 8: SaldosPeriodoTmp1 - Agrupación inicial (QLIK líneas 1-19)
-- =============================================================================
SaldosPeriodoTmp1 AS (
    SELECT 
        'SDO' AS TipoMov,
        mf.MaterialId,
        mf.Centro,
        mf.Almacen,
        mf.Proyecto,
        mf.PeriodoSalId,
        -- MaterialKey como en QLIK
        CONCAT(mf.MaterialId, '-', mf.Centro, '-', mf.Almacen, '-', mf.Proyecto) AS MaterialKey,
        SUM(CASE WHEN mf.DebeHaber = 'H' THEN -1 * mf.MENGE ELSE mf.MENGE END) AS SaldoCantidad,
        SUM(CASE WHEN mf.DebeHaber = 'H' THEN -1 * mf.MENGE ELSE mf.MENGE END * 
            ISNULL(TRY_CAST(REPLACE(pr.STPRS, ',', '.') AS DECIMAL(18,4)), 0)) AS SaldoImporteUSD
    FROM MovimientosFiltrados mf
    LEFT JOIN SAP_COMPRAS.Precio pr 
        ON mf.MaterialId = pr.MATNR
        AND mf.Centro = pr.WERKS
        AND ISNULL(mf.ClaseValoracion, '') = ISNULL(pr.BWTAR, '')
        AND ISNULL(mf.StockEspecial, '') = ISNULL(pr.SOBKZ, '')
        AND ISNULL(mf.ElementoPep, '') = ISNULL(pr.PSPNR, '')
    GROUP BY 
        mf.MaterialId, mf.Centro, mf.Almacen, mf.Proyecto, mf.PeriodoSalId,
        CONCAT(mf.MaterialId, '-', mf.Centro, '-', mf.Almacen, '-', mf.Proyecto)
),

-- =============================================================================
-- CTE 9: MaterialKeys únicos para CROSS JOIN con Periodos
-- =============================================================================
MaterialKeysUnicos AS (
    SELECT DISTINCT 
        MaterialId, Centro, Almacen, Proyecto, MaterialKey
    FROM SaldosPeriodoTmp1
),

-- =============================================================================
-- CTE 10: Todas las combinaciones MaterialKey × Periodo (QLIK líneas 63-90)
-- =============================================================================
TodasCombinaciones AS (
    SELECT 
        mk.MaterialId,
        mk.Centro,
        mk.Almacen,
        mk.Proyecto,
        mk.MaterialKey,
        p.PeriodoSalId,
        p.FechaPeriodo,
        ISNULL(s.SaldoCantidad, 0) AS SaldoCantidad,
        ISNULL(s.SaldoImporteUSD, 0) AS SaldoImporteUSD
    FROM MaterialKeysUnicos mk
    CROSS JOIN Periodos p
    LEFT JOIN SaldosPeriodoTmp1 s 
        ON mk.MaterialKey = s.MaterialKey 
        AND p.PeriodoSalId = s.PeriodoSalId
),

-- =============================================================================
-- CTE 11: SDO con acumulados (QLIK líneas 93-121)
-- =============================================================================
SaldosPorPeriodo AS (
    SELECT 
        'SDO' AS TipoMov,
        tc.MaterialId,
        tc.Centro,
        tc.Almacen,
        tc.Proyecto,
        tc.MaterialKey,
        tc.PeriodoSalId,
        tc.FechaPeriodo,
        tc.SaldoCantidad,
        tc.SaldoImporteUSD,
        -- Saldo acumulado
        SUM(tc.SaldoCantidad) OVER (
            PARTITION BY tc.MaterialKey 
            ORDER BY tc.PeriodoSalId 
            ROWS UNBOUNDED PRECEDING
        ) AS SaldoAcum,
        -- SKU
        CASE 
            WHEN SUM(tc.SaldoCantidad) OVER (
                PARTITION BY tc.MaterialKey 
                ORDER BY tc.PeriodoSalId 
                ROWS UNBOUNDED PRECEDING
            ) > 0 THEN 1 ELSE 0 
        END AS SKU,
        -- Saldo USD Acumulado
        SUM(tc.SaldoImporteUSD) OVER (
            PARTITION BY tc.MaterialKey 
            ORDER BY tc.PeriodoSalId 
            ROWS UNBOUNDED PRECEDING
        ) AS SaldoUSDAcum
    FROM TodasCombinaciones tc
)

-- =============================================================================
-- CONSULTA FINAL: UNION de MOV + S.I + CIN + SDO
-- =============================================================================

-- MOV y S.I filtrados por CentrosActivos
SELECT 
    mf.TipoMov,
    mf.MaterialId,
    mf.Centro,
    mf.Almacen,
    mf.ClaseValoracion,
    mf.StockEspecial,
    mf.ElementoPep,
    mf.DebeHaber,
    mf.CHARG AS Lote,
    mf.MBLNR AS Documento,
    mf.MJAHR AS Ejercicio,
    mf.ZEILE AS PosicionDoc,
    mf.BWART AS ClaseMovimientoId,
    mf.LIFNR AS ProveedorId,
    mf.WAERS AS Moneda,
    mf.GSBER AS DivisionId,
    mf.KOSTL AS CentroCostoId,
    mf.BUKRS AS EmpresaId,
    mf.BUDAT AS Fecha,
    mf.BLDAT AS FechaDocumento,
    mf.CPUDT AS FechaEntrada,
    mf.AEDAT AS FechaModificacion,
    mf.USNAM AS UsuarioUltModif,
    mf.SAKTO AS CuentaMayor,
    mf.MaterialPrecioKey,
    CONCAT(mf.BWART, mf.StockEspecial) AS ClaseMovimientoKey,
    mf.Proyecto,
    mf.PeriodoSalId,
    CASE WHEN mf.DebeHaber = 'S' THEN mf.MENGE ELSE 0 END AS CantidadEntrada,
    CASE WHEN mf.DebeHaber = 'H' THEN mf.MENGE ELSE 0 END AS CantidadSalida,
    CASE WHEN mf.DebeHaber = 'H' THEN -1 * mf.MENGE ELSE mf.MENGE END AS Cantidad,
    -- Campos CIN (NULL para MOV/S.I)
    CAST(NULL AS NVARCHAR(50)) AS DocumentoControl,
    CAST(NULL AS NVARCHAR(50)) AS ControlPeriodo,
    CAST(NULL AS DATE) AS FechaRecuento,
    CAST(NULL AS DECIMAL(18,3)) AS CantidadTeorica,
    CAST(NULL AS NVARCHAR(50)) AS UnidadMedida,
    CAST(NULL AS NVARCHAR(50)) AS TipoStockId,
    CAST(NULL AS DECIMAL(18,2)) AS CantxPrecioT,
    CAST(NULL AS DECIMAL(18,2)) AS CantxPrecioR,
    -- Campos SDO (NULL para MOV/S.I)
    CAST(NULL AS DECIMAL(18,3)) AS SaldoAcum,
    CAST(NULL AS INT) AS SKU,
    CAST(NULL AS DECIMAL(18,2)) AS SaldoUSDAcum
FROM MovimientosFiltrados mf

UNION ALL

-- CIN (NO filtrado por CentrosActivos - se concatena después en QLIK)
SELECT 
    c.TipoMov,
    c.MaterialId,
    c.Centro,
    c.Almacen,
    c.ClaseValoracion,
    c.StockEspecial,
    c.ElementoPep,
    c.DebeHaber,
    c.CHARG AS Lote,
    c.MBLNR AS Documento,
    c.MJAHR AS Ejercicio,
    c.ZEILE AS PosicionDoc,
    c.BWART AS ClaseMovimientoId,
    c.LIFNR AS ProveedorId,
    c.WAERS AS Moneda,
    c.GSBER AS DivisionId,
    c.KOSTL AS CentroCostoId,
    c.BUKRS AS EmpresaId,
    c.BUDAT AS Fecha,
    c.BLDAT AS FechaDocumento,
    c.CPUDT AS FechaEntrada,
    c.AEDAT AS FechaModificacion,
    c.USNAM AS UsuarioUltModif,
    c.SAKTO AS CuentaMayor,
    c.MaterialPrecioKey,
    CAST(NULL AS NVARCHAR(100)) AS ClaseMovimientoKey,
    c.Proyecto,
    c.PeriodoSalId,
    CAST(NULL AS DECIMAL(18,3)) AS CantidadEntrada,
    CAST(NULL AS DECIMAL(18,3)) AS CantidadSalida,
    c.MENGE AS Cantidad,
    -- Campos CIN
    c.DocumentoControl,
    c.ControlPeriodo,
    c.FechaRecuento,
    c.CantidadTeorica,
    c.UnidadMedida,
    c.TipoStockId,
    c.CantxPrecioT,
    c.CantxPrecioR,
    -- Campos SDO (NULL para CIN)
    CAST(NULL AS DECIMAL(18,3)) AS SaldoAcum,
    CAST(NULL AS INT) AS SKU,
    CAST(NULL AS DECIMAL(18,2)) AS SaldoUSDAcum
FROM ControlInventario c

UNION ALL

-- SDO (Saldos por Período)
SELECT 
    sdo.TipoMov,
    sdo.MaterialId,
    sdo.Centro,
    sdo.Almacen,
    CAST(NULL AS NVARCHAR(50)) AS ClaseValoracion,
    CAST(NULL AS NVARCHAR(50)) AS StockEspecial,
    CAST(NULL AS NVARCHAR(50)) AS ElementoPep,
    CAST(NULL AS NVARCHAR(50)) AS DebeHaber,
    CAST(NULL AS NVARCHAR(50)) AS Lote,
    CAST(NULL AS NVARCHAR(50)) AS Documento,
    CAST(NULL AS NVARCHAR(50)) AS Ejercicio,
    CAST(NULL AS NVARCHAR(50)) AS PosicionDoc,
    CAST(NULL AS NVARCHAR(50)) AS ClaseMovimientoId,
    CAST(NULL AS NVARCHAR(50)) AS ProveedorId,
    CAST(NULL AS NVARCHAR(50)) AS Moneda,
    CAST(NULL AS NVARCHAR(50)) AS DivisionId,
    CAST(NULL AS NVARCHAR(50)) AS CentroCostoId,
    CAST(NULL AS NVARCHAR(50)) AS EmpresaId,
    sdo.FechaPeriodo AS Fecha,
    sdo.FechaPeriodo AS FechaDocumento,
    CAST(NULL AS DATE) AS FechaEntrada,
    CAST(NULL AS DATE) AS FechaModificacion,
    CAST(NULL AS NVARCHAR(50)) AS UsuarioUltModif,
    CAST(NULL AS NVARCHAR(50)) AS CuentaMayor,
    sdo.MaterialKey AS MaterialPrecioKey,
    CAST(NULL AS NVARCHAR(100)) AS ClaseMovimientoKey,
    sdo.Proyecto,
    sdo.PeriodoSalId,
    CAST(NULL AS DECIMAL(18,3)) AS CantidadEntrada,
    CAST(NULL AS DECIMAL(18,3)) AS CantidadSalida,
    sdo.SaldoCantidad AS Cantidad,
    -- Campos CIN (NULL para SDO)
    CAST(NULL AS NVARCHAR(50)) AS DocumentoControl,
    CAST(NULL AS NVARCHAR(50)) AS ControlPeriodo,
    CAST(NULL AS DATE) AS FechaRecuento,
    CAST(NULL AS DECIMAL(18,3)) AS CantidadTeorica,
    CAST(NULL AS NVARCHAR(50)) AS UnidadMedida,
    CAST(NULL AS NVARCHAR(50)) AS TipoStockId,
    CAST(NULL AS DECIMAL(18,2)) AS CantxPrecioT,
    CAST(NULL AS DECIMAL(18,2)) AS CantxPrecioR,
    -- Campos SDO
    sdo.SaldoAcum,
    sdo.SKU,
    sdo.SaldoUSDAcum
FROM SaldosPorPeriodo sdo;
```
