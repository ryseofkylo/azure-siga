---
esquema: dbo
tabla: V_DIM_PREVENTAS
objeto: dbo.V_DIM_PREVENTAS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 12
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_DIM_PREVENTAS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.PREVENTACLIENTE]]
- [[SIGASC.PREVENTAPRODUCTO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PREVENTANRO` | int | 0% |
| 3 | `PKPREVENTANRO` | varchar | 0% |
| 4 | `CLIENTENROPREVENTA` | int | 2% |
| 5 | `PREVENTAPRODCONGEN` | int | 7% |
| 6 | `PKPREVENTAFIN` | varchar | 0% |
| 7 | `PREVENTAUSR` | varchar | 0% |
| 8 | `PROMOTORID` | int | 0% |
| 9 | `PREVENTAMEDCOBROID` | int | 0% |
| 10 | `PRODUCTOID` | int | 0% |
| 11 | `POLITICAID` | int | 0% |
| 12 | `PROMOCIONID` | int | 27% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_DIM_PREVENTAS
-- Extraida: 2026-08-07T15:27:52.087352+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_DIM_PREVENTAS]
AS SELECT p.EMPRESAID, p.PREVENTANRO, p.PKPREVENTANRO, p.CLIENTENROPREVENTA, o.PREVENTAPRODCONGEN,
	   CASE WHEN ( ( preventaprodcongen IS NULL ) OR ( preventaprodcongen = 0 ) )
			THEN CONCAT( p.pkpreventanro, CONCAT( '_', p.clientenropreventa ) ) 
			ELSE CONCAT( p.pkpreventanro, CONCAT( '_', CONCAT( p.clientenropreventa,
				 CONCAT( '_', o.preventaprodcongen ) ) ) ) 
			END AS PKPREVENTAFIN,
	   p.PREVENTAUSR, p.PROMOTORID, p.PREVENTAMEDCOBROID, o.PRODUCTOID, o.POLITICAID, o.PROMOCIONID
FROM SIGASC.PREVENTACLIENTE p
LEFT JOIN SIGASC.PREVENTAPRODUCTO o ON ( ( p.empresaid = o.empresaid ) AND ( p.preventanro = o.preventanro ) )
WHERE p.preventafching >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101);
```
