---
esquema: SIGASC
tabla: FACTURA
objeto: SIGASC.FACTURA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKFACTURANRO` (único en muestra de 200)
n_columnas: 73
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURA

> **BASE TABLE** · Dominio: **Core SIGA** · 73 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKFACTURANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKFACTURA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `FACTURATPO` | varchar | 0% |
| 4 | `FACTURANRO` | int | 0% |
| 5 | `CLIENTENRO` | int | 0% |
| 6 | `FACTURASTS` | varchar | 0% |
| 7 | `FACTURAFCH` | datetime2 | 0% |
| 8 | `FACTURAVTO` | datetime2 | 0% |
| 9 | `FACTURAFCOB` | datetime2 | 34% |
| 10 | `FACTURAFICOB` | datetime2 | 34% |
| 11 | `FACTURAPRN` | int | 0% |
| 12 | `MONEDAID` | int | 0% |
| 13 | `FACTURAUSR` | varchar | 0% |
| 14 | `MEDCOBFAC` | int | 0% |
| 15 | `COBRADORID` | int | 0% |
| 16 | `FACTURAGEN` | varchar | 0% |
| 17 | `FACTURANRONC` | int | 0% |
| 18 | `FACTURAULTLIN` | int | 0% |
| 19 | `CMPTEUNIDAD` | int | 0% |
| 20 | `CMPTELETRA` | varchar | 0% |
| 21 | `CMPTEPTOVTA` | int | 0% |
| 22 | `CMPTENRO` | int | 0% |
| 23 | `FACTURAPERIODO` | int | 0% |
| 24 | `FACTURARUT` | varchar | 0% |
| 25 | `FACTURAVTO2` | datetime2 | 0% |
| 26 | `FACTURAVTO3` | datetime2 | 0% |
| 27 | `FACTURACC` | int | 0% |
| 28 | `FACTURACATPO` | varchar | 0% |
| 29 | `FACTURACANRO` | varchar | 0% |
| 30 | `CMPTETIPO` | int | 0% |
| 31 | `FACTURACAVTO` | datetime2 | 92% |
| 32 | `FACTURASDO` | real | 0% |
| 33 | `MOTIVOFACID` | int | 0% |
| 34 | `CMPTEEFISCAL` | int | 0% |
| 35 | `FACTURACONDICIONIVA` | int | 0% |
| 36 | `FACTURAFCHHORA` | datetime2 | 0% |
| 37 | `FACTURAINSERT4` | varchar | 92% |
| 38 | `FACTURAINSERT3` | varchar | 92% |
| 39 | `FACTURAINSERT2` | varchar | 92% |
| 40 | `FACTURAINSERT1` | varchar | 92% |
| 41 | `FACTURACARTA` | varchar | 92% |
| 42 | `FACTURATOTAL` | real | 0% |
| 43 | `FACTURATOTALV2` | real | 0% |
| 44 | `FACTURATOTALV3` | real | 0% |
| 45 | `FACTURABARRIOID` | int | 92% |
| 46 | `FACTURACP` | varchar | 0% |
| 47 | `FACTURACLIENTENOM` | varchar | 0% |
| 48 | `FACTURACLIENTEAPE` | varchar | 0% |
| 49 | `FACTURAGEOINI` | varchar | 0% |
| 50 | `FACTURAGEOMAN` | int | 0% |
| 51 | `FACTURAGEODIV2` | int | 0% |
| 52 | `FACTURAGEODIV1` | int | 0% |
| 53 | `FACTURACALLEUBICACION` | varchar | 0% |
| 54 | `FACTURAMANZANA` | varchar | 0% |
| 55 | `FACTURATORRE` | varchar | 0% |
| 56 | `FACTURAPISO` | varchar | 0% |
| 57 | `FACTURACASA` | varchar | 0% |
| 58 | `FACTURAAPTO` | varchar | 0% |
| 59 | `FACTURAPUERTA` | varchar | 0% |
| 60 | `FACTURACALLEID` | int | 0% |
| 61 | `FACTURACIUDADID` | int | 0% |
| 62 | `FACTURAESTADOID` | int | 92% |
| 63 | `FACTURAEDIFICIONRO` | int | 0% |
| 64 | `FACTURAUBITPO` | varchar | 92% |
| 65 | `FACTURATOTALDEV` | real | 0% |
| 66 | `FACTURATOTALREFINANCIA` | real | 92% |
| 67 | `FACTURAFCHPRESCRIPTA` | datetime2 | 98% |
| 68 | `FACTURALINK` | varchar | 92% |
| 69 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 70 | `FACTURAQR` | varchar | 92% |
| 71 | `PIPELINERUNID` | varchar | 0% |
| 72 | `PKFACTURATPO` | varchar | 0% |
| 73 | `PKFACTURANRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `FACTURATPO` (varchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (int) → [[clave-FACTURANRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `MONEDAID` (int) → [[clave-MONEDAID]]
- `COBRADORID` (int) → [[clave-COBRADORID]]
- `CMPTENRO` (int) → [[clave-CMPTENRO]]
- `FACTURACANRO` (varchar) → [[clave-FACTURACANRO]]
- `MOTIVOFACID` (int) → [[clave-MOTIVOFACID]]
- `FACTURABARRIOID` (int) → [[clave-FACTURABARRIOID]]
- `FACTURACALLEID` (int) → [[clave-FACTURACALLEID]]
- `FACTURACIUDADID` (int) → [[clave-FACTURACIUDADID]]
- `FACTURAESTADOID` (int) → [[clave-FACTURAESTADOID]]
- `FACTURAEDIFICIONRO` (int) → [[clave-FACTURAEDIFICIONRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKFACTURATPO` (varchar) → [[clave-PKFACTURATPO]]
- `PKFACTURANRO` (varchar) → [[clave-PKFACTURANRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.FACTURALINEA]] · `FACTURA.FACTURATPO = FACTURALINEA.FACTURATPO` — view_join (BI_FACTURA_DETALLE_ALL), alta
- [[SIGASC.POLITICA]] · `FACTURA.EMPRESAID = POLITICA.EMPRESAID` — view_join (BI_FACTURA_DETALLE_ALL), alta
- [[SIGAMSASC.EMPRESA]] · `FACTURA.EMPRESAID = EMPRESA.EMPRESAID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.VM_CLIENTE]] · `FACTURA.EMPRESAID = VM_CLIENTE.EMPRESAID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.VM_CLIENTE]] · `FACTURA.CLIENTENRO = VM_CLIENTE.CLIENTENRO` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.RECIBOFAC]] · `FACTURA.FACTURANRO = RECIBOFAC.FACTURANRO` — view_join (V_COBRANZAS_BASE), alta
- [[SIGASC.FACTURALINEA]] · `FACTURA.FACTURANRO = FACTURALINEA.FACTURANRO` — view_join (V_COBRANZAS_BASE), alta

## Reglas de negocio conocidas
**Filtros**
- `f.facturatpo = 'F'` — _de_ [[dbo.vContratos_MF_Cuota1]]
- `f.empresaid = 10` — _de_ [[dbo.vContratos_MF_Cuota1]]
- `f.facturaperiodo = 202305` — _de_ [[dbo.vFACTURACION_DETALLE_202305_cp]]
- `f.facturaperiodo = 202306` — _de_ [[dbo.vFACTURACION_DETALLE_202306_cp]]
- `f.facturaperiodo = 202307` — _de_ [[dbo.vFACTURACION_DETALLE_202307_cp]]
- `f.facturaperiodo = 202308` — _de_ [[dbo.vFACTURACION_DETALLE_202308_cp]]
- `f.facturaperiodo = 202309` — _de_ [[dbo.vFACTURACION_DETALLE_202309_cp]]
- `f.facturaperiodo = 202310` — _de_ [[dbo.vFACTURACION_DETALLE_202310_cp]]
- `f.facturatpo='F'` — _de_ [[dbo.v_Segmentacion]]
- `f.facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM')` — _de_ [[dbo.v_Segmentacion]]
- `f.facturaperiodo = FORMAT(DATEADD(month,12,DATEADD(year, -1,GETDATE())),'yyyyMM')` — _de_ [[dbo.v_Segmentacion]]
- `f.clientenro not in ( SELECT distinct clientenro FROM sigasc.factura f where F.facturatpo = 'F' and f.facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM') )` — _de_ [[dbo.v_Segmentacion]]
- `f.facturaperiodo = FORMAT(DATEADD(month,11,DATEADD(year, -1,GETDATE())),'yyyyMM')` — _de_ [[dbo.v_Segmentacion]]
- `f.clientenro not in ( SELECT distinct clientenro FROM sigasc.factura f where F.facturatpo = 'F' and (f.facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM') or f.facturaperiodo = FORMAT(DATEADD(month,12,DATEADD(year, -1,GETDATE())),'yyyyMM')) )` — _de_ [[dbo.v_Segmentacion]]
- `(f.facturaperiodo = FORMAT(DATEADD(month,13,DATEADD(year, -1,GETDATE())),'yyyyMM') or f.facturaperiodo = FORMAT(DATEADD(month,12,DATEADD(year, -1,GETDATE())),'yyyyMM'))` — _de_ [[dbo.v_Segmentacion]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]], [[dbo.v_Segmentacion]]

**Derivaciones (CASE)**
- _de_ [[dbo.BI_FACTURA_DETALLE_ALL]]:
  ```sql
  CASE WHEN f.facturaperiodo = 0 THEN YEAR(DATEADD(month,1,FACTURAFCH))*100 + MONTH(DATEADD(month,1,FACTURAFCH)) ELSE f.facturaperiodo END
  ```
- _de_ [[dbo.BI_FACTURA_ENCABEZADO_ALL]]:
  ```sql
  CASE WHEN f.facturaperiodo = 0 THEN YEAR(FACTURAFCH )*100 + MONTH(FACTURAFCH) ELSE f.facturaperiodo END
  ```
- _de_ [[dbo.V_COBRANZAS_BASE]]:
  ```sql
  CASE e.empresadevengavto WHEN 1 THEN Isnull( l.facturalinimp / Nullif(f.facturatotal , 0) , 0) WHEN 2 THEN Isnull( l.facturalinimpv2 / Nullif(f.facturatotalv2 , 0), 0) WHEN 3 THEN Isnull( l.facturalinimpv3 / Nullif(f.facturatotalv3 , 0), 0) END
  ```
- _de_ [[dbo.V_COBRANZAS_BASE]]:
  ```sql
  CASE e.empresadevengavto WHEN 1 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimp / Nullif(f.facturatotal , 0) , 0) ) WHEN 2 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimpv2 / Nullif(f.facturatotalv2 , 0), 0) ) WHEN 3 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimpv3 / Nullif(f.facturatotalv3 , 0), 0) ) END
  ```

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_DETALLE_ALL]]
- [[dbo.BI_FACTURA_ENCABEZADO_ALL]]
- [[dbo.V_COBRANZAS_BASE]]
- [[dbo.V_FACTURACION_BDDD]]
- [[dbo.V_FACTURACION_ESTADO_BDDD]]
- [[dbo.V_NOTASCREDITO]]
- [[dbo.V_RECIBO]]
- [[dbo.vContratos_MF_Cuota1]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
- [[dbo.v_Segmentacion]]
