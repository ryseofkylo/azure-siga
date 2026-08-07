---
esquema: SIGASC
tabla: ORDENSRV_OPT2
objeto: SIGASC.ORDENSRV_OPT2
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `ORDENNRO` (único en muestra de 200)
n_columnas: 78
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ORDENSRV_OPT2

> **BASE TABLE** · Dominio: **Core SIGA** · 78 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ORDENNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ORDENNRO` | varchar | 0% |
| 3 | `ORDENTPO` | varchar | 0% |
| 4 | `CLIENTENROORD` | int | 0% |
| 5 | `CONTRATONRO` | varchar | 0% |
| 6 | `MOTIVOORDID` | int | 0% |
| 7 | `ORDENSTS` | varchar | 0% |
| 8 | `ORDENFING` | datetime2 | 0% |
| 9 | `ORDENHING` | datetime2 | 100% |
| 10 | `TECNICOID` | int | 45% |
| 11 | `ORDENFFIN` | datetime2 | 45% |
| 12 | `ORDENHFIN` | datetime2 | 100% |
| 13 | `ORDENAGENDAFCH` | datetime2 | 100% |
| 14 | `ORDENUSRING` | varchar | 0% |
| 15 | `ORDENUSR` | varchar | 0% |
| 16 | `ORDENGEN` | varchar | 0% |
| 17 | `ORDENSOL` | varchar | 0% |
| 18 | `ORDENTRBRED` | int | 0% |
| 19 | `ORDCALLEID` | int | 1% |
| 20 | `ORDPUERTA` | varchar | 0% |
| 21 | `ORDAPTO` | varchar | 0% |
| 22 | `ORDGEODIV1` | int | 0% |
| 23 | `ORDGEODIV2` | int | 0% |
| 24 | `ORDGEOMAN` | int | 0% |
| 25 | `ORDGEOINI` | varchar | 0% |
| 26 | `ORDENOBS` | varchar | 0% |
| 27 | `ORDENFPROCESO` | datetime2 | 55% |
| 28 | `ORDENHPROCESO` | datetime2 | 100% |
| 29 | `ORDENARTULTLIN` | int | 0% |
| 30 | `CENTROSTKIDORD` | int | 0% |
| 31 | `ORDENARTCONFIRMADO` | int | 0% |
| 32 | `ORDENARTCNFUSR` | varchar | 0% |
| 33 | `ORDENARTCNFFCH` | datetime2 | 55% |
| 34 | `ORDENAGENDANRO` | int | 0% |
| 35 | `ORDENAGENDATUR` | int | 0% |
| 36 | `ORDENCNXID` | int | 0% |
| 37 | `ORDCALLEUBICACION` | varchar | 0% |
| 38 | `MOTIVOORDORIGENID` | int | 0% |
| 39 | `MOTIVOORDINGID` | int | 16% |
| 40 | `ORDENZONA` | int | 0% |
| 41 | `ORDENENPROCESO` | varchar | 0% |
| 42 | `ORDEDIFICIONRO` | int | 0% |
| 43 | `ORDENFCOM` | datetime2 | 100% |
| 44 | `ORDENHCOM` | datetime2 | 100% |
| 45 | `ORDENFACTUALIZA` | datetime2 | 55% |
| 46 | `ORDENCANTIDAD` | int | 0% |
| 47 | `ORDENUBITPO` | varchar | 0% |
| 48 | `ORDENCONEXIONID` | varchar | 0% |
| 49 | `CENTROOPERATIVOID` | int | 0% |
| 50 | `ORDMANZANA` | varchar | 0% |
| 51 | `ORDTORRE` | varchar | 0% |
| 52 | `ORDPISO` | varchar | 0% |
| 53 | `ORDCASA` | varchar | 0% |
| 54 | `TECNICO2ID` | int | 45% |
| 55 | `ORDCIUDADID` | int | 0% |
| 56 | `TECNICOIDCIERREAUX` | int | 45% |
| 57 | `TECNICOIDCIERRE` | int | 45% |
| 58 | `AFBIENIDCIERRE` | int | 45% |
| 59 | `AFBIENID` | int | 45% |
| 60 | `PRODUCTIVIDADTURNOIDCIERRE` | int | 45% |
| 61 | `PRODUCTIVIDADDIAFCHCIERRE` | datetime2 | 100% |
| 62 | `PRODUCTIVIDADTURNOIDASIGNACION` | int | 45% |
| 63 | `PRODUCTIVIDADDIAFCHASIGNACION` | datetime2 | 100% |
| 64 | `ORDENVISITADA` | varchar | 45% |
| 65 | `ORDENSRVOBSNUM` | int | 0% |
| 66 | `ORDENSRVNAPCIERRE` | int | 45% |
| 67 | `ORDENSRVNAPINGRESO` | int | 45% |
| 68 | `ORDENSRVNAPPUECIE` | int | 45% |
| 69 | `ORDENSRVCLIBARRIO` | int | 45% |
| 70 | `ORDENSRVNAPRX` | float | 45% |
| 71 | `ORDENPROYECTOSAP` | int | 88% |
| 72 | `ORDENSAPCONFIRMADO` | int | 88% |
| 73 | `ORDENTIPOCONEXION` | varchar | 93% |
| 74 | `ORDENFCHCONEXIONFUTURA` | datetime2 | 100% |
| 75 | `ORDENTPOCIERRE` | varchar | 96% |
| 76 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 77 | `ORDENSRVFCHACTUALIZACION` | datetime2 | 100% |
| 78 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ORDENNRO` (varchar) → [[clave-ORDENNRO]]
- `CLIENTENROORD` (int) → [[clave-CLIENTENROORD]]
- `CONTRATONRO` (varchar) → [[clave-CONTRATONRO]]
- `MOTIVOORDID` (int) → [[clave-MOTIVOORDID]]
- `TECNICOID` (int) → [[clave-TECNICOID]]
- `ORDCALLEID` (int) → [[clave-ORDCALLEID]]
- `ORDENAGENDANRO` (int) → [[clave-ORDENAGENDANRO]]
- `ORDENCNXID` (int) → [[clave-ORDENCNXID]]
- `MOTIVOORDORIGENID` (int) → [[clave-MOTIVOORDORIGENID]]
- `MOTIVOORDINGID` (int) → [[clave-MOTIVOORDINGID]]
- `ORDEDIFICIONRO` (int) → [[clave-ORDEDIFICIONRO]]
- `ORDENCONEXIONID` (varchar) → [[clave-ORDENCONEXIONID]]
- `CENTROOPERATIVOID` (int) → [[clave-CENTROOPERATIVOID]]
- `TECNICO2ID` (int) → [[clave-TECNICO2ID]]
- `ORDCIUDADID` (int) → [[clave-ORDCIUDADID]]
- `TECNICOIDCIERRE` (int) → [[clave-TECNICOIDCIERRE]]
- `AFBIENID` (int) → [[clave-AFBIENID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
