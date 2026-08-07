---
esquema: dbo
tabla: V_COBRANZAS
objeto: dbo.V_COBRANZAS
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 20
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_COBRANZAS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.COBRANZAS]]
- [[dbo.V_COBRANZAS_1_APL]]
- [[dbo.V_COBRANZAS_SOLO_INT]]

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
| 10 | `RECIBOFCHCOB` | datetime2 | 0% |
| 11 | `RECIBOTPO` | varchar | 0% |
| 12 | `FACTURATPO` | varchar | 0% |
| 13 | `FACTURANRO` | varchar | 0% |
| 14 | `RECIBOFACIMPRBO` | real | 0% |
| 15 | `FACTURAFCH` | datetime2 | 0% |
| 16 | `FACTURAPERIODO` | int | 0% |
| 17 | `FACTURANEGOCIO` | varchar | 0% |
| 18 | `MONTOORIGEN` | float | 0% |
| 19 | `CONTRIBUCION` | float | 0% |
| 20 | `MONTOCOBRANZA` | float | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_COBRANZAS
-- Extraida: 2026-08-07T15:27:45.816948+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_COBRANZAS]
AS SELECT f.EMPRESAID, ( f.pkrecibonro ) AS RECIBONRO, f.CLIENTENRO, f.RECIBOFCH, f.RECIBOSTS, 
			f.MEDCOBRBO, f.RECIBOIMP, f.RECIBOUSR, f.RECIBOGEN, f.RECIBOFCHCOB, f.RECIBOTPO, 
			f.FACTURATPO, f.FACTURANRO, f.RECIBOFACIMPRBO, f.FACTURAFCH, f.FACTURAPERIODO, f.FACTURANEGOCIO,
			--  MONTOORIGEN -- Monto resultante entre el Monto Línea de la Factura y las Notas.
			( f.montolinea + ISNULL(n.montolinea,0) ) AS MONTOORIGEN, 
			-- CONTRIBUCION -- % del Monto Origen respecto al total de la Factura.
	 		( f.montolinea + ISNULL(n.montolinea,0) ) / 
			NULLIF( SUM( f.montolinea + ISNULL(n.montolinea,0) ) OVER ( PARTITION BY f.pkrecibonro, f.facturanro ORDER BY f.pkrecibonro ), 0 )  AS CONTRIBUCION, 
			-- MONTOCOBRANZA -- Monto Final de Cobranza respecto cada negocio facturado.
			CASE WHEN ( f.facturanro IS NULL ) THEN ROUND( f.reciboimp, 2 )
			ELSE (
		  		CASE WHEN ( x.pkrecibonro IS NOT NULL )
						THEN ( CASE WHEN ( t.pkrecibonro IS NOT NULL )
									THEN ( CASE WHEN ( f.facturafch IS NOT NULL )
							 					THEN ROUND( ( f.recibofacimprbo ) *
													(	( f.montolinea + ISNULL(n.montolinea,0) ) / 
													NULLIF( SUM( f.montolinea + ISNULL(n.montolinea,0) ) OVER ( PARTITION BY f.pkrecibonro, f.facturanro ORDER BY f.pkrecibonro ), 0 ) )
													+ ( f.reciboimp - f.recibofacimprbo ), 2 )
												ELSE ROUND( f.recibofacimprbo + ( f.reciboimp - f.recibofacimprbo ), 2 )
										END
										)
									ELSE (
											CASE WHEN ( f.facturanegocio = 'TVC' )
												THEN (
					 									CASE WHEN ( f.facturafch IS NOT NULL )
							 								THEN ROUND( ( f.recibofacimprbo ) *
																(	( f.montolinea + ISNULL(n.montolinea,0) ) / 
																NULLIF( SUM( f.montolinea + ISNULL(n.montolinea,0) ) OVER ( PARTITION BY f.pkrecibonro, f.facturanro ORDER BY f.pkrecibonro ), 0 ) )
																+ ( f.reciboimp - f.recibofacimprbo ), 2 )
															ELSE ROUND( f.recibofacimprbo + ( f.reciboimp - f.recibofacimprbo ), 2 )
														END
													)
												ELSE (   CASE WHEN ( f.facturafch IS NOT NULL )
																THEN ROUND( ( f.recibofacimprbo ) *
																	(	( f.montolinea + ISNULL(n.montolinea,0) ) / 
																	NULLIF( SUM( f.montolinea + ISNULL(n.montolinea,0) ) OVER ( PARTITION BY f.pkrecibonro, f.facturanro ORDER BY f.pkrecibonro ), 0 ) ), 2 )
																ELSE ROUND( f.recibofacimprbo, 2 )
														END
													)
											END
										)
								END
							)
						ELSE (   CASE WHEN ( f.facturafch IS NOT NULL )
												THEN ROUND( ( f.recibofacimprbo ) *
													(	( f.montolinea + ISNULL(n.montolinea,0) ) / 
													NULLIF( SUM( f.montolinea + ISNULL(n.montolinea,0) ) OVER ( PARTITION BY f.pkrecibonro, f.facturanro ORDER BY f.pkrecibonro ), 0 ) ), 2 )
												ELSE ROUND( f.recibofacimprbo, 2 )
										END
										)
				END
				)
	END AS MONTOCOBRANZA
	FROM ( SELECT * FROM SIGASC.COBRANZAS WHERE facturatpo LIKE '%F%' OR facturatpo IS NULL ) f
	LEFT JOIN ( SELECT EMPRESAID, FACTURANRONC, FACTURANEGOCIO, SUM( montolinea ) AS MONTOLINEA 
				FROM SIGASC.COBRANZAS
				WHERE ( facturatpo LIKE '%N%' OR facturatpo LIKE '%D%' )
				GROUP BY empresaid, facturanronc, facturanegocio
			) n
	ON ( ( f.facturanro = CONCAT( n.empresaid, CONCAT( '_', n.facturanronc ) ) ) AND ( f.facturanegocio = n.facturanegocio ) )
	LEFT JOIN V_COBRANZAS_1_APL x   ON ( x.pkrecibonro = f.pkrecibonro )
	LEFT JOIN V_COBRANZAS_SOLO_INT t ON ( t.pkrecibonro = f.pkrecibonro );
```
