---
esquema: dbo
tabla: H_VM_CLIENTE_NUEVA
objeto: dbo.H_VM_CLIENTE_NUEVA
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 versión de `CLIENTENRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 19
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.H_VM_CLIENTE_NUEVA

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 19 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `CLIENTENRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | nvarchar | 0% |
| 3 | `CLIENTESTS` | nvarchar | 0% |
| 4 | `CLIENTENATURALEZAID` | int | 60% |
| 5 | `MEDCOBROID` | int | 0% |
| 6 | `CICLOID` | int | 0% |
| 7 | `NEGOCIOSEGMENTOTIPOID` | int | 74% |
| 8 | `NEGOCIOSEGMENTO` | int | 0% |
| 9 | `CLIENTETPO` | int | 0% |
| 10 | `CLICALID` | int | 0% |
| 11 | `GEOMANID` | int | 0% |
| 12 | `GEODIV1ID` | int | 0% |
| 13 | `GEODIV2ID` | int | 0% |
| 14 | `GEOMANINI` | nvarchar | 1% |
| 15 | `CLIENTECORDX` | nvarchar | 0% |
| 16 | `CLIENTECORDY` | nvarchar | 0% |
| 17 | `PIPELINERUNID` | nvarchar | 0% |
| 18 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 19 | `hash` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (nvarchar) → [[clave-CLIENTENRO]]
- `CLIENTENATURALEZAID` (int) → [[clave-CLIENTENATURALEZAID]]
- `MEDCOBROID` (int) → [[clave-MEDCOBROID]]
- `CICLOID` (int) → [[clave-CICLOID]]
- `NEGOCIOSEGMENTOTIPOID` (int) → [[clave-NEGOCIOSEGMENTOTIPOID]]
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `CLIENTETPO` (int) → [[clave-CLIENTETPO]]
- `CLICALID` (int) → [[clave-CLICALID]]
- `GEOMANID` (int) → [[clave-GEOMANID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
