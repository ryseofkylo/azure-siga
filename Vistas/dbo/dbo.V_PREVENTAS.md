---
esquema: dbo
tabla: V_PREVENTAS
objeto: dbo.V_PREVENTAS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 20
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_PREVENTAS

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
| 4 | `PREVENTASTS` | varchar | 0% |
| 5 | `PREVENTATPO` | varchar | 0% |
| 6 | `CLIENTENROPREVENTA` | int | 2% |
| 7 | `NEGOCIOSEGMENTO` | int | 0% |
| 8 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 9 | `PREVENTAFCHING` | datetime2 | 0% |
| 10 | `PREVENTAUSR` | varchar | 0% |
| 11 | `PROMOTORID` | int | 0% |
| 12 | `PREVENTAMEDCOBROID` | int | 0% |
| 13 | `PREVENTAFCHFIN` | datetime2 | 1% |
| 14 | `PREVENTAPRODLIN` | int | 0% |
| 15 | `PRODUCTOID` | int | 0% |
| 16 | `POLITICAID` | int | 0% |
| 17 | `PROMOCIONID` | int | 27% |
| 18 | `PREVENTAPRODSTS` | varchar | 0% |
| 19 | `PREVENTAPRODCONGEN` | int | 7% |
| 20 | `PREVENTAPRODCANTIDAD` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_PREVENTAS
-- Extraida: 2026-08-07T15:28:12.442097+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_PREVENTAS]
AS SELECT p.EMPRESAID, p.PREVENTANRO, p.PKPREVENTANRO, p.PREVENTASTS, p.PREVENTATPO, p.CLIENTENROPREVENTA,
		   p.NEGOCIOSEGMENTO, p.NEGOCIOSEGMENTOTIPOID,
		   p.PREVENTAFCHING, p.PREVENTAUSR, p.PROMOTORID, p.PREVENTAMEDCOBROID, p.PREVENTAFCHFIN,
		   o.PREVENTAPRODLIN, o.PRODUCTOID, o.POLITICAID, o.PROMOCIONID, o.PREVENTAPRODSTS,
		   o.PREVENTAPRODCONGEN, o.PREVENTAPRODCANTIDAD
	FROM SIGASC.PREVENTACLIENTE p 
	LEFT JOIN SIGASC.PREVENTAPRODUCTO o ON ( ( p.empresaid = o.empresaid ) AND ( p.preventanro = o.preventanro ) )
	WHERE p.preventafching >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101);
```
