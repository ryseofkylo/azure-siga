---
esquema: BIGDATA
tabla: AGRUPACIONMEDCOBROBD
objeto: BIGDATA.AGRUPACIONMEDCOBROBD
tipo_objeto: BASE TABLE
dominio: Big Data
canonico: true
grain: 1 fila = 1 `MEDIOCOBROIDBD` (único en muestra de 111)
n_columnas: 6
tags:
  - esquema/BIGDATA
  - dominio/big-data
  - tipo/tabla-base
  - canonico
---

# BIGDATA.AGRUPACIONMEDCOBROBD

> **BASE TABLE** · Dominio: **Big Data** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `MEDIOCOBROIDBD` (único en muestra de 111)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MEDIOCOBROIDBD` | int | 0% |
| 2 | `MEDIOCOBRONOMBREBD` | varchar | 0% |
| 3 | `MEDIOCOBROGRUPOBD` | varchar | 0% |
| 4 | `MEDIOCOBROCANALBD` | varchar | 0% |
| 5 | `CLASIFICACION` | varchar | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.MEDIOCOBRO]] · `AGRUPACIONMEDCOBROBD.MEDIOCOBROIDBD = MEDIOCOBRO.MEDCOBROID` — view_join (V_MEDIOCOBRO), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_COBRANZAOFICINA]], [[dbo.V_MEDIOCOBRO]]

## Vistas que la consumen (referencia)
- [[dbo.V_COBRANZAOFICINA]]
- [[dbo.V_MEDIOCOBRO]]
