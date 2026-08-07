---
esquema: SIGASC
tabla: H_VM_CONTRATO_CLIENTE
objeto: SIGASC.H_VM_CONTRATO_CLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `CONTRATONRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_VM_CONTRATO_CLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `CONTRATONRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CONTRATONRO` | nvarchar | 0% |
| 3 | `CLIENTENRO` | nvarchar | 0% |
| 4 | `POLITICAID` | nvarchar | 0% |
| 5 | `PRODUCTOID` | nvarchar | 0% |
| 6 | `CONTRATOSTS` | nvarchar | 0% |
| 7 | `PLANCOMERCIALCLIENTEITEM` | int | 72% |
| 8 | `PLANCOMERCIALGESTIONID` | int | 72% |
| 9 | `PLANCOMERCIALCLIENTEID` | int | 72% |
| 10 | `PIPELINERUNID` | nvarchar | 0% |
| 11 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 12 | `hash` | nvarchar | 0% |
| 13 | `NEGOCIOSEGMENTO` | int | 0% |
| 14 | `NEGOCIOSEGMENTOTIPOID` | int | 80% |
| 15 | `row_number` | bigint | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (nvarchar) → [[clave-CONTRATONRO]]
- `CLIENTENRO` (nvarchar) → [[clave-CLIENTENRO]]
- `POLITICAID` (nvarchar) → [[clave-POLITICAID]]
- `PRODUCTOID` (nvarchar) → [[clave-PRODUCTOID]]
- `PLANCOMERCIALGESTIONID` (int) → [[clave-PLANCOMERCIALGESTIONID]]
- `PLANCOMERCIALCLIENTEID` (int) → [[clave-PLANCOMERCIALCLIENTEID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `NEGOCIOSEGMENTOTIPOID` (int) → [[clave-NEGOCIOSEGMENTOTIPOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
