---
esquema: SIGASC
tabla: ORDENTRB
objeto: SIGASC.ORDENTRB
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKORDTRBNRO` (único en muestra de 200)
n_columnas: 58
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ORDENTRB

> **BASE TABLE** · Dominio: **Core SIGA** · 58 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKORDTRBNRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `ORDTRBNRO` | int | 0% |
| 3 | `ORDTRBFCH` | datetime2 | 0% |
| 4 | `TECNICOID` | int | 0% |
| 5 | `ORDTRBCPTOID` | varchar | 0% |
| 6 | `ORDTRBOBS` | varchar | 55% |
| 7 | `CIUDADID` | int | 100% |
| 8 | `ORDTRBEDIFICIONRO` | int | 80% |
| 9 | `ORDTRBFCHINICIAL` | datetime2 | 2% |
| 10 | `ORDTRBFCHFINAL` | datetime2 | 4% |
| 11 | `ORDTRBSTS` | varchar | 0% |
| 12 | `ORDTRBUSRING` | varchar | 0% |
| 13 | `ORDTRBFCHING` | datetime2 | 0% |
| 14 | `ORDTRBUSRAGE` | varchar | 76% |
| 15 | `ORDTRBFCHAGE` | datetime2 | 76% |
| 16 | `ORDTRBUSREMI` | varchar | 76% |
| 17 | `ORDTRBFCHEMI` | datetime2 | 76% |
| 18 | `ORDTRBUSRCUM` | varchar | 75% |
| 19 | `ORDTRBCALID` | int | 80% |
| 20 | `ORDTRBCALPUERTA` | varchar | 80% |
| 21 | `ORDTRBUBICACION` | varchar | 12% |
| 22 | `GEODIV1ID` | int | 80% |
| 23 | `GEODIV2ID` | int | 80% |
| 24 | `GEOMANID` | int | 80% |
| 25 | `GEOMANINI` | varchar | 80% |
| 26 | `ORDTRBCORDY` | varchar | 76% |
| 27 | `ORDTRBCORDX` | varchar | 76% |
| 28 | `ORDTRBHORA` | datetime2 | 0% |
| 29 | `ORDTRBHORAINICIAL` | datetime2 | 10% |
| 30 | `ORDTRBHORAFINAL` | datetime2 | 10% |
| 31 | `ORDTRBCORTE` | int | 66% |
| 32 | `ORDTRBENPROCESO` | varchar | 2% |
| 33 | `ORDTRBFCHCUM` | datetime2 | 75% |
| 34 | `ORDTRBCLIENTENRO` | int | 98% |
| 35 | `ORDTRBCTT` | varchar | 86% |
| 36 | `ORDTRBTEL` | varchar | 100% |
| 37 | `MOTIVOORDID` | int | 3% |
| 38 | `MOTIVOORDORIGENID` | int | 100% |
| 39 | `ORDTRBVINCULO` | int | 100% |
| 40 | `ORDTRBFHUPD` | datetime2 | 92% |
| 41 | `ORDTRBNROEXTERNO` | int | 100% |
| 42 | `ORDTRBCNTRECLAMOS` | int | 76% |
| 43 | `TECNICO2ID` | int | 1% |
| 44 | `AFBIENID` | int | 6% |
| 45 | `PRODUCTIVIDADDIAFCH` | datetime2 | 6% |
| 46 | `PRODUCTIVIDADTURNOID` | int | 6% |
| 47 | `AFBIENIDCIERRE` | int | 6% |
| 48 | `TECNICOIDCIERREAUX` | int | 1% |
| 49 | `TECNICOIDCIERRE` | int | 0% |
| 50 | `PRODUCTIVIDADTURNOIDCIERRE` | int | 6% |
| 51 | `PRODUCTIVIDADDIAFCHCIERRE` | datetime2 | 6% |
| 52 | `ORDTRBARTULTLIN` | int | 70% |
| 53 | `ORDTRBCNTMZNA` | int | 62% |
| 54 | `ORDENTRBSAPCONFIRMADO` | int | 100% |
| 55 | `ORDENTRBPROYECTOSAP` | int | 100% |
| 56 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 57 | `PIPELINERUNID` | varchar | 0% |
| 58 | `PKORDTRBNRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TECNICOID` (int) → [[clave-TECNICOID]]
- `CIUDADID` (int) → [[clave-CIUDADID]]
- `GEODIV1ID` (int) → [[clave-GEODIV1ID]]
- `GEODIV2ID` (int) → [[clave-GEODIV2ID]]
- `GEOMANID` (int) → [[clave-GEOMANID]]
- `MOTIVOORDID` (int) → [[clave-MOTIVOORDID]]
- `MOTIVOORDORIGENID` (int) → [[clave-MOTIVOORDORIGENID]]
- `TECNICO2ID` (int) → [[clave-TECNICO2ID]]
- `AFBIENID` (int) → [[clave-AFBIENID]]
- `TECNICOIDCIERRE` (int) → [[clave-TECNICOIDCIERRE]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKORDTRBNRO` (varchar) → [[clave-PKORDTRBNRO]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.EMPRESASMULTI]] · `ORDENTRB.EMPRESAID = EMPRESASMULTI.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.CENTROOPERATIVOSUCURSAL]] · `ORDENTRB.EMPRESAID = CENTROOPERATIVOSUCURSAL.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.CENTROOPERATIVOSUCURSAL]] · `ORDENTRB.CENTROOPERATIVOID = CENTROOPERATIVOSUCURSAL.CENTROOPERATIVOID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta
- [[SIGASC.VM_CLIENTE]] · `ORDENTRB.EMPRESAID = VM_CLIENTE.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_ORDINAL_V1), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
