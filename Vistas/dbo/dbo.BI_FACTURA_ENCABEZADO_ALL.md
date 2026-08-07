---
esquema: dbo
tabla: BI_FACTURA_ENCABEZADO_ALL
objeto: dbo.BI_FACTURA_ENCABEZADO_ALL
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

# dbo.BI_FACTURA_ENCABEZADO_ALL

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.EMPRESA]]
- [[SIGASC.CLIENTENATURALEZA]]
- [[SIGASC.FACTURA]]
- [[SIGASC.MEDIOCOBRO]]
- [[SIGASC.REPARTO]]
- [[SIGASC.VM_CLIENTE]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `facturanro` | int | 0% |
| 2 | `periodo` | int | 0% |
| 3 | `facturagen` | varchar | 0% |
| 4 | `facturatpo` | varchar | 0% |
| 5 | `importe` | real | 0% |
| 6 | `importedev` | real | 0% |
| 7 | `empresaid` | int | 0% |
| 8 | `clientenro` | int | 0% |
| 9 | `empresa` | varchar | 0% |
| 10 | `clienteape` | varchar | 0% |
| 11 | `clientenom` | varchar | 0% |
| 12 | `CLIENTESTSNOMBRE` | varchar | 0% |
| 13 | `clientecitpo` | varchar | 0% |
| 14 | `clienteci` | varchar | 0% |
| 15 | `clientests` | varchar | 0% |
| 16 | `negociosegmento` | int | 0% |
| 17 | `clientetpo` | int | 0% |
| 18 | `clientenaturalezanom` | varchar | 96% |
| 19 | `MEDIO_COBRO` | varchar | 0% |
| 20 | `REPARTO` | varchar | 0% |
| 21 | `DEBITO_AUTOMATICO` | varchar | 0% |
| 22 | `EMAIL_SIGA` | varchar | 0% |
| 23 | `FechaFactura` | datetime2 | 0% |
| 24 | `FechaHoraFactura` | datetime2 | 0% |
| 25 | `FechaVto` | datetime2 | 0% |
| 26 | `FACTURANRONC` | int | 0% |
| 27 | `FACTURAUSR` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.BI_FACTURA_ENCABEZADO_ALL
-- Extraida: 2026-08-07T15:27:31.307938+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[BI_FACTURA_ENCABEZADO_ALL]
AS SELECT F.facturanro,
			CASE
	   	  	WHEN f.facturaperiodo = 0 THEN
			YEAR(FACTURAFCH )*100 + MONTH(FACTURAFCH)
		  	ELSE f.facturaperiodo
		  END AS periodo,
		  f.facturagen,
		  TRIM(F.facturatpo) AS facturatpo,
		  F.facturatotal AS importe,
		  F.facturatotaldev AS importedev,
		  cl.empresaid,
		  cl.clientenro,
		  TRIM(e.EMPRESANOM) AS empresa,
		  TRIM(cl.clienteape) AS clienteape,
		  TRIM(cl.clientenom) AS clientenom,
		  case cl.clientests 
		  	when 'I' then 'INGRESADO'
            when 'P' then 'PENDIENTE'
            when 'E' then 'EMITIDO'
            when 'C' then 'CONECTADO'
            when 'X' then 'DESCONECTADO'
            when 'A' then 'ANULADO'
            when 'B' then 'BAJA PENDIENTE'
            when 'M' then 'SUSPENSION POR MORA'
            when 'J' then 'BAJA INCUMPLIDA'
            else cl.clientests 
            end AS "CLIENTESTSNOMBRE",
		  TRIM(cl.clientecitpo) AS clientecitpo,
		  cl.clienteci,
		  TRIM(cl.clientests) AS clientests,
		  cl.negociosegmento AS negociosegmento,
		  cl.clientetpo AS clientetpo,
          TRIM(CN.CLIENTENATURALEZANOM) AS clientenaturalezanom,
		  mcob.medcobronombre MEDIO_COBRO,
		  rep.repartonombre REPARTO,
		  case mcob.medcobrotpo 
            when 'B' then 'ADHERIDO'
            when 'T' then 'ADHERIDO'
            when 'N' then 'ADHERIDO'
            else 'NO ADHERIDO'
          End as "DEBITO_AUTOMATICO",
		  cl.clienteemailppl EMAIL_SIGA,
		  F.FACTURAFCH AS FechaFactura,
		  F.FACTURAFCHHORA FechaHoraFactura,
		  F.FACTURAVTO FechaVto,
		 -- ROW_NUMBER () OVER (PARTITION BY f.clientenro ORDER BY f.facturaperiodo DESC) AS PERIODOORDEN,
   	  f.FACTURANRONC,
   	  f.FACTURAUSR 
	 FROM sigasc.factura f
	 INNER JOIN SIGAMSASC.EMPRESA e 
	 		ON e.EMPRESAID  = f.EMPRESAID 
	 INNER JOIN SIGASC.VM_CLIENTE cl 
			 ON f.empresaid = cl.empresaid 
			 AND f.clientenro = cl.clientenro
	 LEFT JOIN sigasc.CLIENTENATURALEZA CN 
			ON cl.CLIENTENATURALEZAID = CN.CLIENTENATURALEZAID 
    LEFT JOIN sigasc.mediocobro mcob
          ON mcob.medcobroid = cl.medcobroid
    LEFT JOIN sigasc.reparto rep
          ON rep.repartoid = cl.repartocliid
             AND rep.empresaid = cl.empresaid;
```
