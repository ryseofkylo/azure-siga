---
esquema: SIGASC
tabla: TAREATIPOLOCALIDAD
objeto: SIGASC.TAREATIPOLOCALIDAD
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKTAREATIPOLOCALIDAD` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.TAREATIPOLOCALIDAD

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKTAREATIPOLOCALIDAD` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKTAREATIPOLOCALIDAD` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `TAREATIPOID` | int | 0% |
| 4 | `CIUDADID` | int | 0% |
| 5 | `GEODIV1ID` | int | 0% |
| 6 | `GEODIV2ID` | int | 0% |
| 7 | `PIPELINERUNID` | varchar | 0% |
| 8 | `PKTAREATIPOID` | varchar | 0% |
| 9 | `PKCIUDADID` | varchar | 0% |
| 10 | `PKGEODIV1ID` | varchar | 0% |
| 11 | `PKGEODIV2ID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TAREATIPOID` (int) → [[clave-TAREATIPOID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKTAREATIPOID` (varchar) → [[clave-PKTAREATIPOID]]
- `PKCIUDADID` (varchar) → [[clave-PKCIUDADID]]
- `PKGEODIV1ID` (varchar) → [[clave-PKGEODIV1ID]]
- `PKGEODIV2ID` (varchar) → [[clave-PKGEODIV2ID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
