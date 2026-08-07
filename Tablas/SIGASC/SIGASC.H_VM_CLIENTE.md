---
esquema: SIGASC
tabla: H_VM_CLIENTE
objeto: SIGASC.H_VM_CLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKCLIENTENRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 20
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_VM_CLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 20 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKCLIENTENRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | int | 0% |
| 3 | `CLIENTESTS` | nvarchar | 0% |
| 4 | `CLIENTENATURALEZAID` | int | 4% |
| 5 | `MEDCOBROID` | int | 0% |
| 6 | `CICLOID` | int | 0% |
| 7 | `NEGOCIOSEGMENTOTIPOID` | int | 34% |
| 8 | `NEGOCIOSEGMENTO` | int | 0% |
| 9 | `CLIENTETPO` | int | 0% |
| 10 | `CLICALID` | int | 0% |
| 11 | `GEOMANID` | int | 0% |
| 12 | `GEODIV1ID` | int | 0% |
| 13 | `GEODIV2ID` | int | 0% |
| 14 | `GEOMANINI` | nvarchar | 0% |
| 15 | `CLIENTECORDX` | nvarchar | 0% |
| 16 | `CLIENTECORDY` | nvarchar | 0% |
| 17 | `PIPELINERUNID` | nvarchar | 0% |
| 18 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 19 | `hash` | nvarchar | 0% |
| 20 | `PKCLIENTENRO` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `CLIENTENATURALEZAID` (int) → [[clave-CLIENTENATURALEZAID]]
- `MEDCOBROID` (int) → [[clave-MEDCOBROID]]
- `CICLOID` (int) → [[clave-CICLOID]]
- `NEGOCIOSEGMENTOTIPOID` (int) → [[clave-NEGOCIOSEGMENTOTIPOID]]
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `CLIENTETPO` (int) → [[clave-CLIENTETPO]]
- `CLICALID` (int) → [[clave-CLICALID]]
- `GEOMANID` (int) → [[clave-GEOMANID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (nvarchar) → [[clave-PKCLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.V_PRODUCTODATOS]] · `H_VM_CLIENTE.PKCLIENTENRO = V_PRODUCTODATOS.PKCLIENTENRO` — view_join (V_CLIENTEDATOS), alta

## Reglas de negocio conocidas
**Filtros**
- `h.bdmodifieddate <= p.bdmodifieddate` — _de_ [[dbo.V_CLIENTEDATOS]]
- `h.pkclientenro = '23_5737066'` — _de_ [[dbo.V_CLIENTEDATOS]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_CLIENTEDATOS]], [[dbo.v_HistoricoCliente]], [[dbo.v_HistoricoClientexy]], [[dbo.v_Segmentacion]]

## Vistas que la consumen (referencia)
- [[dbo.V_CLIENTEDATOS]]
- [[dbo.v_HistoricoCliente]]
- [[dbo.v_HistoricoClientexy]]
- [[dbo.v_Segmentacion]]
