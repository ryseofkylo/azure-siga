---
esquema: SIGASC
tabla: H_ARTICULOSERIE
objeto: SIGASC.H_ARTICULOSERIE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKARTICULOSERIE` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_ARTICULOSERIE

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKARTICULOSERIE` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKH_ARTICULOSERIE` | nvarchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `ARTICULOSERIE` | nvarchar | 0% |
| 4 | `ARTICULOID` | int | 0% |
| 5 | `ARTICULOSTS` | nvarchar | 0% |
| 6 | `PIPELINERUNID` | nvarchar | 0% |
| 7 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 8 | `hash` | nvarchar | 0% |
| 9 | `PKARTICULOSERIE` | nvarchar | 0% |
| 10 | `PKARTICULOID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ARTICULOID` (int) → [[clave-ARTICULOID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `PKARTICULOSERIE` (nvarchar) → [[clave-PKARTICULOSERIE]]
- `PKARTICULOID` (nvarchar) → [[clave-PKARTICULOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
