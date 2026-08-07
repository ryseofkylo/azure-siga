---
esquema: dbo
tabla: V_FILTRO_BAJASVOLUN
objeto: dbo.V_FILTRO_BAJASVOLUN
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

# dbo.V_FILTRO_BAJASVOLUN

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.v_bajasvoluntarias]]

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
| 9 | `CENTROOPERATIVO` | nvarchar | 0% |
| 10 | `SERVICIO` | int | 0% |
| 11 | `FECHAINGRESO` | datetime2 | 0% |
| 12 | `STATUSSERVICIO` | nvarchar | 0% |
| 13 | `MOTIVO` | nvarchar | 0% |
| 14 | `AGENDADA` | datetime2 | 0% |
| 15 | `NOMBRE` | nvarchar | 0% |
| 16 | `STATUSCLIENTE` | nvarchar | 0% |
| 17 | `TELEFONOCLIENTE` | nvarchar | 0% |
| 18 | `ORDEN` | real | 82% |
| 19 | `STATUSORDEN` | nvarchar | 82% |
| 20 | `AGENDAMIENTO` | nvarchar | 82% |
| 21 | `PRINCIPAL` | nvarchar | 0% |
| 22 | `DEUDA` | real | 37% |
| 23 | `CANTIDADDECUOTAS` | int | 0% |
| 24 | `SERVICIONOMBRE` | nvarchar | 0% |
| 25 | `FECHADESCONEXION` | datetime2 | 0% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `DEBITOAUTOMATICO` | nvarchar | 0% |
| 28 | `PROMOTOR` | nvarchar | 4% |
| 29 | `PROMOTORGRUPO` | nvarchar | 4% |
| 30 | `FECHACONEXION` | datetime2 | 0% |
| 31 | `DEPARTAMENTO` | nvarchar | 0% |
| 32 | `LOCALIDAD` | nvarchar | 0% |
| 33 | `SEGMENTO` | nvarchar | 0% |
| 34 | `SINCARGO` | nvarchar | 0% |
| 35 | `ULTPERIODO` | int | 0% |
| 36 | `IMPORTEULTFACTURA` | real | 0% |
| 37 | `ULTPAGO` | datetime2 | 0% |
| 38 | `NOMBREPROMOCION` | nvarchar | 89% |
| 39 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 40 | `USUARIO` | nvarchar | 0% |
| 41 | `CLITIPO` | nvarchar | 0% |
| 42 | `IDPLANCOMERCIAL` | real | 100% |
| 43 | `PLANCOMERCIAL` | nvarchar | 100% |
| 44 | `CODMZN` | nvarchar | 0% |
| 45 | `IDZONA` | real | 9% |
| 46 | `ZONA` | nvarchar | 9% |
| 47 | `CLIENTESRVOBSERVACION` | nvarchar | 0% |
| 48 | `PIPELINERUNID` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_FILTRO_BAJASVOLUN
-- Extraida: 2026-08-07T15:27:57.133689+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_FILTRO_BAJASVOLUN]
AS SELECT * FROM V_BAJASVOLUNTARIAS
WHERE ((productotipo IN ( 'BASICO','BASICO CATV EOC','BASICO CATV GPON','CABLE MODEM','CORPORATIVO','EOC','GPON','INTERNET' )
AND principal = 'PRINCIPAL' AND ( statusorden IS NOT NULL AND statusorden <> 'SUSPENDIDA' )) or
productotipo = 'MIO' OR prodnombre like '%ASISTENCIA%INTEGRAL%' );
```
