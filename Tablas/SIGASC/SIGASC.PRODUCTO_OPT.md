---
esquema: SIGASC
tabla: PRODUCTO_OPT
objeto: SIGASC.PRODUCTO_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PRODUCTOID` (único en muestra de 200)
n_columnas: 33
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTO_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 33 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PRODUCTOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PRODUCTOID` | nvarchar | 0% |
| 3 | `PRODUCTONOMBRE` | nvarchar | 0% |
| 4 | `PRODUCTOTPO` | nvarchar | 0% |
| 5 | `PRODUCTOPPL` | nvarchar | 0% |
| 6 | `PRODUCTOSTS` | nvarchar | 0% |
| 7 | `PRODUCTOPPV` | int | 0% |
| 8 | `PRODUCTOAPROVISIONAR` | nvarchar | 0% |
| 9 | `PRODUCTOCONADICIONAL` | int | 0% |
| 10 | `PRODUCTOPRNFORMULARIO` | nvarchar | 0% |
| 11 | `NEGOCIOID` | nvarchar | 0% |
| 12 | `PRODUCTOINGPREVENTA` | int | 0% |
| 13 | `PRODUCTOHPP` | int | 0% |
| 14 | `PRODUCTONOMPEQ` | nvarchar | 0% |
| 15 | `PRODUCTOCONCAMBIO` | int | 0% |
| 16 | `PRODUCTOCONMUDANZA` | int | 0% |
| 17 | `PRODUCTODETALLE` | nvarchar | 0% |
| 18 | `PRODUCTOCARTELERAID` | int | 0% |
| 19 | `PRODUCTOCARTELERANOMBRE` | nvarchar | 0% |
| 20 | `PRODUCTOCARTELERAACTIVO` | int | 0% |
| 21 | `PRODUCTOCONSUCURSAL` | int | 0% |
| 22 | `PRODUCTOCARTELERAIMAGEN` | int | 0% |
| 23 | `PRODUCTOCONFACTORCONTEO` | int | 0% |
| 24 | `MOROSIDADCRITERIOID` | int | 8% |
| 25 | `PRODUCTOCONMUDANZADSC` | int | 0% |
| 26 | `PRODUCTOCONDERIVADO` | int | 0% |
| 27 | `PRODUCTOCONCAMBIOCANTIDAD` | int | 0% |
| 28 | `PRODUCTOUNICO` | int | 49% |
| 29 | `PRODUCTOPPLID` | int | 78% |
| 30 | `PRODUCTOPRGIMPRESION` | nvarchar | 51% |
| 31 | `FORMID` | int | 62% |
| 32 | `PRODUCTOGENCORTEFISICO` | int | 0% |
| 33 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PRODUCTOID` (nvarchar) → [[clave-PRODUCTOID]]
- `PRODUCTOTPO` (nvarchar) → [[clave-PRODUCTOTPO]]
- `NEGOCIOID` (nvarchar) → [[clave-NEGOCIOID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
