---
esquema: SIGASC
tabla: ZONA
objeto: SIGASC.ZONA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKZONAID` (único en muestra de 200)
n_columnas: 15
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ZONA

> **BASE TABLE** · Dominio: **Core SIGA** · 15 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKZONAID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKZONA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `ZONATPO` | varchar | 0% |
| 4 | `ZONAID` | int | 0% |
| 5 | `ZONANOMBRE` | varchar | 0% |
| 6 | `ZONAGRUPO` | varchar | 45% |
| 7 | `ZONANODOID` | varchar | 96% |
| 8 | `ZONAGENERICA` | varchar | 70% |
| 9 | `ZONAFCHACTUALIZACION` | datetime2 | 0% |
| 10 | `ZONAGISID` | int | 0% |
| 11 | `ZONATECNOLOGIA` | varchar | 65% |
| 12 | `ZONASTS` | varchar | 0% |
| 13 | `PIPELINERUNID` | varchar | 0% |
| 14 | `PKZONATPO` | varchar | 0% |
| 15 | `PKZONAID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKZONATPO` (varchar) → [[clave-PKZONATPO]]
- `PKZONAID` (varchar) → [[clave-PKZONAID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
