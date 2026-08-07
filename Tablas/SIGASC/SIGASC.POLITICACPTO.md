---
esquema: SIGASC
tabla: POLITICACPTO
objeto: SIGASC.POLITICACPTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPOLITICACPTO` (único en muestra de 200)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.POLITICACPTO

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPOLITICACPTO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPOLITICACPTO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `POLITICAID` | int | 0% |
| 4 | `POLITICALIN` | int | 0% |
| 5 | `CPTOFACID` | int | 0% |
| 6 | `CUOTAID` | int | 0% |
| 7 | `POLITICACPTOTPO` | varchar | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKPOLITICAID` | varchar | 0% |
| 10 | `PKPOLITICALIN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `CUOTAID` (int) → [[clave-CUOTAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPOLITICAID` (varchar) → [[clave-PKPOLITICAID]]
- `PKPOLITICALIN` (varchar) → [[clave-PKPOLITICALIN]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.POLITICAPRC]] · `POLITICACPTO.PKPOLITICAID = POLITICAPRC.PKPOLITICAID` — view_join (V_POLITICAPRC), alta

## Reglas de negocio conocidas
**Filtros**
- `c.politicacptotpo = 'C'` — _de_ [[dbo.V_POLITICAPRC]]
- `p.politicacptotpo = 'C'` — _de_ [[dbo.V_PREV_POLITICAPRC]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_PREV_POLITICAPRC_2]]

## Vistas que la consumen (referencia)
- [[dbo.V_POLITICAPRC]]
- [[dbo.V_POLITICAPRC_PPP]]
- [[dbo.V_PREV_POLITICAPRC]]
- [[dbo.V_PREV_POLITICAPRC_2]]
