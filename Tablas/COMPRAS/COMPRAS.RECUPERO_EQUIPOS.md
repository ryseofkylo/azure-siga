---
esquema: COMPRAS
tabla: RECUPERO_EQUIPOS
objeto: COMPRAS.RECUPERO_EQUIPOS
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `articulo_serie`, `nro_cliente`, `motivo`
n_columnas: 8
tags:
  - esquema/COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# COMPRAS.RECUPERO_EQUIPOS

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 8 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `articulo_serie`, `nro_cliente`, `motivo`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `id_empresa` | nvarchar | 0% |
| 2 | `nro_cliente` | nvarchar | 2% |
| 3 | `producto_tipo` | nvarchar | 89% |
| 4 | `nombre_articulo` | nvarchar | 89% |
| 5 | `articulo_serie` | nvarchar | 0% |
| 6 | `motivo` | nvarchar | 0% |
| 7 | `periodo` | nvarchar | 0% |
| 8 | `empresa_rec` | nvarchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
