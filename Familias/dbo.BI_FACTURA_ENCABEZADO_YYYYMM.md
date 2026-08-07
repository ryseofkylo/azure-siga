---
objeto: dbo.BI_FACTURA_ENCABEZADO_YYYYMM
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

# Familia: dbo.BI_FACTURA_ENCABEZADO_YYYYMM

> Serie de **2 objetos** con esquema (casi) idéntico, particionados por período. Consultá el **miembro del período** que necesites; el esquema común es el de abajo.

## Esquema común (según BI_FACTURA_ENCABEZADO_202301)
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `facturanro` | int | 0% |
| 2 | `periodo` | int | 0% |
| 3 | `facturagen` | varchar | 0% |
| 4 | `facturatpo` | varchar | 0% |
| 5 | `importe` | float | 0% |
| 6 | `importedev` | float | 0% |
| 7 | `empresaid` | int | 0% |
| 8 | `clientenro` | int | 0% |
| 9 | `empresa` | nvarchar | 0% |
| 10 | `clienteape` | varchar | 0% |
| 11 | `clientenom` | varchar | 0% |
| 12 | `CLIENTESTSNOMBRE` | varchar | 0% |
| 13 | `clientecitpo` | varchar | 0% |
| 14 | `clienteci` | varchar | 0% |
| 15 | `clientests` | varchar | 0% |
| 16 | `negociosegmento` | int | 0% |
| 17 | `clientetpo` | int | 0% |
| 18 | `clientenaturalezanom` | nvarchar | 0% |
| 19 | `MEDIO_COBRO` | nvarchar | 0% |
| 20 | `REPARTO` | nvarchar | 0% |
| 21 | `DEBITO_AUTOMATICO` | varchar | 0% |
| 22 | `EMAIL_SIGA` | varchar | 2% |
| 23 | `FechaFactura` | datetime2 | 0% |
| 24 | `FechaHoraFactura` | datetime2 | 0% |
| 25 | `FechaVto` | datetime2 | 4% |
| 26 | `FACTURANRONC` | int | 0% |
| 27 | `FACTURAUSR` | varchar | 0% |

## Miembros disponibles
- `dbo.BI_FACTURA_ENCABEZADO_202301` (27 col)
- `dbo.BI_FACTURA_ENCABEZADO_202302` (27 col)