---
esquema: SIGASC
tabla: RECIBOFAC
objeto: SIGASC.RECIBOFAC
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.RECIBOFAC

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKRECIBOFAC` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `RECIBONRO` | int | 0% |
| 4 | `FACTURATPO` | varchar | 0% |
| 5 | `FACTURANRO` | int | 0% |
| 6 | `RECIBOFACIMP` | real | 0% |
| 7 | `RECIBOFACIMPRBO` | real | 0% |
| 8 | `RECIBOFACIMPTPO` | varchar | 0% |
| 9 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 10 | `PIPELINERUNID` | varchar | 0% |
| 11 | `PKFACTURANRO` | varchar | 0% |
| 12 | `PKFACTURATPO` | varchar | 0% |
| 13 | `PKRECIBONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `RECIBONRO` (int) → [[clave-RECIBONRO]]
- `FACTURATPO` (varchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (int) → [[clave-FACTURANRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKFACTURANRO` (varchar) → [[clave-PKFACTURANRO]]
- `PKFACTURATPO` (varchar) → [[clave-PKFACTURATPO]]
- `PKRECIBONRO` (varchar) → [[clave-PKRECIBONRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.RECIBO]] · `RECIBOFAC.RECIBONRO = RECIBO.RECIBONRO` — view_join (v_COBRANZA), alta
- [[SIGASC.FACTURACION]] · `RECIBOFAC.FACTURANRO = FACTURACION.FACTURANRO` — view_join (v_COBRANZA), alta
- [[SIGASC.FACTURA]] · `RECIBOFAC.FACTURANRO = FACTURA.FACTURANRO` — view_join (V_COBRANZAS_BASE), alta

## Reglas de negocio conocidas

**Derivaciones (CASE)**
- _de_ [[dbo.v_COBRANZA]]:
  ```sql
  CASE e.empresadevengavto WHEN 1 THEN ( b.recibofacimp * ( f.facturalinimp / f.facturatotal ) ) WHEN 2 THEN ( b.recibofacimp * ( f.facturalinimpv2 / f.facturatotalv2 ) ) WHEN 3 THEN ( b.recibofacimp * ( f.facturalinimpv3 / f.facturatotalv3 ) ) END
  ```
- _de_ [[dbo.V_COBRANZAS_BASE]]:
  ```sql
  CASE e.empresadevengavto WHEN 1 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimp / Nullif(f.facturatotal , 0) , 0) ) WHEN 2 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimpv2 / Nullif(f.facturatotalv2 , 0), 0) ) WHEN 3 THEN ( b.RECIBOFACIMPRBO * Isnull( l.facturalinimpv3 / Nullif(f.facturatotalv3 , 0), 0) ) END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_COBRANZAS_1_APL]]
- [[dbo.V_COBRANZAS_BASE]]
- [[dbo.V_COBRANZAS_MAS_APL]]
- [[dbo.V_RECIBO]]
- [[dbo.v_COBRANZA]]
