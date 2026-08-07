---
esquema: SIGASC
tabla: H_CONTRATO_CLIENTE
objeto: SIGASC.H_CONTRATO_CLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKCONTRATONRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 17
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_CONTRATO_CLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 17 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKCONTRATONRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PKCONTRATONRO` | nvarchar | 0% |
| 3 | `PKCLIENTENRO` | nvarchar | 0% |
| 4 | `PKPOLITICAID` | nvarchar | 0% |
| 5 | `PKPRODUCTOID` | nvarchar | 0% |
| 6 | `CONTRATOSTS` | nvarchar | 0% |
| 7 | `PLANCOMERCIALCLIENTEITEM` | int | 52% |
| 8 | `PLANCOMERCIALGESTIONID` | int | 52% |
| 9 | `PLANCOMERCIALCLIENTEID` | int | 52% |
| 10 | `PIPELINERUNID` | nvarchar | 0% |
| 11 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 12 | `hash` | nvarchar | 0% |
| 13 | `NEGOCIOSEGMENTO` | int | 0% |
| 14 | `NEGOCIOSEGMENTOTIPOID` | int | 70% |
| 15 | `CLIENTESTS` | nvarchar | 0% |
| 16 | `CLIENTETPO` | int | 0% |
| 17 | `CONTRATOCNT` | int | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PKCONTRATONRO` (nvarchar) → [[clave-PKCONTRATONRO]]
- `PKCLIENTENRO` (nvarchar) → [[clave-PKCLIENTENRO]]
- `PKPOLITICAID` (nvarchar) → [[clave-PKPOLITICAID]]
- `PKPRODUCTOID` (nvarchar) → [[clave-PKPRODUCTOID]]
- `PLANCOMERCIALGESTIONID` (int) → [[clave-PLANCOMERCIALGESTIONID]]
- `PLANCOMERCIALCLIENTEID` (int) → [[clave-PLANCOMERCIALCLIENTEID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `NEGOCIOSEGMENTOTIPOID` (int) → [[clave-NEGOCIOSEGMENTOTIPOID]]
- `CLIENTETPO` (int) → [[clave-CLIENTETPO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PRODUCTO]] · `H_CONTRATO_CLIENTE.PKPRODUCTOID = PRODUCTO.PKPRODUCTOID` — view_join (V_CLIENTEDATOS_SINFILTRO), alta

## Reglas de negocio conocidas
**Filtros**
- 🪦🚦 `NOT (h.CLIENTESTS = 'X' AND h.BDMODIFIEDDATE = CONVERT(date,'19000101'))` — _de_ [[SIGASC.V_CONTRATOS_BASE]]
- 🚦 `c.CONTRATOSTS = 'C'` — _de_ [[SIGASC.V_CONTRATOS_EXTENDIDOS]]
- `h2.BDMODIFIEDDATE > h.BDMODIFIEDDATE` — _de_ [[SIGASC.V_CONTRATOS_EXTENDIDOS]]
- 🪦🚦 `NOT (h2.CLIENTESTS = 'X' AND h2.BDMODIFIEDDATE = CONVERT(date,'19000101'))` — _de_ [[SIGASC.V_CONTRATOS_EXTENDIDOS]]
- ♻️ dedup: vistas que deduplican esta tabla → [[SIGASC.V_CONTRATOS_EXTENDIDOS]], [[dbo.V_CLIENTEDATOS_SINFILTRO]], [[dbo.V_PRODUCTODATOS]]

**Derivaciones (CASE)**
- _de_ [[SIGASC.V_CONTRATOS_BASE]]:
  ```sql
  CASE WHEN h.NEGOCIOSEGMENTO = 1 AND h.NEGOCIOSEGMENTOTIPOID = 3 THEN CONCAT(h.EMPRESAID, '_1') WHEN h.EMPRESAID = 23 AND h.NEGOCIOSEGMENTO = 3 AND h.NEGOCIOSEGMENTOTIPOID = 1 THEN CONCAT(h.EMPRESAID, '_', h.NEGOCIOSEGMENTO) ELSE CONCAT(h.EMPRESAID, '_', CONCAT(CAST(h.NEGOCIOSEGMENTO AS varchar(10)), COALESCE(CAST(h.NEGOCIOSEGMENTOTIPOID AS varchar(10)), ''))) END
  ```
- _de_ [[SIGASC.V_CONTRATOS_EXTENDIDOS]]:
  ```sql
  CASE WHEN h.NEGOCIOSEGMENTO = 1 AND h.NEGOCIOSEGMENTOTIPOID = 3 THEN CONCAT(h.EMPRESAID, '_1') WHEN h.EMPRESAID = 23 AND h.NEGOCIOSEGMENTO = 3 AND h.NEGOCIOSEGMENTOTIPOID = 1 THEN CONCAT(h.EMPRESAID, '_', h.NEGOCIOSEGMENTO) ELSE CONCAT( h.EMPRESAID, '_', CONCAT( CAST(h.NEGOCIOSEGMENTO AS varchar(10)), COALESCE(CAST(h.NEGOCIOSEGMENTOTIPOID AS varchar(10)), '') ) ) END
  ```

## Vistas que la consumen (referencia)
- [[SIGASC.V_CONTRATOS_BASE]]
- [[SIGASC.V_CONTRATOS_EXTENDIDOS]]
- [[dbo.V_CLIENTEDATOS_SINFILTRO]]
- [[dbo.V_CLIENTESPRODDATOS]]
- [[dbo.V_PRODUCTODATOS]]
