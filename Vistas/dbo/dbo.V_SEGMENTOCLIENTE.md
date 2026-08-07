---
esquema: dbo
tabla: V_SEGMENTOCLIENTE
objeto: dbo.V_SEGMENTOCLIENTE
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 5
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_SEGMENTOCLIENTE

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.EMPRESA]]
- [[SIGASC.NEGOCIOSEGMENTO]]
- [[SIGASC.NEGOCIOSEGMENTOTIPO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `NEGOCIOSEGMENTO` | int | 0% |
| 3 | `NEGOCIOSEGMENTONOMBRE` | nvarchar | 0% |
| 4 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 5 | `NEGOCIOSEGMENTOTIPONOM` | nvarchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_SEGMENTOCLIENTE
-- Extraida: 2026-08-07T15:28:18.639914+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_SEGMENTOCLIENTE]
AS SELECT e.EMPRESAID, n.NEGOCIOSEGMENTO, n.NEGOCIOSEGMENTONOMBRE, t.NEGOCIOSEGMENTOTIPOID, t.NEGOCIOSEGMENTOTIPONOM 
FROM SIGASC.NEGOCIOSEGMENTO n
INNER JOIN SIGASC.NEGOCIOSEGMENTOTIPO t ON ( n.negociosegmento = t.negociosegmento )
FULL JOIN SIGAMSASC.EMPRESA e ON ( e.empresaid = e.empresaid )
WHERE e.empresaid <> '23'
UNION ALL
SELECT e.EMPRESAID, n.NEGOCIOSEGMENTO, n.NEGOCIOSEGMENTONOMBRE, NEGOCIOSEGMENTOTIPOID, NEGOCIOSEGMENTOTIPONOM
FROM SIGASC.NEGOCIOSEGMENTO n
INNER JOIN SIGASC.NEGOCIOSEGMENTOTIPO t ON ( n.negociosegmento = t.negociosegmento )
FULL JOIN SIGAMSASC.EMPRESA e ON ( e.empresaid = e.empresaid )
WHERE e.empresaid = '23'
AND NOT ( ( n.NEGOCIOSEGMENTO = 3 ) AND ( t.NEGOCIOSEGMENTOTIPOID = 1 ) )
UNION ALL
SELECT e.EMPRESAID, s.NEGOCIOSEGMENTO, s.NEGOCIOSEGMENTONOMBRE, NULL, NULL
FROM SIGASC.NEGOCIOSEGMENTO s 
FULL JOIN SIGAMSASC.EMPRESA e ON ( e.empresaid = e.empresaid );
```
