---
esquema: SIGASC
tabla: PLANCOMERCIAL
objeto: SIGASC.PLANCOMERCIAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPLANCOMERCIALID` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PLANCOMERCIAL

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPLANCOMERCIALID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PLANCOMERCIALID` | int | 0% |
| 3 | `PLANCOMERCIALNOMBRE` | varchar | 0% |
| 4 | `PLANCOMERCIALCARTELERANOMBRE` | varchar | 0% |
| 5 | `NEGOCIOSEGMENTO` | int | 0% |
| 6 | `PLANCOMERCIALMONEDAID` | int | 0% |
| 7 | `PLANCOMERCIALFCHALTA` | datetime2 | 0% |
| 8 | `PLANCOMERCIALFCHBAJA` | datetime2 | 100% |
| 9 | `PLANCOMERCIALCONZONA` | int | 0% |
| 10 | `PLANCOMERCIALCONSUCURSAL` | int | 0% |
| 11 | `PLANCOMERCIALSTS` | varchar | 0% |
| 12 | `PLANCOMERCIALUSR` | varchar | 0% |
| 13 | `PIPELINERUNID` | varchar | 0% |
| 14 | `PKPLANCOMERCIALID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PLANCOMERCIALID` (int) → [[clave-PLANCOMERCIALID]]
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPLANCOMERCIALID` (varchar) → [[clave-PKPLANCOMERCIALID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
