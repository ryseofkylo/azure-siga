---
esquema: SIGASC
tabla: HISTORICOENTIDADREG
objeto: SIGASC.HISTORICOENTIDADREG
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKHISTORICOENTIDADREG` (único en muestra de 200)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.HISTORICOENTIDADREG

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKHISTORICOENTIDADREG` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKHISTORICOENTIDADREG` | nvarchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `HSTENTIDADID` | nvarchar | 0% |
| 4 | `HSTENTIDADATT` | nvarchar | 0% |
| 5 | `HSTENTIDADREGPKVAL` | nvarchar | 0% |
| 6 | `HSTENTIDADREGFCH` | datetime2 | 0% |
| 7 | `HSTENTIDADREGVALOLD` | nvarchar | 0% |
| 8 | `HSTENTIDADREGVALNEW` | nvarchar | 0% |
| 9 | `HSTENTIDADREGUSR` | nvarchar | 0% |
| 10 | `HSTENTIDADREGORI` | nvarchar | 0% |
| 11 | `HSTENTIDADREGMODO` | nvarchar | 0% |
| 12 | `HSTENTIDADREGCLIENTENRO` | int | 0% |
| 13 | `ORGANIZACIONID` | int | 12% |
| 14 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 15 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ORGANIZACIONID` (int) → [[clave-ORGANIZACIONID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.ORDENSRV]] · `HISTORICOENTIDADREG.EMPRESAID = ORDENSRV.EMPRESAID` — view_join (V_ORDENINSTALACION), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_ORDENINSTALACION]]

**Derivaciones (CASE)**
- _de_ [[dbo.V_ORDENINSTALACION]]:
  ```sql
  CASE WHEN ( r.ordennro IS NOT NULL ) THEN 'SI' ELSE 'NO' END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_ORDENINSTALACION]]
