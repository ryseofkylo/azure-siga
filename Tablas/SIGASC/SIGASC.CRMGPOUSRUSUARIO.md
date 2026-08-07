---
esquema: SIGASC
tabla: CRMGPOUSRUSUARIO
objeto: SIGASC.CRMGPOUSRUSUARIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMUSR` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMGPOUSRUSUARIO

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMUSR` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCRMGPOUSRUSUARIO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CRMGPOUSR` | int | 0% |
| 4 | `CRMUSR` | varchar | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKCRMGPOUSR` | varchar | 0% |
| 7 | `PKCRMUSR` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMGPOUSR` (varchar) → [[clave-PKCRMGPOUSR]]
- `PKCRMUSR` (varchar) → [[clave-PKCRMUSR]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
