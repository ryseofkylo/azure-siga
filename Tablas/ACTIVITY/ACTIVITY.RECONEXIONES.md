---
esquema: ACTIVITY
tabla: RECONEXIONES
objeto: ACTIVITY.RECONEXIONES
tipo_objeto: BASE TABLE
dominio: Actividad y Bajas
canonico: true
grain: 1 fila = 1 `ORDENNRO` (único en muestra de 200)
n_columnas: 45
tags:
  - esquema/ACTIVITY
  - dominio/actividad-y-bajas
  - tipo/tabla-base
  - canonico
---

# ACTIVITY.RECONEXIONES

> **BASE TABLE** · Dominio: **Actividad y Bajas** · 45 columnas · Consultá esta tabla directamente (**tabla-first**).
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
| 20 | `CENTROOPERATIVO` | nvarchar | 0% |
| 21 | `ORDENNRO` | int | 0% |
| 22 | `ORDENTPO` | nvarchar | 0% |
| 23 | `ORDENSTS` | nvarchar | 0% |
| 24 | `ORDENFING` | datetime2 | 0% |
| 25 | `ORDENFFIN` | datetime2 | 0% |
| 26 | `SEGMENTO` | nvarchar | 1% |
| 27 | `SINCARGO` | nvarchar | 0% |
| 28 | `ORDENFPROCESO` | datetime2 | 0% |
| 29 | `FORMAGENERADA` | nvarchar | 0% |
| 30 | `TIENERETENCION` | nvarchar | 0% |
| 31 | `PROMOCIONES` | nvarchar | 44% |
| 32 | `PROMOTORID` | int | 0% |
| 33 | `PROMOTOR` | nvarchar | 0% |
| 34 | `GRUPOPROMOTOR` | nvarchar | 0% |
| 35 | `ULTFECHADESCNEGOCIO` | datetime2 | 0% |
| 36 | `MOTIVO` | nvarchar | 80% |
| 37 | `CATEGORIACLIENTE` | nvarchar | 0% |
| 38 | `CLITIPO` | nvarchar | 0% |
| 39 | `IDPLANCOMERCIAL` | real | 100% |
| 40 | `PLANCOMERCIAL` | nvarchar | 100% |
| 41 | `CODMZN` | nvarchar | 0% |
| 42 | `IDZONA` | real | 12% |
| 43 | `ZONA` | nvarchar | 12% |
| 44 | `MEDIODECOBRO` | nvarchar | 0% |
| 45 | `PIPELINERUNID` | nvarchar | 0% |

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
