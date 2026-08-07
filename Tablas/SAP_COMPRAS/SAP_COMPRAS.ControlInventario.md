---
esquema: SAP_COMPRAS
tabla: ControlInventario
objeto: SAP_COMPRAS.ControlInventario
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `IBLNR`, `WRTBM`, `WRTZL`
n_columnas: 19
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.ControlInventario

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 19 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `IBLNR`, `WRTBM`, `WRTZL`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `IBLNR` | nvarchar | 0% |
| 2 | `GJAH` | nvarchar | 0% |
| 3 | `ZEILI` | nvarchar | 0% |
| 4 | `MATNR` | nvarchar | 0% |
| 5 | `WERKS` | nvarchar | 0% |
| 6 | `LGORT` | nvarchar | 0% |
| 7 | `CHARG` | nvarchar | 30% |
| 8 | `SOBK` | nvarchar | 98% |
| 9 | `BSTA` | nvarchar | 0% |
| 10 | `ZLDAT` | nvarchar | 0% |
| 11 | `BUDAT` | nvarchar | 0% |
| 12 | `BUCHM` | nvarchar | 0% |
| 13 | `MENGE` | nvarchar | 0% |
| 14 | `MEINS` | nvarchar | 0% |
| 15 | `MBLNR` | nvarchar | 88% |
| 16 | `MJAH` | nvarchar | 0% |
| 17 | `ZEILE` | nvarchar | 0% |
| 18 | `WRTZL` | nvarchar | 0% |
| 19 | `WRTBM` | nvarchar | 0% |

## Claves de join presentes
- `MATNR` (nvarchar) → [[clave-MATNR]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[SAP_COMPRAS.vw_Movimientos_QLIK]]

## Vistas que la consumen (referencia)
- [[SAP_COMPRAS.vw_Movimientos_QLIK]]
