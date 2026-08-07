---
esquema: SIGASC
tabla: H_MOROSIDAD
objeto: SIGASC.H_MOROSIDAD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKCLIENTENRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_MOROSIDAD

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKCLIENTENRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKH_MOROSIDAD` | nvarchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `MOROSIDADMES` | int | 0% |
| 5 | `MOROSIDADSTS` | nvarchar | 0% |
| 6 | `PIPELINERUNID` | nvarchar | 0% |
| 7 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 8 | `hash` | nvarchar | 0% |
| 9 | `PKCLIENTENRO` | nvarchar | 0% |
| 10 | `PKMOROSIDADMES` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (nvarchar) → [[clave-PKCLIENTENRO]]
- `PKMOROSIDADMES` (nvarchar) → [[clave-PKMOROSIDADMES]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
