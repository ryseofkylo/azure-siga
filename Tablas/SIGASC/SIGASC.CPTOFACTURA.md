---
esquema: SIGASC
tabla: CPTOFACTURA
objeto: SIGASC.CPTOFACTURA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCPTOFACID` (único en muestra de 200)
n_columnas: 18
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CPTOFACTURA

> **BASE TABLE** · Dominio: **Core SIGA** · 18 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCPTOFACID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CPTOFACID` | int | 0% |
| 3 | `CPTOFACNOMBRE` | varchar | 0% |
| 4 | `CPTOFACTPO` | varchar | 0% |
| 5 | `IVAID` | int | 0% |
| 6 | `CPTOFACDTO` | int | 0% |
| 7 | `CPTOPROVEXT` | int | 44% |
| 8 | `CPTOFACGRUPOID` | int | 0% |
| 9 | `CPTOMOROSIDADCRITERIOID` | int | 9% |
| 10 | `CPTOFACUSADSC` | int | 94% |
| 11 | `CPTOFACDSC` | varchar | 94% |
| 12 | `CPTOFACUNICOPRIORIDAD` | int | 14% |
| 13 | `CPTOFACUNICONPLAY` | int | 14% |
| 14 | `CPTOFACUNICO` | int | 14% |
| 15 | `CPTOFACSTS` | varchar | 0% |
| 16 | `CPTOFACDISTRIBUIRALICUOTA` | int | 0% |
| 17 | `PIPELINERUNID` | varchar | 0% |
| 18 | `PKCPTOFACID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `IVAID` (int) → [[clave-IVAID]]
- `CPTOFACGRUPOID` (int) → [[clave-CPTOFACGRUPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.CPTOFACTURAGRUPO]] · `CPTOFACTURA.CPTOFACGRUPOID = CPTOFACTURAGRUPO.CPTOFACGRUPOID` — view_join (V_CONCEPTOFACTURA), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]]

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_DETALLE_ALL]]
- [[dbo.V_COBRANZAS_BASE]]
- [[dbo.V_CONCEPTOFACTURA]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
