---
esquema: dbo
tabla: V_RECUPEROMOR_360
objeto: dbo.V_RECUPEROMOR_360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 53
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_RECUPEROMOR_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
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
| 7 | `PRODUCTOTIPO` | nvarchar | 0% |
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
| 23 | `DEUDA` | real | 16% |
| 24 | `CANTIDADDECUOTAS` | int | 0% |
| 25 | `TELEFONOCLIENTE` | nvarchar | 0% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `MEDIODEREPARTO` | nvarchar | 0% |
| 28 | `SEGMENTO` | nvarchar | 0% |
| 29 | `SINCARGO` | nvarchar | 0% |
| 30 | `PROMOTORGRUPO` | nvarchar | 0% |
| 31 | `NOMBREPROMOCION` | nvarchar | 14% |
| 32 | `USUARIOPROMOCION` | nvarchar | 14% |
| 33 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 34 | `CLITIPO` | nvarchar | 0% |
| 35 | `IDPLANCOMERCIAL` | real | 100% |
| 36 | `PLANCOMERCIAL` | nvarchar | 100% |
| 37 | `CODMZN` | nvarchar | 0% |
| 38 | `IDZONA` | real | 7% |
| 39 | `ZONA` | nvarchar | 7% |
| 40 | `PIPELINERUNID` | nvarchar | 0% |
| 41 | `PKPREVENTANRO` | varchar | 0% |
| 42 | `PREVENTATPO` | varchar | 0% |
| 43 | `NEGOCIOSEGMENTO` | int | 0% |
| 44 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 45 | `PREVENTAUSR` | varchar | 0% |
| 46 | `PROMOTORID` | int | 0% |
| 47 | `PREVENTAMEDCOBROID` | int | 0% |
| 48 | `PRODUCTOPREVENTA` | int | 0% |
| 49 | `POLITICAID` | int | 0% |
| 50 | `PROMOCIONID` | int | 6% |
| 51 | `POLITICAPRC` | float | 0% |
| 52 | `PREVENTAFCHING` | datetime2 | 0% |
| 53 | `PREVENTAFCHFIN` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_RECUPEROMOR_360
-- Extraida: 2026-08-07T15:28:16.340461+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_RECUPEROMOR_360]
AS SELECT n.*,
		   p.PKPREVENTANRO, p.PREVENTATPO, p.NEGOCIOSEGMENTO, p.NEGOCIOSEGMENTOTIPOID, p.PREVENTAUSR, 
		   p.PROMOTORID, p.PREVENTAMEDCOBROID, p.PRODUCTOID AS PRODUCTOPREVENTA, p.POLITICAID, p.PROMOCIONID,
		   p.POLITICAPRC, p.PREVENTAFCHING, p.PREVENTAFCHFIN
	FROM V_FILTRO_RECUPMORSOS n
	INNER JOIN ( SELECT * FROM V_PREVENTAS_FINAL WHERE PREVENTASTS = 'F' ) p
	ON (	 ( n.empresaid = p.empresaid ) AND ( n.clientenro = p.clientenropreventa ) AND ( n.contrato = p.preventaprodcongen ) 
		 AND ( n.FECHADEPROCESADA >= p.PREVENTAFCHING )
	   );
```
