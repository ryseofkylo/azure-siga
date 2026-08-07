---
esquema: SIGASC
tabla: ORDENSRV
objeto: SIGASC.ORDENSRV
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKORDENNRO` (único en muestra de 200)
n_columnas: 79
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ORDENSRV

> **BASE TABLE** · Dominio: **Core SIGA** · 79 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKORDENNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ORDENNRO` | int | 0% |
| 3 | `ORDENTPO` | varchar | 0% |
| 4 | `CLIENTENROORD` | int | 0% |
| 5 | `CONTRATONRO` | int | 0% |
| 6 | `MOTIVOORDID` | int | 0% |
| 7 | `ORDENSTS` | varchar | 0% |
| 8 | `ORDENFING` | datetime2 | 0% |
| 9 | `ORDENHING` | datetime2 | 100% |
| 10 | `TECNICOID` | int | 17% |
| 11 | `ORDENFFIN` | datetime2 | 14% |
| 12 | `ORDENHFIN` | datetime2 | 100% |
| 13 | `ORDENAGENDAFCH` | datetime2 | 48% |
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
| 26 | `ORDENOBS` | varchar | 2% |
| 27 | `ORDENFPROCESO` | datetime2 | 28% |
| 28 | `ORDENHPROCESO` | datetime2 | 100% |
| 29 | `ORDENARTULTLIN` | int | 0% |
| 30 | `CENTROSTKIDORD` | int | 0% |
| 31 | `ORDENARTCONFIRMADO` | int | 0% |
| 32 | `ORDENARTCNFUSR` | varchar | 0% |
| 33 | `ORDENARTCNFFCH` | datetime2 | 57% |
| 34 | `ORDENAGENDANRO` | int | 0% |
| 35 | `ORDENAGENDATUR` | int | 0% |
| 36 | `ORDENCNXID` | int | 0% |
| 37 | `ORDCALLEUBICACION` | varchar | 0% |
| 38 | `MOTIVOORDORIGENID` | int | 0% |
| 39 | `MOTIVOORDINGID` | int | 4% |
| 40 | `ORDENZONA` | int | 0% |
| 41 | `ORDENENPROCESO` | varchar | 0% |
| 42 | `ORDEDIFICIONRO` | int | 0% |
| 43 | `ORDENFCOM` | datetime2 | 97% |
| 44 | `ORDENHCOM` | datetime2 | 100% |
| 45 | `ORDENFACTUALIZA` | datetime2 | 34% |
| 46 | `ORDENCANTIDAD` | int | 0% |
| 47 | `ORDENUBITPO` | varchar | 0% |
| 48 | `ORDENCONEXIONID` | varchar | 0% |
| 49 | `CENTROOPERATIVOID` | int | 0% |
| 50 | `ORDMANZANA` | varchar | 0% |
| 51 | `ORDTORRE` | varchar | 0% |
| 52 | `ORDPISO` | varchar | 0% |
| 53 | `ORDCASA` | varchar | 0% |
| 54 | `TECNICO2ID` | int | 32% |
| 55 | `ORDCIUDADID` | int | 0% |
| 56 | `TECNICOIDCIERREAUX` | int | 34% |
| 57 | `TECNICOIDCIERRE` | int | 8% |
| 58 | `AFBIENIDCIERRE` | int | 34% |
| 59 | `AFBIENID` | int | 34% |
| 60 | `PRODUCTIVIDADTURNOIDCIERRE` | int | 34% |
| 61 | `PRODUCTIVIDADDIAFCHCIERRE` | datetime2 | 62% |
| 62 | `PRODUCTIVIDADTURNOIDASIGNACION` | int | 34% |
| 63 | `PRODUCTIVIDADDIAFCHASIGNACION` | datetime2 | 48% |
| 64 | `ORDENVISITADA` | varchar | 16% |
| 65 | `ORDENSRVOBSNUM` | int | 0% |
| 66 | `ORDENSRVNAPCIERRE` | int | 10% |
| 67 | `ORDENSRVNAPINGRESO` | int | 10% |
| 68 | `ORDENSRVNAPPUECIE` | int | 10% |
| 69 | `ORDENSRVCLIBARRIO` | int | 34% |
| 70 | `ORDENSRVNAPRX` | real | 10% |
| 71 | `ORDENPROYECTOSAP` | int | 62% |
| 72 | `ORDENSAPCONFIRMADO` | int | 62% |
| 73 | `ORDENTIPOCONEXION` | varchar | 66% |
| 74 | `ORDENFCHCONEXIONFUTURA` | datetime2 | 100% |
| 75 | `ORDENTPOCIERRE` | varchar | 64% |
| 76 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 77 | `ORDENSRVFCHACTUALIZACION` | datetime2 | 8% |
| 78 | `PIPELINERUNID` | varchar | 0% |
| 79 | `PKORDENNRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `ORDENNRO` (int) → [[clave-ORDENNRO]]
- `CLIENTENROORD` (int) → [[clave-CLIENTENROORD]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
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
- `PKORDENNRO` (varchar) → [[clave-PKORDENNRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.VM_CLIENTE]] · `ORDENSRV.EMPRESAID = VM_CLIENTE.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.VM_CLIENTE]] · `ORDENSRV.CLIENTENROORD = VM_CLIENTE.CLIENTENRO` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.EMPRESASMULTI]] · `ORDENSRV.EMPRESAID = EMPRESASMULTI.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.TECNICO]] · `ORDENSRV.EMPRESAID = TECNICO.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.TECNICO]] · `ORDENSRV.TECNICOIDCIERRE = TECNICO.TECNICOID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.CONTRATO]] · `ORDENSRV.EMPRESAID = CONTRATO.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.CONTRATO]] · `ORDENSRV.CONTRATONRO = CONTRATO.CONTRATONRO` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.CONTRATO]] · `ORDENSRV.CLIENTENROORD = CONTRATO.CLIENTENRO` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.HISTORICOENTIDADREG]] · `ORDENSRV.EMPRESAID = HISTORICOENTIDADREG.EMPRESAID` — view_join (V_ORDENINSTALACION), alta

