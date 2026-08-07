---
esquema: dbo
tabla: V_BAJASVOLUNTARIAS_NETAS
objeto: dbo.V_BAJASVOLUNTARIAS_NETAS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 52
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_BAJASVOLUNTARIAS_NETAS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[dbo.V_FILTRO_BAJASVOLUN]]
- [[dbo.V_FILTRO_RECUPVOLUNTARIOS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTE` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODNOMBRE` | nvarchar | 0% |
| 7 | `PRODUCTOTIPO` | nvarchar | 0% |
| 8 | `SUCURAL` | int | 0% |
| 9 | `CENTROOPERATIVO` | nvarchar | 8% |
| 10 | `SERVICIO` | int | 0% |
| 11 | `FECHAINGRESO` | datetime2 | 0% |
| 12 | `STATUSSERVICIO` | nvarchar | 0% |
| 13 | `MOTIVO` | nvarchar | 0% |
| 14 | `AGENDADA` | datetime2 | 0% |
| 15 | `NOMBRE` | nvarchar | 0% |
| 16 | `STATUSCLIENTE` | nvarchar | 0% |
| 17 | `TELEFONOCLIENTE` | nvarchar | 8% |
| 18 | `ORDEN` | real | 78% |
| 19 | `STATUSORDEN` | nvarchar | 68% |
| 20 | `AGENDAMIENTO` | nvarchar | 68% |
| 21 | `PRINCIPAL` | nvarchar | 0% |
| 22 | `DEUDA` | real | 58% |
| 23 | `CANTIDADDECUOTAS` | int | 0% |
| 24 | `SERVICIONOMBRE` | nvarchar | 0% |
| 25 | `FECHADESCONEXION` | datetime2 | 10% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `DEBITOAUTOMATICO` | nvarchar | 0% |
| 28 | `PROMOTOR` | nvarchar | 24% |
| 29 | `PROMOTORGRUPO` | nvarchar | 24% |
| 30 | `FECHACONEXION` | datetime2 | 0% |
| 31 | `DEPARTAMENTO` | nvarchar | 0% |
| 32 | `LOCALIDAD` | nvarchar | 0% |
| 33 | `SEGMENTO` | nvarchar | 0% |
| 34 | `SINCARGO` | nvarchar | 0% |
| 35 | `ULTPERIODO` | int | 0% |
| 36 | `IMPORTEULTFACTURA` | real | 0% |
| 37 | `ULTPAGO` | datetime2 | 0% |
| 38 | `NOMBREPROMOCION` | nvarchar | 59% |
| 39 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 40 | `USUARIO` | nvarchar | 0% |
| 41 | `CLITIPO` | nvarchar | 0% |
| 42 | `IDPLANCOMERCIAL` | real | 100% |
| 43 | `PLANCOMERCIAL` | nvarchar | 82% |
| 44 | `CODMZN` | nvarchar | 0% |
| 45 | `IDZONA` | real | 12% |
| 46 | `ZONA` | nvarchar | 12% |
| 47 | `CLIENTESRVOBSERVACION` | nvarchar | 0% |
| 48 | `PIPELINERUNID` | nvarchar | 0% |
| 49 | `PERIODOINGRESO` | nvarchar | 0% |
| 50 | `ORDENNRO` | bigint | 0% |
| 51 | `BAJANETA` | varchar | 0% |
| 52 | `CONTRATOFINS` | date | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_BAJASVOLUNTARIAS_NETAS
-- Extraida: 2026-08-07T15:27:41.149491+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_BAJASVOLUNTARIAS_NETAS]
AS SELECT v.*, CASE WHEN b.ORDEN IS NULL THEN 'Y' ELSE 'N' END AS BAJANETA, CONVERT( DATE, c.CONTRATOFINS ) AS CONTRATOFINS
FROM 
( SELECT m.*, ROW_NUMBER() OVER ( PARTITION BY CLIENTE, CONTRATO, PERIODOINGRESO ORDER BY CLIENTE ) AS ORDENNRO
  FROM ( SELECT f.*, FORMAT( fechaingreso, 'yyyyMM' ) AS PERIODOINGRESO FROM V_FILTRO_BAJASVOLUN f ) m
) v
LEFT JOIN
( SELECT r.*, ROW_NUMBER() OVER ( PARTITION BY CLIENTENRO, CONTRATONRO, PERIODOFIN ORDER BY CLIENTENRO ) AS ORDEN
  FROM ( SELECT x.*, FORMAT( fechafinalizacion, 'yyyyMM' ) AS PERIODOFIN FROM V_FILTRO_RECUPVOLUNTARIOS x ) r
) b
ON (      ( v.CLIENTE = b.CLIENTENRO ) 
	  AND ( v.CONTRATO = b.CONTRATONRO ) 
	  AND ( v.ORDENNRO = b.ORDEN ) 
	  AND ( v.PERIODOINGRESO = b.PERIODOFIN ) 
	)
LEFT JOIN SIGASC.CONTRATO c ON ( ( c.empresaid = v.empresaid ) AND ( c.contratonro = v.contrato ) );
```
