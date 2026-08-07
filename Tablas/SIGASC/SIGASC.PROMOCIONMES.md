---
esquema: SIGASC
tabla: PROMOCIONMES
objeto: SIGASC.PROMOCIONMES
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPROMOCIONMES` (único en muestra de 200)
n_columnas: 17
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PROMOCIONMES

> **BASE TABLE** · Dominio: **Core SIGA** · 17 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPROMOCIONMES` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPROMOCIONMES` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PROMOCIONID` | int | 0% |
| 4 | `PROMOCIONMES` | int | 0% |
| 5 | `PROMOCIONDTOPRJ` | real | 0% |
| 6 | `PROMOCIONDTOPRC` | real | 0% |
| 7 | `PROMOCIONPRCVTO3` | real | 0% |
| 8 | `PROMOCIONPRCVTO2` | real | 0% |
| 9 | `PROMOCIONPRC` | real | 0% |
| 10 | `PROMOCIONDEBPRCVTO3` | real | 0% |
| 11 | `PROMOCIONDEBPRCVTO2` | real | 0% |
| 12 | `PROMOCIONDEBPRC` | real | 0% |
| 13 | `PROMOCIONDEBDTOPRJ` | real | 0% |
| 14 | `PROMOCIONDEBDTOPRC` | real | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |
| 16 | `PKPROMOCIONID` | varchar | 0% |
| 17 | `PKPROMOCIONMES` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PROMOCIONID` (int) → [[clave-PROMOCIONID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPROMOCIONID` (varchar) → [[clave-PKPROMOCIONID]]
- `PKPROMOCIONMES` (varchar) → [[clave-PKPROMOCIONMES]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PROMOCION]] · `PROMOCIONMES.PROMOCIONID = PROMOCION.PROMOCIONID` — view_join (v_EscalonPromo), alta
- [[SIGASC.PROMOCION]] · `PROMOCIONMES.EMPRESAID = PROMOCION.EMPRESAID` — view_join (v_EscalonPromo), alta
- [[dbo.V_INDICEPROMOCIONMES]] · `PROMOCIONMES.PKPROMOCIONID = V_INDICEPROMOCIONMES.PKPROMOCIONID` — view_join (V_PROMOCION), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_INDICEPROMOCIONMES]]

## Vistas que la consumen (referencia)
- [[dbo.V_INDICEPROMOCIONMES]]
- [[dbo.V_PROMOCION]]
- [[dbo.v_EscalonPromo]]
- [[dbo.v_promomes]]
