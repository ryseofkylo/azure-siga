---
esquema: ACTIVITY
tabla: BAJASVOLUNTARIAS
objeto: ACTIVITY.BAJASVOLUNTARIAS
tipo_objeto: BASE TABLE
dominio: Actividad y Bajas
canonico: true
grain: 1 fila = 1 `CONTRATO` (único en muestra de 200)
n_columnas: 48
tags:
  - esquema/ACTIVITY
  - dominio/actividad-y-bajas
  - tipo/tabla-base
  - canonico
---

# ACTIVITY.BAJASVOLUNTARIAS

> **BASE TABLE** · Dominio: **Actividad y Bajas** · 48 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CONTRATO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTE` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODNOMBRE` | nvarchar | 0% |
| 7 | `PRODUCTOTIPO` | nvarchar | 0% |
| 8 | `SUCURAL` | int | 0% |
| 9 | `CENTROOPERATIVO` | nvarchar | 0% |
| 10 | `SERVICIO` | int | 0% |
| 11 | `FECHAINGRESO` | datetime2 | 0% |
| 12 | `STATUSSERVICIO` | nvarchar | 0% |
| 13 | `MOTIVO` | nvarchar | 0% |
| 14 | `AGENDADA` | datetime2 | 0% |
| 15 | `NOMBRE` | nvarchar | 0% |
| 16 | `STATUSCLIENTE` | nvarchar | 0% |
| 17 | `TELEFONOCLIENTE` | nvarchar | 0% |
| 18 | `ORDEN` | real | 66% |
| 19 | `STATUSORDEN` | nvarchar | 66% |
| 20 | `AGENDAMIENTO` | nvarchar | 66% |
| 21 | `PRINCIPAL` | nvarchar | 0% |
| 22 | `DEUDA` | real | 72% |
| 23 | `CANTIDADDECUOTAS` | int | 0% |
| 24 | `SERVICIONOMBRE` | nvarchar | 0% |
| 25 | `FECHADESCONEXION` | datetime2 | 0% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `DEBITOAUTOMATICO` | nvarchar | 0% |
| 28 | `PROMOTOR` | nvarchar | 6% |
| 29 | `PROMOTORGRUPO` | nvarchar | 6% |
| 30 | `FECHACONEXION` | datetime2 | 0% |
| 31 | `DEPARTAMENTO` | nvarchar | 0% |
| 32 | `LOCALIDAD` | nvarchar | 0% |
| 33 | `SEGMENTO` | nvarchar | 0% |
| 34 | `SINCARGO` | nvarchar | 0% |
| 35 | `ULTPERIODO` | int | 0% |
| 36 | `IMPORTEULTFACTURA` | real | 0% |
| 37 | `ULTPAGO` | datetime2 | 0% |
| 38 | `NOMBREPROMOCION` | nvarchar | 84% |
| 39 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 40 | `USUARIO` | nvarchar | 0% |
| 41 | `CLITIPO` | nvarchar | 0% |
| 42 | `IDPLANCOMERCIAL` | real | 100% |
| 43 | `PLANCOMERCIAL` | nvarchar | 100% |
| 44 | `CODMZN` | nvarchar | 0% |
| 45 | `IDZONA` | real | 5% |
| 46 | `ZONA` | nvarchar | 5% |
| 47 | `CLIENTESRVOBSERVACION` | nvarchar | 0% |
| 48 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `CLIENTE` (int) → [[clave-CLIENTE]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATO` (int) → [[clave-CONTRATO]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.v_bajasvoluntarias]]
