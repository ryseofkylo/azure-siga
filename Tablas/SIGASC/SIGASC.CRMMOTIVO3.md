---
esquema: SIGASC
tabla: CRMMOTIVO3
objeto: SIGASC.CRMMOTIVO3
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCRMMOTIVO3` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMMOTIVO3

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCRMMOTIVO3` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCRMMOTIVO3` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CRMMOTIVO1` | int | 0% |
| 4 | `CRMMOTIVO2` | int | 0% |
| 5 | `CRMMOTIVO3` | int | 0% |
| 6 | `CRMMOTIVO3NOM` | varchar | 0% |
| 7 | `CRMMOTIVO3PGM` | varchar | 83% |
| 8 | `CRMMOTIVO3ACTIVO` | int | 0% |
| 9 | `CRMMOTIVO3FIN` | int | 0% |
| 10 | `PIPELINERUNID` | varchar | 0% |
| 11 | `PKCRMMOTIVO1` | varchar | 0% |
| 12 | `PKCRMMOTIVO2` | varchar | 0% |
| 13 | `PKCRMMOTIVO3` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMMOTIVO1` (varchar) → [[clave-PKCRMMOTIVO1]]
- `PKCRMMOTIVO2` (varchar) → [[clave-PKCRMMOTIVO2]]
- `PKCRMMOTIVO3` (varchar) → [[clave-PKCRMMOTIVO3]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.CRMMOTIVO1]] · `CRMMOTIVO3.PKCRMMOTIVO1 = CRMMOTIVO1.PKCRMMOTIVO1` — view_join (V_CRMMOTIVO), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_CRMMOTIVO]]

## Vistas que la consumen (referencia)
- [[dbo.V_CRMMOTIVO]]
