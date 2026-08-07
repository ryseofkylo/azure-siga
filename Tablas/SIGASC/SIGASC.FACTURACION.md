---
esquema: SIGASC
tabla: FACTURACION
objeto: SIGASC.FACTURACION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`FACTURANRO`) — compuesto, tentativo (muestra 10)
n_columnas: 88
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURACION

> **BASE TABLE** · Dominio: **Core SIGA** · 88 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`FACTURANRO`) — compuesto, tentativo (muestra 10)

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
| 9 | `FACTURAFCOB` | datetime2 | 8% |
| 10 | `FACTURAFICOB` | datetime2 | 8% |
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
| 31 | `FACTURACAVTO` | datetime2 | 0% |
| 32 | `FACTURASDO` | real | 0% |
| 33 | `MOTIVOFACID` | int | 0% |
| 34 | `CMPTEEFISCAL` | int | 0% |
| 35 | `FACTURACONDICIONIVA` | int | 0% |
| 36 | `FACTURAFCHHORA` | datetime2 | 0% |
| 37 | `FACTURAINSERT4` | varchar | 0% |
| 38 | `FACTURAINSERT3` | varchar | 0% |
| 39 | `FACTURAINSERT2` | varchar | 0% |
| 40 | `FACTURAINSERT1` | varchar | 0% |
| 41 | `FACTURACARTA` | varchar | 0% |
| 42 | `FACTURATOTAL` | real | 0% |
| 43 | `FACTURATOTALV2` | real | 0% |
| 44 | `FACTURATOTALV3` | real | 0% |
| 45 | `FACTURABARRIOID` | int | 0% |
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
| 62 | `FACTURAESTADOID` | int | 0% |
| 63 | `FACTURAEDIFICIONRO` | int | 0% |
| 64 | `FACTURAUBITPO` | varchar | 0% |
| 65 | `FACTURATOTALDEV` | real | 0% |
| 66 | `FACTURATOTALREFINANCIA` | real | 0% |
| 67 | `FACTURAFCHPRESCRIPTA` | datetime2 | 100% |
| 68 | `FACTURALINK` | varchar | 0% |
| 69 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 70 | `PIPELINERUNID` | varchar | 0% |
| 71 | `PKFACTURATPO` | varchar | 0% |
| 72 | `PKFACTURANRO` | varchar | 0% |
| 73 | `PKFACTURALIN` | nvarchar | 0% |
| 74 | `CPTOFACID` | int | 0% |
| 75 | `FACTURAPRJIVA` | real | 0% |
| 76 | `FACTURALINCUO` | nvarchar | 0% |
| 77 | `FACTURALINIMP` | real | 0% |
| 78 | `FACTURALINCOD` | int | 0% |
| 79 | `FACTURAPOL` | int | 0% |
| 80 | `FACTURAPRM` | int | 0% |
| 81 | `FACTURALINTPO` | nvarchar | 0% |
| 82 | `FACTURALINIMPV2` | real | 0% |
| 83 | `FACTURALINIMPV3` | real | 0% |
| 84 | `FACTURALINCNT` | int | 0% |
| 85 | `FACTURAAFIPIVAID` | int | 0% |
| 86 | `FACTURACMB` | int | 0% |
| 87 | `FACTURALINIVAIMP` | real | 0% |
| 88 | `PKPRODUCTOID` | nvarchar | 2% |

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
- `PKFACTURALIN` (nvarchar) → [[clave-PKFACTURALIN]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `PKPRODUCTOID` (nvarchar) → [[clave-PKPRODUCTOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.RECIBOFAC]] · `FACTURACION.FACTURANRO = RECIBOFAC.FACTURANRO` — view_join (v_COBRANZA), alta

## Reglas de negocio conocidas
**Filtros**
- `f.facturatpo IN ('F','N','D')` — _de_ [[dbo.V_FACTURACION]]
- `f.facturacatpo = 'E'` — _de_ [[dbo.V_FACTURACION]]
- `f.facturacc = 1` — _de_ [[dbo.V_FACTURACION]]
- `e.facturatpo = 'F'` — _de_ [[dbo.V_ULTIMAFACTURACION]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_ULTIMAFACTURACION]]

**Derivaciones (CASE)**
- _de_ [[dbo.v_COBRANZA]]:
  ```sql
  CASE e.empresadevengavto WHEN 1 THEN f.facturalinimp WHEN 2 THEN f.facturalinimpv2 WHEN 3 THEN f.facturalinimpv3 END
  ```
- _de_ [[dbo.v_COBRANZA]]:
  ```sql
  CASE e.empresadevengavto WHEN 1 THEN ( f.facturalinimp / f.facturatotal ) WHEN 2 THEN ( f.facturalinimpv2 / f.facturatotalv2 ) WHEN 3 THEN ( f.facturalinimpv3 / f.facturatotalv3 ) END
  ```
- _de_ [[dbo.v_COBRANZA]]:
  ```sql
  CASE e.empresadevengavto WHEN 1 THEN ( b.recibofacimp * ( f.facturalinimp / f.facturatotal ) ) WHEN 2 THEN ( b.recibofacimp * ( f.facturalinimpv2 / f.facturatotalv2 ) ) WHEN 3 THEN ( b.recibofacimp * ( f.facturalinimpv3 / f.facturatotalv3 ) ) END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_FACTURACION]]
- [[dbo.V_FACTURACION_2]]
- [[dbo.V_FACTURACION_PERIODO]]
- [[dbo.V_OTRA_FACTURACION]]
- [[dbo.V_ULTIMAFACTURACION]]
- [[dbo.v_COBRANZA]]
