---
esquema: SIGASC
tabla: SERVICIO
objeto: SIGASC.SERVICIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKSERVICIOID` (único en muestra de 200)
n_columnas: 22
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.SERVICIO

> **BASE TABLE** · Dominio: **Core SIGA** · 22 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKSERVICIOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `SERVICIOID` | int | 0% |
| 3 | `SERVICIONOMBRE` | varchar | 0% |
| 4 | `SERVICIOCLASEID` | int | 0% |
| 5 | `SERVICIOFACTURAR` | varchar | 0% |
| 6 | `SERVICIOSTS` | varchar | 0% |
| 7 | `CPTOFACID` | int | 36% |
| 8 | `SERVICIOREQCONTRATO` | int | 0% |
| 9 | `SERVICIOMOTORDID` | int | 28% |
| 10 | `SERVICIOGENORDEN` | varchar | 0% |
| 11 | `SERVICIOSISTEMA` | int | 0% |
| 12 | `SERVICIOULTTARIFA` | int | 0% |
| 13 | `SERVICIOCNTMAX` | int | 0% |
| 14 | `SERVICIOGENINGRESO` | int | 0% |
| 15 | `SERVICIOHABPREVENTA` | int | 0% |
| 16 | `SERVICIOAPROVISIONAR` | varchar | 0% |
| 17 | `SERVICIOGENMASIVO` | int | 100% |
| 18 | `SERVICIOCONTROLFACIMP` | int | 100% |
| 19 | `SERVICIOFORMULARIOHTML` | int | 93% |
| 20 | `SERVICIOFORMULARIO` | varchar | 93% |
| 21 | `PIPELINERUNID` | varchar | 0% |
| 22 | `PKSERVICIOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `SERVICIOID` (int) → [[clave-SERVICIOID]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
