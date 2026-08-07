---
esquema: SAP_COMPRAS
tabla: Precio
objeto: SAP_COMPRAS.Precio
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `WERKS`, `MATNR`, `VERPR`
n_columnas: 7
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.Precio

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `WERKS`, `MATNR`, `VERPR`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MATNR` | varchar | 0% |
| 2 | `WERKS` | char | 0% |
| 3 | `BWTAR` | varchar | 49% |
| 4 | `SOBKZ` | char | 100% |
| 5 | `PSPNR` | varchar | 100% |
| 6 | `VERPR` | decimal | 0% |
| 7 | `STPRS` | decimal | 0% |

## Claves de join presentes
- `MATNR` (varchar) → [[clave-MATNR]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[SAP_COMPRAS.vw_Movimientos_QLIK]]

## Vistas que la consumen (referencia)
- [[SAP_COMPRAS.vw_Movimientos_QLIK]]
- [[dbo.Precios_Almacen]]
