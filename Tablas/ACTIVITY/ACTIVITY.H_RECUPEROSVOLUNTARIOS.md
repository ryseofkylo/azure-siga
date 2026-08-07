---
esquema: ACTIVITY
tabla: H_RECUPEROSVOLUNTARIOS
objeto: ACTIVITY.H_RECUPEROSVOLUNTARIOS
tipo_objeto: BASE TABLE
dominio: Actividad y Bajas
canonico: true
grain: 1 fila = 1 versión de `CONTRATONRO` por `FECHAFINALIZACION` — histórica/versionada (inferido de muestra)
n_columnas: 29
tags:
  - esquema/ACTIVITY
  - dominio/actividad-y-bajas
  - tipo/tabla-base
  - canonico
---

# ACTIVITY.H_RECUPEROSVOLUNTARIOS

> **BASE TABLE** · Dominio: **Actividad y Bajas** · 29 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `CONTRATONRO` por `FECHAFINALIZACION` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENRO` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODUCTO` | nvarchar | 0% |
| 7 | `TIPOPROD` | nvarchar | 0% |
| 8 | `SUCURSALID` | int | 0% |
| 9 | `CENTROOPERATIVO` | nvarchar | 0% |
| 10 | `NOMBRE` | nvarchar | 0% |
| 11 | `MEDIODECOBRO` | nvarchar | 0% |
| 12 | `CLIENTETST` | nvarchar | 0% |
| 13 | `TELEFONO` | nvarchar | 0% |
| 14 | `DEPARTAMENTO` | nvarchar | 0% |
| 15 | `LOCALIDAD` | nvarchar | 0% |
| 16 | `PRINCIPAL` | nvarchar | 0% |
| 17 | `CONTRATOSTS` | nvarchar | 0% |
| 18 | `FECHAFINALIZACION` | datetime2 | 0% |
| 19 | `SEGMENTO` | nvarchar | 0% |
| 20 | `SINCARGO` | nvarchar | 0% |
| 21 | `PROMOCIONES` | nvarchar | 60% |
| 22 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 23 | `CLIENTETIPO` | nvarchar | 0% |
| 24 | `IDPLANCOMERCIAL` | real | 98% |
| 25 | `PLANCOMERCIAL` | nvarchar | 86% |
| 26 | `CODMZN` | nvarchar | 0% |
| 27 | `IDZONA` | real | 12% |
| 28 | `ZONA` | nvarchar | 12% |
| 29 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.v_recuperosvoluntarios]]
