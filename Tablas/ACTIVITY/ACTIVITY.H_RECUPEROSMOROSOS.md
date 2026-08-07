---
esquema: ACTIVITY
tabla: H_RECUPEROSMOROSOS
objeto: ACTIVITY.H_RECUPEROSMOROSOS
tipo_objeto: BASE TABLE
dominio: Actividad y Bajas
canonico: true
grain: 1 fila = 1 versión de `CLIENTENRO` por `FECHADEPROCESADA` — histórica/versionada (inferido de muestra)
n_columnas: 40
tags:
  - esquema/ACTIVITY
  - dominio/actividad-y-bajas
  - tipo/tabla-base
  - canonico
---

# ACTIVITY.H_RECUPEROSMOROSOS

> **BASE TABLE** · Dominio: **Actividad y Bajas** · 40 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `CLIENTENRO` por `FECHADEPROCESADA` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENRO` | int | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `EMPNOMBRE` | nvarchar | 0% |
| 4 | `CONTRATO` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `PRODNOMBRE` | nvarchar | 0% |
| 7 | `PRODUCTOTIPO` | nvarchar | 0% |
| 8 | `MOROSIDADMES` | int | 0% |
| 9 | `SUCURSAL` | int | 0% |
| 10 | `CENTROOPERATIVO` | nvarchar | 0% |
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
| 23 | `DEUDA` | real | 18% |
| 24 | `CANTIDADDECUOTAS` | int | 0% |
| 25 | `TELEFONOCLIENTE` | nvarchar | 0% |
| 26 | `MEDIODECOBRO` | nvarchar | 0% |
| 27 | `MEDIODEREPARTO` | nvarchar | 0% |
| 28 | `SEGMENTO` | nvarchar | 0% |
| 29 | `SINCARGO` | nvarchar | 0% |
| 30 | `PROMOTORGRUPO` | nvarchar | 4% |
| 31 | `NOMBREPROMOCION` | nvarchar | 54% |
| 32 | `USUARIOPROMOCION` | nvarchar | 54% |
| 33 | `CATEGORIADECLIENTE` | nvarchar | 0% |
| 34 | `CLITIPO` | nvarchar | 0% |
| 35 | `IDPLANCOMERCIAL` | real | 99% |
| 36 | `PLANCOMERCIAL` | nvarchar | 90% |
| 37 | `CODMZN` | nvarchar | 0% |
| 38 | `IDZONA` | real | 7% |
| 39 | `ZONA` | nvarchar | 6% |
| 40 | `PIPELINERUNID` | nvarchar | 0% |

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
- [[dbo.v_recuperosmorosos]]
