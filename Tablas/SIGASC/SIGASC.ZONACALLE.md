---
esquema: SIGASC
tabla: ZONACALLE
objeto: SIGASC.ZONACALLE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `ZONACALLEGISID` (único en muestra de 200)
n_columnas: 25
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ZONACALLE

> **BASE TABLE** · Dominio: **Core SIGA** · 25 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ZONACALLEGISID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKZONACALLE` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `ZONATPO` | varchar | 0% |
| 4 | `ZONAID` | int | 0% |
| 5 | `CIUDADID` | int | 0% |
| 6 | `GEODIV1ID` | int | 0% |
| 7 | `GEODIV2ID` | int | 0% |
| 8 | `GEOMANID` | int | 0% |
| 9 | `CALLEID` | int | 0% |
| 10 | `GEOMANINI` | varchar | 0% |
| 11 | `ZONAHAB` | int | 0% |
| 12 | `ZONAHABFCH` | datetime2 | 14% |
| 13 | `ZONAHABVTA` | datetime2 | 14% |
| 14 | `ZONACALLEFCHACTUALIZACION` | datetime2 | 0% |
| 15 | `ZONACALLEGISID` | int | 0% |
| 16 | `ZONACALLEESTADO` | varchar | 0% |
| 17 | `PIPELINERUNID` | varchar | 0% |
| 18 | `PKZONATPO` | varchar | 0% |
| 19 | `PKZONAID` | varchar | 0% |
| 20 | `PKCIUDADID` | varchar | 0% |
| 21 | `PKGEODIV1ID` | varchar | 0% |
| 22 | `PKGEODIV2ID` | varchar | 0% |
| 23 | `PKGEOMANID` | varchar | 0% |
| 24 | `PKCALLEID` | varchar | 0% |
| 25 | `PKGEOMANINI` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]
- `GEOMANID` (int) → [[clave-GEOMANID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKZONATPO` (varchar) → [[clave-PKZONATPO]]
- `PKZONAID` (varchar) → [[clave-PKZONAID]]
- `PKCIUDADID` (varchar) → [[clave-PKCIUDADID]]
- `PKGEODIV1ID` (varchar) → [[clave-PKGEODIV1ID]]
- `PKGEODIV2ID` (varchar) → [[clave-PKGEODIV2ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
