---
esquema: dbo
tabla: V_RECIBO
objeto: dbo.V_RECIBO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 15
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_RECIBO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.FACTURA]]
- [[SIGASC.RECIBO]]
- [[SIGASC.RECIBOFAC]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `RECIBONRO` | varchar | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `RECIBOFCH` | datetime2 | 0% |
| 5 | `RECIBOSTS` | varchar | 0% |
| 6 | `MEDCOBRBO` | int | 0% |
| 7 | `RECIBOIMP` | float | 0% |
| 8 | `RECIBOSDO` | float | 0% |
| 9 | `RECIBOUSR` | varchar | 0% |
| 10 | `RECIBOGEN` | varchar | 0% |
| 11 | `RECIBOFCHCOB` | datetime2 | 0% |
| 12 | `RECIBOTPO` | varchar | 0% |
| 13 | `RECIBOMODALIDAD` | varchar | 0% |
| 14 | `MOTIVOFACID` | int | 0% |
| 15 | `FACTURAPERIODO` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_RECIBO
-- Extraida: 2026-08-07T15:28:15.354171+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_RECIBO]
AS SELECT r.EMPRESAID, r.RECIBONRO, r.CLIENTENRO, r.RECIBOFCH, 
		   r.RECIBOSTS, r.MEDCOBRBO, r.RECIBOIMP, r.RECIBOSDO, 
		   r.RECIBOUSR, r.RECIBOGEN, r.RECIBOFCHCOB, 
		   r.RECIBOTPO, r.RECIBOMODALIDAD, r.MOTIVOFACID,
		   MIN(ISNULL(f.FACTURAPERIODO,0)) AS FACTURAPERIODO
		   --CASE WHEN ( COUNT(DISTINCT f.facturanro) > 1 ) 
			--	THEN ( MIN(ISNULL(f.FACTURAPERIODO,0)) AS FACTURAPERIODO
		   /*f.FACTURAPERIODO,
		   f.FACTURATPO,
		   f.FACTURANRO,
		   e.RECIBOFACIMP,
		   e.RECIBOFACIMPRBO*/
	FROM SIGASC.RECIBO r
    LEFT JOIN SIGASC.RECIBOFAC e ON ( r.recibonro = e.recibonro )
	LEFT JOIN SIGASC.FACTURA f ON ( ( e.facturanro = f.facturanro ) AND ( e.facturatpo = f.facturatpo ) )
	WHERE r.recibosts <> 'X'
	AND r.recibotpo = 'R'
	--AND trim(RECIBOFACIMPTPO) <> 'R'
	--AND r.recibonro IN ('18_169415','1_23280833')
	--AND f.facturatpo LIKE '%F'
	AND CONVERT(DATE,r.RECIBOFCH) >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-4,GETDATE())),101) -- 3 ULTIMOS MESES 
	GROUP BY r.EMPRESAID, r.RECIBONRO, r.CLIENTENRO, r.RECIBOFCH, 
		   r.RECIBOSTS, r.MEDCOBRBO, r.RECIBOIMP, r.RECIBOSDO, 
		   r.RECIBOUSR, r.RECIBOGEN, r.RECIBOFCHCOB, 
		   r.RECIBOTPO, r.RECIBOMODALIDAD, r.MOTIVOFACID;
```
