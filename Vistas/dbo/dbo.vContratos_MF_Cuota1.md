---
esquema: dbo
tabla: vContratos_MF_Cuota1
objeto: dbo.vContratos_MF_Cuota1
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 3
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.vContratos_MF_Cuota1

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.FACTURA]]
- [[SIGASC.FACTURALINEA]]
- [[SIGASC.PRODUCTO]]
- [[SIGASC.PROMOCION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `empresaid` | int |  |
| 2 | `clientenro` | int |  |
| 3 | `CONTRATONRO` | int |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.vContratos_MF_Cuota1
-- Extraida: 2026-08-07T15:28:23.916874+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[vContratos_MF_Cuota1]
AS WITH FACT AS(
	SELECT f.empresaid,
          F.clientenro,
		  d.FACTURALINCOD as CONTRATONRO,
		  D.facturaprm AS promocionid,
        case
        when P.PRODUCTOTPO IN ('B','Z','W') then 'TV'
        when P.PRODUCTOTPO IN ('C','I','L','E') then 'INTERNET'
        ELSE NULL
        END AS TIPOPRODUCTO,
		 cast(
			case when 
					d.facturalincuo is null 
					or len(ltrim(rtrim(d.facturalincuo))) =0 
					or PATINDEX('%/%',ltrim(rtrim(d.facturalincuo))) =0
					OR ISNUMERIC(left(ltrim(rtrim(d.facturalincuo)), PATINDEX('%/%',ltrim(rtrim(d.facturalincuo)))-1))=0 
				then null
				else left(ltrim(rtrim(d.facturalincuo)), PATINDEX('%/%',ltrim(rtrim(d.facturalincuo)))-1) 
			end
			as int) as CuotaDesde
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
          LEFT JOIN sigasc.promocion pr
            ON PR.promocionid = D.facturaprm
              AND PR.empresaid = f.empresaid
where facturaperiodo = 202305
and f.facturatpo = 'F'
and f.empresaid = 10
and pr.PROMOCIONTPODTO = 'F'
and p.PRODUCTOPPL = 'P')
SELECT empresaid,
          clientenro,
		  CONTRATONRO
FROM FACT 
WHERE CUOTADESDE = 1
AND  promocionid > 0
GROUP BY empresaid,
          clientenro,CONTRATONRO,TIPOPRODUCTO;
```
