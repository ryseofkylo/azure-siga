---
esquema: SIGASC
tabla: IVACONDICIONIVA
objeto: SIGASC.IVACONDICIONIVA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `IVAID`, `AFIPIVAID`, `CONDICIONIVA`
n_columnas: 4
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.IVACONDICIONIVA

> **BASE TABLE** · Dominio: **Core SIGA** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `IVAID`, `AFIPIVAID`, `CONDICIONIVA`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `IVAID` | int | 0% |
| 2 | `CONDICIONIVA` | int | 0% |
| 3 | `AFIPIVAID` | int | 0% |
| 4 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `IVAID` (int) → [[clave-IVAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
