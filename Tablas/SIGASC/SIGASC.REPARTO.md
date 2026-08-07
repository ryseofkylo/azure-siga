---
esquema: SIGASC
tabla: REPARTO
objeto: SIGASC.REPARTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKREPARTOID` (único en muestra de 157)
n_columnas: 9
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.REPARTO

> **BASE TABLE** · Dominio: **Core SIGA** · 9 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKREPARTOID` (único en muestra de 157)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `REPARTOID` | int | 0% |
| 3 | `REPARTONOMBRE` | varchar | 0% |
| 4 | `REPARTOSTS` | varchar | 0% |
| 5 | `REPARTOCONREVISTA` | int | 0% |
| 6 | `REPARTOCONFACTURAE` | int | 0% |
| 7 | `REPARTOCONFACTURA` | int | 0% |
| 8 | `PIPELINERUNID` | varchar | 0% |
| 9 | `PKREPARTOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.VM_CLIENTE]] · `REPARTO.REPARTOID = VM_CLIENTE.REPARTOCLIID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.VM_CLIENTE]] · `REPARTO.EMPRESAID = VM_CLIENTE.EMPRESAID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_ENCABEZADO_ALL]]
