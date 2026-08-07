---
esquema: SIGASC
tabla: RECIBOLINEA
objeto: SIGASC.RECIBOLINEA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)
n_columnas: 28
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.RECIBOLINEA

> **BASE TABLE** · Dominio: **Core SIGA** · 28 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKRECIBONRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKRECIBOLINEA` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `RECIBONRO` | int | 0% |
| 4 | `RBOCPGOLINEA` | int | 0% |
| 5 | `CPGOTIPOID` | int | 0% |
| 6 | `CPGOTIPOVALID` | int | 0% |
| 7 | `RBOCPGOMONEDAID` | int | 0% |
| 8 | `RBOCPGOTIPOCAMBIO` | real | 0% |
| 9 | `RBOCPGOIMPORTE` | real | 0% |
| 10 | `RBOCPGOVTO` | datetime2 | 100% |
| 11 | `RBOCPGOCP` | varchar | 0% |
| 12 | `RBOCPGODOCNRO` | varchar | 0% |
| 13 | `RBOCPGOHS` | int | 0% |
| 14 | `RBOCPGOCONTROLSTS` | varchar | 0% |
| 15 | `RBOCPGOCONTROLUSR` | varchar | 0% |
| 16 | `RBOCPGOCONTROLFCH` | datetime2 | 100% |
| 17 | `RBOCPGODOCNROSEG` | varchar | 0% |
| 18 | `RBOCPGOTITULAR` | varchar | 0% |
| 19 | `RBOCPGODNI` | varchar | 0% |
| 20 | `RBOCPGOLOTE` | varchar | 0% |
| 21 | `RBOCPGOCUPON` | varchar | 0% |
| 22 | `RBOCPGOCUIT` | varchar | 0% |
| 23 | `CPGOTIPOVALCUOTAID` | int | 100% |
| 24 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 25 | `RBOCPGODOCNROFIN` | varchar | 100% |
| 26 | `PIPELINERUNID` | varchar | 0% |
| 27 | `PKRBOCPGOLINEA` | varchar | 0% |
| 28 | `PKRECIBONRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `RECIBONRO` (int) → [[clave-RECIBONRO]]
- `CPGOTIPOID` (int) → [[clave-CPGOTIPOID]]
- `CPGOTIPOVALID` (int) → [[clave-CPGOTIPOVALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKRECIBONRO` (varchar) → [[clave-PKRECIBONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_COBRANZAOFICINA]]

## Vistas que la consumen (referencia)
- [[dbo.V_COBRANZAOFICINA]]
