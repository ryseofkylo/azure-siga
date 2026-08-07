---
esquema: SIGASC
tabla: CENTROSTOCK
objeto: SIGASC.CENTROSTOCK
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCENTROSTKID` (único en muestra de 200)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CENTROSTOCK

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCENTROSTKID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CENTROSTKID` | int | 0% |
| 3 | `CENTROSTKNOMBRE` | varchar | 0% |
| 4 | `CENTROSTKTPO` | varchar | 0% |
| 5 | `CENTROSTKENTREEMPRESAS` | int | 0% |
| 6 | `CENTROSTKCODEXT` | varchar | 100% |
| 7 | `CENTROSTKSTS` | varchar | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKCENTROSTKID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
