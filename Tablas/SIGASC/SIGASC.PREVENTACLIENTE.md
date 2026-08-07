---
esquema: SIGASC
tabla: PREVENTACLIENTE
objeto: SIGASC.PREVENTACLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPREVENTANRO` (único en muestra de 200)
n_columnas: 109
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PREVENTACLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 109 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPREVENTANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PREVENTANRO` | int | 0% |
| 3 | `CIUDADID` | int | 0% |
| 4 | `PREVENTATPO` | varchar | 0% |
| 5 | `CLIENTENROPREVENTA` | int | 1% |
| 6 | `PREVENTANOM` | varchar | 0% |
| 7 | `PREVENTAAPE` | varchar | 0% |
| 8 | `PREVENTATEL` | varchar | 0% |
| 9 | `PREVENTATELTPO` | varchar | 0% |
| 10 | `PREVENTATEL2` | varchar | 48% |
| 11 | `PREVENTATELTPO2` | varchar | 0% |
| 12 | `PREVENTACI` | varchar | 0% |
| 13 | `PREVENTAEMAIL` | varchar | 26% |
| 14 | `PREVENTARUT` | varchar | 100% |
| 15 | `PREVENTACALID` | int | 0% |
| 16 | `PREVENTACALPUERTA` | varchar | 0% |
| 17 | `PREVENTACALAPTO` | varchar | 82% |
| 18 | `PREVENTACALUBICACION` | varchar | 36% |
| 19 | `PREVENTAGEODIV1` | int | 0% |
| 20 | `PREVENTAGEODIV2` | int | 0% |
| 21 | `PREVENTAGEOMAN` | int | 0% |
| 22 | `PREVENTAFCHING` | datetime2 | 0% |
| 23 | `PREVENTASTS` | varchar | 0% |
| 24 | `PREVENTAUSR` | varchar | 0% |
| 25 | `PROMOTORID` | int | 0% |
| 26 | `PREVENTAULTLIN` | int | 0% |
| 27 | `PREVENTAULTLINSRV` | int | 0% |
| 28 | `PREVENTACOBCAL` | int | 0% |
| 29 | `PREVENTACOBCALPUERTA` | varchar | 0% |
| 30 | `PREVENTACOBCALAPTO` | varchar | 82% |
| 31 | `PREVENTACOBCALUBI` | varchar | 36% |
| 32 | `PREVENTACOBGEODIV1` | int | 0% |
| 33 | `PREVENTACOBGEODIV2` | int | 0% |
| 34 | `PREVENTACOBGEOMAN` | int | 0% |
| 35 | `PREVENTALEGCALNOM` | varchar | 100% |
| 36 | `PREVENTAOBS` | varchar | 80% |
| 37 | `PREVENTAGRUPOID` | int | 0% |
| 38 | `PREVENTACITPO` | varchar | 0% |
| 39 | `PREVENTACONPRE` | datetime2 | 100% |
| 40 | `PREVENTALEGNOM` | varchar | 100% |
| 41 | `PREVENTALEGTEL` | varchar | 100% |
| 42 | `PREVENTAMEDCOBROID` | int | 0% |
| 43 | `PREVENTADEBNRO` | varchar | 7% |
| 44 | `PREVENTADEBCI` | varchar | 10% |
| 45 | `PREVENTADEBVTO` | datetime2 | 94% |
| 46 | `PREVENTAESQUINA1ID` | int | 50% |
| 47 | `PREVENTAESQUINA2ID` | int | 71% |
| 48 | `PREVENTAGEOMANINI` | varchar | 2% |
| 49 | `PREVENTACOBGEOMANINI` | varchar | 42% |
| 50 | `PREVENTAFCHFIN` | datetime2 | 0% |
| 51 | `PREVENTAFCHENV` | datetime2 | 100% |
| 52 | `SUCURSALID` | int | 0% |
| 53 | `PREVENTACP` | varchar | 0% |
| 54 | `CONDICIONIVA` | int | 0% |
| 55 | `PREVENTADEBTITULAR` | varchar | 18% |
| 56 | `PREVENTADEBBANCO` | int | 18% |
| 57 | `PREVENTAPROPIEDAD` | varchar | 0% |
| 58 | `PREVENTAVINCULOTPO` | varchar | 0% |
| 59 | `PREVENTAVINCULOPADRE` | int | 0% |
| 60 | `PREVENTAVINCULOFACTURA` | varchar | 0% |
| 61 | `PREVENTAIMPUESTO` | int | 0% |
| 62 | `PREVENTACLIENTEUBITPO` | varchar | 0% |
| 63 | `PREVENTACOBCP` | varchar | 0% |
| 64 | `PREVENTACOBMANZANA` | varchar | 80% |
| 65 | `PREVENTACOBCASA` | varchar | 76% |
| 66 | `PREVENTACOBTORRE` | varchar | 97% |
| 67 | `PREVENTACOBPISO` | varchar | 94% |
| 68 | `PREVENTACALMANZANA` | varchar | 80% |
| 69 | `PREVENTACALCASA` | varchar | 75% |
| 70 | `PREVENTACALTORRE` | varchar | 97% |
| 71 | `PREVENTACALPISO` | varchar | 94% |
| 72 | `PREVENTAFCHNAC` | datetime2 | 94% |
| 73 | `PREVENTACBU` | varchar | 13% |
| 74 | `PREVENTACOBBARRIO` | int | 86% |
| 75 | `PREVENTACALBARRIO` | int | 80% |
| 76 | `CLIENTETPO` | int | 0% |
| 77 | `NEGOCIOSEGMENTO` | int | 0% |
| 78 | `PREVENTASEXO` | varchar | 0% |
| 79 | `PREVENTACOBCIUDAD` | int | 0% |
| 80 | `PREVENTAMODIFICAR` | int | 42% |
| 81 | `PREVENTAREPARTOCLIID` | int | 0% |
| 82 | `PREVENTAESEMPRESA` | int | 6% |
| 83 | `NEGOCIOSEGMENTOTIPOID` | int | 7% |
| 84 | `PREVENTAAGENTECOMPRA` | varchar | 100% |
| 85 | `PREVENTAPROVCABLE` | varchar | 100% |
| 86 | `PREVENTAPROVINTERNET` | varchar | 100% |
| 87 | `PREVENTACABLEPACK` | varchar | 100% |
| 88 | `PREVENTACONTACTADO` | varchar | 100% |
| 89 | `PREVENTANIVELINTENCION` | varchar | 100% |
| 90 | `PREVENTANROFULCRUM` | varchar | 100% |
| 91 | `PREVENTACORDY` | varchar | 74% |
| 92 | `PREVENTACORDX` | varchar | 74% |
| 93 | `PREVENTAPROYECTOSAP` | int | 100% |
| 94 | `PREVENTAFCHCONEXIONFUTURA` | datetime2 | 100% |
| 95 | `PREVENTATIPOCONEXION` | varchar | 7% |
| 96 | `PREVENTAAPP` | int | 100% |
| 97 | `PREVENTATELPERS2` | varchar | 8% |
| 98 | `PREVENTATELCONT2` | varchar | 100% |
| 99 | `PREVENTATELWHATSAPP2` | int | 0% |
| 100 | `PREVENTATELCARACT2` | int | 50% |
| 101 | `PREVENTATELPERS` | varchar | 8% |
| 102 | `PREVENTATELCONT` | varchar | 100% |
| 103 | `PREVENTATELWHATSAPP` | int | 0% |
| 104 | `PREVENTATELCARACT` | int | 8% |
| 105 | `PREVENTACLANDESTINOTIPOID` | int | 8% |
| 106 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 107 | `PREVENTABTNCOPORATIVO` | int | 0% |
| 108 | `PIPELINERUNID` | varchar | 0% |
| 109 | `PKPREVENTANRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PREVENTANRO` (int) → [[clave-PREVENTANRO]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `CLIENTENROPREVENTA` (int) → [[clave-CLIENTENROPREVENTA]]
- `PROMOTORID` (int) → [[clave-PROMOTORID]]
- `PREVENTAMEDCOBROID` (int) → [[clave-PREVENTAMEDCOBROID]]
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `CLIENTETPO` (int) → [[clave-CLIENTETPO]]
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `NEGOCIOSEGMENTOTIPOID` (int) → [[clave-NEGOCIOSEGMENTOTIPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPREVENTANRO` (varchar) → [[clave-PKPREVENTANRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PREVENTAPRODUCTO]] · `PREVENTACLIENTE.EMPRESAID = PREVENTAPRODUCTO.EMPRESAID` — view_join (V_DIM_PREVENTAS), alta

## Reglas de negocio conocidas
**Filtros**
- `p.preventafching >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101)` — _de_ [[dbo.V_DIM_PREVENTAS]]

**Derivaciones (CASE)**
- _de_ [[dbo.V_DIM_PREVENTAS]]:
  ```sql
  CASE WHEN ( ( preventaprodcongen IS NULL ) OR ( preventaprodcongen = 0 ) ) THEN CONCAT( p.pkpreventanro, CONCAT( '_', p.clientenropreventa ) ) ELSE CONCAT( p.pkpreventanro, CONCAT( '_', CONCAT( p.clientenropreventa, CONCAT( '_', o.preventaprodcongen ) ) ) ) END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_DIM_PREVENTAS]]
- [[dbo.V_PREVENTAS]]
