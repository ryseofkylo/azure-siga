---
esquema: SIGASC
tabla: H_FACTURA
objeto: SIGASC.H_FACTURA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKFACTURANRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_FACTURA

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKFACTURANRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKH_FACTURA` | nvarchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `FACTURATPO` | nvarchar | 0% |
| 4 | `FACTURANRO` | int | 0% |
| 5 | `FACTURASTS` | nvarchar | 0% |
| 6 | `PIPELINERUNID` | nvarchar | 0% |
| 7 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 8 | `hash` | nvarchar | 0% |
| 9 | `PKFACTURATPO` | nvarchar | 0% |
| 10 | `PKFACTURANRO` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `FACTURATPO` (nvarchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (int) → [[clave-FACTURANRO]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `PKFACTURATPO` (nvarchar) → [[clave-PKFACTURATPO]]
- `PKFACTURANRO` (nvarchar) → [[clave-PKFACTURANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
