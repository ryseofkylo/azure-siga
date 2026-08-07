---
esquema: dbo
tabla: V_RETENCIONES
objeto: dbo.V_RETENCIONES
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 12
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_RETENCIONES

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.CONTRATOPROMOCION]]
- [[dbo.V_PROMOCION]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CONTRATONRO` | varchar | 0% |
| 3 | `CLIENTENRO` | varchar | 0% |
| 4 | `PROMOCIONID` | varchar | 0% |
| 5 | `PRODUCTOID` | varchar | 0% |
| 6 | `CONTRATOPRMFCH` | date | 0% |
| 7 | `CONTRATOPRMFFIN` | date | 12% |
| 8 | `CONTRATOPRMFCHCXL` | date | 93% |
| 9 | `CONTRATOPRMUSR` | varchar | 0% |
| 10 | `CONTRATOPRMSTS` | varchar | 0% |
| 11 | `CONTRATOPRMMES` | int | 0% |
| 12 | `promocionclase` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_RETENCIONES
-- Extraida: 2026-08-07T15:28:17.624556+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_RETENCIONES]
AS SELECT cp.EMPRESAID,
		( cp.PKCONTRATONRO ) AS CONTRATONRO,
		( c.PKCLIENTENRO )   AS CLIENTENRO,
		CONCAT(CONCAT(cp.empresaid,'_'),cp.promocionid) AS PROMOCIONID,
		( c.PKPRODUCTOID )   AS PRODUCTOID,
		CONVERT(DATE,cp.CONTRATOPRMFCH) AS CONTRATOPRMFCH,
		CONVERT(DATE,cp.CONTRATOPRMFFIN) AS CONTRATOPRMFFIN,
		CONVERT(DATE,CONTRATOPRMFCHCXL) AS CONTRATOPRMFCHCXL,
		cp.CONTRATOPRMUSR,		   
		cp.CONTRATOPRMSTS,
		cp.CONTRATOPRMMES,
		p.promocionclase
FROM ( SELECT * FROM SIGASC.CONTRATOPROMOCION WHERE LEN(contratoprmfch) > 10 ) cp
INNER JOIN SIGASC.CONTRATO c ON ( cp.pkcontratonro = c.pkcontratonro )
INNER JOIN V_PROMOCION p     ON ( CONCAT(CONCAT(cp.empresaid,'_'),cp.promocionid ) = p.promocionid )
WHERE c.empresaid NOT IN ('101','102')
--AND cp.contratoprmusr <> 'SIGA'
--AND p.promocionclase IN ('R','P -- CLASE PROMOCION = "RETENCION"
AND p.empresaid <> 0
AND ( cp.contratoprmsts <> 'C'
		OR ( cp.contratoprmsts = 'C' AND contratoprmfchcxl IS NULL )
	    OR ( cp.contratoprmsts = 'C' AND CONVERT(DATE,CONTRATOPRMFCH) <> CONVERT(DATE,CONTRATOPRMFCHCXL ) )
		OR ( cp.contratoprmsts = 'C' AND contratoprmmes <> 0 )
	)
AND CONVERT(DATE,CONTRATOPRMFCH) >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101);
```
