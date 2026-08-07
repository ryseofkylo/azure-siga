---
esquema: dbo
tabla: V_FACTURACION_BDDD
objeto: dbo.V_FACTURACION_BDDD
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 9
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_FACTURACION_BDDD

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.FACTURA]]
- [[dbo.V_MEDIOCOBRO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `empresaid` | int | 0% |
| 2 | `clientenro` | int | 0% |
| 3 | `facturasts` | varchar | 0% |
| 4 | `facturafch` | datetime2 | 0% |
| 5 | `FACTURAPERIODO` | int | 0% |
| 6 | `FACTURAVTO` | datetime2 | 0% |
| 7 | `facturafcob` | datetime2 | 5% |
| 8 | `MEDCOBFAC` | int | 0% |
| 9 | `MEDIOCOBROCANALBD` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_FACTURACION_BDDD
-- Extraida: 2026-08-07T15:27:54.401753+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_FACTURACION_BDDD]
AS SELECT f.empresaid, f.clientenro, f.facturasts, f.facturafch, f.FACTURAPERIODO, f.FACTURAVTO, f.facturafcob,  f.MEDCOBFAC, m.[MEDIOCOBROCANALBD]
  --facturatotal
 
 FROM [SIGASC].[FACTURA] F
 left join  [dbo].[V_MEDIOCOBRO] M
 on f.MEDCOBFAC = m.MEDCOBROID

 where  f.FACTURAPERIODO BETWEEN
      (YEAR(DATEADD(MONTH, -12, DATEADD(MONTH, 1, GETDATE()))) * 100
     + MONTH(DATEADD(MONTH, -12, DATEADD(MONTH, 1, GETDATE()))))
  AND (YEAR(DATEADD(MONTH, 1, GETDATE())) * 100
     + MONTH(DATEADD(MONTH, 1, GETDATE())))
 --([FACTURAPERIODO]>=202502 and [FACTURAPERIODO]<202602) 
and facturatpo='F' 
AND EMPRESAID NOT IN (15,19,23);
```
