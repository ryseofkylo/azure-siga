---
esquema: SIGASC
tabla: COBRADOR
objeto: SIGASC.COBRADOR
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCOBRADORID` (único en muestra de 200)
n_columnas: 10
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.COBRADOR

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCOBRADORID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `COBRADORID` | int | 0% |
| 3 | `COBRADORNOMBRE` | varchar | 0% |
| 4 | `COBRADORSTS` | varchar | 0% |
| 5 | `USUARIOID` | int | 0% |
| 6 | `COBRADORASGDIRECTA` | int | 0% |
| 7 | `ENTIDADPAGOELECTRONICOID` | int | 100% |
| 8 | `COBRADORTECNICOID` | int | 100% |
| 9 | `PIPELINERUNID` | varchar | 0% |
| 10 | `PKCOBRADORID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `COBRADORID` (int) → [[clave-COBRADORID]]
- `USUARIOID` (int) → [[clave-USUARIOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCOBRADORID` (varchar) → [[clave-PKCOBRADORID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
