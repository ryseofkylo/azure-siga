---
esquema: SIGASC
tabla: CRMREGISTRONOCLIENTE
objeto: SIGASC.CRMREGISTRONOCLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMNOCLIENTENRO` (único en muestra de 200)
n_columnas: 25
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMREGISTRONOCLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 25 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMNOCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CRMNOCLIENTENRO` | int | 0% |
| 3 | `CRMCLIENTEAPE` | varchar | 0% |
| 4 | `CRMCLIENTENOM` | varchar | 0% |
| 5 | `CRMCLIENTECI` | varchar | 0% |
| 6 | `CRMCLIENTETEL` | varchar | 0% |
| 7 | `CIUDADID` | int | 0% |
| 8 | `CRMCALID` | int | 0% |
| 9 | `CRMCALPUERTA` | varchar | 0% |
| 10 | `CRMCALAPTO` | varchar | 0% |
| 11 | `CRMEMAIL` | varchar | 0% |
| 12 | `CRMNOCLIENTEASIGNADO` | int | 0% |
| 13 | `CRMCONDICIONIVA` | int | 6% |
| 14 | `CRMESEMPRESA` | int | 6% |
| 15 | `CRMCLIENTERUT` | varchar | 6% |
| 16 | `CRMCALPISO` | varchar | 6% |
| 17 | `CRMGEODIV2ID` | int | 6% |
| 18 | `CRMGEODIV1ID` | int | 6% |
| 19 | `CRMMANZANA` | varchar | 6% |
| 20 | `CRMTORRE` | varchar | 6% |
| 21 | `CRMUBICACION` | varchar | 6% |
| 22 | `CRMCLIENTECITPO` | varchar | 6% |
| 23 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 24 | `PIPELINERUNID` | varchar | 0% |
| 25 | `PKCRMNOCLIENTENRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
