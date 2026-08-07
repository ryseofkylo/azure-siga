---
esquema: dbo
tabla: V_USUARIO
objeto: dbo.V_USUARIO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 10
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_USUARIO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.USUARIO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `USUARIOID` | varchar |  |
| 2 | `USUARIONOMBRE` | nvarchar |  |
| 3 | `USUARIOLGN` | nvarchar |  |
| 4 | `ORGANIZACIONID` | int |  |
| 5 | `USUARIOFCHINGRESO` | datetime2 |  |
| 6 | `USUARIOSEXO` | nvarchar |  |
| 7 | `USUARIOLEGAJO` | nvarchar |  |
| 8 | `USUARIOSTS` | nvarchar |  |
| 9 | `ADACTIVO` | int |  |
| 10 | `ADUSERNAME` | nvarchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_USUARIO
-- Extraida: 2026-08-07T15:28:23.254940+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_USUARIO]
AS SELECT CAST( USUARIOID AS VARCHAR(10) ) AS USUARIOID, USUARIONOMBRE, USUARIOLGN, ORGANIZACIONID, 
		   USUARIOFCHINGRESO, USUARIOSEXO,  USUARIOLEGAJO, USUARIOSTS, ADACTIVO, ADUSERNAME
    FROM SIGAMSASC.USUARIO
	UNION ALL
	SELECT '01', 'SISTEMA', 'ROOT', 0, NULL, NULL, NULL, NULL, NULL, NULL
	UNION ALL
	SELECT '02', 'SISTEMA2', 'SUCURSAL VIRTUAL', 0, NULL, NULL, NULL, NULL, NULL, NULL
	UNION ALL
	SELECT '03', 'SISTEMA3', 'SV EXPRESS', 0, NULL, NULL, NULL, NULL, NULL, NULL
	UNION ALL
	SELECT '04', 'SISTEMA4', 'CALLCENTER', 0, NULL, NULL, NULL, NULL, NULL, NULL
	UNION ALL
	SELECT '05', 'SISTEMA5', 'IVRCALL', 0, NULL, NULL, NULL, NULL, NULL, NULL;
```
