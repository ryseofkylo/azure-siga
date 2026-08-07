---
esquema: SIGASC
tabla: COMBO
objeto: SIGASC.COMBO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCOMBOID` (único en muestra de 200)
n_columnas: 17
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COMBO

> **BASE TABLE** · Dominio: **Core SIGA** · 17 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCOMBOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `COMBOID` | int | 0% |
| 3 | `COMBONOMBRE` | varchar | 0% |
| 4 | `COMBOPRDCNT` | int | 0% |
| 5 | `COMBOPRDTOT` | int | 0% |
| 6 | `COMBOPRIORIDAD` | int | 0% |
| 7 | `COMBOTPOFAC` | varchar | 0% |
| 8 | `COMBOSTS` | varchar | 0% |
| 9 | `POLITICACOMBOID` | int | 0% |
| 10 | `COMBOCONTROLFECHATOPE` | datetime2 | 90% |
| 11 | `COMBOCONTROLFECHAACTIVO` | int | 0% |
| 12 | `COMBOCPTOFACID` | int | 100% |
| 13 | `COMBOAPLCPTO` | varchar | 0% |
| 14 | `COMBONOMBREFAC` | varchar | 0% |
| 15 | `COMBOENFACTURA` | int | 2% |
| 16 | `PIPELINERUNID` | varchar | 0% |
| 17 | `PKCOMBOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `COMBOID` (int) → [[clave-COMBOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCOMBOID` (varchar) → [[clave-PKCOMBOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]]

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_DETALLE_ALL]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
