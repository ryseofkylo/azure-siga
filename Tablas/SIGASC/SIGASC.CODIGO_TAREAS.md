---
esquema: SIGASC
tabla: CODIGO_TAREAS
objeto: SIGASC.CODIGO_TAREAS
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `CODIGO`, `COEFICIENTE`, `GRUPO`
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CODIGO_TAREAS

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `CODIGO`, `COEFICIENTE`, `GRUPO`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CODIGO` | nvarchar | 1% |
| 2 | `GRUPO` | nvarchar | 1% |
| 3 | `COEFICIENTE` | decimal | 1% |
| 4 | `GRUPO_CLIENTE` | nvarchar | 1% |
| 5 | `DESCRIPCION` | nvarchar | 99% |
| 6 | `FechaCarga` | datetime2 | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
