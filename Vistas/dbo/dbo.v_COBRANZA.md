---
esquema: dbo
tabla: v_COBRANZA
objeto: dbo.v_COBRANZA
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 21
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_COBRANZA

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.EMPRESA]]
- [[SIGASC.FACTURACION]]
- [[SIGASC.RECIBO]]
- [[SIGASC.RECIBOFAC]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int |  |
| 2 | `RECIBONRO` | varchar |  |
| 3 | `CLIENTENRO` | int |  |
| 4 | `RECIBOFCH` | datetime2 |  |
| 5 | `RECIBOSTS` | varchar |  |
| 6 | `MEDCOBRBO` | int |  |
| 7 | `RECIBOIMP` | float |  |
| 8 | `RECIBOUSR` | varchar |  |
| 9 | `RECIBOGEN` | varchar |  |
| 10 | `RECIBOFCHCOB` | datetime2 |  |
| 11 | `RECIBOTPO` | varchar |  |
| 12 | `FACTURATPO` | varchar |  |
| 13 | `FACTURANRO` | varchar |  |
| 14 | `RECIBOFACIMP` | float |  |
| 15 | `FACTURAFCH` | datetime2 |  |
| 16 | `FACTURAPERIODO` | int |  |
| 17 | `FACTURALIN` | nvarchar |  |
| 18 | `CPTOFACID` | int |  |
| 19 | `MONTOLINEA` | real |  |
| 20 | `CONTRIBUCION` | real |  |
| 21 | `COBRANZALINEA` | float |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_COBRANZA
-- Extraida: 2026-08-07T15:27:45.152398+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [v_COBRANZA]
AS SELECT r.EMPRESAID, r.RECIBONRO, r.CLIENTENRO, r.RECIBOFCH, r.RECIBOSTS,
	   r.MEDCOBRBO, r.RECIBOIMP, r.RECIBOUSR, r.RECIBOGEN, r.RECIBOFCHCOB, r.RECIBOTPO, 
	   b.FACTURATPO, b.FACTURANRO, b.RECIBOFACIMP,
	   f.FACTURAFCH, f.FACTURAPERIODO, f.FACTURALIN, f.CPTOFACID, 
	   CASE e.empresadevengavto
	   WHEN 1 THEN f.facturalinimp
	   WHEN 2 THEN f.facturalinimpv2 
	   WHEN 3 THEN f.facturalinimpv3  
       END AS MONTOLINEA,
	   CASE e.empresadevengavto
	   WHEN 1 THEN ( f.facturalinimp / f.facturatotal )
	   WHEN 2 THEN ( f.facturalinimpv2 / f.facturatotalv2 )
	   WHEN 3 THEN ( f.facturalinimpv3 / f.facturatotalv3 ) 
       END AS CONTRIBUCION,
	   CASE e.empresadevengavto
	   WHEN 1 THEN ( b.recibofacimp * ( f.facturalinimp / f.facturatotal ) )
	   WHEN 2 THEN ( b.recibofacimp * ( f.facturalinimpv2 / f.facturatotalv2 ) )
	   WHEN 3 THEN ( b.recibofacimp * ( f.facturalinimpv3 / f.facturatotalv3 ) )
       END AS COBRANZALINEA
FROM sigasc.RECIBO r
LEFT JOIN sigasc.RECIBOFAC b ON ( r.recibonro = b.recibonro )
LEFT JOIN sigasc.FACTURACION f ON ( f.facturanro = b.facturanro )
LEFT JOIN sigamsasc.EMPRESA e ON ( r.empresaid = e.empresaid )
WHERE r.recibosts <> 'X'
AND r.recibotpo = 'R'
--AND r.recibonro = '4_4019808'
AND convert(date, r.recibofch) >= '2022/12/01' and convert(date,r.recibofch) < '2023/01/01';
```
