---
esquema: MAPPING
tabla: CODIGOSAREAS
objeto: MAPPING.CODIGOSAREAS
tipo_objeto: BASE TABLE
dominio: Mapping
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `LOCALIDAD`, `CODIGOAREA`, `PROVINCIA`
n_columnas: 3
tags:
  - esquema/MAPPING
  - dominio/mapping
  - tipo/tabla-base
  - canonico
---

# MAPPING.CODIGOSAREAS

> **BASE TABLE** · Dominio: **Mapping** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `LOCALIDAD`, `CODIGOAREA`, `PROVINCIA`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CODIGOAREA` | int | 0% |
| 2 | `PROVINCIA` | varchar | 0% |
| 3 | `LOCALIDAD` | varchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
