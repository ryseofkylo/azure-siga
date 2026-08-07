---
esquema: SAP_COMPRAS
tabla: vw_Cotizaciones
objeto: SAP_COMPRAS.vw_Cotizaciones
tipo_objeto: VIEW
dominio: Compras y Finanzas (SAP)
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 2
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/vista
  - referencia
---

# SAP_COMPRAS.vw_Cotizaciones

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SAP_COMPRAS.Moneda]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `FechaCotizacion` | date |  |
| 2 | `Cotizacion` | decimal |  |

## Definición (CREATE VIEW)
```sql
-- Vista: SAP_COMPRAS.vw_Cotizaciones
-- Extraida: 2026-08-07T15:28:36.480493+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [SAP_COMPRAS].[vw_Cotizaciones]
AS SELECT 
    TRY_CAST(GDATU AS DATE) AS FechaCotizacion,
    TRY_CAST(UKURS AS DECIMAL(18,6)) AS Cotizacion
FROM SAP_COMPRAS.Moneda
WHERE FCURR = 'ARS' 
  AND TCURR = 'USD'
  AND TRY_CAST(GDATU AS DATE) IS NOT NULL;
```
