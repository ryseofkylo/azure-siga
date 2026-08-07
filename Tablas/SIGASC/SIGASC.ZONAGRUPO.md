---
esquema: SIGASC
tabla: ZONAGRUPO
objeto: SIGASC.ZONAGRUPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKZONAGRUPO` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ZONAGRUPO

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKZONAGRUPO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKZONAGRUPO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `ZONATPO` | varchar | 0% |
| 4 | `ZONAGRUPO` | varchar | 0% |
| 5 | `ZONAGRUPONOMBRE` | varchar | 0% |
| 6 | `ZONAGRUPOID` | varchar | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |
| 8 | `PKZONATPO` | varchar | 0% |
| 9 | `PKZONAGRUPO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKZONATPO` (varchar) → [[clave-PKZONATPO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
