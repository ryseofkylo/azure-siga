---
esquema: VISMA
tabla: Raet_Organigrama
objeto: VISMA.Raet_Organigrama
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (Visma)
canonico: true
grain: 1 fila = 1 `ternro` (único en muestra de 200)
n_columnas: 28
tags:
  - esquema/VISMA
  - dominio/compras-y-finanzas-_visma_
  - tipo/tabla-base
  - canonico
---

# VISMA.Raet_Organigrama

> **BASE TABLE** · Dominio: **Compras y Finanzas (Visma)** · 28 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ternro` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ternro` | int | 0% |
| 2 | `Empleado` | bigint | 0% |
| 3 | `Apellido` | nvarchar | 0% |
| 4 | `Nombre` | nvarchar | 0% |
| 5 | `FechaUltAlta` | datetime2 | 0% |
| 6 | `FechaUltBaja` | datetime2 | 42% |
| 7 | `CUIL` | nvarchar | 0% |
| 8 | `Estado` | nvarchar | 0% |
| 9 | `Empresa` | nvarchar | 0% |
| 10 | `Sucursal` | nvarchar | 0% |
| 11 | `Convenio` | nvarchar | 0% |
| 12 | `Lugar_de_Trabajo` | nvarchar | 0% |
| 13 | `Sector` | nvarchar | 0% |
| 14 | `Sexo` | nvarchar | 0% |
| 15 | `Edad` | bigint | 0% |
| 16 | `Antiguedad` | bigint | 0% |
| 17 | `FechaNac` | datetime2 | 0% |
| 18 | `Tablero_de_Gestion` | nvarchar | 0% |
| 19 | `Contrato` | nvarchar | 0% |
| 20 | `Obra_Social_elegida` | nvarchar | 0% |
| 21 | `Puesto` | nvarchar | 0% |
| 22 | `Categoria` | nvarchar | 0% |
| 23 | `Provincia` | nvarchar | 0% |
| 24 | `REPORTAA` | bigint | 0% |
| 25 | `Sector_ORG` | nvarchar | 0% |
| 26 | `Sub_Sector_ORG` | nvarchar | 0% |
| 27 | `Grupo_Liquidacion` | nvarchar | 0% |
| 28 | `Categ_Recibo` | nvarchar | 10% |

## Claves de join presentes
- `Sucursal` (nvarchar) → [[clave-SUCURSAL]]
- `Contrato` (nvarchar) → [[clave-CONTRATO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
