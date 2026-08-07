---
esquema: SIGASC
tabla: PLANCOMERCIALCLIENTE
objeto: SIGASC.PLANCOMERCIALCLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPLANCOMERCIALCLIENTEID` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PLANCOMERCIALCLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPLANCOMERCIALCLIENTEID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPLANCOMERCIALCLIENTE` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `PLANCOMERCIALCLIENTEID` | int | 0% |
| 5 | `PLANCOMERCIALID` | int | 0% |
| 6 | `POLITICAPLANID` | int | 0% |
| 7 | `PLANCOMERCIALCLIENTEFCHING` | datetime2 | 0% |
| 8 | `PLANCOMERCIALCLIENTEFCHPRC` | datetime2 | 0% |
| 9 | `PLANCOMERCIALCLIENTEUSR` | varchar | 0% |
| 10 | `PLANCOMERCIALCLIENTESTS` | varchar | 0% |
| 11 | `PLANCOMERCIALCLIENTEGEN` | varchar | 0% |
| 12 | `PIPELINERUNID` | varchar | 0% |
| 13 | `PKCLIENTENRO` | varchar | 0% |
| 14 | `PKPLANCOMERCIALCLIENTEID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PLANCOMERCIALCLIENTEID` (int) → [[clave-PLANCOMERCIALCLIENTEID]]
- `PLANCOMERCIALID` (int) → [[clave-PLANCOMERCIALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
