---
esquema: dbo
tabla: vFACTURACION_DETALLE_202308_cp
objeto: dbo.vFACTURACION_DETALLE_202308_cp
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 29
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.vFACTURACION_DETALLE_202308_cp

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.COMBO]]
- [[SIGASC.CONTRATO]]
- [[SIGASC.CONTRATOPROMOCION]]
- [[SIGASC.CPTOFACTURA]]
- [[SIGASC.FACTURA]]
- [[SIGASC.FACTURALINEA]]
- [[SIGASC.POLITICA]]
- [[SIGASC.PRODUCTO]]
- [[SIGASC.PROMOCION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `empresaid` | int |  |
| 2 | `PERIODO` | int |  |
| 3 | `clientenro` | int |  |
| 4 | `facturatpo` | varchar |  |
| 5 | `facturagen` | varchar |  |
| 6 | `facturanro` | int |  |
| 7 | `TOTAL` | float |  |
| 8 | `CUOTA` | varchar |  |
| 9 | `NROLINEA` | int |  |
| 10 | `IVA` | real |  |
| 11 | `productonombre` | varchar |  |
| 12 | `contratonro` | int |  |
| 13 | `IMPORTE_LINEA` | float |  |
| 14 | `CONCEPTO` | varchar |  |
| 15 | `POLITICA` | varchar |  |
| 16 | `PROMO` | varchar |  |
| 17 | `COMBO` | varchar |  |
| 18 | `PROMOID` | int |  |
| 19 | `PoliticaId` | int |  |
| 20 | `cptofacid` | int |  |
| 21 | `Comboid` | int |  |
| 22 | `PRODUCTOID` | int |  |
| 23 | `PRODUCTOTPO` | varchar |  |
| 24 | `TIPOPRODUCTO` | varchar |  |
| 25 | `PRODUCTOPPL` | varchar |  |
| 26 | `FACTURAFCH` | datetime2 |  |
| 27 | `CuotaDesde` | int |  |
| 28 | `CuotaHasta` | int |  |
| 29 | `contratoprmusr` | varchar |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.vFACTURACION_DETALLE_202308_cp
-- Extraida: 2026-08-07T15:28:25.173939+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vFACTURACION_DETALLE_202308_cp]
AS SELECT DISTINCT f.empresaid,
          F.facturaperiodo AS PERIODO,
          F.clientenro,
          F.facturatpo,
          F.facturagen,
          F.facturanro,
          FLOOR(F.facturatotal) AS TOTAL,
          D.facturalincuo AS CUOTA,
          D.facturalin AS NROLINEA,
          D.facturalinivaimp AS IVA,
          TRIM(P.productonombre) AS productonombre,
          c.contratonro,
          FLOOR(D.facturalinimp) AS IMPORTE_LINEA,
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
           case
        when P.PRODUCTOTPO IN ('B','Z','W') then 'TV'
        when P.PRODUCTOTPO IN ('C','I','N','L','E') then 'INTERNET'
        ELSE NULL
        END AS TIPOPRODUCTO,
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
         ,cp.contratoprmusr
FROM sigasc.factura f
INNER JOIN sigasc.facturalinea d
  ON F.facturanro = D.facturanro 
  AND F.empresaid = D.empresaid
  AND f.FACTURATPO = d.FACTURATPO 
LEFT JOIN sigasc.contrato c
  ON D.empresaid = C.empresaid
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
  AND D.facturacmb = CMB.comboid
LEFT JOIN (
    SELECT
        cp.empresaid,
        cp.contratonro,
        cp.promocionid,
        MAX(cp.contratoprmfch) AS max_contratoprmfch
    FROM
        sigasc.contratopromocion cp
    WHERE
        cp.empresaid = 10
    GROUP BY
        cp.empresaid,
        cp.contratonro,
        cp.promocionid
) AS cp_max ON f.empresaid = cp_max.empresaid AND d.facturalincod = cp_max.contratonro AND d.facturaprm = cp_max.promocionid
LEFT JOIN sigasc.contratopromocion cp ON cp.empresaid = cp_max.empresaid AND cp.contratonro = cp_max.contratonro AND cp.promocionid = cp_max.promocionid AND cp.contratoprmfch = cp_max.max_contratoprmfch
WHERE
    f.facturaperiodo = 202308
    AND f.facturatpo = 'F'
    AND f.empresaid = 10
    AND p.productoppl = 'P';
```
