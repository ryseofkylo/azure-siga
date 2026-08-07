---
esquema: SIGASC
tabla: NEGOCIOSEGMENTO
objeto: SIGASC.NEGOCIOSEGMENTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `NEGOCIOSEGMENTO` (único en muestra de 4)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.NEGOCIOSEGMENTO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `NEGOCIOSEGMENTO` (único en muestra de 4)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `NEGOCIOSEGMENTO` | int | 0% |
| 2 | `NEGOCIOSEGMENTONOMBRE` | varchar | 0% |
| 3 | `NEGOCIOSEGMENTOOFICIAL` | int | 0% |
| 4 | `NEGOCIOSEGMENTOCONTACTO` | int | 0% |
| 5 | `NEGOCIOSEGMENTOADMITESKEELO` | int | 0% |
| 6 | `NEGOCIOSEGMENTONODIRECCION` | int | 100% |
| 7 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.NEGOCIOSEGMENTOTIPO]] · `NEGOCIOSEGMENTO.NEGOCIOSEGMENTO = NEGOCIOSEGMENTOTIPO.NEGOCIOSEGMENTO` — view_join (V_SEGMENTOCLIENTE), alta

## Reglas de negocio conocidas
**Filtros**
- `NOT ( ( n.NEGOCIOSEGMENTO = 3 ) AND ( t.NEGOCIOSEGMENTOTIPOID = 1 ) )` — _de_ [[dbo.V_SEGMENTOCLIENTE]]

## Vistas que la consumen (referencia)
- [[dbo.V_SEGMENTOCLIENTE]]
