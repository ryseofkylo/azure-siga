---
esquema: SIGASC
tabla: H_CONTRATOPROMOCION
objeto: SIGASC.H_CONTRATOPROMOCION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKCONTRATONRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_CONTRATOPROMOCION

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKCONTRATONRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKH_CONTRATOPROMOCION` | nvarchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CONTRATONRO` | int | 0% |
| 4 | `CONTRATOPRMFCH` | datetime2 | 0% |
| 5 | `CONTRATOPRMSTS` | nvarchar | 0% |
| 6 | `PIPELINERUNID` | nvarchar | 0% |
| 7 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 8 | `hash` | nvarchar | 0% |
| 9 | `PKCONTRATONRO` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `PKCONTRATONRO` (nvarchar) → [[clave-PKCONTRATONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
