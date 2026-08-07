---
esquema: dbo
tabla: V_RECUPEROVOL_360
objeto: dbo.V_RECUPEROVOL_360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 42
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_RECUPEROVOL_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_FILTRO_RECUPVOLUNTARIOS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENRO` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODUCTO` | nvarchar | 0% |
| 7 | `TIPOPROD` | nvarchar | 0% |
| 8 | `SUCURSALID` | int | 0% |
| 9 | `CENTROOPERATIVO` | nvarchar | 2% |
| 10 | `NOMBRE` | nvarchar | 0% |
| 11 | `MEDIODECOBRO` | nvarchar | 0% |
| 12 | `CLIENTETST` | nvarchar | 0% |
| 13 | `TELEFONO` | nvarchar | 0% |
| 14 | `DEPARTAMENTO` | nvarchar | 0% |
| 15 | `LOCALIDAD` | nvarchar | 0% |
| 16 | `PRINCIPAL` | nvarchar | 0% |
| 17 | `CONTRATOSTS` | nvarchar | 0% |
| 18 | `FECHAFINALIZACION` | datetime2 | 0% |
| 19 | `SEGMENTO` | nvarchar | 0% |
| 20 | `SINCARGO` | nvarchar | 0% |
| 21 | `PROMOCIONES` | nvarchar | 32% |
| 22 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 23 | `CLIENTETIPO` | nvarchar | 0% |
| 24 | `IDPLANCOMERCIAL` | real | 100% |
| 25 | `PLANCOMERCIAL` | nvarchar | 100% |
| 26 | `CODMZN` | nvarchar | 0% |
| 27 | `IDZONA` | real | 6% |
| 28 | `ZONA` | nvarchar | 6% |
| 29 | `PIPELINERUNID` | nvarchar | 0% |
| 30 | `PKPREVENTANRO` | varchar | 0% |
| 31 | `PREVENTATPO` | varchar | 0% |
| 32 | `NEGOCIOSEGMENTO` | int | 0% |
| 33 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 34 | `PREVENTAUSR` | varchar | 0% |
| 35 | `PROMOTORID` | int | 0% |
| 36 | `PREVENTAMEDCOBROID` | int | 0% |
| 37 | `PRODUCTOPREVENTA` | int | 0% |
| 38 | `POLITICAID` | int | 0% |
| 39 | `PROMOCIONID` | int | 2% |
| 40 | `POLITICAPRC` | float | 0% |
| 41 | `PREVENTAFCHING` | datetime2 | 0% |
| 42 | `PREVENTAFCHFIN` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_RECUPEROVOL_360
-- Extraida: 2026-08-07T15:28:17.300942+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_RECUPEROVOL_360]
AS SELECT n.*,
		   p.PKPREVENTANRO, p.PREVENTATPO, p.NEGOCIOSEGMENTO, p.NEGOCIOSEGMENTOTIPOID, p.PREVENTAUSR, 
		   p.PROMOTORID, p.PREVENTAMEDCOBROID, p.PRODUCTOID AS PRODUCTOPREVENTA, p.POLITICAID, p.PROMOCIONID,
		   p.POLITICAPRC, p.PREVENTAFCHING, p.PREVENTAFCHFIN
	FROM V_FILTRO_RECUPVOLUNTARIOS n
	INNER JOIN ( SELECT * FROM V_PREVENTAS_FINAL WHERE PREVENTASTS = 'F' ) p
	ON (	 ( n.empresaid = p.empresaid ) AND ( n.clientenro = p.clientenropreventa ) AND ( n.contratonro = p.preventaprodcongen ) 
		 AND ( n.FECHAFINALIZACION >= p.PREVENTAFCHING )
	   );
```
