---
esquema: dbo
tabla: V_USUARIO_ORGANIZACION
objeto: dbo.V_USUARIO_ORGANIZACION
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 6
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_USUARIO_ORGANIZACION

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_ORGANIZACION]]
- [[dbo.V_USUARIO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `usuarioid` | varchar |  |
| 2 | `usuarionombre` | varchar |  |
| 3 | `usuariolgn` | varchar |  |
| 4 | `organizacionid` | int |  |
| 5 | `ORGANIZACIONNOMBRE` | varchar |  |
| 6 | `ORGANIZACIONGRUPO` | varchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_USUARIO_ORGANIZACION
-- Extraida: 2026-08-07T15:28:23.593258+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_USUARIO_ORGANIZACION]
AS SELECT  u.usuarioid, u.usuarionombre, u.usuariolgn, u.organizacionid,o.[ORGANIZACIONNOMBRE],o.[ORGANIZACIONGRUPO]
 FROM [dbo].[V_USUARIO]  u
left join  [dbo].[V_ORGANIZACION]  o
on u.ORGANIZACIONID=  o.[ORGANIZACIONID];
```
