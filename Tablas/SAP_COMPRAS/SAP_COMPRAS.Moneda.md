---
esquema: SAP_COMPRAS
tabla: Moneda
objeto: SAP_COMPRAS.Moneda
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `GDATU`, `UKURS`, `FCURR`
n_columnas: 4
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.Moneda

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 4 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `GDATU`, `UKURS`, `FCURR`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `FCURR` | nvarchar | 0% |
| 2 | `TCURR` | nvarchar | 0% |
| 3 | `GDATU` | nvarchar | 0% |
| 4 | `UKURS` | decimal | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.CotizacionControlInv]], [[dbo.Cotizaciones_Almacen]]

## Vistas que la consumen (referencia)
- [[SAP_COMPRAS.vw_Cotizaciones]]
- [[dbo.CotizacionControlInv]]
- [[dbo.Cotizaciones_Almacen]]
