---
objeto: dbo.BI_FACTURA_DETALLE_YYYYMM
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

# Familia: dbo.BI_FACTURA_DETALLE_YYYYMM

> Serie de **2 objetos** con esquema (casi) idéntico, particionados por período. Consultá el **miembro del período** que necesites; el esquema común es el de abajo.

## Esquema común (según BI_FACTURA_DETALLE_202301)
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PERIODO` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `FACTURATPO` | varchar | 0% |
| 5 | `FACTURAGEN` | varchar | 0% |
| 6 | `FACTURANRO` | int | 0% |
| 7 | `TOTAL` | float | 0% |
| 8 | `CUOTA` | varchar | 0% |
| 9 | `NROLINEA` | int | 0% |
| 10 | `IVA` | float | 0% |
| 11 | `PRODUCTONOMBRE` | nvarchar | 10% |
| 12 | `CONTRATONRO` | int | 10% |
| 13 | `IMPORTE_LINEA` | float | 0% |
| 14 | `CONCEPTO` | nvarchar | 0% |
| 15 | `POLITICA` | nvarchar | 10% |
| 16 | `PROMO` | nvarchar | 94% |
| 17 | `COMBO` | nvarchar | 97% |
| 18 | `PROMOID` | int | 0% |
| 19 | `POLITICAID` | int | 0% |
| 20 | `CPTOFACID` | int | 0% |
| 21 | `COMBOID` | int | 0% |
| 22 | `PRODUCTOID` | nvarchar | 10% |
| 23 | `PRODUCTOTPO` | nvarchar | 10% |
| 24 | `PRODUCTOPPL` | nvarchar | 10% |
| 25 | `CuotaDesde` | int | 10% |
| 26 | `CuotaHasta` | int | 10% |

## Miembros disponibles
- `dbo.BI_FACTURA_DETALLE_202301` (26 col)
- `dbo.BI_FACTURA_DETALLE_202302` (26 col)