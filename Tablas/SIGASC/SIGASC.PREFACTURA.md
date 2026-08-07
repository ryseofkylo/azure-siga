---
esquema: SIGASC
tabla: PREFACTURA
objeto: SIGASC.PREFACTURA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTE` (único en muestra de 200)
n_columnas: 26
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREFACTURA

> **BASE TABLE** · Dominio: **Core SIGA** · 26 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTE` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTE` | int | 0% |
| 2 | `STS` | varchar | 0% |
| 3 | `CANTIDAD` | int | 0% |
| 4 | `MEDCOBRODSC` | varchar | 0% |
| 5 | `REPARTO` | varchar | 100% |
| 6 | `PRODUCTODSC` | varchar | 0% |
| 7 | `POLITICADSC` | varchar | 0% |
| 8 | `PROMOCIONES` | int | 0% |
| 9 | `MOROSIDAD` | varchar | 100% |
| 10 | `CLASE` | varchar | 100% |
| 11 | `IMPORTE` | real | 0% |
| 12 | `IMPORTEV2` | real | 0% |
| 13 | `IMPORTEV3` | real | 0% |
| 14 | `NADA` | varchar | 100% |
| 15 | `NOMBRE` | varchar | 100% |
| 16 | `CALLE` | varchar | 100% |
| 17 | `PUERTA` | varchar | 0% |
| 18 | `APTO` | varchar | 86% |
| 19 | `UBICACION` | varchar | 100% |
| 20 | `UNIDAD` | int | 0% |
| 21 | `CONDICIONIVA` | varchar | 0% |
| 22 | `CUIT` | varchar | 80% |
| 23 | `CICLO` | varchar | 0% |
| 24 | `IMPSIGA` | real | 17% |
| 25 | `IMPSIGANEW` | real | 84% |
| 26 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `CLIENTE` (int) → [[clave-CLIENTE]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
