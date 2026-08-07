---
esquema: SIGASC
tabla: CONTRATO
objeto: SIGASC.CONTRATO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)
n_columnas: 41
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CONTRATO

> **BASE TABLE** · Dominio: **Core SIGA** · 41 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CONTRATONRO` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `PRODUCTOID` | int | 0% |
| 5 | `POLITICAID` | int | 0% |
| 6 | `CONTRATOFING` | datetime2 | 0% |
| 7 | `CONTRATOFINS` | datetime2 | 0% |
| 8 | `CONTRATOFREF` | datetime2 | 0% |
| 9 | `CONTRATOFREN` | datetime2 | 100% |
| 10 | `CONTRATOFDES` | datetime2 | 100% |
| 11 | `CONTRATOFULT` | datetime2 | 0% |
| 12 | `CONTRATOVINI` | datetime2 | 0% |
| 13 | `CONTRATOVFIN` | datetime2 | 0% |
| 14 | `CONTRATOSTS` | varchar | 0% |
| 15 | `CONTRATOUSR` | varchar | 0% |
| 16 | `INGRESOID` | int | 0% |
| 17 | `CONTRATOORINRO` | int | 0% |
| 18 | `PROMOTORID` | int | 0% |
| 19 | `CONTRATOPRN` | int | 0% |
| 20 | `CONTRATOCOD` | varchar | 0% |
| 21 | `CONTRATOFIRMADO` | int | 0% |
| 22 | `CONTRATOCNT` | int | 0% |
| 23 | `MOTIVOBAJAID` | int | 0% |
| 24 | `CONTRATOHPP` | varchar | 0% |
| 25 | `CONTRATOGEN` | varchar | 0% |
| 26 | `CONTRATOEXCLUIR` | varchar | 0% |
| 27 | `CONTRATORECONEXION` | varchar | 10% |
| 28 | `CONTRATOMULT` | varchar | 96% |
| 29 | `CONTRATOFCORTE` | datetime2 | 100% |
| 30 | `CONTRATODESHABILITADO` | int | 100% |
| 31 | `PLANCOMERCIALCLIENTEITEM` | int | 100% |
| 32 | `PLANCOMERCIALGESTIONID` | int | 100% |
| 33 | `PLANCOMERCIALCLIENTEID` | int | 100% |
| 34 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 35 | `CONTRATOFCHACTUALIZACION` | datetime2 | 100% |
| 36 | `CONTRATOSKEELONRO` | int | 100% |
| 37 | `PIPELINERUNID` | varchar | 0% |
| 38 | `PKCONTRATONRO` | varchar | 0% |
| 39 | `PKCLIENTENRO` | varchar | 0% |
| 40 | `PKPOLITICAID` | varchar | 0% |
| 41 | `PKPRODUCTOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PROMOTORID` (int) → [[clave-PROMOTORID]]
- `PLANCOMERCIALGESTIONID` (int) → [[clave-PLANCOMERCIALGESTIONID]]
- `PLANCOMERCIALCLIENTEID` (int) → [[clave-PLANCOMERCIALCLIENTEID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCONTRATONRO` (varchar) → [[clave-PKCONTRATONRO]]
- `PKCLIENTENRO` (varchar) → [[clave-PKCLIENTENRO]]
- `PKPOLITICAID` (varchar) → [[clave-PKPOLITICAID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.ORDENSRV]] · `CONTRATO.EMPRESAID = ORDENSRV.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.ORDENSRV]] · `CONTRATO.CONTRATONRO = ORDENSRV.CONTRATONRO` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.ORDENSRV]] · `CONTRATO.CLIENTENRO = ORDENSRV.CLIENTENROORD` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.PRODUCTO]] · `CONTRATO.EMPRESAID = PRODUCTO.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.PRODUCTO]] · `CONTRATO.PRODUCTOID = PRODUCTO.PRODUCTOID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.CONTRATOPROMOCION]] · `CONTRATO.EMPRESAID = CONTRATOPROMOCION.EMPRESAID` — view_join (v_promomes), alta
- [[SIGASC.CONTRATOPROMOCION]] · `CONTRATO.CONTRATONRO = CONTRATOPROMOCION.CONTRATONRO` — view_join (v_promomes), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `c.contratosts <> 'X'` — _de_ [[dbo.v_promomes]]
- `C.EMPRESAID NOT IN (15,19)` — _de_ [[dbo.V_RECLAMOS_BDDD]]
- `c.empresaid NOT IN ('101','102')` — _de_ [[dbo.V_RETENCIONES]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_BAJASMOROSAS_NETAS]], [[dbo.V_BAJASVOLUNTARIAS_NETAS]], [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]], [[dbo.v_Segmentacion]]

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_DETALLE_ALL]]
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
- [[dbo.V_BAJASMOROSAS_NETAS]]
- [[dbo.V_BAJASVOLUNTARIAS_NETAS]]
- [[dbo.V_COBRANZAS_BASE]]
- [[dbo.V_CONTRATOS_BDDD]]
- [[dbo.V_FACTURACION]]
- [[dbo.V_FACTURACION_2]]
- [[dbo.V_FACTURACION_PERIODO]]
- [[dbo.V_ORDENESPENDIENTES]]
- [[dbo.V_ORDENSRV_DESCONEX]]
- [[dbo.V_ORDENSRV_INST]]
- [[dbo.V_ORDENSRV_RECLAMOS]]
- [[dbo.V_OTRA_FACTURACION]]
- [[dbo.V_RECLAMOS_BDDD]]
- [[dbo.V_RETENCIONES]]
- [[dbo.vContratos_MF_Cuota1]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
- [[dbo.v_Segmentacion]]
- [[dbo.v_promomes]]
