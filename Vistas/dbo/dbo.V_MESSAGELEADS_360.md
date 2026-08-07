---
esquema: dbo
tabla: V_MESSAGELEADS_360
objeto: dbo.V_MESSAGELEADS_360
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

# dbo.V_MESSAGELEADS_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_ClientMessage]]
- [[dbo.V_LEADS_360]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Date` | datetime2 | 0% |
| 3 | `Text` | nvarchar | 0% |
| 4 | `CasoId` | bigint | 0% |
| 5 | `CREATION_DATE` | datetime2 | 0% |
| 6 | `CLOSE_DATE` | datetime2 | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_MESSAGELEADS_360
-- Extraida: 2026-08-07T15:28:02.128790+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_MESSAGELEADS_360]
AS SELECT c.*, e.CREATION_DATE, e.CLOSE_DATE
FROM dbo.SG_CLIENTMESSAGE c
INNER JOIN 
	( SELECT DISTINCT CASOID FROM dbo.SG_CLIENTMESSAGE
	  WHERE text IN ('Hola, me gustaría contratar un servicio ¿Me pueden ayudar?',
					 'Hola, quiero que me asesoren', 
					 'Hola, me gustaría que me asesoren',
					 'Me interesa la promo del folleto' )
	) m
ON ( c.casoid = m.casoid )
INNER JOIN V_LEADS_360 e ON ( e.id = c.casoid ) 
WHERE e.campaign = 'Whatsapp';
```
