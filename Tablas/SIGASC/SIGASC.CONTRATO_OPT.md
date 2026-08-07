---
esquema: SIGASC
tabla: CONTRATO_OPT
objeto: SIGASC.CONTRATO_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CONTRATONRO` (único en muestra de 200)
n_columnas: 35
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CONTRATO_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 35 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CONTRATONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CONTRATONRO` | nvarchar | 0% |
| 3 | `CLIENTENRO` | nvarchar | 0% |
| 4 | `PRODUCTOID` | nvarchar | 0% |
| 5 | `POLITICAID` | nvarchar | 0% |
| 6 | `CONTRATOFING` | datetime2 | 0% |
| 7 | `CONTRATOFINS` | datetime2 | 6% |
| 8 | `CONTRATOFREF` | datetime2 | 6% |
| 9 | `CONTRATOFREN` | datetime2 | 100% |
| 10 | `CONTRATOFDES` | datetime2 | 59% |
| 11 | `CONTRATOFULT` | datetime2 | 0% |
| 12 | `CONTRATOVINI` | datetime2 | 6% |
| 13 | `CONTRATOVFIN` | datetime2 | 6% |
| 14 | `CONTRATOSTS` | nvarchar | 0% |
| 15 | `CONTRATOUSR` | nvarchar | 0% |
| 16 | `INGRESOID` | int | 0% |
| 17 | `CONTRATOORINRO` | int | 0% |
| 18 | `PROMOTORID` | int | 2% |
| 19 | `CONTRATOPRN` | int | 0% |
| 20 | `CONTRATOCOD` | nvarchar | 0% |
| 21 | `CONTRATOFIRMADO` | int | 0% |
| 22 | `CONTRATOCNT` | int | 0% |
| 23 | `MOTIVOBAJAID` | int | 0% |
| 24 | `CONTRATOHPP` | nvarchar | 0% |
| 25 | `CONTRATOGEN` | nvarchar | 0% |
| 26 | `CONTRATOEXCLUIR` | nvarchar | 0% |
| 27 | `CONTRATORECONEXION` | nvarchar | 32% |
| 28 | `CONTRATOMULT` | nvarchar | 46% |
| 29 | `CONTRATOFCORTE` | datetime2 | 100% |
| 30 | `CONTRATODESHABILITADO` | int | 52% |
| 31 | `PLANCOMERCIALCLIENTEITEM` | int | 74% |
| 32 | `PLANCOMERCIALGESTIONID` | int | 74% |
| 33 | `PLANCOMERCIALCLIENTEID` | int | 74% |
| 34 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 35 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (nvarchar) → [[clave-CONTRATONRO]]
- `CLIENTENRO` (nvarchar) → [[clave-CLIENTENRO]]
- `PRODUCTOID` (nvarchar) → [[clave-PRODUCTOID]]
- `POLITICAID` (nvarchar) → [[clave-POLITICAID]]
- `PROMOTORID` (int) → [[clave-PROMOTORID]]
- `PLANCOMERCIALGESTIONID` (int) → [[clave-PLANCOMERCIALGESTIONID]]
- `PLANCOMERCIALCLIENTEID` (int) → [[clave-PLANCOMERCIALCLIENTEID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
