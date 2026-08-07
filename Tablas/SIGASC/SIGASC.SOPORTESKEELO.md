---
esquema: SIGASC
tabla: SOPORTESKEELO
objeto: SIGASC.SOPORTESKEELO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKSOPORTESKEELO` (único en muestra de 200)
n_columnas: 32
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.SOPORTESKEELO

> **BASE TABLE** · Dominio: **Core SIGA** · 32 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKSOPORTESKEELO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKSOPORTESKEELO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPRESANOMBRE` | varchar | 0% |
| 4 | `CLIENTENRO` | int | 0% |
| 5 | `NRO_DOC` | varchar | 0% |
| 6 | `ADMITESKEELO` | varchar | 0% |
| 7 | `CONTRATONRO` | int | 0% |
| 8 | `CLIENTE_STATUS` | varchar | 0% |
| 9 | `PRODUCTOID` | int | 0% |
| 10 | `PRODUCTONOMBRE` | varchar | 0% |
| 11 | `SENALID` | int | 0% |
| 12 | `SENALNOMBRE` | varchar | 0% |
| 13 | `PROMOCION_EN_PPAL` | varchar | 0% |
| 14 | `CLIENTETPOID` | int | 0% |
| 15 | `CLITIPO` | varchar | 0% |
| 16 | `PRODUCTO_TIPO` | varchar | 0% |
| 17 | `SEGMENTOID` | int | 0% |
| 18 | `SEGMENTO` | varchar | 0% |
| 19 | `POLITICAID` | int | 0% |
| 20 | `POLITICA_NOMBRE` | varchar | 0% |
| 21 | `CONTRATO_STATUS` | varchar | 0% |
| 22 | `DEVICE` | varchar | 0% |
| 23 | `FECHA_GENERACION` | datetime2 | 0% |
| 24 | `FECHA_INFORMACION` | datetime2 | 0% |
| 25 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 26 | `CATEGORIA_CLIENTE` | varchar | 0% |
| 27 | `SUB_UNIDAD` | varchar | 0% |
| 28 | `CLIENTESTS` | varchar | 0% |
| 29 | `CONTRATOSTS` | varchar | 0% |
| 30 | `PIPELINERUNID` | varchar | 0% |
| 31 | `PKCLIENTENRO` | varchar | 0% |
| 32 | `PKCONTRATONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `SENALID` (int) → [[clave-SENALID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]
- `PKCONTRATONRO` (varchar) → [[clave-PKCONTRATONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
