---
esquema: SIGASC
tabla: POLITICAPRC
objeto: SIGASC.POLITICAPRC
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPOLITICAPRC` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.POLITICAPRC

> **BASE TABLE** · Dominio: **Core SIGA** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPOLITICAPRC` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPOLITICAPRC` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `POLITICAID` | int | 0% |
| 4 | `POLITICALIN` | int | 0% |
| 5 | `POLITICAFCH` | datetime2 | 0% |
| 6 | `POLITICAPRC` | real | 0% |
| 7 | `POLITICAPRCVTO2` | real | 0% |
| 8 | `POLITICAPRCVTO3` | real | 0% |
| 9 | `POLITICAPRCACTIVACARTELERA` | int | 0% |
| 10 | `PIPELINERUNID` | varchar | 0% |
| 11 | `PKPOLITICAID` | varchar | 0% |
| 12 | `PKPOLITICALIN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPOLITICAID` (varchar) → [[clave-PKPOLITICAID]]
- `PKPOLITICALIN` (varchar) → [[clave-PKPOLITICALIN]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.POLITICACPTO]] · `POLITICAPRC.PKPOLITICAID = POLITICACPTO.PKPOLITICAID` — view_join (V_POLITICAPRC), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_POLITICAPRC]]
- [[dbo.V_POLITICAPRC_PPP]]
- [[dbo.V_PREV_POLITICAPRC]]
