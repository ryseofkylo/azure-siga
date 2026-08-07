---
esquema: SIGASC
tabla: CMPTEPREIMPRESO
objeto: SIGASC.CMPTEPREIMPRESO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCMPTEPREIMPRESONRO` (único en muestra de 200)
n_columnas: 31
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CMPTEPREIMPRESO

> **BASE TABLE** · Dominio: **Core SIGA** · 31 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCMPTEPREIMPRESONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCMPTEPREIMPRESO` | varchar | 0% |
| 2 | `EMPRESAFISCALID` | int | 0% |
| 3 | `CMPTEPREIMPRESOLETRA` | varchar | 0% |
| 4 | `CMPTEPREIMPRESOPTOVTA` | int | 0% |
| 5 | `CMPTEPREIMPRESONRO` | int | 0% |
| 6 | `CMPTEPREIMPRESOENTIDAD` | varchar | 0% |
| 7 | `CMPTEPREIMPRESOSTS` | varchar | 0% |
| 8 | `CMPTEPREIMPRESOFCHING` | datetime2 | 0% |
| 9 | `CMPTEPREIMPRESOFCHVTO` | datetime2 | 100% |
| 10 | `CMPTEPREIMPRESOUSR` | varchar | 0% |
| 11 | `CMPTEPREIMPRESOCAINRO` | varchar | 100% |
| 12 | `CMPTEPREIMPRESOCAIVTO` | datetime2 | 100% |
| 13 | `EMPRESAID` | int | 0% |
| 14 | `COBRADORID` | int | 0% |
| 15 | `CAJAGRUPOID` | int | 100% |
| 16 | `CMPTEPREIMPRESOUSRPRC` | varchar | 100% |
| 17 | `CMPTEPREIMPRESOFCHPRC` | datetime2 | 100% |
| 18 | `CMPTEPREIMPRESOFACTPO` | varchar | 100% |
| 19 | `CMPTEPREIMPRESOFACNRO` | int | 100% |
| 20 | `CMPTEPREIMPRESOCAJANRO` | int | 100% |
| 21 | `CMPTEPREIMPRESOTIPOID` | int | 0% |
| 22 | `CMPTEPREIMPRESOMOTIVOID` | int | 0% |
| 23 | `CMPTEPREIMPRESOOBS` | varchar | 0% |
| 24 | `CMPTEPREIMPRESOANULAFCH` | datetime2 | 100% |
| 25 | `CMPTEPREIMPRESOANULAUSR` | varchar | 0% |
| 26 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 27 | `PIPELINERUNID` | varchar | 0% |
| 28 | `PKCMPTEPREIMPRESOLETRA` | varchar | 0% |
| 29 | `PKCMPTEPREIMPRESOPTOVTA` | varchar | 0% |
| 30 | `PKCMPTEPREIMPRESONRO` | varchar | 0% |
| 31 | `PKCMPTEPREIMPRESOENTIDAD` | varchar | 0% |

## Claves de join presentes
- `EMPRESAFISCALID` (int) → [[clave-EMPRESAFISCALID]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `COBRADORID` (int) → [[clave-COBRADORID]]
- `CAJAGRUPOID` (int) → [[clave-CAJAGRUPOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
