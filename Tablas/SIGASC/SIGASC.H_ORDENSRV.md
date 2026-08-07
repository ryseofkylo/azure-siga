---
esquema: SIGASC
tabla: H_ORDENSRV
objeto: SIGASC.H_ORDENSRV
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKORDENNRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_ORDENSRV

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKORDENNRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ORDENNRO` | int | 0% |
| 3 | `ORDENSTS` | nvarchar | 0% |
| 4 | `PIPELINERUNID` | nvarchar | 0% |
| 5 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 6 | `hash` | nvarchar | 0% |
| 7 | `PKORDENNRO` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ORDENNRO` (int) → [[clave-ORDENNRO]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `PKORDENNRO` (nvarchar) → [[clave-PKORDENNRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[dbo.V_ORDENINSTALACION]] · `H_ORDENSRV.PKORDENNRO = V_ORDENINSTALACION.PKORDENNRO` — view_join (V_HIST_ORDENSRV_360), alta

## Reglas de negocio conocidas
**Filtros**
- `v.bdmodifieddate >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101)` — _de_ [[dbo.V_HIST_ORDENSRV_360]]
- `v.bdmodifieddate < GETDATE()` — _de_ [[dbo.V_HIST_ORDENSRV_360]]

## Vistas que la consumen (referencia)
- [[dbo.V_HIST_ORDENSRV_360]]
