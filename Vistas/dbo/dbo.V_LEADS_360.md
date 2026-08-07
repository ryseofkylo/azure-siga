---
esquema: dbo
tabla: V_LEADS_360
objeto: dbo.V_LEADS_360
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

# dbo.V_LEADS_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.SG_Caso]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Source` | nvarchar | 0% |
| 3 | `Creation_date` | datetime2 | 0% |
| 4 | `Close_date` | datetime2 | 0% |
| 5 | `Client_id` | bigint | 0% |
| 6 | `Client_crm_id` | nvarchar | 12% |
| 7 | `Client_name` | nvarchar | 0% |
| 8 | `Client_ext_id` | nvarchar | 0% |
| 9 | `File` | nvarchar | 0% |
| 10 | `FechaProcesado` | datetime2 | 0% |
| 11 | `NroCliente` | nvarchar | 12% |
| 12 | `Campaign` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_LEADS_360
-- Extraida: 2026-08-07T15:27:59.797624+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_LEADS_360]
AS SELECT *
FROM dbo.SG_CASO
WHERE CAMPAIGN IN ('Redes Sociales','Redes Sociales 2','RRSS Leads','RRSS Leads 2','Unbounce','Whatsapp','WP Leads')
AND CLOSE_DATE >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101);
```
