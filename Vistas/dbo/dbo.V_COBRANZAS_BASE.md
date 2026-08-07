---
esquema: dbo
tabla: V_COBRANZAS_BASE
objeto: dbo.V_COBRANZAS_BASE
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 24
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_COBRANZAS_BASE

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.EMPRESA]]
- [[SIGASC.CONTRATO]]
- [[SIGASC.CPTOFACTURA]]
- [[SIGASC.FACTURA]]
- [[SIGASC.FACTURALINEA]]
- [[SIGASC.PRODUCTO]]
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
| 14 | `RECIBOFACIMPRBO` | float |  |
| 15 | `FACTURAFCH` | datetime2 |  |
| 16 | `FACTURAPERIODO` | int |  |
| 17 | `FACTURALIN` | nvarchar |  |
| 18 | `CPTOFACID` | int |  |
| 19 | `CPTOFACGRUPOID` | int |  |
| 20 | `PRODUCTOID` | nvarchar |  |
| 21 | `PRODUCTOTPO` | nvarchar |  |
| 22 | `MONTOLINEA` | real |  |
| 23 | `CONTRIBUCION` | real |  |
| 24 | `COBRANZALINEA` | float |  |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_COBRANZAS_BASE
-- Extraida: 2026-08-07T15:27:47.469134+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_COBRANZAS_BASE]
AS SELECT r.EMPRESAID,
r.RECIBONRO,r.CLIENTENRO,r.RECIBOFCH,r.RECIBOSTS,r.MEDCOBRBO,
r.RECIBOIMP,r.RECIBOUSR,r.RECIBOGEN,r.RECIBOFCHCOB,r.RECIBOTPO,
b.FACTURATPO,b.FACTURANRO,b.RECIBOFACIMPRBO,
f.FACTURAFCH,f.FACTURAPERIODO,l.FACTURALIN,l.CPTOFACID,
c.CPTOFACGRUPOID, p.PRODUCTOID, p.PRODUCTOTPO,
CASE e.empresadevengavto 
WHEN 1 THEN l.facturalinimp
WHEN 2 THEN l.facturalinimpv2
WHEN 3 THEN l.facturalinimpv3
END MONTOLINEA,
CASE e.empresadevengavto
WHEN 1 THEN Isnull( l.facturalinimp / Nullif(f.facturatotal , 0) , 0)
WHEN 2 THEN Isnull( l.facturalinimpv2 / Nullif(f.facturatotalv2 , 0), 0)
WHEN 3 THEN Isnull( l.facturalinimpv3 / Nullif(f.facturatotalv3 , 0), 0)
END AS CONTRIBUCION,
CASE e.empresadevengavto
WHEN 1 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimp / Nullif(f.facturatotal , 0) , 0) )
WHEN 2 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimpv2 / Nullif(f.facturatotalv2 , 0), 0) )
WHEN 3 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimpv3 / Nullif(f.facturatotalv3 , 0), 0) )
END AS COBRANZALINEA
FROM sigasc.RECIBO r
LEFT JOIN sigasc.RECIBOFAC b ON ( r.recibonro = b.recibonro )
LEFT JOIN sigasc.FACTURA f ON ( b.facturanro = f.facturanro ) 
LEFT JOIN sigasc.FACTURALINEA l ON ( f.facturanro = l.facturanro ) 
--LEFT JOIN sigasc.FACTURACION f ON ( f.facturanro = b.facturanro )
LEFT JOIN sigamsasc.EMPRESA e ON ( r.empresaid = e.empresaid )
LEFT JOIN sigasc.CPTOFACTURA c ON ( c.cptofacid = CONCAT(l.empresaid,CONCAT('_',l.cptofacid)) )
LEFT JOIN sigasc.CONTRATO t ON ( t.contratonro = CONCAT(l.facturalincod,CONCAT('_',l.facturalincod)) )
LEFT JOIN sigasc.PRODUCTO p ON ( t.productoid = p.productoid )
WHERE r.recibosts <> 'X'
--AND r.recibonro = '10_3990419'
AND r.recibotpo = 'R'
AND r.RECIBOFCH >= DATEADD(MM, -6, GETDATE());
```
