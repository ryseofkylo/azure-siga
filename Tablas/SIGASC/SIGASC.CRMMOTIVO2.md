---
esquema: SIGASC
tabla: CRMMOTIVO2
objeto: SIGASC.CRMMOTIVO2
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCRMMOTIVO2` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMMOTIVO2

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCRMMOTIVO2` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCRMMOTIVO2` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CRMMOTIVO1` | int | 0% |
| 4 | `CRMMOTIVO2` | int | 0% |
| 5 | `CRMMOTIVO2NOM` | varchar | 0% |
| 6 | `CRMMOTIVO2PGM` | varchar | 86% |
| 7 | `CRMMOTIVO2ACTIVO` | int | 0% |
| 8 | `CRMMOTIVO2FIN` | int | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCRMMOTIVO1` | varchar | 0% |
| 11 | `PKCRMMOTIVO2` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMMOTIVO1` (varchar) → [[clave-PKCRMMOTIVO1]]
- `PKCRMMOTIVO2` (varchar) → [[clave-PKCRMMOTIVO2]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.CRMMOTIVO1]] · `CRMMOTIVO2.PKCRMMOTIVO1 = CRMMOTIVO1.PKCRMMOTIVO1` — view_join (V_CRMMOTIVO), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_CRMMOTIVO]]

## Vistas que la consumen (referencia)
- [[dbo.V_CRMMOTIVO]]
