---
esquema: dbo
tabla: V_SG_MENSAJE
objeto: dbo.V_SG_MENSAJE
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 3
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_SG_MENSAJE

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_ClientMessage]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `IDMENSAJE` | bigint | 0% |
| 2 | `TEXT` | nvarchar | 0% |
| 3 | `CASOID` | bigint | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_SG_MENSAJE
-- Extraida: 2026-08-07T15:28:19.619293+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_SG_MENSAJE]
AS SELECT m.id AS IDMENSAJE,
		   m.TEXT,
		   m.CASOID
	FROM SG_CLIENTMESSAGE m
	WHERE text IN ('Estoy en Super','Continuar mi gestión','Necesito asistencia técnica')
	AND m.casoid IN ( SELECT DISTINCT c.id FROM SG_CASO c 
					  WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) );
```
