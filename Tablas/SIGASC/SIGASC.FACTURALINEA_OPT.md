---
esquema: SIGASC
tabla: FACTURALINEA_OPT
objeto: SIGASC.FACTURALINEA_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PK_FACTURALINEA` (único en muestra de 200)
n_columnas: 21
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURALINEA_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 21 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PK_FACTURALINEA` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PK_FACTURALINEA` | nvarchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `FACTURATPO` | nvarchar | 0% |
| 4 | `FACTURANRO` | nvarchar | 0% |
| 5 | `FACTURALIN` | nvarchar | 0% |
| 6 | `CPTOFACID` | int | 0% |
| 7 | `FACTURAPRJIVA` | real | 0% |
| 8 | `FACTURALINCUO` | nvarchar | 0% |
| 9 | `FACTURALINIMP` | real | 0% |
| 10 | `FACTURALINCOD` | int | 0% |
| 11 | `FACTURAPOL` | int | 0% |
| 12 | `FACTURAPRM` | int | 0% |
| 13 | `FACTURALINTPO` | nvarchar | 0% |
| 14 | `FACTURALINIMPV2` | real | 0% |
| 15 | `FACTURALINIMPV3` | real | 0% |
| 16 | `FACTURALINCNT` | int | 0% |
| 17 | `FACTURAAFIPIVAID` | int | 0% |
| 18 | `FACTURACMB` | int | 100% |
| 19 | `FACTURALINIVAIMP` | real | 0% |
| 20 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 21 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `FACTURATPO` (nvarchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (nvarchar) → [[clave-FACTURANRO]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
