---
objeto: dbo.vRETENCIONES_YYYYMM
tipo_objeto: FAMILIA (particiones por período)
esquema: dbo
dominio: Data Warehouse / BI
canonico: true
familia: true
n_miembros: 1
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/familia
  - canonico
---

# Familia: dbo.vRETENCIONES_YYYYMM

> Serie de **1 objetos** con esquema (casi) idéntico, particionados por período. Consultá el **miembro del período** que necesites; el esquema común es el de abajo.

## Esquema común (según vRETENCIONES_202308)
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `porc_facturacion` | numeric |  |
| 2 | `contador` | int |  |
| 3 | `Key` | varchar |  |
| 4 | `Cuotas_Pendientes` | int |  |
| 5 | `porc_dec` | numeric |  |
| 6 | `acumulado` | numeric |  |
| 7 | `empresaid` | int |  |
| 8 | `PERIODO` | int |  |
| 9 | `FECHA_FAC` | date |  |
| 10 | `clientenro` | int |  |
| 11 | `NEGOCIOSEGMENTO` | int |  |
| 12 | `CLIENTETPO` | int |  |
| 13 | `CLIENTENATURALEZANOM` | varchar |  |
| 14 | `MEDIO_COBRO` | varchar |  |
| 15 | `facturatpo` | varchar |  |
| 16 | `facturagen` | varchar |  |
| 17 | `facturanro` | int |  |
| 18 | `TOTAL` | real |  |
| 19 | `CUOTA` | varchar |  |
| 20 | `NROLINEA` | int |  |
| 21 | `IVA` | real |  |
| 22 | `productonombre` | varchar |  |
| 23 | `contratonro` | int |  |
| 24 | `IMPORTE_LINEA` | numeric |  |
| 25 | `CONCEPTO` | varchar |  |
| 26 | `POLITICA` | varchar |  |
| 27 | `PROMO` | varchar |  |
| 28 | `COMBO` | varchar |  |
| 29 | `PROMOID` | int |  |
| 30 | `PoliticaId` | int |  |
| 31 | `cptofacid` | int |  |
| 32 | `Comboid` | int |  |
| 33 | `PRODUCTOID` | int |  |
| 34 | `PRODUCTOTPO` | varchar |  |
| 35 | `PRODUCTOPPL` | varchar |  |
| 36 | `FACTURAFCH` | datetime2 |  |
| 37 | `AUXILIAR` | int |  |
| 38 | `PROMOCIONCLASE` | varchar |  |
| 39 | `PROMOCIONTPODTO` | varchar |  |
| 40 | `CUOTADESDE` | int |  |
| 41 | `CUOTAHASTA` | int |  |

## Miembros disponibles
- `dbo.vRETENCIONES_202308` (41 col)