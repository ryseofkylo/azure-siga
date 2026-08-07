---
esquema: SIGASC
tabla: CMEVENTO
objeto: SIGASC.CMEVENTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCMEVEID` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMEVENTO

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCMEVEID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CMSISTEMAID` | int | 0% |
| 2 | `CMEVEID` | int | 0% |
| 3 | `CMODEMID` | varchar | 0% |
| 4 | `CMEVETPO` | int | 0% |
| 5 | `CMEVESTS` | varchar | 0% |
| 6 | `CMEVEPRIORIDAD` | int | 0% |
| 7 | `CMEVEFCH` | datetime2 | 0% |
| 8 | `CMEVEHORA` | datetime2 | 100% |
| 9 | `CMEVEFCHAGE` | datetime2 | 0% |
| 10 | `CMEVEUSR` | varchar | 0% |
| 11 | `CMEVECOD` | int | 0% |
| 12 | `CMEVEINTENTO` | int | 0% |
| 13 | `CMEVEEMPRESAID` | int | 0% |
| 14 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |
| 16 | `PKCMEVEID` | varchar | 0% |

## Claves de join presentes
- `CMSISTEMAID` (int) → [[clave-CMSISTEMAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
