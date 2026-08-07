---
esquema: SIGASC
tabla: AFBIEN
objeto: SIGASC.AFBIEN
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKAFBIENID` (único en muestra de 200)
n_columnas: 22
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.AFBIEN

> **BASE TABLE** · Dominio: **Core SIGA** · 22 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKAFBIENID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `AFBIENID` | int | 0% |
| 3 | `AFBIENNOMBRE` | varchar | 0% |
| 4 | `AFBIENIDINTERNO` | varchar | 0% |
| 5 | `AFBIENIDINTERNONUM` | int | 0% |
| 6 | `AFBIENTIPOID` | int | 0% |
| 7 | `AFBIENTIPOSUBID` | int | 0% |
| 8 | `AFBIENESTADO` | varchar | 0% |
| 9 | `AFBIENINGRESO` | varchar | 0% |
| 10 | `PROVEEDORID` | int | 0% |
| 11 | `MONEDAID` | int | 0% |
| 12 | `AFBIENIMPORTE` | real | 96% |
| 13 | `CENTROSTKID` | int | 1% |
| 14 | `AFBIENFCHALTA` | datetime2 | 0% |
| 15 | `AFBIENUSUARIOALTA` | varchar | 0% |
| 16 | `AFBIENOBS` | varchar | 61% |
| 17 | `AFBIENFCHBAJA` | datetime2 | 100% |
| 18 | `AFBIENUSUARIOBAJA` | varchar | 96% |
| 19 | `AFBIENULTIMOEVENTO` | int | 3% |
| 20 | `AFBIENFOTO` | int | 22% |
| 21 | `PIPELINERUNID` | varchar | 0% |
| 22 | `PKAFBIENID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `AFBIENID` (int) → [[clave-AFBIENID]]
- `MONEDAID` (int) → [[clave-MONEDAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
