---
esquema: dbo
tabla: v_listapromociones
objeto: dbo.v_listapromociones
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 1
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_listapromociones

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATOPROMOCION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PROMOCIONID` | varchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_listapromociones
-- Extraida: 2026-08-07T15:28:00.458037+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [v_listapromociones]
AS select Distinct CONCAT(CONCAT(empresaid,'_'),promocionid) AS PROMOCIONID
		 from sigasc.contratopromocion
		 where CONVERT(DATE,SUBSTRING(CONTRATOPRMFCH,CHARINDEX('_',CONTRATOPRMFCH)+1,LEN(CONTRATOPRMFCH))) >= '2022/07/01' 
		 and len(contratoprmfch) > 10;
```
