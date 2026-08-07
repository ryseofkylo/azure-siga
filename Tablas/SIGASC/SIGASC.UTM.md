---
esquema: SIGASC
tabla: UTM
objeto: SIGASC.UTM
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKUTM_ID` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.UTM

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKUTM_ID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `UTM_ID` | int | 0% |
| 2 | `UTM_GUID` | varchar | 0% |
| 3 | `UTM_EMPRESA` | int | 0% |
| 4 | `UTM_CLIENTE` | int | 0% |
| 5 | `UTM_FCHHORA_INI` | datetime2 | 0% |
| 6 | `UTM_FCHHORA_FIN` | datetime2 | 0% |
| 7 | `UTM_NOMBRE` | varchar | 0% |
| 8 | `UTM_APELLIDO` | varchar | 0% |
| 9 | `UTM_EMAIL` | varchar | 0% |
| 10 | `UTM_SOURCE` | varchar | 0% |
| 11 | `UTM_MEDIUM` | varchar | 0% |
| 12 | `UTM_CAMPAIGN` | varchar | 0% |
| 13 | `UTM_PRODUCTOS` | varchar | 0% |
| 14 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |
| 16 | `PKUTM_ID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
