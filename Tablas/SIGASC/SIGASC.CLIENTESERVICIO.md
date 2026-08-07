---
esquema: SIGASC
tabla: CLIENTESERVICIO
objeto: SIGASC.CLIENTESERVICIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTESRVNRO` (único en muestra de 200)
n_columnas: 57
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTESERVICIO

> **BASE TABLE** · Dominio: **Core SIGA** · 57 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTESRVNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTESRVNRO` | int | 0% |
| 3 | `SERVICIOID` | int | 0% |
| 4 | `CLIENTESRVCONTRATO` | int | 0% |
| 5 | `CLIENTESRVORDEN` | int | 0% |
| 6 | `CLIENTESRVFING` | datetime2 | 0% |
| 7 | `CLIENTESRVHING` | datetime2 | 100% |
| 8 | `CLIENTESRVSTS` | varchar | 0% |
| 9 | `CLIENTESRVUSR` | varchar | 0% |
| 10 | `CLIENTESRVFAGE` | datetime2 | 100% |
| 11 | `CLIENTESRVFACFCH` | datetime2 | 100% |
| 12 | `CLISRVMOTORDID` | int | 0% |
| 13 | `CLIENTENRO` | int | 0% |
| 14 | `CLIENTESRVCANTIDAD` | int | 0% |
| 15 | `SERVICIOTARIFAID` | int | 0% |
| 16 | `CUOTAID` | int | 0% |
| 17 | `CLIENTESRVPRC` | real | 0% |
| 18 | `MONEDAIDSRV` | int | 0% |
| 19 | `CLIENTESRVFACTURA` | varchar | 0% |
| 20 | `CLIENTESRVCALLEID` | int | 0% |
| 21 | `CLIENTESRVPUERTA` | varchar | 0% |
| 22 | `CLIENTESRVAPTO` | varchar | 0% |
| 23 | `CLIENTESRVGEODIV1` | int | 0% |
| 24 | `CLIENTESRVGEODIV2` | int | 0% |
| 25 | `CLIENTESRVGEOMAN` | int | 0% |
| 26 | `CLIENTESRVGEOINI` | varchar | 0% |
| 27 | `CLIENTESRVESQ1` | int | 0% |
| 28 | `CLIENTESRVESQ2` | int | 0% |
| 29 | `CLIENTESRVFACSTS` | varchar | 0% |
| 30 | `CLIENTESRVPRODUCTO` | int | 0% |
| 31 | `CLIENTESRVUBITPO` | varchar | 0% |
| 32 | `CLIENTESRVCALLEUBI` | varchar | 0% |
| 33 | `CLIENTESRVSUCURSALID` | int | 0% |
| 34 | `CLIENTESRVCIUDADID` | int | 0% |
| 35 | `CLIENTESRVCXLUSR` | varchar | 0% |
| 36 | `CLIENTESRVCXLFCH` | datetime2 | 100% |
| 37 | `CLIENTESRVCPA` | varchar | 0% |
| 38 | `CLIENTESRVCP` | varchar | 0% |
| 39 | `CLIENTESRVMANZANA` | varchar | 0% |
| 40 | `CLIENTESRVTORRE` | varchar | 0% |
| 41 | `CLIENTESRVPISO` | varchar | 0% |
| 42 | `CLIENTESRVCASA` | varchar | 0% |
| 43 | `CLIENTESRVOBSERVACION` | varchar | 0% |
| 44 | `CLIENTESRVARTICULOID` | int | 0% |
| 45 | `CLIENTESERVICIOBARRIO` | int | 0% |
| 46 | `CLIENTESRVMEDIOCOBROID` | int | 28% |
| 47 | `CLIENTESRVPROYECTOSAP` | int | 28% |
| 48 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 49 | `CLIENTESRVZONAID` | int | 0% |
| 50 | `CLIENTESRVOLDID` | int | 100% |
| 51 | `CLIENTESRVNAPID` | int | 100% |
| 52 | `CLIENTESRVNAPPUERTOID` | int | 100% |
| 53 | `CLIENTESRVCORDY` | varchar | 100% |
| 54 | `CLIENTESRVCORDX` | varchar | 100% |
| 55 | `CLIENTESERVICIOBTNCORPORATIVO` | int | 0% |
| 56 | `PIPELINERUNID` | varchar | 0% |
| 57 | `PKCLIENTESRVNRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTESRVNRO` (int) → [[clave-CLIENTESRVNRO]]
- `SERVICIOID` (int) → [[clave-SERVICIOID]]
- `CLISRVMOTORDID` (int) → [[clave-CLISRVMOTORDID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `SERVICIOTARIFAID` (int) → [[clave-SERVICIOTARIFAID]]
- `CUOTAID` (int) → [[clave-CUOTAID]]
- `CLIENTESRVCALLEID` (int) → [[clave-CLIENTESRVCALLEID]]
- `CLIENTESRVSUCURSALID` (int) → [[clave-CLIENTESRVSUCURSALID]]
- `CLIENTESRVCIUDADID` (int) → [[clave-CLIENTESRVCIUDADID]]
- `CLIENTESRVARTICULOID` (int) → [[clave-CLIENTESRVARTICULOID]]
- `CLIENTESRVMEDIOCOBROID` (int) → [[clave-CLIENTESRVMEDIOCOBROID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTESRVNRO` (varchar) → [[clave-PKCLIENTESRVNRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
