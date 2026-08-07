---
esquema: SAP_COMPRAS
tabla: MaterialesCentro
objeto: SAP_COMPRAS.MaterialesCentro
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `WERKS`, `MATNR`, `EISBE`
n_columnas: 4
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.MaterialesCentro

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `WERKS`, `MATNR`, `EISBE`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MATNR` | nvarchar | 0% |
| 2 | `WERKS` | nvarchar | 0% |
| 3 | `EISBE` | decimal | 0% |
| 4 | `MINBE` | decimal | 0% |

## Claves de join presentes
- `MATNR` (nvarchar) → [[clave-MATNR]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.StockSeguridad]]
