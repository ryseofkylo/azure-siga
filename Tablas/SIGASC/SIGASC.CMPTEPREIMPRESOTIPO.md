---
esquema: SIGASC
tabla: CMPTEPREIMPRESOTIPO
objeto: SIGASC.CMPTEPREIMPRESOTIPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCMPTEPREIMPRESOTIPOID` (único en muestra de 44)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMPTEPREIMPRESOTIPO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCMPTEPREIMPRESOTIPOID` (único en muestra de 44)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CMPTEPREIMPRESOTIPOID` | int | 0% |
| 3 | `CMPTEPREIMPRESOTIPONOMBRE` | varchar | 0% |
| 4 | `CMPTEPREIMPRESOTIPOSTS` | varchar | 0% |
| 5 | `CMPTEPREIMPRESOLIMITE` | int | 0% |
| 6 | `PIPELINERUNID` | varchar | 0% |
| 7 | `PKCMPTEPREIMPRESOTIPOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
