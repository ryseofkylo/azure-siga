---
esquema: dbo
tabla: V_BAJASVOL_360
objeto: dbo.V_BAJASVOL_360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 65
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_BAJASVOL_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_BAJASVOLUNTARIAS_NETAS]]

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
| 9 | `CENTROOPERATIVO` | nvarchar | 2% |
| 10 | `SERVICIO` | int | 0% |
| 11 | `FECHAINGRESO` | datetime2 | 0% |
| 12 | `STATUSSERVICIO` | nvarchar | 0% |
| 13 | `MOTIVO` | nvarchar | 0% |
| 14 | `AGENDADA` | datetime2 | 0% |
| 15 | `NOMBRE` | nvarchar | 0% |
| 16 | `STATUSCLIENTE` | nvarchar | 0% |
| 17 | `TELEFONOCLIENTE` | nvarchar | 0% |
| 18 | `ORDEN` | real | 5% |
| 19 | `STATUSORDEN` | nvarchar | 5% |
| 20 | `AGENDAMIENTO` | nvarchar | 5% |
| 21 | `PRINCIPAL` | nvarchar | 0% |
| 22 | `DEUDA` | real | 68% |
| 23 | `CANTIDADDECUOTAS` | int | 0% |
| 24 | `SERVICIONOMBRE` | nvarchar | 0% |
| 25 | `FECHADESCONEXION` | datetime2 | 0% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `DEBITOAUTOMATICO` | nvarchar | 0% |
| 28 | `PROMOTOR` | nvarchar | 0% |
| 29 | `PROMOTORGRUPO` | nvarchar | 0% |
| 30 | `FECHACONEXION` | datetime2 | 0% |
| 31 | `DEPARTAMENTO` | nvarchar | 0% |
| 32 | `LOCALIDAD` | nvarchar | 0% |
| 33 | `SEGMENTO` | nvarchar | 0% |
| 34 | `SINCARGO` | nvarchar | 0% |
| 35 | `ULTPERIODO` | int | 2% |
| 36 | `IMPORTEULTFACTURA` | real | 2% |
| 37 | `ULTPAGO` | datetime2 | 0% |
| 38 | `NOMBREPROMOCION` | nvarchar | 70% |
| 39 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 40 | `USUARIO` | nvarchar | 0% |
| 41 | `CLITIPO` | nvarchar | 0% |
| 42 | `IDPLANCOMERCIAL` | real | 100% |
| 43 | `PLANCOMERCIAL` | nvarchar | 100% |
| 44 | `CODMZN` | nvarchar | 0% |
| 45 | `IDZONA` | real | 14% |
| 46 | `ZONA` | nvarchar | 14% |
| 47 | `CLIENTESRVOBSERVACION` | nvarchar | 0% |
| 48 | `PIPELINERUNID` | nvarchar | 0% |
| 49 | `PERIODOINGRESO` | nvarchar | 0% |
| 50 | `ORDENNRO` | bigint | 0% |
| 51 | `BAJANETA` | varchar | 0% |
| 52 | `CONTRATOFINS` | date | 0% |
| 53 | `PKPREVENTANRO` | varchar | 0% |
| 54 | `PREVENTATPO` | varchar | 0% |
| 55 | `NEGOCIOSEGMENTO` | int | 0% |
| 56 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 57 | `PREVENTAUSR` | varchar | 0% |
| 58 | `PROMOTORID` | int | 0% |
| 59 | `PREVENTAMEDCOBROID` | int | 0% |
| 60 | `PRODUCTOPREVENTA` | int | 0% |
| 61 | `POLITICAID` | int | 0% |
| 62 | `PROMOCIONID` | int | 2% |
| 63 | `POLITICAPRC` | float | 0% |
| 64 | `PREVENTAFCHING` | datetime2 | 0% |
| 65 | `PREVENTAFCHFIN` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_BAJASVOL_360
-- Extraida: 2026-08-07T15:27:40.465651+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_BAJASVOL_360]
AS SELECT n.*,
		   p.PKPREVENTANRO, p.PREVENTATPO, p.NEGOCIOSEGMENTO, p.NEGOCIOSEGMENTOTIPOID, p.PREVENTAUSR, 
		   p.PROMOTORID, p.PREVENTAMEDCOBROID, p.PRODUCTOID AS PRODUCTOPREVENTA, p.POLITICAID, p.PROMOCIONID,
		   p.POLITICAPRC, p.PREVENTAFCHING, p.PREVENTAFCHFIN
	FROM V_BAJASVOLUNTARIAS_NETAS n
	INNER JOIN ( SELECT * FROM V_PREVENTAS_FINAL WHERE PREVENTASTS = 'F' ) p
	ON (	 ( n.empresaid = p.empresaid ) AND ( n.cliente = p.clientenropreventa ) AND ( n.contrato = p.preventaprodcongen ) 
		 AND ( n.FECHAINGRESO >= p.PREVENTAFCHING )
	   );
```
