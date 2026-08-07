---
esquema: SIGASC
tabla: CLIENTETPO
objeto: SIGASC.CLIENTETPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTETPO` (único en muestra de 93)
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTETPO

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTETPO` (único en muestra de 93)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTETPO` | int | 0% |
| 2 | `CLIENTETPONOM` | varchar | 0% |
| 3 | `CLIENTETPOMULTIPLE` | int | 0% |
| 4 | `CLIENTETPOFACTORCONTEO` | real | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `CLIENTETPO` (int) → [[clave-CLIENTETPO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.VM_CLIENTE]] · `CLIENTETPO.CLIENTETPO = VM_CLIENTE.CLIENTETPO` — view_join (PushMTI), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.PushMTI]]
- [[dbo.vProyeccion]]
