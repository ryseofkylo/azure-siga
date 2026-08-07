---
esquema: dbo
tabla: V_CLIENTEDATOS
objeto: dbo.V_CLIENTEDATOS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 8
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_CLIENTEDATOS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_VM_CLIENTE]]
- [[dbo.V_PRODUCTODATOS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PKCLIENTENRO` | nvarchar | 0% |
| 3 | `BDMODIFIEDDATE` | date | 0% |
| 4 | `NEGOCIOSEGMENTO` | int | 0% |
| 5 | `NEGOCIOSEGMENTOTIPOID` | int | 6% |
| 6 | `CLIENTESTS` | nvarchar | 0% |
| 7 | `CLIENTETPO` | int | 0% |
| 8 | `CLIENTENATURALEZAID` | int | 100% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_CLIENTEDATOS
-- Extraida: 2026-08-07T15:27:43.497535+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_CLIENTEDATOS]
AS SELECT DISTINCT d.*, s.CLIENTENATURALEZAID
FROM V_PRODUCTODATOS d
LEFT JOIN
	( SELECT c.PKCLIENTENRO, a.BDMODIFIEDDATE AS FECHADATOS, c.CLIENTENATURALEZAID
	  FROM SIGASC.H_VM_CLIENTE c
	  INNER JOIN ( SELECT p.PKCLIENTENRO, p.BDMODIFIEDDATE, h.BDMODIFIEDDATE AS FECHACLIENTE
				   FROM SIGASC.H_VM_CLIENTE h
				   INNER JOIN V_PRODUCTODATOS p ON ( h.pkclientenro = p.pkclientenro ) 
				   WHERE h.bdmodifieddate <= p.bdmodifieddate 
				   and h.pkclientenro = '23_5737066'
				 ) a
	  ON ( ( c.pkclientenro = a.pkclientenro ) AND ( c.bdmodifieddate = a.fechacliente ) )
	) s
ON ( ( d.pkclientenro = s.pkclientenro ) AND ( d.bdmodifieddate = s.fechadatos ) );
```
