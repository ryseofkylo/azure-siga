---
esquema: SIGASC
tabla: PRODUCTOTPO
objeto: SIGASC.PRODUCTOTPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PRODUCTOTPO` (único en muestra de 25)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTOTPO

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PRODUCTOTPO` (único en muestra de 25)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PRODUCTOTPO` | varchar | 0% |
| 2 | `PRODUCTOTPONOMBRE` | varchar | 0% |
| 3 | `PRODUCTOGENORDEN` | int | 0% |
| 4 | `PRODUCTOESADICIONAL` | int | 0% |
| 5 | `PRODUCTOTPOPRIORIDAD` | int | 0% |
| 6 | `PRODUCTOTPOVALIDAPPL` | int | 72% |
| 7 | `PRODUCTOBAJAREQAUTORIZACION` | int | 8% |
| 8 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PRODUCTOTPO` (varchar) → [[clave-PRODUCTOTPO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PRODUCTO]] · `PRODUCTOTPO.PRODUCTOTPO = PRODUCTO.PRODUCTOTPO` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.ORDENES_PENDIENTES]] · `PRODUCTOTPO.PRODUCTOTPO = ORDENES_PENDIENTES.TIPOPRODUCTO` — view_join (V_TAREAS_PENDIENTES), alta
- [[SIGASC.ORDENES_REALIZADAS]] · `PRODUCTOTPO.PRODUCTOTPO = ORDENES_REALIZADAS.TIPOPRODUCTO` — view_join (V_TAREAS_REALIZADAS), alta

## Reglas de negocio conocidas
**Filtros**
- `o.productotpo IN ('B','W','Z')` — _de_ [[dbo.V_TAREAS_PENDIENTES]]
- `o.productotpo IN ('E','C','I','N','L','S','T')` — _de_ [[dbo.V_TAREAS_PENDIENTES]]
- `o.productotpo IN ('E','C','I','N','L')` — _de_ [[dbo.V_TAREAS_REALIZADAS]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_TAREAS_PENDIENTES]], [[dbo.V_TAREAS_REALIZADAS]]

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
- [[dbo.V_TAREAS_PENDIENTES]]
- [[dbo.V_TAREAS_REALIZADAS]]
