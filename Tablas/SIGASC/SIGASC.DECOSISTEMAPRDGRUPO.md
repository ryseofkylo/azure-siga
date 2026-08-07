---
esquema: SIGASC
tabla: DECOSISTEMAPRDGRUPO
objeto: SIGASC.DECOSISTEMAPRDGRUPO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `DECOGRUPOCLAVE`, `DECOSISID`, `PIPELINERUNID`
n_columnas: 3
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DECOSISTEMAPRDGRUPO

> **BASE TABLE** · Dominio: **Core SIGA** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `DECOGRUPOCLAVE`, `DECOSISID`, `PIPELINERUNID`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `DECOSISID` | int | 0% |
| 2 | `DECOGRUPOCLAVE` | varchar | 0% |
| 3 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `DECOSISID` (int) → [[clave-DECOSISID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
