---
esquema: dbo
tabla: V_SG_CASO
objeto: dbo.V_SG_CASO
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

# dbo.V_SG_CASO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]
- [[dbo.SG_ClientMessage]]
- [[dbo.SG_Tag]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CASOID` | bigint | 0% |
| 2 | `IDMENSAJE` | bigint | 100% |
| 3 | `IDTAG` | bigint | 100% |
| 4 | `CLOSE_DATE` | date | 0% |
| 5 | `NROCLIENTE` | nvarchar | 27% |
| 6 | `CAMPAIGN` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_SG_CASO
-- Extraida: 2026-08-07T15:28:18.970188+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_SG_CASO]
AS SELECT c.id AS CASOID,
		   m.id AS IDMENSAJE,
		   t.IDTAG,
		   CONVERT(DATE, c.close_date) AS CLOSE_DATE,
		   c.NROCLIENTE,
		   c.CAMPAIGN
	FROM SG_CASO c
	LEFT JOIN ( SELECT * FROM SG_CLIENTMESSAGE WHERE text IN ('Estoy en Super','Continuar mi gestión','Necesito asistencia técnica') ) m ON ( c.id = m.casoid )
	LEFT JOIN ( SELECT * FROM SG_TAG 
				WHERE NAME IN ('Cliente no responde','Cliente retenido','Imposibilidad de contacto','No retenido','No retenidos',
							   'OT Generada','RETENIDO','Solicito prioridad','Solucionado en línea' ) ) t
	ON ( c.id = t.casoid )
	WHERE c.close_date >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101);
```