## Reglas de negocio conocidas
**Filtros**
- `ORD.ORDENTPO = 'R'` — _de_ [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
- `O.TECNICOIDCIERRE > 0` — _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]
- `o.tecnicoidcierre > 0` — _de_ [[dbo.V_ORDENESPENDIENTES]]
- 🚦 `o.ordensts IN ('E','A','P','R','S','F')` — _de_ [[dbo.V_ORDENESPENDIENTES]]
- `o.ordentpo = 'I'` — _de_ [[dbo.V_ORDENINSTALACION]]
- `o.ordengen = 'C'` — _de_ [[dbo.V_ORDENINSTALACION]]
- `o.ordenfing >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-13,GETDATE())),101)` — _de_ [[dbo.V_ORDENINSTALACION]]
- `o.ordenfing < GETDATE()` — _de_ [[dbo.V_ORDENINSTALACION]]
- `FORMAT(os.ORDENFING,'yyyyMM') in ( select periodo from Logica_fechas_anteriores )` — _de_ [[dbo.v_Segmentacion]]
- `FORMAT(os.ORDENFING,'yyyyMM') in ( select periodo from Logica_fechas_actual )` — _de_ [[dbo.v_Segmentacion]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_NPS_RECLAMOS]], [[dbo.V_ORDENINSTALACION]], [[dbo.V_SOLUCIONORDEN]], [[dbo.v_Segmentacion]]

**Derivaciones (CASE)**
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  case O.EMPRESAID WHEN 21 THEN 4 ELSE O.EMPRESAID END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  case O.EMPRESAID WHEN 21 THEN 'SUPERCANAL CATAMARCA' ELSE TRIM(EMP.EMPRESANOM) END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and o.PRODUCTOTPO = 'B' and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and o.PRODUCTOTPO = 'B' and O.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and o.PRODUCTOTPO = 'L' and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and o.PRODUCTOTPO = 'Z' and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and o.PRODUCTOTPO = 'R' and O.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and o.PRODUCTOTPO = 'D' and O.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE WHEN O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' AND o.PRODUCTOTPO IN('C','I') and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE WHEN O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' AND o.PRODUCTOTPO = 'E' and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  CASE WHEN O.ORDENTPO = 'I' AND o.PRODUCTOTPO = 'N' and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  case o.EMPRESAID when 1 then case COP.CENTROOPERATIVOID when 3 then 'CP. SAN MARTIN MZA' else 'CP. MENDOZA' end when 16 then case COP.CENTROOPERATIVOID when 2 then 'CP. CHILECITO' else 'CP. LA RIOJA' end when 3 then 'CP. TUCUMAN' when 21 then 'CP. CATAMARCA' else REPLACE(CENTROOPERATIVONOMBRE,'C.O.','CP.') end
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE o.ordengen WHEN 'C' THEN 'CONTRATO' WHEN 'N' THEN 'NORMAL' WHEN 'Z' THEN 'MUDANZA' WHEN 'M' THEN 'MOROSIDAD' WHEN 'Q' THEN 'CAMBIO DE PRODUCTO' WHEN 'S' THEN 'SERVICIO' ELSE 'OTROS' END
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE o.ORDENTPO WHEN 'I' THEN 'INSTALACION' WHEN 'D' THEN 'DESCONEXION' WHEN 'S' THEN 'SERVICIO' WHEN 'E' THEN 'RETIRO EQUIPO' WHEN 'R' THEN 'RECLAMO' END
  ```
- _de_ [[dbo.V_ORDENESPENDIENTES]]:
  ```sql
  CASE o.empresaid WHEN 21 THEN 4 ELSE o.empresaid END
  ```

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
- [[dbo.V_NPS_RECLAMOS]]
- [[dbo.V_ORDENESPENDIENTES]]
- [[dbo.V_ORDENINSTALACION]]
- [[dbo.V_ORDENSRV]]
- [[dbo.V_ORDENSRV_DESCONEX]]
- [[dbo.V_ORDENSRV_INST]]
- [[dbo.V_ORDENSRV_RECLAMOS]]
- [[dbo.V_RECLAMOS_360]]
- [[dbo.V_RECLAMOS_BDDD]]
- [[dbo.V_SOLUCIONORDEN]]
- [[dbo.v_Segmentacion]]
