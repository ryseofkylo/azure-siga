---
esquema: SIGASC
tabla: H_PREVENTACLIENTE
objeto: SIGASC.H_PREVENTACLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKPREVENTANRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_PREVENTACLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKPREVENTANRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PREVENTANRO` | int | 0% |
| 3 | `PREVENTASTS` | nvarchar | 0% |
| 4 | `PIPELINERUNID` | nvarchar | 0% |
| 5 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 6 | `hash` | nvarchar | 0% |
| 7 | `PKPREVENTANRO` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (nvarchar) → [[clave-PKPREVENTANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
