---
esquema: VISMA
tabla: RAET_Horas
objeto: VISMA.RAET_Horas
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (Visma)
canonico: true
grain: 1 fila = 1 `Id` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/VISMA
  - dominio/compras-y-finanzas-_visma_
  - tipo/tabla-base
  - canonico
---

# VISMA.RAET_Horas

> **BASE TABLE** · Dominio: **Compras y Finanzas (Visma)** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Id` | bigint | 0% |
| 2 | `Ternro` | int | 0% |
| 3 | `Empleado` | bigint | 0% |
| 4 | `Apellido` | nvarchar | 0% |
| 5 | `Nombre` | nvarchar | 0% |
| 6 | `Hctipohoradesc` | nvarchar | 0% |
| 7 | `Fecha` | datetime2 | 0% |
| 8 | `Empresa` | nvarchar | 0% |
| 9 | `Sucursal` | nvarchar | 0% |
| 10 | `Convenio` | nvarchar | 0% |
| 11 | `LugarDeTrabajo` | nvarchar | 0% |
| 12 | `Sector` | nvarchar | 0% |
| 13 | `Puesto` | nvarchar | 0% |
| 14 | `total_horas` | decimal | 0% |

## Claves de join presentes
- `Id` (bigint) → [[clave-ID]]
- `Sucursal` (nvarchar) → [[clave-SUCURSAL]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
