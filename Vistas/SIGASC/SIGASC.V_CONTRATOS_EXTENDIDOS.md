---
esquema: SIGASC
tabla: V_CONTRATOS_EXTENDIDOS
objeto: SIGASC.V_CONTRATOS_EXTENDIDOS
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

# SIGASC.V_CONTRATOS_EXTENDIDOS

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_CONTRATO_CLIENTE]]
- [[SIGASC.PRODUCTO]]

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
-- Vista: SIGASC.V_CONTRATOS_EXTENDIDOS
-- Extraida: 2026-08-07T15:28:37.487452+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [SIGASC].[V_CONTRATOS_EXTENDIDOS] AS WITH clientes_ppl AS (
    SELECT DISTINCT c.PKCLIENTENRO
    FROM SIGASC.H_CONTRATO_CLIENTE c
    JOIN SIGASC.PRODUCTO p
      ON p.PKPRODUCTOID = c.PKPRODUCTOID
    WHERE c.CONTRATOSTS = 'C'
      AND p.PRODUCTOPPL = 'P'
      AND p.PRODUCTOTPO IN ('B','Z','W','R')  -- CABLE (ajusta si aplica)
)
SELECT
    h.EMPRESAID,
    h.PKCONTRATONRO,
    h.PKCLIENTENRO,
    h.PKPOLITICAID,
    h.PKPRODUCTOID,
    h.CONTRATOSTS,
    h.NEGOCIOSEGMENTO,
    h.NEGOCIOSEGMENTOTIPOID,
    h.CLIENTESTS,
    h.CLIENTETPO,
    h.CONTRATOCNT,
    h.BDMODIFIEDDATE,

    nx.RegEndDate                                      AS [Reg End Date],
    CONVERT(varchar(10), h.BDMODIFIEDDATE, 103)        AS [Reg Start Date],

    CASE
        WHEN h.NEGOCIOSEGMENTO = 1 AND h.NEGOCIOSEGMENTOTIPOID = 3
            THEN CONCAT(h.EMPRESAID, '_1')
        WHEN h.EMPRESAID = 23 AND h.NEGOCIOSEGMENTO = 3 AND h.NEGOCIOSEGMENTOTIPOID = 1
            THEN CONCAT(h.EMPRESAID, '_', h.NEGOCIOSEGMENTO)
        ELSE CONCAT(
                h.EMPRESAID, '_',
                CONCAT(
                    CAST(h.NEGOCIOSEGMENTO AS varchar(10)),
                    COALESCE(CAST(h.NEGOCIOSEGMENTOTIPOID AS varchar(10)), '')
                )
            )
    END AS [Cliente Negocio Segmento ID],

    SUBSTRING(h.PKCLIENTENRO,  CHARINDEX('_', h.PKCLIENTENRO)  + 1, LEN(h.PKCLIENTENRO))  AS [Cliente Numero],
    SUBSTRING(h.PKCONTRATONRO, CHARINDEX('_', h.PKCONTRATONRO) + 1, LEN(h.PKCONTRATONRO)) AS [Contrato Numero],

    CASE WHEN cp.PKCLIENTENRO IS NOT NULL THEN 'Y' ELSE 'N' END AS [ProductoPpl Conectado]
FROM SIGASC.H_CONTRATO_CLIENTE h
OUTER APPLY (
    SELECT TOP (1) h2.BDMODIFIEDDATE AS RegEndDate
    FROM SIGASC.H_CONTRATO_CLIENTE h2
    WHERE h2.PKCONTRATONRO = h.PKCONTRATONRO
      AND h2.BDMODIFIEDDATE > h.BDMODIFIEDDATE
      AND NOT (h2.CLIENTESTS = 'X' AND h2.BDMODIFIEDDATE = CONVERT(date,'19000101'))
    ORDER BY h2.BDMODIFIEDDATE
) nx
LEFT JOIN clientes_ppl cp
  ON cp.PKCLIENTENRO = h.PKCLIENTENRO
WHERE NOT (h.CLIENTESTS = 'X' AND h.BDMODIFIEDDATE = CONVERT(date,'19000101'));
```
