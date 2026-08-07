---
esquema: SIGASC
tabla: RECIBO
objeto: SIGASC.RECIBO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)
n_columnas: 34
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.RECIBO

> **BASE TABLE** · Dominio: **Core SIGA** · 34 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `RECIBONRO` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `RECIBOFCH` | datetime2 | 0% |
| 5 | `RECIBOHORA` | datetime2 | 100% |
| 6 | `RECIBOSTS` | varchar | 0% |
| 7 | `MEDCOBRBO` | int | 0% |
| 8 | `MONEDAID` | int | 0% |
| 9 | `RECIBOIMP` | real | 0% |
| 10 | `RECIBOSDO` | real | 0% |
| 11 | `RECIBOUSR` | varchar | 0% |
| 12 | `RECIBOGEN` | varchar | 0% |
| 13 | `RECIBOFCHCOB` | datetime2 | 0% |
| 14 | `CAJANRO` | int | 0% |
| 15 | `RECIBOCXLUSR` | varchar | 0% |
| 16 | `RECIBOCXLFCH` | datetime2 | 100% |
| 17 | `RECIBOTRNNRO` | varchar | 0% |
| 18 | `RECIBOTPO` | varchar | 0% |
| 19 | `RECIBOCBU` | varchar | 0% |
| 20 | `RECIBOMODALIDAD` | varchar | 0% |
| 21 | `MOTIVOFACID` | int | 0% |
| 22 | `RECIBONRORBO` | int | 0% |
| 23 | `RECIBOCMPTENRO` | int | 0% |
| 24 | `RECIBOCMPTEPTOVTA` | int | 0% |
| 25 | `RECIBOCMPTELETRA` | varchar | 0% |
| 26 | `COBRADORRBOID` | int | 0% |
| 27 | `RECIBOCMPTEEFISCAL` | int | 0% |
| 28 | `RECIBOCMPTEUNIDAD` | int | 0% |
| 29 | `RECIBOCIERRE` | int | 0% |
| 30 | `RECIBODUPLICADO` | varchar | 0% |
| 31 | `RECIBOCLIENTENROAPLICADO` | int | 0% |
| 32 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 33 | `PIPELINERUNID` | varchar | 0% |
| 34 | `PKRECIBONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `RECIBONRO` (int) → [[clave-RECIBONRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `MONEDAID` (int) → [[clave-MONEDAID]]
- `CAJANRO` (int) → [[clave-CAJANRO]]
- `MOTIVOFACID` (int) → [[clave-MOTIVOFACID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKRECIBONRO` (varchar) → [[clave-PKRECIBONRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.RECIBOFAC]] · `RECIBO.RECIBONRO = RECIBOFAC.RECIBONRO` — view_join (v_COBRANZA), alta
- [[SIGAMSASC.EMPRESA]] · `RECIBO.EMPRESAID = EMPRESA.EMPRESAID` — view_join (v_COBRANZA), alta

## Reglas de negocio conocidas
**Filtros**
- 🚦 `r.recibosts <> 'X'` — _de_ [[dbo.v_COBRANZA]]
- `r.recibotpo = 'R'` — _de_ [[dbo.v_COBRANZA]]
- `convert(date, r.recibofch) >= '2022/12/01'` — _de_ [[dbo.v_COBRANZA]]
- `convert(date,r.recibofch) < '2023/01/01'` — _de_ [[dbo.v_COBRANZA]]
- `r.RECIBOFCH >= DATEADD(MM, -17, GETDATE())` — _de_ [[dbo.V_COBRANZAS_1_APL]]
- `r.RECIBOFCH >= DATEADD(MM, -6, GETDATE())` — _de_ [[dbo.V_COBRANZAS_BASE]]
- `CONVERT(DATE,r.RECIBOFCH) >= CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,-13,GETDATE()))-1),DATEADD(mm,-4,GETDATE())),101)` — _de_ [[dbo.V_RECIBO]]

## Vistas que la consumen (referencia)
- [[dbo.V_COBRANZAS_1_APL]]
- [[dbo.V_COBRANZAS_BASE]]
- [[dbo.V_COBRANZAS_MAS_APL]]
- [[dbo.V_RECIBO]]
- [[dbo.v_COBRANZA]]
