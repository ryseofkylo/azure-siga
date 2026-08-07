---
esquema: SIGASC
tabla: CORTE
objeto: SIGASC.CORTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCORTECONTRATONRO` (único en muestra de 200)
n_columnas: 17
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CORTE

> **BASE TABLE** · Dominio: **Core SIGA** · 17 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCORTECONTRATONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCORTE` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `CORTEFECHA` | datetime2 | 0% |
| 5 | `CORTEMODO` | varchar | 0% |
| 6 | `CORTETIPO` | varchar | 0% |
| 7 | `CORTEUSUARIO` | varchar | 0% |
| 8 | `CORTESTS` | varchar | 0% |
| 9 | `CORTEPRCUSUARIO` | varchar | 0% |
| 10 | `CORTEPRCFECHA` | datetime2 | 0% |
| 11 | `CORTECNTERROR` | int | 0% |
| 12 | `CORTECONTRATONRO` | int | 0% |
| 13 | `CORTEDISPOSITIVO` | varchar | 0% |
| 14 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 15 | `PIPELINERUNID` | varchar | 0% |
| 16 | `PKCLIENTENRO` | varchar | 0% |
| 17 | `PKCORTECONTRATONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
