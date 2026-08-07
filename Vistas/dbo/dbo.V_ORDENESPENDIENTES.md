---
esquema: dbo
tabla: V_ORDENESPENDIENTES
objeto: dbo.V_ORDENESPENDIENTES
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 17
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_ORDENESPENDIENTES

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CONTRATO]]
- [[SIGASC.ORDENSRV]]
- [[SIGASC.PRODUCTO]]
- [[SIGASC.TECNICO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENROORD` | int | 0% |
| 3 | `TECNICO` | int | 0% |
| 4 | `TECNICOEMPLEADONRO` | int | 0% |
| 5 | `TECNICO1_TIPO` | varchar | 0% |
| 6 | `ID_TECNICO2` | int | 2% |
| 7 | `TECNICO2_EMPLEADONRO` | int | 2% |
| 8 | `TECNICO2_TIPO` | varchar | 2% |
| 9 | `FECHA` | datetime2 | 0% |
| 10 | `CENTROOPERATIVOID` | int | 0% |
| 11 | `ORDENNRO` | int | 0% |
| 12 | `ORDENTPO` | varchar | 0% |
| 13 | `ORDENSTS` | varchar | 0% |
| 14 | `PRODUCTOTPO` | varchar | 0% |
| 15 | `PRODUCTOPPL` | varchar | 0% |
| 16 | `ORDENTRBRED` | int | 0% |
| 17 | `ORDENGEN` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_ORDENESPENDIENTES
-- Extraida: 2026-08-07T15:28:08.170533+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_ORDENESPENDIENTES]
AS SELECT CASE o.empresaid WHEN 21 THEN 4 ELSE o.empresaid END EMPRESAID, -- Si es TVCA --> UDN Catamarca
		   -- EMPRESANOM ( Dimension )
		   o.CLIENTENROORD,
		   o.tecnicoidcierre	 AS TECNICO,
		   t.TECNICOEMPLEADONRO,
		   t.tecnicotpo			 AS TECNICO1_TIPO,
		   o.tecnicoidcierreaux  AS ID_TECNICO2,
		   t2.tecnicoempleadonro AS TECNICO2_EMPLEADONRO,
		   t2.tecnicotpo		 AS TECNICO2_TIPO,
		   o.ordenfproceso		 AS FECHA,
		   o.CENTROOPERATIVOID,
		   o.ORDENNRO,
           o.ORDENTPO,
           o.ORDENSTS,
           p.PRODUCTOTPO,
           p.PRODUCTOPPL,
           o.ORDENTRBRED,
           o.ORDENGEN
	FROM SIGASC.ORDENSRV o
	--INNER JOIN SIGASC.EMPRESAMULTI em	   ON ( o.empresaid = em.empresaid )
	--LEFT JOIN SIGASC.CENTROOPERATIVO cop ON ( em.empresaid = cop.empresaid ) AND ( O.CENTROOPERATIVOID = COP.CENTROOPERATIVOID )
	INNER JOIN SIGASC.TECNICO T		   
	ON ( o.EMPRESAID = t.EMPRESAID ) AND ( o.TECNICOIDCIERRE = t.TECNICOID )
	--INNER JOIN SIGAMSASC.EMPRESA EMP     ON ( o.EMPRESAID = EMP.EMPRESAID )
	--INNER JOIN SIGASC.VM_CLIENTE2 cli ON O.EMPRESAID = CLI.empresaid AND O.CLIENTENROORD = CLI.CLIENTENRO
	INNER JOIN SIGASC.CONTRATO co	  
	ON ( ( o.EMPRESAID = co.EMPRESAID ) AND ( o.CONTRATONRO = CO.CONTRATONRO ) AND ( o.CLIENTENROORD = co.CLIENTENRO ) )
	INNER JOIN SIGASC.PRODUCTO p	  
	ON ( ( co.EMPRESAID = p.EMPRESAID ) AND ( co.PRODUCTOID = p.PRODUCTOID ) )
	--INNER JOIN SIGASC.PRODUCTOTPO PTO ON PTO.PRODUCTOTPO = P.PRODUCTOTPO
    LEFT  JOIN SIGASC.TECNICO t2	  
	ON ( ( o.EMPRESAID = t2.EMPRESAID ) AND ( o.TECNICOIDCIERREAUX = t2.TECNICOID ) )
	WHERE o.tecnicoidcierre > 0 
	AND o.ordensts IN ('E','A','P','R','S','F');
```
