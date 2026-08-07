---
esquema: SIGASC
tabla: SENAL
objeto: SIGASC.SENAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SENALID` (único en muestra de 198)
n_columnas: 8
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.SENAL

> **BASE TABLE** · Dominio: **Core SIGA** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SENALID` (único en muestra de 198)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SENALID` | int | 0% |
| 2 | `SENALNOMBRE` | varchar | 0% |
| 3 | `SENALIMAGEN` | varbinary |  |
| 4 | `SENALIMAGENEXTENSION` | varchar | 0% |
| 5 | `SENALCODIGO` | varchar | 0% |
| 6 | `SENALIMAGENNOMBRE` | varchar | 0% |
| 7 | `SENALPPV` | int | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `SENALID` (int) → [[clave-SENALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PRODUCTOSENAL]] · `SENAL.SENALID = PRODUCTOSENAL.SENALID` — view_join (vSENAL_PROYECCION), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_PRODUCTOSENAL]]
- [[dbo.vSENAL_PROYECCION]]
