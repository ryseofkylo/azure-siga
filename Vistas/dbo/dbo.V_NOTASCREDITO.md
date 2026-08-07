---
esquema: dbo
tabla: V_NOTASCREDITO
objeto: dbo.V_NOTASCREDITO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 19
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_NOTASCREDITO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.EMPRESA]]
- [[SIGASC.FACTURA]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `PKCLIENTENRO` | varchar | 0% |
| 4 | `FACTURANRO` | int | 0% |
| 5 | `PKFACTURANRO` | varchar | 0% |
| 6 | `FACTURAFCH` | datetime2 | 0% |
| 7 | `PERIODOGENERADA` | nvarchar | 0% |
| 8 | `PERIODONC` | int | 0% |
| 9 | `FACTURAGEN` | varchar | 0% |
| 10 | `FACTURATPO` | varchar | 0% |
| 11 | `IMPORTE` | real | 0% |
| 12 | `MEDCOBFAC` | int | 0% |
| 13 | `FACTURAUSR` | varchar | 0% |
| 14 | `MOTIVOFACID` | int | 0% |
| 15 | `APLICAFACTURA` | int | 0% |
| 16 | `APLICAPKFACTURA` | varchar | 0% |
| 17 | `APLICAFACTURAFCH` | datetime2 | 0% |
| 18 | `APLICAFACTURAIMPORTE` | real | 0% |
| 19 | `APLICAPERIODO` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_NOTASCREDITO
-- Extraida: 2026-08-07T15:28:03.120351+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_NOTASCREDITO]
AS SELECT  n.EMPRESAID,
	   n.CLIENTENRO,
	   CONCAT( n.empresaid, CONCAT( '_', n.clientenro ) ) AS PKCLIENTENRO,
	   n.FACTURANRO,
	   n.PKFACTURANRO,
	   n.FACTURAFCH,
	   FORMAT( n.facturafch, 'yyyyMM' ) AS PERIODOGENERADA,
	   CASE WHEN ( n.facturaperiodo = 0 ) THEN FORMAT( n.facturafch, 'yyyyMM' ) ELSE n.facturaperiodo END AS PERIODONC,
	   n.FACTURAGEN,
	   n.FACTURATPO,
	  -- CASE e.empresadevengavto 
			--WHEN 1 THEN n.FACTURATOTAL
			--WHEN 2 THEN n.FACTURATOTALV2
			--WHEN 3 THEN n.FACTURATOTALV3
			--ELSE n.FACTURATOTAL
	  -- END AS IMPORTE,
	  n.FACTURATOTAL AS IMPORTE,
	  -- CASE e.empresadevengavto 
			--WHEN 1 THEN n.FACTURAVTO
			--WHEN 2 THEN n.FACTURAVTO2
			--WHEN 3 THEN n.FACTURAVTO3
			--ELSE n.FACTURAVTO
	  -- END AS FECHAVTO,
	   n.MEDCOBFAC,
	   n.FACTURAUSR,
	   n.MOTIVOFACID,
	   f.FACTURANRO		AS APLICAFACTURA, 
	   f.PKFACTURANRO   AS APLICAPKFACTURA, 
	   f.FACTURAFCH		AS APLICAFACTURAFCH,
	   f.FACTURATOTAL as APLICAFACTURAIMPORTE,
	   CASE WHEN ( f.facturaperiodo = 0 ) THEN FORMAT( f.facturafch, 'yyyyMM' ) ELSE f.facturaperiodo END AS APLICAPERIODO
	  -- ,CASE e.empresadevengavto
			--WHEN 1 THEN f.FACTURATOTAL
			--WHEN 2 THEN f.FACTURATOTALV2
			--WHEN 3 THEN f.FACTURATOTALV3
			--ELSE f.FACTURATOTAL
	  -- END AS APLICATOTAL
FROM
( SELECT * FROM SIGASC.FACTURA WHERE FACTURATPO = 'N'
  AND (   
	    ( facturaperiodo <> 0 
		  AND facturaperiodo >= FORMAT( DATEADD(dd,-(DAY(DATEADD(mm,-1,GETDATE()))-1),DATEADD(mm,-13,GETDATE())), 'yyyyMM') -- 13 ULTIMOS PERIODOS DE FACTURACION
        )
     OR ( facturaperiodo = 0
	      AND facturafch >= DATEADD(dd,-(DAY(DATEADD(mm,-1,CAST(GETDATE() AS DATE)))-1),DATEADD(mm,-13,CAST(GETDATE() AS DATE))) -- 13 ULTIMOS MESES
        )
	  )
) n
LEFT JOIN ( SELECT * FROM SIGASC.FACTURA WHERE FACTURATPO = 'F' ) f ON ( CONCAT(n.empresaid, CONCAT('_', n.facturanronc)) = f.pkfacturanro )
LEFT JOIN SIGAMSASC.EMPRESA e ON ( f.empresaid = e.empresaid )
WHERE n.facturausr <> 'SAS';
```
