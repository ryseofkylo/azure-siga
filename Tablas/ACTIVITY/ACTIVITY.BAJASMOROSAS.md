---
esquema: ACTIVITY
tabla: BAJASMOROSAS
objeto: ACTIVITY.BAJASMOROSAS
tipo_objeto: BASE TABLE
dominio: Actividad y Bajas
canonico: true
grain: 1 fila = 1 `CONTRATO` (único en muestra de 200)
n_columnas: 44
tags:
  - esquema/ACTIVITY
  - dominio/actividad-y-bajas
  - tipo/tabla-base
  - canonico
---

# ACTIVITY.BAJASMOROSAS

> **BASE TABLE** · Dominio: **Actividad y Bajas** · 44 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CONTRATO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENRO` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODNOMBRE` | nvarchar | 0% |
| 7 | `TIPOPROD` | nvarchar | 0% |
| 8 | `MOROSIDADMES` | int | 0% |
| 9 | `SUCURSAL` | int | 0% |
| 10 | `CENTROOPERATIVO` | nvarchar | 8% |
| 11 | `SUCURSALNOMBRE` | nvarchar | 0% |
| 12 | `NOMBREDELCLIENTE` | nvarchar | 0% |
| 13 | `MAIL` | nvarchar | 0% |
| 14 | `DEPARTAMENTO` | nvarchar | 0% |
| 15 | `LOCALIDAD` | nvarchar | 0% |
| 16 | `ESTADODELCLIENTE` | nvarchar | 0% |
| 17 | `PRINCIPAL` | nvarchar | 0% |
| 18 | `ESTADODELCONTRATO` | nvarchar | 0% |
| 19 | `TIPODEMOROSIDAD` | nvarchar | 0% |
| 20 | `FECHADEPROCESADA` | datetime2 | 0% |
| 21 | `ESTADODEMOROSIDAD` | nvarchar | 0% |
| 22 | `ULTIMAFECHAPAGO` | datetime2 | 0% |
| 23 | `DEUDA` | real | 12% |
| 24 | `CANTIDADDECUOTAS` | int | 0% |
| 25 | `TELEFONOCLIENTE` | nvarchar | 8% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `MEDIODEREPARTO` | nvarchar | 0% |
| 28 | `SEGMENTO` | nvarchar | 0% |
| 29 | `SINCARGO` | nvarchar | 0% |
| 30 | `PROMOTORGRUPO` | nvarchar | 12% |
| 31 | `NOMBREPROMOCION` | nvarchar | 88% |
| 32 | `ULTIMAFACTURA` | real | 0% |
| 33 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 34 | `CLITIPO` | nvarchar | 0% |
| 35 | `FECHAMOROGENERADA` | datetime2 | 0% |
| 36 | `MOROSIDADFORMAGENERADA` | nvarchar | 0% |
| 37 | `EXISTEOTRA` | nvarchar | 0% |
| 38 | `IDPLANCOMERCIAL` | real | 100% |
| 39 | `PLANCOMERCIAL` | nvarchar | 100% |
| 40 | `QORDENESCANCELADAS` | int | 0% |
| 41 | `CODMZN` | nvarchar | 0% |
| 42 | `IDZONA` | real | 32% |
| 43 | `ZONA` | nvarchar | 32% |
| 44 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATO` (int) → [[clave-CONTRATO]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `SUCURSAL` (int) → [[clave-SUCURSAL]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.v_bajasmorosas]]
