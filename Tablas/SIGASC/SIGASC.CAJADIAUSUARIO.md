---
esquema: SIGASC
tabla: CAJADIAUSUARIO
objeto: SIGASC.CAJADIAUSUARIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKCAJADIAUSUARIO` (único en muestra de 200)
n_columnas: 13
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CAJADIAUSUARIO

> **BASE TABLE** · Dominio: **Core SIGA** · 13 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKCAJADIAUSUARIO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKCAJADIAUSUARIO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `CAJADIAFCH` | datetime2 | 0% |
| 4 | `CAJANRO` | int | 0% |
| 5 | `CAJADIAUSR` | varchar | 0% |
| 6 | `MEDCOBROCAJA` | int | 0% |
| 7 | `CAJADIAUSRSTS` | varchar | 0% |
| 8 | `CAJADIAUSRFCHCIERRE` | datetime2 | 100% |
| 9 | `CAJADIAUSRUSRCIERRE` | varchar | 0% |
| 10 | `PIPELINERUNID` | varchar | 0% |
| 11 | `PKCAJANRO` | varchar | 0% |
| 12 | `PKCAJADIAUSR` | varchar | 0% |
| 13 | `PKMEDCOBROCAJA` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CAJANRO` (int) → [[clave-CAJANRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCAJANRO` (varchar) → [[clave-PKCAJANRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
