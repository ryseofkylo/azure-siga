---
esquema: dbo
tabla: PushMTI
objeto: dbo.PushMTI
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 4
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.PushMTI

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.CLIENTETPO]]
- [[SIGASC.VM_CLIENTE]]
- [[dbo.TablaExclusion]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `SUCURSALID` | int | 0% |
| 3 | `CLIENTETPONOM` | varchar | 0% |
| 4 | `CLIENTES_SIN_AI` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.PushMTI
-- Extraida: 2026-08-07T15:27:34.707162+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[PushMTI]
AS SELECT c.EMPRESAID,c.SUCURSALID,ct.CLIENTETPONOM,count(c.clientenro) as CLIENTES_SIN_AI
	FROM sigasc.vm_cliente c
	left join sigasc.clientetpo ct
	on c.clientetpo = ct.clientetpo
	where c.clientests = 'C'
	and empresaid not in(15,19,20,23,27,28)
	and c.clientenro not in(
		select t.clientenro
		from tablaexclusion t
	)
	and c.clientetpo not in(
            991,                                       
            992,                           
            993,              
            995,                          
            996,                           
            984,                   
            986,                   
            988,                                  
            1005, 
			1006,                                             
            1007,                            
            1008,                                        
            1009
        )
	and empresaid <=28
	group by c.EMPRESAID,c.SUCURSALID,ct.CLIENTETPONOM;
```
