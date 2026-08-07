---
esquema: SIGASC
tabla: CRMMOTIVOORDEN
objeto: SIGASC.CRMMOTIVOORDEN
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCRMMOTIVOORDEN` (único en muestra de 51)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMMOTIVOORDEN

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCRMMOTIVOORDEN` (único en muestra de 51)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCRMMOTIVOORDEN` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `MOTIVOORDINGID` | int | 0% |
| 4 | `CRMMOTIVO1` | int | 0% |
| 5 | `CRMMOTIVO2` | int | 0% |
| 6 | `CRMMOTIVO3` | int | 0% |
| 7 | `CRMMOTIVO4` | int | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKMOTIVOORDINGID` | varchar | 0% |
| 10 | `PKCRMMOTIVO1` | varchar | 0% |
| 11 | `PKCRMMOTIVO2` | varchar | 0% |
| 12 | `PKCRMMOTIVO3` | varchar | 0% |
| 13 | `PKCRMMOTIVO4` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `MOTIVOORDINGID` (int) → [[clave-MOTIVOORDINGID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMMOTIVO1` (varchar) → [[clave-PKCRMMOTIVO1]]
- `PKCRMMOTIVO2` (varchar) → [[clave-PKCRMMOTIVO2]]
- `PKCRMMOTIVO3` (varchar) → [[clave-PKCRMMOTIVO3]]
- `PKCRMMOTIVO4` (varchar) → [[clave-PKCRMMOTIVO4]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
