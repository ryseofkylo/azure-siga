---
esquema: SIGASC
tabla: V_CONTRATOS_BASE
objeto: SIGASC.V_CONTRATOS_BASE
tipo_objeto: VIEW
dominio: Core SIGA
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/vista
  - referencia
---

# SIGASC.V_CONTRATOS_BASE

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_CONTRATO_CLIENTE]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int |  |
| 2 | `PKCONTRATONRO` | nvarchar |  |
| 3 | `PKCLIENTENRO` | nvarchar |  |
| 4 | `PKPOLITICAID` | nvarchar |  |
| 5 | `PKPRODUCTOID` | nvarchar |  |
| 6 | `CONTRATOSTS` | nvarchar |  |
| 7 | `NEGOCIOSEGMENTO` | int |  |
| 8 | `NEGOCIOSEGMENTOTIPOID` | int |  |
| 9 | `CLIENTESTS` | nvarchar |  |
| 10 | `CLIENTETPO` | int |  |
| 11 | `CONTRATOCNT` | int |  |
| 12 | `BDMODIFIEDDATE` | datetime2 |  |

## Definición (CREATE VIEW)
```sql
-- Vista: SIGASC.V_CONTRATOS_BASE
-- Extraida: 2026-08-07T15:28:37.160839+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [SIGASC].[V_CONTRATOS_BASE]
AS SELECT
    h.EMPRESAID, h.PKCONTRATONRO, h.PKCLIENTENRO, h.PKPOLITICAID, h.PKPRODUCTOID,
    h.CONTRATOSTS, h.NEGOCIOSEGMENTO, h.NEGOCIOSEGMENTOTIPOID, h.CLIENTESTS,
    h.CLIENTETPO, h.CONTRATOCNT, h.BDMODIFIEDDATE,
    CONVERT(varchar(10), h.BDMODIFIEDDATE, 103) AS [Reg Start Date],
    CASE
        WHEN h.NEGOCIOSEGMENTO = 1 AND h.NEGOCIOSEGMENTOTIPOID = 3 THEN CONCAT(h.EMPRESAID, '_1')
        WHEN h.EMPRESAID = 23 AND h.NEGOCIOSEGMENTO = 3 AND h.NEGOCIOSEGMENTOTIPOID = 1 THEN CONCAT(h.EMPRESAID, '_', h.NEGOCIOSEGMENTO)
        ELSE CONCAT(h.EMPRESAID, '_', CONCAT(CAST(h.NEGOCIOSEGMENTO AS varchar(10)), COALESCE(CAST(h.NEGOCIOSEGMENTOTIPOID AS varchar(10)), '')))
    END AS [Cliente Negocio Segmento ID],
    SUBSTRING(h.PKCLIENTENRO,  CHARINDEX('_', h.PKCLIENTENRO)  + 1, LEN(h.PKCLIENTENRO))  AS [Cliente Numero],
    SUBSTRING(h.PKCONTRATONRO, CHARINDEX('_', h.PKCONTRATONRO) + 1, LEN(h.PKCONTRATONRO)) AS [Contrato Numero]
FROM SIGASC.H_CONTRATO_CLIENTE h
WHERE NOT (h.CLIENTESTS = 'X' AND h.BDMODIFIEDDATE = CONVERT(date,'19000101'));
```
