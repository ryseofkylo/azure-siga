---
esquema: SIGASC
tabla: VM_CLIENTE
objeto: SIGASC.VM_CLIENTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)
n_columnas: 91
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.VM_CLIENTE

> **BASE TABLE** · Dominio: **Core SIGA** · 91 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CICLOID` | int | 0% |
| 2 | `CIUDADID` | int | 0% |
| 3 | `CLANDESTINOCLIFCHING` | datetime2 | 100% |
| 4 | `CLANDESTINOTIPOID` | int | 14% |
| 5 | `CLICALAPTO` | varchar | 0% |
| 6 | `CLICALBARRIO` | int | 36% |
| 7 | `CLICALCASA` | varchar | 24% |
| 8 | `CLICALID` | int | 0% |
| 9 | `CLICALMANZANA` | varchar | 25% |
| 10 | `CLICALPISO` | varchar | 35% |
| 11 | `CLICALPUERTA` | varchar | 0% |
| 12 | `CLICALTORRE` | varchar | 36% |
| 13 | `CLICALUBICACION` | varchar | 0% |
| 14 | `CLICOBAPTO` | varchar | 0% |
| 15 | `CLICOBBARRIO` | int | 36% |
| 16 | `CLICOBCASA` | varchar | 8% |
| 17 | `CLICOBCP` | varchar | 0% |
| 18 | `CLICOBDIRNOTIENE` | int | 59% |
| 19 | `CLICOBGEODIV1` | int | 0% |
| 20 | `CLICOBGEODIV2` | int | 0% |
| 21 | `CLICOBGEOINI` | varchar | 0% |
| 22 | `CLICOBGEOMAN` | int | 0% |
| 23 | `CLICOBID` | int | 0% |
| 24 | `CLICOBMANZANA` | varchar | 9% |
| 25 | `CLICOBPISO` | varchar | 16% |
| 26 | `CLICOBPUERTA` | varchar | 0% |
| 27 | `CLICOBTORRE` | varchar | 16% |
| 28 | `CLICOBUBICACION` | varchar | 0% |
| 29 | `CLIENTEAPE` | varchar | 0% |
| 30 | `CLIENTECI` | varchar | 0% |
| 31 | `CLIENTECITPO` | varchar | 0% |
| 32 | `CLIENTECODADICIONAL` | int | 60% |
| 33 | `CLIENTECODEXT` | varchar | 46% |
| 34 | `CLIENTECONDICIONVTA` | varchar | 18% |
| 35 | `CLIENTECORDTPO` | varchar | 0% |
| 36 | `CLIENTECORDX` | varchar | 0% |
| 37 | `CLIENTECORDY` | varchar | 0% |
| 38 | `CLIENTECP` | varchar | 0% |
| 39 | `CLIENTECPA` | varchar | 51% |
| 40 | `CLIENTEDEBBANCO` | int | 12% |
| 41 | `CLIENTEDEBCI` | varchar | 0% |
| 42 | `CLIENTEDEBTITULAR` | varchar | 0% |
| 43 | `CLIENTEEDIFICIONRO` | int | 40% |
| 44 | `CLIENTEEMAILNOSEUSA` | varchar | 59% |
| 45 | `CLIENTEEMAILPPL` | varchar | 0% |
| 46 | `CLIENTEESEMPRESA` | int | 7% |
| 47 | `CLIENTEFCHING` | datetime2 | 0% |
| 48 | `CLIENTEFCHNAC` | datetime2 | 78% |
| 49 | `CLIENTEHPP` | int | 0% |
| 50 | `CLIENTEIDCOD` | varchar | 25% |
| 51 | `CLIENTEIDNRO` | int | 26% |
| 52 | `CLIENTEIMPUESTO` | int | 0% |
| 53 | `CLIENTENATURALEZAID` | int | 0% |
| 54 | `CLIENTENOM` | varchar | 0% |
| 55 | `CLIENTENRO` | int | 0% |
| 56 | `CLIENTEPIN` | int | 0% |
| 57 | `CLIENTEPINREQ` | int | 0% |
| 58 | `CLIENTEPROPIEDAD` | varchar | 0% |
| 59 | `CLIENTERUT` | varchar | 39% |
| 60 | `CLIENTESEXO` | varchar | 0% |
| 61 | `CLIENTESTS` | varchar | 0% |
| 62 | `CLIENTETPO` | int | 0% |
| 63 | `CLIENTEUBITPO` | varchar | 0% |
| 64 | `CLIENTEUSRING` | varchar | 0% |
| 65 | `CLIENTEVINCULOFACTURA` | varchar | 0% |
| 66 | `CLIENTEVINCULOPADRE` | int | 0% |
| 67 | `CLIENTEVINCULOTPO` | varchar | 0% |
| 68 | `CLIESQUINA1ID` | int | 24% |
| 69 | `CLIESQUINA2ID` | int | 34% |
| 70 | `CONDICIONIVA` | int | 0% |
| 71 | `DISTRIBUIDORID` | int | 51% |
| 72 | `EMPRESAID` | int | 0% |
| 73 | `GEODIV1ID` | int | 0% |
| 74 | `GEODIV2ID` | int | 0% |
| 75 | `GEOMANID` | int | 0% |
| 76 | `GEOMANINI` | varchar | 1% |
| 77 | `MEDCOBROID` | int | 0% |
| 78 | `NEGOCIOSEGMENTO` | int | 0% |
| 79 | `NEGOCIOSEGMENTOTIPOID` | int | 44% |
| 80 | `REPARTOCLIID` | int | 0% |
| 81 | `REPARTOCOBID` | int | 51% |
| 82 | `SUCURSALID` | int | 0% |
| 83 | `VODCANTIDADINVITADOS` | int | 0% |
| 84 | `VODSESIONCONTROL` | varchar | 0% |
| 85 | `VODSESIONESSIM` | int | 0% |
| 86 | `VODUSUARIO` | varchar | 0% |
| 87 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 88 | `CLIENTEADMITESKEELO` | int | 10% |
| 89 | `PIPELINERUNID` | varchar | 0% |
| 90 | `PKCLIENTENRO` | varchar | 0% |
| 91 | `MEDCOBROTARJETA` | int | 94% |

## Claves de join presentes
- `CICLOID` (int) → [[clave-CICLOID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `CLICALID` (int) → [[clave-CLICALID]]
- `CLIENTENATURALEZAID` (int) → [[clave-CLIENTENATURALEZAID]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
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
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.FACTURA]] · `VM_CLIENTE.EMPRESAID = FACTURA.EMPRESAID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.FACTURA]] · `VM_CLIENTE.CLIENTENRO = FACTURA.CLIENTENRO` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.CLIENTENATURALEZA]] · `VM_CLIENTE.CLIENTENATURALEZAID = CLIENTENATURALEZA.CLIENTENATURALEZAID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.MEDIOCOBRO]] · `VM_CLIENTE.MEDCOBROID = MEDIOCOBRO.MEDCOBROID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.REPARTO]] · `VM_CLIENTE.REPARTOCLIID = REPARTO.REPARTOID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.REPARTO]] · `VM_CLIENTE.EMPRESAID = REPARTO.EMPRESAID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.ORDENTRB]] · `VM_CLIENTE.EMPRESAID = ORDENTRB.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.CENTROOPERATIVOSUCURSAL]] · `VM_CLIENTE.SUCURSALID = CENTROOPERATIVOSUCURSAL.CENTROOPESUCURSALID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.CENTROOPERATIVOSUCURSAL]] · `VM_CLIENTE.EMPRESAID = CENTROOPERATIVOSUCURSAL.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.ORDENSRV]] · `VM_CLIENTE.EMPRESAID = ORDENSRV.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.ORDENSRV]] · `VM_CLIENTE.CLIENTENRO = ORDENSRV.CLIENTENROORD` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.CLIENTETPO]] · `VM_CLIENTE.CLIENTETPO = CLIENTETPO.CLIENTETPO` — view_join (PushMTI), alta
- [[SIGASC.FACTURALINEA]] · `VM_CLIENTE.CLIENTENRO = FACTURALINEA.CLIENTENRO` — view_join (v_Segmentacion), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `c.clientests = 'C'` — _de_ [[dbo.PushMTI]]
- `c.clientenro not in( select t.clientenro from tablaexclusion t )` — _de_ [[dbo.PushMTI]]
- `c.clientetpo not in( 991, 992, 993, 995, 996, 984, 986, 988, 1005, 1006, 1007, 1008, 1009 )` — _de_ [[dbo.PushMTI]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.v_Segmentacion]]

**Derivaciones (CASE)**
- _de_ [[dbo.BI_FACTURA_ENCABEZADO_ALL]]:
  ```sql
  case cl.clientests when 'I' then 'INGRESADO' when 'P' then 'PENDIENTE' when 'E' then 'EMITIDO' when 'C' then 'CONECTADO' when 'X' then 'DESCONECTADO' when 'A' then 'ANULADO' when 'B' then 'BAJA PENDIENTE' when 'M' then 'SUSPENSION POR MORA' when 'J' then 'BAJA INCUMPLIDA' else cl.clientests end
  ```

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_ENCABEZADO_ALL]]
- [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
- [[dbo.PushMTI]]
- [[dbo.V_CONTRATOS_BDDD]]
- [[dbo.vProyeccion]]
- [[dbo.v_Segmentacion]]
