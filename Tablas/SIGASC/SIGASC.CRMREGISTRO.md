---
esquema: SIGASC
tabla: CRMREGISTRO
objeto: SIGASC.CRMREGISTRO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMNRO` (único en muestra de 200)
n_columnas: 40
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMREGISTRO

> **BASE TABLE** · Dominio: **Core SIGA** · 40 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CRMNRO` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `CRMFCHINI` | datetime2 | 0% |
| 5 | `CRMFCHFIN` | datetime2 | 100% |
| 6 | `CRMUSRING` | varchar | 0% |
| 7 | `CRMUSRACT` | varchar | 0% |
| 8 | `CRMTIPO` | varchar | 0% |
| 9 | `CRMMEDIO` | varchar | 0% |
| 10 | `CRMNIVELINI` | varchar | 0% |
| 11 | `CRMNIVELFIN` | varchar | 0% |
| 12 | `CRMRESULTADO` | int | 0% |
| 13 | `CRMSTS` | varchar | 0% |
| 14 | `CRMOBS` | varchar | 0% |
| 15 | `CRMMOTIVO1` | int | 0% |
| 16 | `CRMMOTIVO2` | int | 0% |
| 17 | `CRMMOTIVO3` | int | 0% |
| 18 | `CRMMOTIVO4` | int | 0% |
| 19 | `CRMDOCTPO` | varchar | 0% |
| 20 | `CRMDOCCOD` | varchar | 0% |
| 21 | `CRMLUGARID` | varchar | 0% |
| 22 | `CRMFCHAUX` | datetime2 | 100% |
| 23 | `CRMARCAUDIO` | varchar | 0% |
| 24 | `CRMCAMNRO` | int | 0% |
| 25 | `CRMFLGINGIVR` | int | 0% |
| 26 | `CRMCLASE` | varchar | 0% |
| 27 | `CRMCODIGOEXTERNO` | varchar | 0% |
| 28 | `CRMAGENTECOMPRA` | varchar | 0% |
| 29 | `CRMCABLEPACK` | varchar | 0% |
| 30 | `CRMPROVCABLE` | varchar | 0% |
| 31 | `CRMPROVINTERNET` | varchar | 0% |
| 32 | `CRMCONTACTADO` | varchar | 0% |
| 33 | `CRMNIVELINTENCION` | varchar | 0% |
| 34 | `CRMNROFULCRUM` | varchar | 0% |
| 35 | `CRMCORDY` | varchar | 0% |
| 36 | `CRMCORDX` | varchar | 0% |
| 37 | `CRMORDENNRO` | int | 0% |
| 38 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 39 | `PIPELINERUNID` | varchar | 0% |
| 40 | `PKCRMNRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CRMNRO` (int) → [[clave-CRMNRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `CRMLUGARID` (varchar) → [[clave-CRMLUGARID]]
- `CRMCAMNRO` (int) → [[clave-CRMCAMNRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMNRO` (varchar) → [[clave-PKCRMNRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
**Filtros**
- `C.CRMUSRING <> 'ROOT'` — _de_ [[dbo.V_CRM_BDDD]]
- `CRM.CRMMOTIVO1 in (37,45,38,27)` — _de_ [[dbo.V_NPS_BAJAS]]
- `FORMAT(CRM.CRMFCHINI,'yyyyMM') in ( select periodo from Logica_fechas_anteriores )` — _de_ [[dbo.v_Segmentacion]]
- `FORMAT(CRM.CRMFCHINI,'yyyyMM') in ( select periodo from Logica_fechas_actual )` — _de_ [[dbo.v_Segmentacion]]
- `CRM.CRMMOTIVO1 not in (37,45,38,27)` — _de_ [[dbo.v_Segmentacion]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_NPS_BAJAS]], [[dbo.V_NPS_RECLAMOS]], [[dbo.v_Segmentacion]]

## Vistas que la consumen (referencia)
- [[dbo.V_CRMREGISTRO]]
- [[dbo.V_CRM_BDDD]]
- [[dbo.V_NPS_BAJAS]]
- [[dbo.V_NPS_RECLAMOS]]
- [[dbo.v_Segmentacion]]
