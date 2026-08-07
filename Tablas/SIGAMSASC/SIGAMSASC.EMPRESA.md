---
esquema: SIGAMSASC
tabla: EMPRESA
objeto: SIGAMSASC.EMPRESA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `EMPRESAID` (único en muestra de 29)
n_columnas: 10
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.EMPRESA

> **BASE TABLE** · Dominio: **Core SIGA** · 10 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `EMPRESAID` (único en muestra de 29)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `EMPRESANOM` | varchar | 0% |
| 3 | `PAISID` | int | 0% |
| 4 | `EMPLOGOID` | int | 0% |
| 5 | `EMPRESARAZONSOCIAL` | varchar | 0% |
| 6 | `EMPRESARUT` | varchar | 0% |
| 7 | `EMPRESADIRECCION` | varchar | 0% |
| 8 | `EMPRESADEVENGAVTO` | int | 0% |
| 9 | `EMPRESAFCHACTUALIZACION` | datetime2 | 83% |
| 10 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PAISID` (int) → [[clave-PAISID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.FACTURA]] · `EMPRESA.EMPRESAID = FACTURA.EMPRESAID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[SIGASC.RECIBO]] · `EMPRESA.EMPRESAID = RECIBO.EMPRESAID` — view_join (v_COBRANZA), alta

## Reglas de negocio conocidas
**Filtros**
- `e.empresaid <> '23'` — _de_ [[dbo.V_SEGMENTOCLIENTE]]
- `e.empresaid = '23'` — _de_ [[dbo.V_SEGMENTOCLIENTE]]

**Derivaciones (CASE)**
- _de_ [[dbo.DW_ORDENES_TECNICAS_V5]]:
  ```sql
  case O.EMPRESAID WHEN 21 THEN 'SUPERCANAL CATAMARCA' ELSE TRIM(EMP.EMPRESANOM) END
  ```
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
- [[dbo.BI_FACTURA_ENCABEZADO_ALL]]
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
- [[dbo.V_COBRANZAS_BASE]]
- [[dbo.V_EMPRESA]]
- [[dbo.V_NOTASCREDITO]]
- [[dbo.V_SEGMENTOCLIENTE]]
- [[dbo.v_COBRANZA]]
