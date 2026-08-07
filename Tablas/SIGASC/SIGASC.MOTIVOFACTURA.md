---
esquema: SIGASC
tabla: MOTIVOFACTURA
objeto: SIGASC.MOTIVOFACTURA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `MOTIVOFACID` (único en muestra de 24)
n_columnas: 5
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MOTIVOFACTURA

> **BASE TABLE** · Dominio: **Core SIGA** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `MOTIVOFACID` (único en muestra de 24)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MOTIVOFACID` | int | 0% |
| 2 | `MOTIVOFACNOMBRE` | varchar | 0% |
| 3 | `MOTIVOFACTPO` | varchar | 0% |
| 4 | `MOTIVOFACSTS` | varchar | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `MOTIVOFACID` (int) → [[clave-MOTIVOFACID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_MOTIVOFACTURA]]
