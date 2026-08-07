---
esquema: SAP_COMPRAS
tabla: EstrategiaLiberacion
objeto: SAP_COMPRAS.EstrategiaLiberacion
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `FRGXT`, `FRGSX`, `FRGGR`
n_columnas: 3
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.EstrategiaLiberacion

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `FRGXT`, `FRGSX`, `FRGGR`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `FRGGR` | char | 0% |
| 2 | `FRGSX` | char | 0% |
| 3 | `FRGXT` | varchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
