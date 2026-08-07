---
esquema: SIGASC
tabla: FACTURA_OPT
objeto: SIGASC.FACTURA_OPT
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PK_FACTURA` (único en muestra de 200)
n_columnas: 70
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURA_OPT

> **BASE TABLE** · Dominio: **Core SIGA** · 70 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PK_FACTURA` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `PK_FACTURA` | nvarchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `FACTURATPO` | nvarchar | 0% |
| 4 | `FACTURANRO` | nvarchar | 0% |
| 5 | `CLIENTENRO` | int | 0% |
| 6 | `FACTURASTS` | nvarchar | 0% |
| 7 | `FACTURAFCH` | datetime2 | 0% |
| 8 | `FACTURAVTO` | datetime2 | 0% |
| 9 | `FACTURAFCOB` | datetime2 | 9% |
| 10 | `FACTURAFICOB` | datetime2 | 9% |
| 11 | `FACTURAPRN` | int | 0% |
| 12 | `MONEDAID` | int | 0% |
| 13 | `FACTURAUSR` | nvarchar | 0% |
| 14 | `MEDCOBFAC` | int | 0% |
| 15 | `COBRADORID` | int | 0% |
| 16 | `FACTURAGEN` | nvarchar | 0% |
| 17 | `FACTURANRONC` | int | 0% |
| 18 | `FACTURAULTLIN` | int | 0% |
| 19 | `CMPTEUNIDAD` | int | 0% |
| 20 | `CMPTELETRA` | nvarchar | 0% |
| 21 | `CMPTEPTOVTA` | int | 0% |
| 22 | `CMPTENRO` | int | 0% |
| 23 | `FACTURAPERIODO` | int | 0% |
| 24 | `FACTURARUT` | nvarchar | 0% |
| 25 | `FACTURAVTO2` | datetime2 | 0% |
| 26 | `FACTURAVTO3` | datetime2 | 0% |
| 27 | `FACTURACC` | int | 0% |
| 28 | `FACTURACATPO` | nvarchar | 0% |
| 29 | `FACTURACANRO` | nvarchar | 0% |
| 30 | `CMPTETIPO` | int | 0% |
| 31 | `FACTURACAVTO` | datetime2 | 100% |
| 32 | `FACTURASDO` | real | 0% |
| 33 | `MOTIVOFACID` | int | 0% |
| 34 | `CMPTEEFISCAL` | int | 0% |
| 35 | `FACTURACONDICIONIVA` | int | 0% |
| 36 | `FACTURAFCHHORA` | datetime2 | 0% |
| 37 | `FACTURAINSERT4` | nvarchar | 100% |
| 38 | `FACTURAINSERT3` | nvarchar | 100% |
| 39 | `FACTURAINSERT2` | nvarchar | 100% |
| 40 | `FACTURAINSERT1` | nvarchar | 100% |
| 41 | `FACTURACARTA` | nvarchar | 100% |
| 42 | `FACTURATOTAL` | real | 0% |
| 43 | `FACTURATOTALV2` | real | 0% |
| 44 | `FACTURATOTALV3` | real | 0% |
| 45 | `FACTURABARRIOID` | int | 100% |
| 46 | `FACTURACP` | nvarchar | 0% |
| 47 | `FACTURACLIENTENOM` | nvarchar | 0% |
| 48 | `FACTURACLIENTEAPE` | nvarchar | 0% |
| 49 | `FACTURAGEOINI` | nvarchar | 0% |
| 50 | `FACTURAGEOMAN` | int | 0% |
| 51 | `FACTURAGEODIV2` | int | 0% |
| 52 | `FACTURAGEODIV1` | int | 0% |
| 53 | `FACTURACALLEUBICACION` | nvarchar | 0% |
| 54 | `FACTURAMANZANA` | nvarchar | 0% |
| 55 | `FACTURATORRE` | nvarchar | 0% |
| 56 | `FACTURAPISO` | nvarchar | 0% |
| 57 | `FACTURACASA` | nvarchar | 0% |
| 58 | `FACTURAAPTO` | nvarchar | 0% |
| 59 | `FACTURAPUERTA` | nvarchar | 0% |
| 60 | `FACTURACALLEID` | int | 0% |
| 61 | `FACTURACIUDADID` | int | 0% |
| 62 | `FACTURAESTADOID` | int | 100% |
| 63 | `FACTURAEDIFICIONRO` | int | 0% |
| 64 | `FACTURAUBITPO` | nvarchar | 100% |
| 65 | `FACTURATOTALDEV` | real | 0% |
| 66 | `FACTURATOTALREFINANCIA` | real | 100% |
| 67 | `FACTURAFCHPRESCRIPTA` | datetime2 | 100% |
| 68 | `FACTURALINK` | nvarchar | 100% |
| 69 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 70 | `PIPELINERUNID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `FACTURATPO` (nvarchar) → [[clave-FACTURATPO]]
- `FACTURANRO` (nvarchar) → [[clave-FACTURANRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `MONEDAID` (int) → [[clave-MONEDAID]]
- `COBRADORID` (int) → [[clave-COBRADORID]]
- `CMPTENRO` (int) → [[clave-CMPTENRO]]
- `FACTURACANRO` (nvarchar) → [[clave-FACTURACANRO]]
- `MOTIVOFACID` (int) → [[clave-MOTIVOFACID]]
- `FACTURABARRIOID` (int) → [[clave-FACTURABARRIOID]]
- `FACTURACALLEID` (int) → [[clave-FACTURACALLEID]]
- `FACTURACIUDADID` (int) → [[clave-FACTURACIUDADID]]
- `FACTURAESTADOID` (int) → [[clave-FACTURAESTADOID]]
- `FACTURAEDIFICIONRO` (int) → [[clave-FACTURAEDIFICIONRO]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
