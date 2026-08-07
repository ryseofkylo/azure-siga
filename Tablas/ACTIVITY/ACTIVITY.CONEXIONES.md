---
esquema: ACTIVITY
tabla: CONEXIONES
objeto: ACTIVITY.CONEXIONES
tipo_objeto: BASE TABLE
dominio: Actividad y Bajas
canonico: true
grain: 1 fila = 1 `ORDENNRO` (único en muestra de 200)
n_columnas: 44
tags:
  - esquema/ACTIVITY
  - dominio/actividad-y-bajas
  - tipo/tabla-base
  - canonico
---

# ACTIVITY.CONEXIONES

> **BASE TABLE** · Dominio: **Actividad y Bajas** · 44 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ORDENNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENRO` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATONRO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODNOMBRE` | nvarchar | 0% |
| 7 | `TIPOPROD` | nvarchar | 0% |
| 8 | `PRODPRINCIPAL` | nvarchar | 0% |
| 9 | `POLITICAID` | int | 0% |
| 10 | `POLITICONOMBRE` | nvarchar | 0% |
| 11 | `CONTRATOFING` | datetime2 | 0% |
| 12 | `CONTRATOFINS` | datetime2 | 0% |
| 13 | `CONTRATOSTS` | nvarchar | 0% |
| 14 | `CONTRATOCNT` | int | 0% |
| 15 | `CLIENTENOM` | nvarchar | 0% |
| 16 | `CLIENTEAPE` | nvarchar | 0% |
| 17 | `CLIENTEFCHING` | datetime2 | 0% |
| 18 | `CLIENTESTS` | nvarchar | 0% |
| 19 | `SUCURSALID` | int | 0% |
| 20 | `CENTROOPERATIVO` | nvarchar | 2% |
| 21 | `ORDENNRO` | int | 0% |
| 22 | `ORDENTPO` | nvarchar | 0% |
| 23 | `ORDENSTS` | nvarchar | 0% |
| 24 | `ORDENFING` | datetime2 | 0% |
| 25 | `ORDENFFIN` | datetime2 | 0% |
| 26 | `SEGMENTO` | nvarchar | 0% |
| 27 | `SINCARGO` | nvarchar | 0% |
| 28 | `ORDENFPROCESO` | datetime2 | 0% |
| 29 | `FORMAGENERADA` | nvarchar | 0% |
| 30 | `TIENERETENCION` | nvarchar | 0% |
| 31 | `PROMOTORID` | int | 0% |
| 32 | `PROMOCIONES` | nvarchar | 31% |
| 33 | `PROMOTOR` | nvarchar | 0% |
| 34 | `GRUPOPROMOTOR` | nvarchar | 0% |
| 35 | `CLIENTENUEVO` | nvarchar | 0% |
| 36 | `CATEGORIACLIENTE` | nvarchar | 0% |
| 37 | `CLITIPO` | nvarchar | 0% |
| 38 | `IDPLANCOMERCIAL` | real | 100% |
| 39 | `PLANCOMERCIAL` | nvarchar | 100% |
| 40 | `CODMZN` | nvarchar | 0% |
| 41 | `IDZONA` | real | 20% |
| 42 | `ZONA` | nvarchar | 20% |
| 43 | `MEDIODECOBRO` | nvarchar | 0% |
| 44 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `ORDENNRO` (int) → [[clave-ORDENNRO]]
- `PROMOTORID` (int) → [[clave-PROMOTORID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
