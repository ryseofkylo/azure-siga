---
esquema: dbo
tabla: V_COBRANZAOFICINA
objeto: dbo.V_COBRANZAOFICINA
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

# dbo.V_COBRANZAOFICINA

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[BIGDATA.AGRUPACIONMEDCOBROBD]]
- [[SIGASC.RECIBOLINEA]]
- [[dbo.V_COBRANZAS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `RECIBONRO` | varchar | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `RECIBOFCH` | datetime2 | 0% |
| 5 | `RECIBOSTS` | varchar | 0% |
| 6 | `MEDCOBRBO` | int | 0% |
| 7 | `RECIBOIMP` | real | 0% |
| 8 | `RECIBOUSR` | varchar | 0% |
| 9 | `RECIBOGEN` | varchar | 0% |
| 10 | `MONTOCOBRANZA` | float | 0% |
| 11 | `CPGOTIPOID` | int | 0% |
| 12 | `RECIBOLINEA` | float | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_COBRANZAOFICINA
-- Extraida: 2026-08-07T15:27:45.482974+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_COBRANZAOFICINA]
AS SELECT v.EMPRESAID,
	   v.RECIBONRO, 
	   v.CLIENTENRO,
	   v.RECIBOFCH,
	   v.RECIBOSTS,
	   v.MEDCOBRBO,
	   v.RECIBOIMP,
	   v.RECIBOUSR,
	   v.RECIBOGEN,
	   v.MONTOCOBRANZA,
	   ISNULL( e.CPGOTIPOID, 0 ) AS CPGOTIPOID,
	   ISNULL( ROUND( SUM( e.rbocpgoimporte ), 2), v.MONTOCOBRANZA ) AS RECIBOLINEA
FROM ( SELECT EMPRESAID, RECIBONRO, CLIENTENRO, RECIBOFCH, RECIBOSTS, MEDCOBRBO, RECIBOIMP, RECIBOUSR, RECIBOGEN, 
			  SUM(MONTOCOBRANZA) AS MONTOCOBRANZA 
	   FROM V_COBRANZAS 
	   GROUP BY EMPRESAID, RECIBONRO, CLIENTENRO, RECIBOFCH, RECIBOSTS, MEDCOBRBO, RECIBOIMP, RECIBOUSR, RECIBOGEN
	 ) v
LEFT JOIN SIGASC.RECIBOLINEA e ON ( v.recibonro = e.pkrecibonro )
WHERE v.MEDCOBRBO IN ( SELECT DISTINCT MEDIOCOBROIDBD FROM BIGDATA.AGRUPACIONMEDCOBROBD WHERE MEDIOCOBROGRUPOBD = 'OFICINA' ) 
AND v.EMPRESAID <> '27' --TCC
GROUP BY v.EMPRESAID, v.RECIBONRO, v.CLIENTENRO, v.RECIBOFCH, v.RECIBOSTS, v.MEDCOBRBO, v.RECIBOIMP, v.RECIBOUSR, v.RECIBOGEN, v.MONTOCOBRANZA,
		 e.CPGOTIPOID;
```
