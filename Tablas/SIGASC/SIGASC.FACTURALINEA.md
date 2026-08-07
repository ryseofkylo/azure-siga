---
esquema: SIGASC
tabla: FACTURALINEA
objeto: SIGASC.FACTURALINEA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKFACTURANRO` (único en muestra de 200)
n_columnas: 24
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURALINEA

> **BASE TABLE** · Dominio: **Core SIGA** · 24 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKFACTURANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKFACTURALINEA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `FACTURATPO` | varchar | 0% |
| 4 | `FACTURANRO` | int | 0% |
| 5 | `FACTURALIN` | int | 0% |
| 6 | `CPTOFACID` | int | 0% |
| 7 | `FACTURAPRJIVA` | real | 0% |
| 8 | `FACTURALINCUO` | varchar | 0% |
| 9 | `FACTURALINIMP` | real | 0% |
| 10 | `FACTURALINCOD` | int | 0% |
| 11 | `FACTURAPOL` | int | 0% |
| 12 | `FACTURAPRM` | int | 0% |
| 13 | `FACTURALINTPO` | varchar | 0% |
| 14 | `FACTURALINIMPV2` | real | 0% |
| 15 | `FACTURALINIMPV3` | real | 0% |
| 16 | `FACTURALINCNT` | int | 0% |
| 17 | `FACTURAAFIPIVAID` | int | 0% |
| 18 | `FACTURACMB` | int | 0% |
| 19 | `FACTURALINIVAIMP` | real | 0% |
| 20 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 21 | `PIPELINERUNID` | varchar | 0% |
| 22 | `PKFACTURATPO` | varchar | 0% |
| 23 | `PKFACTURANRO` | varchar | 0% |
| 24 | `PKFACTURALIN` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `FACTURATPO` (varchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (int) → [[clave-FACTURANRO]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKFACTURATPO` (varchar) → [[clave-PKFACTURATPO]]
- `PKFACTURANRO` (varchar) → [[clave-PKFACTURANRO]]
- `PKFACTURALIN` (varchar) → [[clave-PKFACTURALIN]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.FACTURA]] · `FACTURALINEA.FACTURATPO = FACTURA.FACTURATPO` — view_join (BI_FACTURA_DETALLE_ALL), alta
- [[SIGASC.FACTURA]] · `FACTURALINEA.FACTURANRO = FACTURA.FACTURANRO` — view_join (V_COBRANZAS_BASE), alta
- [[SIGASC.VM_CLIENTE]] · `FACTURALINEA.CLIENTENRO = VM_CLIENTE.CLIENTENRO` — view_join (v_Segmentacion), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]], [[dbo.v_Segmentacion]]

**Derivaciones (CASE)**
- _de_ [[dbo.BI_FACTURA_DETALLE_ALL]]:
  ```sql
  case when d.facturalincuo is null or len(ltrim(rtrim(d.facturalincuo))) =0 or PATINDEX('%/%',ltrim(rtrim(d.facturalincuo))) =0 OR ISNUMERIC(left(ltrim(rtrim(d.facturalincuo)), PATINDEX('%/%',ltrim(rtrim(d.facturalincuo)))-1))=0 then null else left(ltrim(rtrim(d.facturalincuo)), PATINDEX('%/%',ltrim(rtrim(d.facturalincuo)))-1) end
  ```
- _de_ [[dbo.BI_FACTURA_DETALLE_ALL]]:
  ```sql
  case when d.facturalincuo is null or len(ltrim(rtrim(d.facturalincuo))) =0 or PATINDEX('%/%',ltrim(rtrim(d.facturalincuo))) =0 OR ISNUMERIC(right(ltrim(rtrim(d.facturalincuo)), len(ltrim(rtrim(d.facturalincuo))) - PATINDEX('%/%',ltrim(rtrim(d.facturalincuo))))) = 0 then null else right(ltrim(rtrim(d.facturalincuo)), len(ltrim(rtrim(d.facturalincuo))) - PATINDEX('%/%',ltrim(rtrim(d.facturalincuo)))) end
  ```
- _de_ [[dbo.V_COBRANZAS_BASE]]:
  ```sql
  CASE e.empresadevengavto WHEN 1 THEN l.facturalinimp WHEN 2 THEN l.facturalinimpv2 WHEN 3 THEN l.facturalinimpv3 END
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
- [[dbo.V_COBRANZAS_BASE]]
- [[dbo.vContratos_MF_Cuota1]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
- [[dbo.v_Segmentacion]]
