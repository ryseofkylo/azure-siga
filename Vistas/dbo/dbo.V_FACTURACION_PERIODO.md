---
esquema: dbo
tabla: V_FACTURACION_PERIODO
objeto: dbo.V_FACTURACION_PERIODO
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 35
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_FACTURACION_PERIODO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.FACTURACION]]
- [[dbo.v_EscalonPromo]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `FACTURATPO` | varchar | 0% |
| 3 | `FACTURANRO` | int | 0% |
| 4 | `CLIENTENRO` | varchar | 0% |
| 5 | `FACTURASTS` | varchar | 0% |
| 6 | `FACTURAFCH` | date | 0% |
| 7 | `FACTURAPERIODO` | int | 0% |
| 8 | `FACTURAVTO` | date | 0% |
| 9 | `FACTURAVTO2` | date | 0% |
| 10 | `FACTURAVTO3` | date | 0% |
| 11 | `FACTURAFCOB` | date | 7% |
| 12 | `FACTURAFICOB` | date | 7% |
| 13 | `FACTURAPRN` | int | 0% |
| 14 | `MEDCOBFAC` | int | 0% |
| 15 | `COBRADORID` | int | 0% |
| 16 | `FACTURAGEN` | varchar | 0% |
| 17 | `FACTURACIUDADID` | int | 0% |
| 18 | `FACTURALIN` | nvarchar | 0% |
| 19 | `CPTOFACID` | int | 0% |
| 20 | `FACTURALINTPO` | nvarchar | 0% |
| 21 | `FACTURALINCUO` | nvarchar | 0% |
| 22 | `FACTURALINIMP` | float | 0% |
| 23 | `FACTURALINIMPV2` | real | 0% |
| 24 | `FACTURALINIMPV3` | real | 0% |
| 25 | `FACTURAPRJIVA` | real | 0% |
| 26 | `FACTURALINIVAIMP` | real | 0% |
| 27 | `FACTURALINCOD` | int | 0% |
| 28 | `FACTURAPOL` | int | 0% |
| 29 | `FACTURAPRM` | int | 0% |
| 30 | `FACTURACMB` | int | 0% |
| 31 | `CuotaDesde` | int | 18% |
| 32 | `PRODUCTOID` | nvarchar | 0% |
| 33 | `IMPORTE_POL` | float | 0% |
| 34 | `IMPORTE_PRM` | float | 0% |
| 35 | `ESCALON` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_FACTURACION_PERIODO
-- Extraida: 2026-08-07T15:27:55.077625+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_FACTURACION_PERIODO]
AS with factura as(SELECT f.EMPRESAID,																				-- EMPRESA
		   --SUBSTRING(f.FACTURATPO,CHARINDEX('_',f.FACTURATPO)+1,LEN(f.FACTURATPO)) AS FACTURATPO,	
		   f.FACTURATPO,																			-- TIPO DE DOCUMENTO
		   f.FACTURANRO,																			-- NRO DE DOCUMENTO
		   CONCAT(CONCAT(f.EMPRESAID,'_'),f.CLIENTENRO) AS CLIENTENRO,								-- NRO DE CLIENTE
		   f.FACTURASTS,																			-- ESTADO DEL DOCUMENTO
		   CONVERT(DATE, f.FACTURAFCH) AS FACTURAFCH,												-- FECHA DE EMISIÓN
		   f.FACTURAPERIODO,																	    -- PERIODO DOCUMENTO			
		   CONVERT(DATE, f.FACTURAVTO)  AS FACTURAVTO,												-- FECHA VTO 1 
		   CONVERT(DATE, f.FACTURAVTO2)  AS FACTURAVTO2,											-- FECHA VTO 2
		   CONVERT(DATE, f.FACTURAVTO3)  AS FACTURAVTO3,											-- FECHA VTO 3
		   CONVERT(DATE, f.FACTURAFCOB) AS FACTURAFCOB,												-- FECHA COBRANZA
		   CONVERT(DATE, f.FACTURAFICOB) AS FACTURAFICOB,											-- --
		   f.FACTURAPRN,																			-- --
		   f.MEDCOBFAC,																				-- MEDIO COBRO
		   f.COBRADORID,																			-- ID COBRADOR
		   f.FACTURAGEN,																			-- CATEGORIA DEL DOCUMENTO
		   f.FACTURACIUDADID,																		-- CIUDAD 
		   --SUBSTRING(f.FACTURALIN,CHARINDEX('_',f.FACTURALIN)+1,LEN(f.FACTURALIN)) AS FACTURALIN,	
		   ( f.PKFACTURALIN ) AS  FACTURALIN,														-- NRO LINEA FACTURA
		   f.CPTOFACID,																				-- CONCEPTO DE FACTURACION
		   f.FACTURALINTPO,																			-- TIPO LINEA FACTURA
		   f.FACTURALINCUO,																			-- PERIODO O CUOTA 
		   ROUND(f.FACTURALINIMP, 2, 1) AS FACTURALINIMP,											-- IMPORTE LINEA FACTURA VTO 1
		   f.FACTURALINIMPV2,																		-- IMPORTE LINEA FACTURA VTO 2
		   f.FACTURALINIMPV3,																		-- IMPORTE LINEA FACTURA VTO 3
		   f.FACTURAPRJIVA,																			-- % IVA
		   f.FACTURALINIVAIMP,																		-- $ IVA
		   f.FACTURALINCOD,																			-- NRO CONTRATO
		   f.FACTURAPOL,																			-- ID POLITICA 
		   f.FACTURAPRM,																			-- ID PROMOCION 
		   f.FACTURACMB,	
           cast(
				CASE
                WHEN f.FACTURALINCUO IS NULL 
					or len(ltrim(rtrim(FACTURALINCUO))) =0 
					or PATINDEX('%/%',ltrim(rtrim(FACTURALINCUO))) =0
					OR ISNUMERIC(left(ltrim(rtrim(FACTURALINCUO)), PATINDEX('%/%',ltrim(rtrim(FACTURALINCUO)))-1))=0
						THEN null
						ELSE left(ltrim(rtrim(FACTURALINCUO)), PATINDEX('%/%',ltrim(rtrim(FACTURALINCUO)))-1)
				END as int) as CuotaDesde,																		-- ID COMBO
		   ( f.PKPRODUCTOID ) AS PRODUCTOID,														    -- ID PRODUCTO
		   CASE WHEN ( ( ISNULL(f.facturaprm, 0) = 0 ) AND ( ISNULL(f.facturacmb, 0) = 0 ) )
				OR	 ( f.cptofacid IN ('9341','9342','9343','9344') )
				THEN ROUND( f.facturalinimp,2,1 )
				ELSE 0
				END AS IMPORTE_POL,
		   CASE WHEN ( ( f.facturaprm <> 0 ) OR ( f.facturacmb <> 0 ) ) 
				AND	 ( f.cptofacid NOT IN ('9341','9342','9343','9344') )
				THEN ROUND( f.facturalinimp,2,1 )
				ELSE 0
				END AS IMPORTE_PRM			
	FROM SIGASC.FACTURACION f
	INNER JOIN SIGASC.CONTRATO c 
	ON ( ( CONCAT(CONCAT(f.empresaid,'_'),f.clientenro) = c.pkclientenro ) 
	AND  ( CONCAT(CONCAT(f.empresaid,'_'),f.facturalincod) = c.pkcontratonro ) )
	WHERE facturaperiodo >= FORMAT( DATEADD(dd,-(DAY(DATEADD(mm,-1,GETDATE()))-1),DATEADD(mm,-13,GETDATE())), 'yyyyMM') -- 13 ULTIMOS PERIODOS DE FACTURACION
	AND f.facturatpo IN ('F')
)

    select f.*,CASE
        		WHEN ep.empresaid IS NOT NULL THEN 1
        		ELSE 0
				END AS ESCALON	
    from factura f
    left join v_EscalonPromo ep
	on ep.empresaid = f.empresaid
	and ep.promocionid = f.facturaprm
    and CuotaDesde= ep.[PROMOCIONMES];
```
