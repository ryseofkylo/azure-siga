---
esquema: SIGASC
tabla: PREVENTAPRODUCTO
objeto: SIGASC.PREVENTAPRODUCTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPREVENTANRO` (único en muestra de 200)
n_columnas: 27
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTAPRODUCTO

> **BASE TABLE** · Dominio: **Core SIGA** · 27 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPREVENTANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPREVENTAPRODUCTO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PREVENTANRO` | int | 0% |
| 4 | `PREVENTAPRODLIN` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `POLITICAID` | int | 0% |
| 7 | `PROMOCIONID` | int | 100% |
| 8 | `PREVENTAPRODSTS` | varchar | 0% |
| 9 | `PREVENTAPRODCONGEN` | int | 0% |
| 10 | `PREVENTAPRODTIENECOND` | int | 0% |
| 11 | `PREVENTAPRODING` | varchar | 0% |
| 12 | `PREVENTAPRODCONORI` | int | 0% |
| 13 | `PREVENTAPRODCONCOD` | varchar | 100% |
| 14 | `PREVENTAPRODCONFIR` | int | 0% |
| 15 | `PREVENTAPRODLINORD` | int | 0% |
| 16 | `PREVENTAPRODLINADI` | int | 0% |
| 17 | `PLANCOMERCIALITEM` | int | 100% |
| 18 | `PREVENTAPRODCANTIDAD` | int | 0% |
| 19 | `PLANCOMERCIALID` | int | 100% |
| 20 | `PLANCOMERCIALPREVENTAITEM` | int | 100% |
| 21 | `PREVENTAGPONNAPPUERTOID` | int | 100% |
| 22 | `PREVENTAGPONNAPID` | int | 100% |
| 23 | `PREVENTAGPONNAPOLDID` | int | 100% |
| 24 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 25 | `PIPELINERUNID` | varchar | 0% |
| 26 | `PKPREVENTANRO` | varchar | 0% |
| 27 | `PKPREVENTAPRODLIN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PROMOCIONID` (int) → [[clave-PROMOCIONID]]
- `PLANCOMERCIALID` (int) → [[clave-PLANCOMERCIALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (varchar) → [[clave-PKPREVENTANRO]]
- `PKPREVENTAPRODLIN` (varchar) → [[clave-PKPREVENTAPRODLIN]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PREVENTACLIENTE]] · `PREVENTAPRODUCTO.EMPRESAID = PREVENTACLIENTE.EMPRESAID` — view_join (V_DIM_PREVENTAS), alta

## Reglas de negocio conocidas

**Derivaciones (CASE)**
- _de_ [[dbo.V_DIM_PREVENTAS]]:
  ```sql
  CASE WHEN ( ( preventaprodcongen IS NULL ) OR ( preventaprodcongen = 0 ) ) THEN CONCAT( p.pkpreventanro, CONCAT( '_', p.clientenropreventa ) ) ELSE CONCAT( p.pkpreventanro, CONCAT( '_', CONCAT( p.clientenropreventa, CONCAT( '_', o.preventaprodcongen ) ) ) ) END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_DIM_PREVENTAS]]
- [[dbo.V_PREVENTAS]]
