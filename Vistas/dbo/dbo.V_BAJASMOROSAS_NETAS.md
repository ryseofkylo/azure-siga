---
esquema: dbo
tabla: V_BAJASMOROSAS_NETAS
objeto: dbo.V_BAJASMOROSAS_NETAS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 48
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_BAJASMOROSAS_NETAS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[dbo.V_FILTRO_BAJASMOROSAS]]
- [[dbo.V_FILTRO_RECUPMORSOS]]

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
| 10 | `CENTROOPERATIVO` | nvarchar | 49% |
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
| 22 | `ULTIMAFECHAPAGO` | datetime2 | 2% |
| 23 | `DEUDA` | real | 46% |
| 24 | `CANTIDADDECUOTAS` | int | 0% |
| 25 | `TELEFONOCLIENTE` | nvarchar | 48% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `MEDIODEREPARTO` | nvarchar | 0% |
| 28 | `SEGMENTO` | nvarchar | 0% |
| 29 | `SINCARGO` | nvarchar | 0% |
| 30 | `PROMOTORGRUPO` | nvarchar | 48% |
| 31 | `NOMBREPROMOCION` | nvarchar | 58% |
| 32 | `ULTIMAFACTURA` | real | 0% |
| 33 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 34 | `CLITIPO` | nvarchar | 0% |
| 35 | `FECHAMOROGENERADA` | datetime2 | 0% |
| 36 | `MOROSIDADFORMAGENERADA` | nvarchar | 0% |
| 37 | `EXISTEOTRA` | nvarchar | 0% |
| 38 | `IDPLANCOMERCIAL` | real | 100% |
| 39 | `PLANCOMERCIAL` | nvarchar | 95% |
| 40 | `QORDENESCANCELADAS` | int | 0% |
| 41 | `CODMZN` | nvarchar | 0% |
| 42 | `IDZONA` | real | 54% |
| 43 | `ZONA` | nvarchar | 54% |
| 44 | `PIPELINERUNID` | nvarchar | 0% |
| 45 | `PERIODOMOROGEN` | nvarchar | 0% |
| 46 | `ORDEN` | bigint | 0% |
| 47 | `BAJANETA` | varchar | 0% |
| 48 | `CONTRATOFINS` | date | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_BAJASMOROSAS_NETAS
-- Extraida: 2026-08-07T15:27:39.130368+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_BAJASMOROSAS_NETAS]
AS SELECT v.*, CASE WHEN b.ORDEN IS NULL THEN 'Y' ELSE 'N' END AS BAJANETA, CONVERT( DATE, c.CONTRATOFINS ) AS CONTRATOFINS
FROM 
( SELECT m.*, ROW_NUMBER() OVER ( PARTITION BY CLIENTENRO, CONTRATO, PERIODOMOROGEN ORDER BY CLIENTENRO ) AS ORDEN
  FROM ( SELECT f.*, FORMAT( fechamorogenerada, 'yyyyMM' ) AS PERIODOMOROGEN FROM V_FILTRO_BAJASMOROSAS f ) m
 ) v
LEFT JOIN
( SELECT r.*, ROW_NUMBER() OVER ( PARTITION BY CLIENTENRO, CONTRATO, PERIODOPROCESO ORDER BY CLIENTENRO ) AS ORDEN
   FROM ( SELECT x.*, FORMAT( fechadeprocesada, 'yyyyMM' ) AS PERIODOPROCESO FROM V_FILTRO_RECUPMORSOS x ) r
) b
ON (      ( v.CLIENTENRO = b.CLIENTENRO ) 
	  AND ( v.CONTRATO = b.CONTRATO ) 
	  AND ( v.ORDEN = b.ORDEN ) 
	  AND ( v.PERIODOMOROGEN = b.PERIODOPROCESO ) 
	)
LEFT JOIN SIGASC.CONTRATO c ON ( ( c.empresaid = v.empresaid ) AND ( c.contratonro = v.contrato ) );
```
