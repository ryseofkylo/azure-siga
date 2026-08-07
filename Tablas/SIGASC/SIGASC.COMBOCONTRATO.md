---
esquema: SIGASC
tabla: COMBOCONTRATO
objeto: SIGASC.COMBOCONTRATO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCONTRATONRO` (único en muestra de 200)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COMBOCONTRATO

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCONTRATONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCOMBOCONTRATO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `COMBOCLIENTENRO` | int | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `COMBOCONTRATOTPO` | varchar | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKCOMBOCLIENTENRO` | varchar | 0% |
| 8 | `PKCONTRATONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCOMBOCLIENTENRO` (varchar) → [[clave-PKCOMBOCLIENTENRO]]
- `PKCONTRATONRO` (varchar) → [[clave-PKCONTRATONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
