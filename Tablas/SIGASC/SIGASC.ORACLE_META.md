---
esquema: SIGASC
tabla: ORACLE_META
objeto: SIGASC.ORACLE_META
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `column_name`, `table_name`, `ordinal_position`
n_columnas: 6
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ORACLE_META

> **BASE TABLE** · Dominio: **Core SIGA** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `column_name`, `table_name`, `ordinal_position`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `schema_name` | varchar | 0% |
| 2 | `table_name` | varchar | 0% |
| 3 | `column_name` | varchar | 0% |
| 4 | `ordinal_position` | int | 0% |
| 5 | `data_type_canonical` | varchar | 0% |
| 6 | `is_nullable` | varchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
