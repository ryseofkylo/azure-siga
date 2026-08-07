---
esquema: SIGASC
tabla: CONTRATOPROMOCION
objeto: SIGASC.CONTRATOPROMOCION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCONTRATOPROMOCION` (único en muestra de 200)
n_columnas: 19
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CONTRATOPROMOCION

> **BASE TABLE** · Dominio: **Core SIGA** · 19 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCONTRATOPROMOCION` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCONTRATOPROMOCION` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CONTRATONRO` | int | 0% |
| 4 | `CONTRATOPRMFCH` | datetime2 | 0% |
| 5 | `PROMOCIONID` | int | 0% |
| 6 | `CONTRATOPRMFINI` | datetime2 | 0% |
| 7 | `CONTRATOPRMFFIN` | datetime2 | 100% |
| 8 | `CONTRATOPRMUSR` | varchar | 0% |
| 9 | `CONTRATOPRMSTS` | varchar | 0% |
| 10 | `CONTRATOPRMFCHCXL` | datetime2 | 100% |
| 11 | `CONTRATOPRMUSRCXL` | varchar | 0% |
| 12 | `CONTRATOPRMMES` | int | 0% |
| 13 | `CONTRATOPRMFCHFINREAL` | datetime2 | 100% |
| 14 | `CONTRATOPRMAUTOMATICO` | int | 100% |
| 15 | `CONTRATOPRMPLANCLIENTEITEM` | int | 0% |
| 16 | `CONTRATOPRMPLANCLIENTEID` | int | 0% |
| 17 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 18 | `PIPELINERUNID` | varchar | 0% |
| 19 | `PKCONTRATONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
- `PROMOCIONID` (int) → [[clave-PROMOCIONID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCONTRATONRO` (varchar) → [[clave-PKCONTRATONRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.CONTRATO]] · `CONTRATOPROMOCION.EMPRESAID = CONTRATO.EMPRESAID` — view_join (v_promomes), alta
- [[SIGASC.CONTRATO]] · `CONTRATOPROMOCION.CONTRATONRO = CONTRATO.CONTRATONRO` — view_join (v_promomes), alta

## Reglas de negocio conocidas
**Filtros**
- `cp.empresaid = 10` — _de_ [[dbo.vFACTURACION_DETALLE_202305_cp]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]], [[dbo.v_listapromociones]]

## Vistas que la consumen (referencia)
- [[dbo.V_RETENCIONES]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
- [[dbo.v_fechasprueba]]
- [[dbo.v_listapromociones]]
- [[dbo.v_promomes]]
