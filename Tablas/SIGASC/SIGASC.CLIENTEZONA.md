---
esquema: SIGASC
tabla: CLIENTEZONA
objeto: SIGASC.CLIENTEZONA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTEZONA

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCLIENTEZONA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `CLIZONATPO` | varchar | 0% |
| 5 | `CLIZONAID` | int | 0% |
| 6 | `CLIZONAUSRING` | varchar | 0% |
| 7 | `CLIZONAFCHING` | datetime2 | 0% |
| 8 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCLIENTENRO` | varchar | 0% |
| 11 | `PKCLIZONATPO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]
- `PKCLIZONATPO` (varchar) → [[clave-PKCLIZONATPO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_CLIENTEZONA_OK]]

## Vistas que la consumen (referencia)
- [[dbo.V_CLIENTEZONA_OK]]
