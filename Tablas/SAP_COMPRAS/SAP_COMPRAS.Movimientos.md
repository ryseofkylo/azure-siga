---
esquema: SAP_COMPRAS
tabla: Movimientos
objeto: SAP_COMPRAS.Movimientos
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `MBLNR`, `BLDAT`, `BUDAT`
n_columnas: 25
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.Movimientos

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 25 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `MBLNR`, `BLDAT`, `BUDAT`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MATNR` | nvarchar | 0% |
| 2 | `WERKS` | nvarchar | 0% |
| 3 | `LGORT` | nvarchar | 0% |
| 4 | `BWTAR` | nvarchar | 32% |
| 5 | `SOBKZ` | nvarchar | 99% |
| 6 | `PSPNR` | nvarchar | 99% |
| 7 | `SHKZG` | nvarchar | 0% |
| 8 | `MENGE` | nvarchar | 0% |
| 9 | `DMBTR` | nvarchar | 0% |
| 10 | `CHARG` | nvarchar | 100% |
| 11 | `MBLNR` | nvarchar | 0% |
| 12 | `MJAHR` | nvarchar | 0% |
| 13 | `ZEILE` | nvarchar | 0% |
| 14 | `BWART` | nvarchar | 0% |
| 15 | `LIFNR` | nvarchar | 96% |
| 16 | `WAERS` | nvarchar | 0% |
| 17 | `GSBER` | nvarchar | 0% |
| 18 | `KOSTL` | nvarchar | 30% |
| 19 | `BUKRS` | nvarchar | 0% |
| 20 | `BLDAT` | nvarchar | 0% |
| 21 | `BUDAT` | nvarchar | 0% |
| 22 | `CPUDT` | nvarchar | 0% |
| 23 | `AEDAT` | nvarchar | 100% |
| 24 | `USNAM` | nvarchar | 0% |
| 25 | `SAKTO` | nvarchar | 24% |

## Claves de join presentes
- `MATNR` (nvarchar) → [[clave-MATNR]]

## Relaciones (derivadas de JOINs de vistas)
- [[SAP_COMPRAS.Material]] · `Movimientos.MATNR = Material.MATNR` — view_join (vw_Movimientos_QLIK), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `EXISTS (SELECT 1 FROM SAP_COMPRAS.Material mat WHERE mat.MATNR = m.MATNR)` — _de_ [[SAP_COMPRAS.vw_Movimientos_QLIK]]
- `LEFT(m.LGORT, 1) <> 'M'` — _de_ [[SAP_COMPRAS.vw_Movimientos_QLIK]]
- `m.LGORT <> '0000'` — _de_ [[SAP_COMPRAS.vw_Movimientos_QLIK]]
- ♻️ dedup: vistas que deduplican esta tabla → [[SAP_COMPRAS.vw_Movimientos_QLIK]]

**Derivaciones (CASE)**
- _de_ [[SAP_COMPRAS.vw_Movimientos_QLIK]]:
  ```sql
  CASE WHEN TRY_CAST(LEFT(m.PSPNR, 1) AS INT) <> 1 THEN 'No' ELSE 'Si' END
  ```

## Vistas que la consumen (referencia)
- [[SAP_COMPRAS.vw_Movimientos_QLIK]]
- [[dbo.Precios_Almacen]]
