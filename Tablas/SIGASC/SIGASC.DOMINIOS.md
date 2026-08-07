---
esquema: SIGASC
tabla: DOMINIOS
objeto: SIGASC.DOMINIOS
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `DESCRIPCION`, `DOMINIONOMBRE`, `VALOR`
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.DOMINIOS

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `DESCRIPCION`, `DOMINIONOMBRE`, `VALOR`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `DOMINIONOMBRE` | varchar | 0% |
| 2 | `VALOR` | varchar | 0% |
| 3 | `DESCRIPCION` | varchar | 0% |
| 4 | `TABLA` | varchar | 20% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_RECLAMOS_BDDD]]
