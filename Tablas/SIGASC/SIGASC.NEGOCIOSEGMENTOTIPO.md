---
esquema: SIGASC
tabla: NEGOCIOSEGMENTOTIPO
objeto: SIGASC.NEGOCIOSEGMENTOTIPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `NEGOCIOSEGMENTOTIPONOM`, `NEGOCIOSEGMENTOTIPOID`, `NEGOCIOSEGMENTO`
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.NEGOCIOSEGMENTOTIPO

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `NEGOCIOSEGMENTOTIPONOM`, `NEGOCIOSEGMENTOTIPOID`, `NEGOCIOSEGMENTO`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `NEGOCIOSEGMENTO` | int | 0% |
| 2 | `NEGOCIOSEGMENTOTIPOID` | int | 0% |
| 3 | `NEGOCIOSEGMENTOTIPONOM` | varchar | 0% |
| 4 | `NEGOCIOSEGMENTOTIPOTRAMITE` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `NEGOCIOSEGMENTOTIPOID` (int) → [[clave-NEGOCIOSEGMENTOTIPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.NEGOCIOSEGMENTO]] · `NEGOCIOSEGMENTOTIPO.NEGOCIOSEGMENTO = NEGOCIOSEGMENTO.NEGOCIOSEGMENTO` — view_join (V_SEGMENTOCLIENTE), alta

## Reglas de negocio conocidas
**Filtros**
- `NOT ( ( n.NEGOCIOSEGMENTO = 3 ) AND ( t.NEGOCIOSEGMENTOTIPOID = 1 ) )` — _de_ [[dbo.V_SEGMENTOCLIENTE]]

## Vistas que la consumen (referencia)
- [[dbo.V_SEGMENTOCLIENTE]]
