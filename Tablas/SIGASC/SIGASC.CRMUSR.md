---
esquema: SIGASC
tabla: CRMUSR
objeto: SIGASC.CRMUSR
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKCRMUSR` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CRMUSR

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKCRMUSR` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CRMUSR` | varchar | 0% |
| 3 | `CRMUSRNOMBRE` | varchar | 0% |
| 4 | `CRMINTERNO` | int | 0% |
| 5 | `CRMCTISTS` | varchar | 0% |
| 6 | `CRMCTITXT` | varchar | 0% |
| 7 | `CRMCTIFH` | datetime2 | 0% |
| 8 | `CRMUSRMEDIO` | varchar | 0% |
| 9 | `CRMUSRTIPO` | varchar | 0% |
| 10 | `CRMOUTFH` | datetime2 | 100% |
| 11 | `CRMOUTARCAUDIO` | varchar | 40% |
| 12 | `CRMOUTCALLERID` | varchar | 40% |
| 13 | `PIPELINERUNID` | varchar | 0% |
| 14 | `PKCRMUSR` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKCRMUSR` (varchar) → [[clave-PKCRMUSR]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
