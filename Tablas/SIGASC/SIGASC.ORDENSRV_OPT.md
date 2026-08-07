---
esquema: SIGASC
tabla: ORDENSRV_OPT
objeto: SIGASC.ORDENSRV_OPT
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

# SIGASC.ORDENSRV_OPT

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
| 6 | `MOTIVOORDID` | int | 2% |
| 7 | `ORDENSTS` | varchar | 0% |
| 8 | `ORDENFING` | datetime2 | 0% |
| 9 | `ORDENHING` | datetime2 | 100% |
| 10 | `TECNICOID` | int | 52% |
| 11 | `ORDENFFIN` | datetime2 | 78% |
| 12 | `ORDENHFIN` | datetime2 | 100% |
| 13 | `ORDENAGENDAFCH` | datetime2 | 88% |
| 14 | `ORDENUSRING` | varchar | 0% |
| 15 | `ORDENUSR` | varchar | 0% |
| 16 | `ORDENGEN` | varchar | 0% |
| 17 | `ORDENSOL` | varchar | 0% |
| 18 | `ORDENTRBRED` | int | 0% |
| 19 | `ORDCALLEID` | int | 0% |
| 20 | `ORDPUERTA` | varchar | 0% |
| 21 | `ORDAPTO` | varchar | 0% |
| 22 | `ORDGEODIV1` | int | 0% |
| 23 | `ORDGEODIV2` | int | 0% |
| 24 | `ORDGEOMAN` | int | 0% |
| 25 | `ORDGEOINI` | varchar | 0% |
| 26 | `ORDENOBS` | varchar | 4% |
| 27 | `ORDENFPROCESO` | datetime2 | 2% |
| 28 | `ORDENHPROCESO` | datetime2 | 100% |
| 29 | `ORDENARTULTLIN` | int | 0% |
| 30 | `CENTROSTKIDORD` | int | 0% |
| 31 | `ORDENARTCONFIRMADO` | int | 0% |
| 32 | `ORDENARTCNFUSR` | varchar | 0% |
| 33 | `ORDENARTCNFFCH` | datetime2 | 18% |
| 34 | `ORDENAGENDANRO` | int | 0% |
| 35 | `ORDENAGENDATUR` | int | 0% |
| 36 | `ORDENCNXID` | int | 0% |
| 37 | `ORDCALLEUBICACION` | varchar | 0% |
| 38 | `MOTIVOORDORIGENID` | int | 8% |
| 39 | `MOTIVOORDINGID` | int | 0% |
| 40 | `ORDENZONA` | int | 0% |
| 41 | `ORDENENPROCESO` | varchar | 0% |
| 42 | `ORDEDIFICIONRO` | int | 0% |
| 43 | `ORDENFCOM` | datetime2 | 96% |
| 44 | `ORDENHCOM` | datetime2 | 100% |
| 45 | `ORDENFACTUALIZA` | datetime2 | 4% |
| 46 | `ORDENCANTIDAD` | int | 0% |
| 47 | `ORDENUBITPO` | varchar | 0% |
| 48 | `ORDENCONEXIONID` | varchar | 0% |
| 49 | `CENTROOPERATIVOID` | int | 78% |
| 50 | `ORDMANZANA` | varchar | 78% |
| 51 | `ORDTORRE` | varchar | 78% |
| 52 | `ORDPISO` | varchar | 78% |
| 53 | `ORDCASA` | varchar | 78% |
| 54 | `TECNICO2ID` | int | 84% |
| 55 | `ORDCIUDADID` | int | 0% |
| 56 | `TECNICOIDCIERREAUX` | int | 85% |
| 57 | `TECNICOIDCIERRE` | int | 54% |
| 58 | `AFBIENIDCIERRE` | int | 99% |
| 59 | `AFBIENID` | int | 99% |
| 60 | `PRODUCTIVIDADTURNOIDCIERRE` | int | 99% |
| 61 | `PRODUCTIVIDADDIAFCHCIERRE` | datetime2 | 100% |
| 62 | `PRODUCTIVIDADTURNOIDASIGNACION` | int | 100% |
| 63 | `PRODUCTIVIDADDIAFCHASIGNACION` | datetime2 | 100% |
| 64 | `ORDENVISITADA` | varchar | 99% |
| 65 | `ORDENSRVOBSNUM` | int | 0% |
| 66 | `ORDENSRVNAPCIERRE` | int | 70% |
| 67 | `ORDENSRVNAPINGRESO` | int | 70% |
| 68 | `ORDENSRVNAPPUECIE` | int | 70% |
| 69 | `ORDENSRVCLIBARRIO` | int | 100% |
| 70 | `ORDENSRVNAPRX` | float | 70% |
| 71 | `ORDENPROYECTOSAP` | int | 100% |
| 72 | `ORDENSAPCONFIRMADO` | int | 100% |
| 73 | `ORDENTIPOCONEXION` | varchar | 100% |
| 74 | `ORDENFCHCONEXIONFUTURA` | datetime2 | 100% |
| 75 | `ORDENTPOCIERRE` | varchar | 100% |
| 76 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 77 | `ORDENSRVFCHACTUALIZACION` | datetime2 | 66% |
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
