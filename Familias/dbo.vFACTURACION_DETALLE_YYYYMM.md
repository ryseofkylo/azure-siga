---
objeto: dbo.vFACTURACION_DETALLE_YYYYMM
tipo_objeto: FAMILIA (particiones por período)
esquema: dbo
dominio: Data Warehouse / BI
canonico: true
familia: true
n_miembros: 2
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/familia
  - canonico
---

# Familia: dbo.vFACTURACION_DETALLE_YYYYMM

> Serie de **2 objetos** con esquema (casi) idéntico, particionados por período. Consultá el **miembro del período** que necesites; el esquema común es el de abajo.

## Esquema común (según vFACTURACION_DETALLE_202309)
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `empresaid` | int |  |
| 2 | `PERIODO` | int |  |
| 3 | `clientenro` | int |  |
| 4 | `facturatpo` | varchar |  |
| 5 | `facturagen` | varchar |  |
| 6 | `facturanro` | int |  |
| 7 | `TOTAL` | real |  |
| 8 | `CUOTA` | varchar |  |
| 9 | `NROLINEA` | int |  |
| 10 | `IVA` | real |  |
| 11 | `productonombre` | varchar |  |
| 12 | `contratonro` | int |  |
| 13 | `IMPORTE_LINEA` | real |  |
| 14 | `CONCEPTO` | varchar |  |
| 15 | `POLITICA` | varchar |  |
| 16 | `PROMO` | varchar |  |
| 17 | `COMBO` | varchar |  |
| 18 | `PROMOID` | int |  |
| 19 | `PoliticaId` | int |  |
| 20 | `cptofacid` | int |  |
| 21 | `Comboid` | int |  |
| 22 | `PRODUCTOID` | int |  |
| 23 | `PRODUCTOTPO` | varchar |  |
| 24 | `PRODUCTOPPL` | varchar |  |
| 25 | `FACTURAFCH` | datetime2 |  |
| 26 | `CuotaDesde` | int |  |
| 27 | `CuotaHasta` | int |  |

## Miembros disponibles
- `dbo.vFACTURACION_DETALLE_202309` (27 col)
- `dbo.vFACTURACION_DETALLE_202310` (27 col)