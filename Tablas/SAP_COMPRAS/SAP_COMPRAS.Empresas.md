---
esquema: SAP_COMPRAS
tabla: Empresas
objeto: SAP_COMPRAS.Empresas
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: 1 fila = 1 `CODE` (único en muestra de 163)
n_columnas: 2
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.Empresas

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 2 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CODE` (único en muestra de 163)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CODE` | varchar | 0% |
| 2 | `VALUE` | varchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
