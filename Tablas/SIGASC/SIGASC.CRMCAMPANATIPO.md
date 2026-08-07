---
esquema: SIGASC
tabla: CRMCAMPANATIPO
objeto: SIGASC.CRMCAMPANATIPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CRMCAMTPOID` (único en muestra de 4)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMCAMPANATIPO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CRMCAMTPOID` (único en muestra de 4)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CRMCAMTPOID` | int | 0% |
| 2 | `CRMCAMTPONOM` | varchar | 0% |
| 3 | `CRMCAMTPOFACTURA` | int | 0% |
| 4 | `CRMCAMTPOCLIENTE` | varchar | 0% |
| 5 | `CRMCAMTPOSMS` | int | 0% |
| 6 | `CRMCAMTPOAVISO` | int | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
