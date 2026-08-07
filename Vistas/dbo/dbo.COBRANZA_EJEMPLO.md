---
esquema: dbo
tabla: COBRANZA_EJEMPLO
objeto: dbo.COBRANZA_EJEMPLO
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

# dbo.COBRANZA_EJEMPLO

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
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
-- Vista: dbo.COBRANZA_EJEMPLO
-- Extraida: 2026-08-07T15:27:31.640387+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [COBRANZA_EJEMPLO]
AS select * from V_COBRANZAS where recibonro = '1_23853141';
```
