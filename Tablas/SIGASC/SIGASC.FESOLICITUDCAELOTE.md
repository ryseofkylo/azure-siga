---
esquema: SIGASC
tabla: FESOLICITUDCAELOTE
objeto: SIGASC.FESOLICITUDCAELOTE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKFELOTENRO` (único en muestra de 200)
n_columnas: 17
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FESOLICITUDCAELOTE

> **BASE TABLE** · Dominio: **Core SIGA** · 17 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKFELOTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKFESOLICITUDCAELOTE` | varchar | 0% |
| 2 | `FEEMPRESAFISCALID` | int | 0% |
| 3 | `FEPUNTOVENTA` | int | 0% |
| 4 | `FECMPTETIPO` | int | 0% |
| 5 | `FELOTENRO` | int | 0% |
| 6 | `FELOTENOMBRE` | varchar | 0% |
| 7 | `FELOTEESTADO` | varchar | 0% |
| 8 | `FELOTECMPTENRODESDE` | int | 0% |
| 9 | `FELOTECMPTENROHASTA` | int | 0% |
| 10 | `FELOTEUSUARIO` | varchar | 0% |
| 11 | `FELOTEFCH` | datetime2 | 0% |
| 12 | `FELOTETIPO` | varchar | 0% |
| 13 | `FELOTECONDICIONIVAREC` | int | 90% |
| 14 | `PIPELINERUNID` | varchar | 0% |
| 15 | `PKFEPUNTOVENTA` | varchar | 0% |
| 16 | `PKFECMPTETIPO` | varchar | 0% |
| 17 | `PKFELOTENRO` | varchar | 0% |

## Claves de join presentes
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
