---
esquema: SIGASC
tabla: AGENDARECURSO
objeto: SIGASC.AGENDARECURSO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKAGENDARECURSO` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.AGENDARECURSO

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKAGENDARECURSO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKAGENDARECURSO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `AGENDAFECHA` | datetime2 | 0% |
| 4 | `TAREATIPOID` | int | 0% |
| 5 | `RECURSOID` | int | 0% |
| 6 | `AGENDARECURSOACTIVO` | varchar | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |
| 8 | `PKTAREATIPOID` | varchar | 0% |
| 9 | `PKRECURSOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TAREATIPOID` (int) → [[clave-TAREATIPOID]]
- `RECURSOID` (int) → [[clave-RECURSOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKTAREATIPOID` (varchar) → [[clave-PKTAREATIPOID]]
- `PKRECURSOID` (varchar) → [[clave-PKRECURSOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
