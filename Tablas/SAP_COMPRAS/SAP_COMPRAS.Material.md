---
esquema: SAP_COMPRAS
tabla: Material
objeto: SAP_COMPRAS.Material
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: 1 fila = 1 `MATNR` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.Material

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `MATNR` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MATNR` | nvarchar | 0% |
| 2 | `MTART` | nvarchar | 0% |
| 3 | `MATKL` | nvarchar | 0% |
| 4 | `MEINS` | nvarchar | 0% |
| 5 | `GEWEI` | nvarchar | 46% |
| 6 | `MSTAE` | nvarchar | 56% |
| 7 | `MAKTX` | nvarchar | 0% |

## Claves de join presentes
- `MATNR` (nvarchar) → [[clave-MATNR]]

## Relaciones (derivadas de JOINs de vistas)
- [[SAP_COMPRAS.Movimientos]] · `Material.MATNR = Movimientos.MATNR` — view_join (vw_Movimientos_QLIK), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `EXISTS (SELECT 1 FROM SAP_COMPRAS.Material mat WHERE mat.MATNR = m.MATNR)` — _de_ [[SAP_COMPRAS.vw_Movimientos_QLIK]]
- 🚦 `EXISTS (SELECT 1 FROM SAP_COMPRAS.Material mat WHERE mat.MATNR = si.MATNR)` — _de_ [[SAP_COMPRAS.vw_Movimientos_QLIK]]
- ♻️ dedup: vistas que deduplican esta tabla → [[SAP_COMPRAS.vw_Movimientos_QLIK]]

## Vistas que la consumen (referencia)
- [[SAP_COMPRAS.vw_Movimientos_QLIK]]
