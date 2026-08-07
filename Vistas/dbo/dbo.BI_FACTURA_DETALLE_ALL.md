---
esquema: dbo
tabla: BI_FACTURA_DETALLE_ALL
objeto: dbo.BI_FACTURA_DETALLE_ALL
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 27
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.BI_FACTURA_DETALLE_ALL

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.COMBO]]
- [[SIGASC.CONTRATO]]
- [[SIGASC.CPTOFACTURA]]
- [[SIGASC.FACTURA]]
- [[SIGASC.FACTURALINEA]]
- [[SIGASC.POLITICA]]
- [[SIGASC.PRODUCTO]]
- [[SIGASC.PROMOCION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `empresaid` | int | 0% |
| 2 | `PERIODO` | int | 0% |
| 3 | `clientenro` | int | 0% |
| 4 | `facturatpo` | varchar | 0% |
| 5 | `facturagen` | varchar | 0% |
| 6 | `facturanro` | int | 0% |
| 7 | `TOTAL` | real | 0% |
| 8 | `CUOTA` | varchar | 0% |
| 9 | `NROLINEA` | int | 0% |
| 10 | `IVA` | real | 0% |
| 11 | `productonombre` | varchar | 34% |
| 12 | `contratonro` | int | 34% |
| 13 | `IMPORTE_LINEA` | real | 0% |
| 14 | `CONCEPTO` | varchar | 0% |
| 15 | `POLITICA` | varchar | 36% |
| 16 | `PROMO` | varchar | 82% |
| 17 | `COMBO` | varchar | 98% |
| 18 | `PROMOID` | int | 0% |
| 19 | `PoliticaId` | int | 0% |
| 20 | `cptofacid` | int | 0% |
| 21 | `Comboid` | int | 38% |
| 22 | `PRODUCTOID` | int | 34% |
| 23 | `PRODUCTOTPO` | varchar | 34% |
| 24 | `PRODUCTOPPL` | varchar | 34% |
| 25 | `FACTURAFCH` | datetime2 | 0% |
| 26 | `CuotaDesde` | int | 40% |
| 27 | `CuotaHasta` | int | 40% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.BI_FACTURA_DETALLE_ALL
-- Extraida: 2026-08-07T15:25:51.862877+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[BI_FACTURA_DETALLE_ALL]
AS SELECT f.empresaid,
          CASE
	   	  	WHEN f.facturaperiodo = 0 THEN
			YEAR(DATEADD(month,1,FACTURAFCH))*100 + MONTH(DATEADD(month,1,FACTURAFCH))
		  	ELSE f.facturaperiodo
		  END AS PERIODO,
          F.clientenro,
          F.facturatpo,
          F.facturagen,
          F.facturanro,
          F.facturatotal AS TOTAL,
          D.facturalincuo AS CUOTA,
          D.facturalin AS NROLINEA,
          D.facturalinivaimp AS IVA,
          TRIM(P.productonombre) AS productonombre,
          c.contratonro,
          D.facturalinimp AS IMPORTE_LINEA,
          trim(CONC.cptofacnombre) AS CONCEPTO,
          trim(POL.politicanombre)  AS POLITICA,
          trim(PR.promocionnombre)   AS PROMO,
          trim(CMB.combonombre)   AS COMBO,
          d.facturaprm AS PROMOID,
          D.facturapol AS PoliticaId,
          d.cptofacid,
          D.facturacmb AS Comboid,
          P.PRODUCTOID,
          P.PRODUCTOTPO,
          P.PRODUCTOPPL, 
          F.FACTURAFCH,
		 cast(
			case when 
					d.facturalincuo is null 
					or len(ltrim(rtrim(d.facturalincuo))) =0 
					or PATINDEX('%/%',ltrim(rtrim(d.facturalincuo))) =0
					OR ISNUMERIC(left(ltrim(rtrim(d.facturalincuo)), PATINDEX('%/%',ltrim(rtrim(d.facturalincuo)))-1))=0 
				then null
				else left(ltrim(rtrim(d.facturalincuo)), PATINDEX('%/%',ltrim(rtrim(d.facturalincuo)))-1) 
			end
			as int) as CuotaDesde,
			cast(
				case when
				d.facturalincuo is null 
					or len(ltrim(rtrim(d.facturalincuo))) =0 
					or PATINDEX('%/%',ltrim(rtrim(d.facturalincuo))) =0
					OR ISNUMERIC(right(ltrim(rtrim(d.facturalincuo)), len(ltrim(rtrim(d.facturalincuo))) - PATINDEX('%/%',ltrim(rtrim(d.facturalincuo))))) = 0 
				then null
				else right(ltrim(rtrim(d.facturalincuo)), len(ltrim(rtrim(d.facturalincuo))) - PATINDEX('%/%',ltrim(rtrim(d.facturalincuo)))) 
				end
				as int) as CuotaHasta 
     FROM sigasc.factura f
          INNER JOIN sigasc.facturalinea d
             ON F.facturanro = D.facturanro 
             AND F.empresaid = D.empresaid
             AND f.FACTURATPO = d.FACTURATPO 
          LEFT JOIN sigasc.contrato c
             ON     D.empresaid = C.empresaid
                AND F.clientenro = C.clientenro
                AND D.facturalincod = C.contratonro
          LEFT JOIN sigasc.producto p
             ON F.empresaid = P.empresaid 
             AND C.productoid = P.productoid
          LEFT JOIN sigasc.cptofactura conc
            ON CONC.empresaid = F.empresaid
              AND CONC.cptofacid = D.cptofacid
          LEFT JOIN sigasc.politica pol
            ON f.empresaid = pol.empresaid
              AND D.facturapol = POL.politicaid
          LEFT JOIN sigasc.promocion pr
            ON PR.promocionid = D.facturaprm
              AND PR.empresaid = f.empresaid
          LEFT JOIN sigasc.combo cmb
            ON f.empresaid = CMB.empresaid 
            	AND D.facturacmb = CMB.comboid;
```
