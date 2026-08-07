---
esquema: dbo
tabla: V_CRMREGISTRO
objeto: dbo.V_CRMREGISTRO
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

# dbo.V_CRMREGISTRO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CRMREGISTRO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `CRMNRO` | varchar | 0% |
| 4 | `CRMOBS` | varchar | 0% |
| 5 | `CRMFCHINI` | date | 0% |
| 6 | `CRMSTS` | varchar | 0% |
| 7 | `CRMMEDIO` | varchar | 0% |
| 8 | `CRMUSRACT` | varchar | 0% |
| 9 | `CRMUSRING` | varchar | 0% |
| 10 | `MOTIVOID` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CRMREGISTRO
-- Extraida: 2026-08-07T15:27:51.760290+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_CRMREGISTRO]
AS SELECT C.EMPRESAID,
	   CONCAT(CONCAT(C.EMPRESAID,'_'),C.CLIENTENRO) AS CLIENTENRO,
	   (c.pkcrmnro) AS CRMNRO,
	   C.CRMOBS,
	   CONVERT(DATE,C.CRMFCHINI) AS CRMFCHINI,
	   C.CRMSTS,  
	   C.CRMMEDIO, 
	   C.CRMUSRACT,
	   C.CRMUSRING,
	   CONCAT(EMPRESAID, '_', ISNULL(CRMMOTIVO1,0), '_', ISNULL(CRMMOTIVO2,0), '_', ISNULL(CRMMOTIVO3,0), '_', ISNULL(CRMMOTIVO4,0) ) AS MOTIVOID
FROM SIGASC.CRMREGISTRO C
WHERE CRMFCHINI >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101) -- 13 ULTIMOS MESES 
AND CRMMOTIVO1 <> '2'		-- CRM QUE NO SEAN DE "CAMPAÑAS"
AND CLIENTENRO <> 0			-- CLIENTENRO DEL CRM DIFERENTE DE 0
AND LEN(clientenro) >= 4	-- CLIENTENRO DEL CRM MAYOR A 4 DIGITOS
AND CRMSTS <> 'A';
```
