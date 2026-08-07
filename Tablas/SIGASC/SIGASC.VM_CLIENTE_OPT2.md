---
esquema: SIGASC
tabla: VM_CLIENTE_OPT2
objeto: SIGASC.VM_CLIENTE_OPT2
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTENRO` (único en muestra de 200)
n_columnas: 88
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.VM_CLIENTE_OPT2

> **BASE TABLE** · Dominio: **Core SIGA** · 88 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CICLOID` | int | 0% |
| 2 | `CIUDADID` | int | 0% |
| 3 | `CLANDESTINOCLIFCHING` | datetime2 | 100% |
| 4 | `CLANDESTINOTIPOID` | int | 0% |
| 5 | `CLICALAPTO` | nvarchar | 0% |
| 6 | `CLICALBARRIO` | int | 20% |
| 7 | `CLICALCASA` | nvarchar | 20% |
| 8 | `CLICALID` | int | 0% |
| 9 | `CLICALMANZANA` | nvarchar | 20% |
| 10 | `CLICALPISO` | nvarchar | 21% |
| 11 | `CLICALPUERTA` | nvarchar | 0% |
| 12 | `CLICALTORRE` | nvarchar | 13% |
| 13 | `CLICALUBICACION` | nvarchar | 0% |
| 14 | `CLICOBAPTO` | nvarchar | 0% |
| 15 | `CLICOBBARRIO` | int | 20% |
| 16 | `CLICOBCASA` | nvarchar | 13% |
| 17 | `CLICOBCP` | nvarchar | 0% |
| 18 | `CLICOBDIRNOTIENE` | int | 23% |
| 19 | `CLICOBGEODIV1` | int | 0% |
| 20 | `CLICOBGEODIV2` | int | 0% |
| 21 | `CLICOBGEOINI` | nvarchar | 1% |
| 22 | `CLICOBGEOMAN` | int | 0% |
| 23 | `CLICOBID` | int | 0% |
| 24 | `CLICOBMANZANA` | nvarchar | 13% |
| 25 | `CLICOBPISO` | nvarchar | 15% |
| 26 | `CLICOBPUERTA` | nvarchar | 0% |
| 27 | `CLICOBTORRE` | nvarchar | 12% |
| 28 | `CLICOBUBICACION` | nvarchar | 0% |
| 29 | `CLIENTEAPE` | nvarchar | 0% |
| 30 | `CLIENTECI` | nvarchar | 0% |
| 31 | `CLIENTECITPO` | nvarchar | 0% |
| 32 | `CLIENTECODADICIONAL` | int | 25% |
| 33 | `CLIENTECODEXT` | nvarchar | 20% |
| 34 | `CLIENTECONDICIONVTA` | nvarchar | 12% |
| 35 | `CLIENTECORDTPO` | nvarchar | 0% |
| 36 | `CLIENTECORDX` | nvarchar | 0% |
| 37 | `CLIENTECORDY` | nvarchar | 0% |
| 38 | `CLIENTECP` | nvarchar | 0% |
| 39 | `CLIENTECPA` | nvarchar | 14% |
| 40 | `CLIENTEDEBBANCO` | int | 5% |
| 41 | `CLIENTEDEBCI` | nvarchar | 0% |
| 42 | `CLIENTEDEBTITULAR` | nvarchar | 0% |
| 43 | `CLIENTEEDIFICIONRO` | int | 12% |
| 44 | `CLIENTEEMAILNOSEUSA` | nvarchar | 86% |
| 45 | `CLIENTEEMAILPPL` | nvarchar | 2% |
| 46 | `CLIENTEESEMPRESA` | int | 11% |
| 47 | `CLIENTEFCHING` | datetime2 | 0% |
| 48 | `CLIENTEFCHNAC` | datetime2 | 78% |
| 49 | `CLIENTEHPP` | int | 0% |
| 50 | `CLIENTEIDCOD` | nvarchar | 12% |
| 51 | `CLIENTEIDNRO` | int | 12% |
| 52 | `CLIENTEIMPUESTO` | int | 0% |
| 53 | `CLIENTENATURALEZAID` | int | 14% |
| 54 | `CLIENTENOM` | nvarchar | 0% |
| 55 | `CLIENTENRO` | nvarchar | 0% |
| 56 | `CLIENTEPIN` | int | 0% |
| 57 | `CLIENTEPINREQ` | int | 0% |
| 58 | `CLIENTEPROPIEDAD` | nvarchar | 0% |
| 59 | `CLIENTERUT` | nvarchar | 25% |
| 60 | `CLIENTESEXO` | nvarchar | 0% |
| 61 | `CLIENTESTS` | nvarchar | 0% |
| 62 | `CLIENTETPO` | int | 0% |
| 63 | `CLIENTEUBITPO` | nvarchar | 0% |
| 64 | `CLIENTEUSRING` | nvarchar | 0% |
| 65 | `CLIENTEVINCULOFACTURA` | nvarchar | 0% |
| 66 | `CLIENTEVINCULOPADRE` | int | 0% |
| 67 | `CLIENTEVINCULOTPO` | nvarchar | 0% |
| 68 | `CLIESQUINA1ID` | int | 9% |
| 69 | `CLIESQUINA2ID` | int | 10% |
| 70 | `CONDICIONIVA` | int | 0% |
| 71 | `DISTRIBUIDORID` | int | 20% |
| 72 | `EMPRESAID` | int | 0% |
| 73 | `GEODIV1ID` | int | 0% |
| 74 | `GEODIV2ID` | int | 0% |
| 75 | `GEOMANID` | int | 0% |
| 76 | `GEOMANINI` | nvarchar | 0% |
| 77 | `MEDCOBROID` | int | 0% |
| 78 | `NEGOCIOSEGMENTO` | int | 0% |
| 79 | `NEGOCIOSEGMENTOTIPOID` | int | 13% |
| 80 | `REPARTOCLIID` | int | 0% |
| 81 | `REPARTOCOBID` | int | 20% |
| 82 | `SUCURSALID` | int | 0% |
| 83 | `VODCANTIDADINVITADOS` | int | 0% |
| 84 | `VODSESIONCONTROL` | nvarchar | 0% |
| 85 | `VODSESIONESSIM` | int | 0% |
| 86 | `VODUSUARIO` | nvarchar | 0% |
| 87 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 88 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `CICLOID` (int) → [[clave-CICLOID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `CLICALID` (int) → [[clave-CLICALID]]
- `CLIENTENATURALEZAID` (int) → [[clave-CLIENTENATURALEZAID]]
- `CLIENTENRO` (nvarchar) → [[clave-CLIENTENRO]]
- `CLIENTETPO` (int) → [[clave-CLIENTETPO]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]
- `GEOMANID` (int) → [[clave-GEOMANID]]
- `MEDCOBROID` (int) → [[clave-MEDCOBROID]]
- `NEGOCIOSEGMENTO` (int) → [[clave-NEGOCIOSEGMENTO]]
- `NEGOCIOSEGMENTOTIPOID` (int) → [[clave-NEGOCIOSEGMENTOTIPOID]]
- `REPARTOCLIID` (int) → [[clave-REPARTOCLIID]]
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
