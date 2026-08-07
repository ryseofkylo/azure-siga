---
esquema: SIGASC
tabla: DECOEVENTO
objeto: SIGASC.DECOEVENTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKDECOEVEID` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECOEVENTO

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKDECOEVEID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `DECOSISID` | int | 0% |
| 2 | `DECOEVEID` | int | 0% |
| 3 | `DECODERID` | varchar | 0% |
| 4 | `DECOEVETPO` | int | 0% |
| 5 | `DECOEVESTS` | varchar | 0% |
| 6 | `DECOEVEPRIORIDAD` | int | 0% |
| 7 | `DECOEVEFCH` | datetime2 | 0% |
| 8 | `DECOEVEHORA` | datetime2 | 100% |
| 9 | `DECOEVEUSR` | varchar | 0% |
| 10 | `DECOEVECOD` | int | 0% |
| 11 | `DECOEVEFCHAGE` | datetime2 | 100% |
| 12 | `DECODERIDEXTERNO` | varchar | 0% |
| 13 | `DECOPAQUETE` | int | 0% |
| 14 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |
| 16 | `PKDECOEVEID` | varchar | 0% |

## Claves de join presentes
- `DECOSISID` (int) → [[clave-DECOSISID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
