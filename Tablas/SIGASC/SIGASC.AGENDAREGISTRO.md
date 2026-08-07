---
esquema: SIGASC
tabla: AGENDAREGISTRO
objeto: SIGASC.AGENDAREGISTRO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKAGENDANRO` (único en muestra de 200)
n_columnas: 44
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.AGENDAREGISTRO

> **BASE TABLE** · Dominio: **Core SIGA** · 44 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKAGENDANRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKAGENDAREGISTRO` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `AGENDAFECHA` | datetime2 | 0% |
| 4 | `TAREATIPOID` | int | 0% |
| 5 | `TURNOID` | int | 0% |
| 6 | `AGENDANRO` | int | 0% |
| 7 | `TAREAID` | int | 0% |
| 8 | `AGENDAREGCAPACIDAD` | real | 0% |
| 9 | `ZONATPO` | varchar | 0% |
| 10 | `ZONAID` | int | 0% |
| 11 | `TECNICOID` | int | 0% |
| 12 | `AGENDAREGSTATUS` | varchar | 0% |
| 13 | `AGENDAREGFCHING` | datetime2 | 0% |
| 14 | `AGENDAREGHORINI` | datetime2 | 100% |
| 15 | `AGENDAREGHORFIN` | datetime2 | 100% |
| 16 | `AGENDAREGFCHCXL` | datetime2 | 100% |
| 17 | `AGENDAREGNRO` | int | 0% |
| 18 | `AGENDAREGOBS` | varchar | 0% |
| 19 | `AGENDAREGGEN` | varchar | 0% |
| 20 | `AGENDAREGUSRING` | varchar | 0% |
| 21 | `RECURSOID` | int | 0% |
| 22 | `AGENDAREGHORENV` | datetime2 | 100% |
| 23 | `AGENDAREGHORACP` | datetime2 | 100% |
| 24 | `AGENDAREGSOLICITUDUSR` | varchar | 0% |
| 25 | `AGENDAREGSOLICITUDFINALIZADA` | datetime2 | 100% |
| 26 | `AGENDAREGSOLICITUDSTS` | varchar | 0% |
| 27 | `AGENDAREGTIEMPOAGR` | int | 0% |
| 28 | `AGENDAREGCONFIRMADAFCH` | datetime2 | 100% |
| 29 | `AGENDAREGCONFIRMADA` | int | 0% |
| 30 | `AGENDAREGSOLICITUDCONFFCH` | datetime2 | 100% |
| 31 | `AGENDAREGSOLICITUDCONF` | int | 0% |
| 32 | `AGENDAREGTECNICOCEL` | varchar | 0% |
| 33 | `AGENDAREGORDENNRO` | int | 0% |
| 34 | `TECNICO2ID` | int | 0% |
| 35 | `AFBIENID` | int | 0% |
| 36 | `AGENDAREGSOLICITUDSTSV2` | varchar | 0% |
| 37 | `AGENDAREGORDENTAREA` | int | 0% |
| 38 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 39 | `AGENDAREGHORNOTIFICADA` | datetime2 | 100% |
| 40 | `AGENDAREGNOTIFICADA` | int | 94% |
| 41 | `PIPELINERUNID` | varchar | 0% |
| 42 | `PKTAREATIPOID` | varchar | 0% |
| 43 | `PKTURNOID` | varchar | 0% |
| 44 | `PKAGENDANRO` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TAREATIPOID` (int) → [[clave-TAREATIPOID]]
- `TURNOID` (int) → [[clave-TURNOID]]
- `TAREAID` (int) → [[clave-TAREAID]]
- `TECNICOID` (int) → [[clave-TECNICOID]]
- `RECURSOID` (int) → [[clave-RECURSOID]]
- `TECNICO2ID` (int) → [[clave-TECNICO2ID]]
- `AFBIENID` (int) → [[clave-AFBIENID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKTAREATIPOID` (varchar) → [[clave-PKTAREATIPOID]]
- `PKTURNOID` (varchar) → [[clave-PKTURNOID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
