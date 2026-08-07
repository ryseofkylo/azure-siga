---
esquema: SAP_COMPRAS
tabla: CondicionPago
objeto: SAP_COMPRAS.CondicionPago
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: 1 fila = 1 `ZTERM` (único en muestra de 129)
n_columnas: 18
tags:
  - esquema/SAP_COMPRAS
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP_COMPRAS.CondicionPago

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 18 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ZTERM` (único en muestra de 129)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ZTERM` | varchar | 0% |
| 2 | `ZTAGG` | varchar | 0% |
| 3 | `ZDART` | char | 1% |
| 4 | `ZFAEL` | varchar | 0% |
| 5 | `ZMONA` | varchar | 0% |
| 6 | `ZTAG1` | varchar | 0% |
| 7 | `ZPRZ1` | decimal | 0% |
| 8 | `ZTAG2` | varchar | 0% |
| 9 | `ZPRZ2` | decimal | 0% |
| 10 | `ZTAG3` | varchar | 0% |
| 11 | `ZSTG1` | varchar | 0% |
| 12 | `ZSMN1` | varchar | 0% |
| 13 | `ZSCHF` | varchar | 47% |
| 14 | `ZLSCH` | varchar | 98% |
| 15 | `XCHPM` | char | 99% |
| 16 | `KOART` | char | 12% |
| 17 | `XSPLT` | varchar | 37% |
| 18 | `TEXT1` | varchar | 3% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
