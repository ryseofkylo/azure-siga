---
esquema: SIGASC
tabla: CONDICIONIVA
objeto: SIGASC.CONDICIONIVA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CONDICIONIVARECEPTORID` (único en muestra de 5)
n_columnas: 11
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CONDICIONIVA

> **BASE TABLE** · Dominio: **Core SIGA** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CONDICIONIVARECEPTORID` (único en muestra de 5)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CONDICIONIVA` | int | 0% |
| 2 | `CONDICIONIVANOMBRE` | varchar | 0% |
| 3 | `CONDICIONIVALETRA` | varchar | 0% |
| 4 | `CONDICIONIVAREQRUT` | int | 0% |
| 5 | `CONDICIONIVALEYENDA` | varchar | 80% |
| 6 | `CONDICIONIVAIMPRIMELEYENDA` | int | 80% |
| 7 | `CONDICIONIVACLASE` | varchar | 100% |
| 8 | `CONDICIONIVARECEPTORID` | int | 0% |
| 9 | `CONDICIONIVASTS` | varchar | 0% |
| 10 | `CONDICIONIVAADMITESKEELO` | int | 0% |
| 11 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
