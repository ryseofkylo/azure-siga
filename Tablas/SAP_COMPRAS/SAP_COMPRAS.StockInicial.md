---
esquema: SAP_COMPRAS
tabla: StockInicial
objeto: SAP_COMPRAS.StockInicial
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `LGORT`, `WERKS`, `MATNR`
n_columnas: 16
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.StockInicial

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `LGORT`, `WERKS`, `MATNR`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MATNR` | nvarchar | 0% |
| 2 | `WERKS` | nvarchar | 0% |
| 3 | `LGORT` | nvarchar | 0% |
| 4 | `BWTAR` | nvarchar | 25% |
| 5 | `SOBKZ` | nvarchar | 98% |
| 6 | `PSPNR` | nvarchar | 98% |
| 7 | `MENGE` | nvarchar | 0% |
| 8 | `DMBTR` | nvarchar | 0% |
| 9 | `WAERS` | nvarchar | 0% |
| 10 | `BUKRS` | nvarchar | 0% |
| 11 | `LABST` | nvarchar | 0% |
| 12 | `UMLME` | nvarchar | 0% |
| 13 | `INSME` | nvarchar | 0% |
| 14 | `EINME` | nvarchar | 0% |
| 15 | `SPEME` | nvarchar | 0% |
| 16 | `RETME` | nvarchar | 0% |

## Claves de join presentes
- `MATNR` (nvarchar) → [[clave-MATNR]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[SAP_COMPRAS.vw_Movimientos_QLIK]]

## Vistas que la consumen (referencia)
- [[SAP_COMPRAS.vw_Movimientos_QLIK]]
- [[dbo.Precios_Almacen]]
