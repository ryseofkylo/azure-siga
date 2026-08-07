---
esquema: SIGASC
tabla: CRMMOTIVO4
objeto: SIGASC.CRMMOTIVO4
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCRMMOTIVO4` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMMOTIVO4

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCRMMOTIVO4` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCRMMOTIVO4` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CRMMOTIVO1` | int | 0% |
| 4 | `CRMMOTIVO2` | int | 0% |
| 5 | `CRMMOTIVO3` | int | 0% |
| 6 | `CRMMOTIVO4` | int | 0% |
| 7 | `CRMMOTIVO4NOM` | varchar | 0% |
| 8 | `CRMMOTIVO4PGM` | varchar | 100% |
| 9 | `CRMMOTIVO4ACTIVO` | int | 0% |
| 10 | `PIPELINERUNID` | varchar | 0% |
| 11 | `PKCRMMOTIVO1` | varchar | 0% |
| 12 | `PKCRMMOTIVO2` | varchar | 0% |
| 13 | `PKCRMMOTIVO3` | varchar | 0% |
| 14 | `PKCRMMOTIVO4` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMMOTIVO1` (varchar) → [[clave-PKCRMMOTIVO1]]
- `PKCRMMOTIVO2` (varchar) → [[clave-PKCRMMOTIVO2]]
- `PKCRMMOTIVO3` (varchar) → [[clave-PKCRMMOTIVO3]]
- `PKCRMMOTIVO4` (varchar) → [[clave-PKCRMMOTIVO4]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.CRMMOTIVO1]] · `CRMMOTIVO4.PKCRMMOTIVO1 = CRMMOTIVO1.PKCRMMOTIVO1` — view_join (V_CRMMOTIVO), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_CRMMOTIVO]]

**Derivaciones (CASE)**
- _de_ [[dbo.V_CRMMOTIVO]]:
  ```sql
  CASE WHEN ( m4.CRMMOTIVO4NOM = '' ) THEN NULL ELSE m4.CRMMOTIVO4NOM END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_CRMMOTIVO]]
