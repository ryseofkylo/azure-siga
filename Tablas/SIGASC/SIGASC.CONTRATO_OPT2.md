---
esquema: SIGASC
tabla: CONTRATO_OPT2
objeto: SIGASC.CONTRATO_OPT2
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTENRO` (único en muestra de 200)
n_columnas: 35
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CONTRATO_OPT2

> **BASE TABLE** · Dominio: **Core SIGA** · 35 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CONTRATONRO` | nvarchar | 0% |
| 3 | `CLIENTENRO` | nvarchar | 0% |
| 4 | `PRODUCTOID` | nvarchar | 0% |
| 5 | `POLITICAID` | nvarchar | 0% |
| 6 | `CONTRATOFING` | datetime2 | 0% |
| 7 | `CONTRATOFINS` | datetime2 | 0% |
| 8 | `CONTRATOFREF` | datetime2 | 0% |
| 9 | `CONTRATOFREN` | datetime2 | 100% |
| 10 | `CONTRATOFDES` | datetime2 | 100% |
| 11 | `CONTRATOFULT` | datetime2 | 0% |
| 12 | `CONTRATOVINI` | datetime2 | 0% |
| 13 | `CONTRATOVFIN` | datetime2 | 0% |
| 14 | `CONTRATOSTS` | nvarchar | 0% |
| 15 | `CONTRATOUSR` | nvarchar | 0% |
| 16 | `INGRESOID` | int | 0% |
| 17 | `CONTRATOORINRO` | int | 0% |
| 18 | `PROMOTORID` | int | 0% |
| 19 | `CONTRATOPRN` | int | 0% |
| 20 | `CONTRATOCOD` | nvarchar | 0% |
| 21 | `CONTRATOFIRMADO` | int | 0% |
| 22 | `CONTRATOCNT` | int | 0% |
| 23 | `MOTIVOBAJAID` | int | 0% |
| 24 | `CONTRATOHPP` | nvarchar | 0% |
| 25 | `CONTRATOGEN` | nvarchar | 0% |
| 26 | `CONTRATOEXCLUIR` | nvarchar | 0% |
| 27 | `CONTRATORECONEXION` | nvarchar | 0% |
| 28 | `CONTRATOMULT` | nvarchar | 100% |
| 29 | `CONTRATOFCORTE` | datetime2 | 100% |
| 30 | `CONTRATODESHABILITADO` | int | 100% |
| 31 | `PLANCOMERCIALCLIENTEITEM` | int | 100% |
| 32 | `PLANCOMERCIALGESTIONID` | int | 100% |
| 33 | `PLANCOMERCIALCLIENTEID` | int | 100% |
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
