---
esquema: SIGASC
tabla: CLIENTEPROMOCIONGRL
objeto: SIGASC.CLIENTEPROMOCIONGRL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTEPROMOCIONGRL

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCLIENTEPROMOCIONGRL` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `PROMOCIONGRLID` | int | 0% |
| 5 | `CLIENTEPRMGRLFCH` | datetime2 | 0% |
| 6 | `CLIENTEPRMGRLUSR` | varchar | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |
| 8 | `PKCLIENTENRO` | varchar | 0% |
| 9 | `PKPROMOCIONGRLID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]
- `PKPROMOCIONGRLID` (varchar) → [[clave-PKPROMOCIONGRLID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
