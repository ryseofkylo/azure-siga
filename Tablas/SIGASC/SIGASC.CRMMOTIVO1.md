---
esquema: SIGASC
tabla: CRMMOTIVO1
objeto: SIGASC.CRMMOTIVO1
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMMOTIVO1` (único en muestra de 200)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMMOTIVO1

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMMOTIVO1` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CRMMOTIVO1` | int | 0% |
| 3 | `CRMMOTIVO1NOM` | varchar | 0% |
| 4 | `CRMMOTIVO1PGM` | varchar | 76% |
| 5 | `CRMMOTIVO1ACTIVO` | int | 0% |
| 6 | `CRMMOTIVO1FIN` | int | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |
| 8 | `PKCRMMOTIVO1` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMMOTIVO1` (varchar) → [[clave-PKCRMMOTIVO1]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.CRMMOTIVO2]] · `CRMMOTIVO1.PKCRMMOTIVO1 = CRMMOTIVO2.PKCRMMOTIVO1` — view_join (V_CRMMOTIVO), alta
- [[SIGASC.CRMMOTIVO3]] · `CRMMOTIVO1.PKCRMMOTIVO1 = CRMMOTIVO3.PKCRMMOTIVO1` — view_join (V_CRMMOTIVO), alta
- [[SIGASC.CRMMOTIVO4]] · `CRMMOTIVO1.PKCRMMOTIVO1 = CRMMOTIVO4.PKCRMMOTIVO1` — view_join (V_CRMMOTIVO), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_CRMMOTIVO]]

## Vistas que la consumen (referencia)
- [[dbo.V_CRMMOTIVO]]
