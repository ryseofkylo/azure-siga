---
esquema: dbo
tabla: v_bajasmorosas
objeto: dbo.v_bajasmorosas
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 44
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_bajasmorosas

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[ACTIVITY.BAJASMOROSAS]]
- [[ACTIVITY.H_BAJASMOROSAS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENRO` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODNOMBRE` | nvarchar | 0% |
| 7 | `TIPOPROD` | nvarchar | 0% |
| 8 | `MOROSIDADMES` | int | 0% |
| 9 | `SUCURSAL` | int | 0% |
| 10 | `CENTROOPERATIVO` | nvarchar | 0% |
| 11 | `SUCURSALNOMBRE` | nvarchar | 0% |
| 12 | `NOMBREDELCLIENTE` | nvarchar | 0% |
| 13 | `MAIL` | nvarchar | 0% |
| 14 | `DEPARTAMENTO` | nvarchar | 0% |
| 15 | `LOCALIDAD` | nvarchar | 0% |
| 16 | `ESTADODELCLIENTE` | nvarchar | 0% |
| 17 | `PRINCIPAL` | nvarchar | 0% |
| 18 | `ESTADODELCONTRATO` | nvarchar | 0% |
| 19 | `TIPODEMOROSIDAD` | nvarchar | 0% |
| 20 | `FECHADEPROCESADA` | datetime2 | 0% |
| 21 | `ESTADODEMOROSIDAD` | nvarchar | 0% |
| 22 | `ULTIMAFECHAPAGO` | datetime2 | 0% |
| 23 | `DEUDA` | real | 8% |
| 24 | `CANTIDADDECUOTAS` | int | 0% |
| 25 | `TELEFONOCLIENTE` | nvarchar | 2% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `MEDIODEREPARTO` | nvarchar | 0% |
| 28 | `SEGMENTO` | nvarchar | 0% |
| 29 | `SINCARGO` | nvarchar | 0% |
| 30 | `PROMOTORGRUPO` | nvarchar | 6% |
| 31 | `NOMBREPROMOCION` | nvarchar | 66% |
| 32 | `ULTIMAFACTURA` | real | 0% |
| 33 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 34 | `CLITIPO` | nvarchar | 0% |
| 35 | `FECHAMOROGENERADA` | datetime2 | 0% |
| 36 | `MOROSIDADFORMAGENERADA` | nvarchar | 0% |
| 37 | `EXISTEOTRA` | nvarchar | 0% |
| 38 | `IDPLANCOMERCIAL` | real | 98% |
| 39 | `PLANCOMERCIAL` | nvarchar | 98% |
| 40 | `QORDENESCANCELADAS` | int | 0% |
| 41 | `CODMZN` | nvarchar | 0% |
| 42 | `IDZONA` | real | 19% |
| 43 | `ZONA` | nvarchar | 19% |
| 44 | `PIPELINERUNID` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_bajasmorosas
-- Extraida: 2026-08-07T15:27:38.785462+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_bajasmorosas]
AS SELECT * FROM ACTIVITY.H_BAJASMOROSAS
UNION ALL
SELECT * FROM ACTIVITY.BAJASMOROSAS;
```
