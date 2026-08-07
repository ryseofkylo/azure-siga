---
esquema: SIGASC
tabla: TECNICO
objeto: SIGASC.TECNICO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKTECNICOID` (único en muestra de 200)
n_columnas: 24
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.TECNICO

> **BASE TABLE** · Dominio: **Core SIGA** · 24 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKTECNICOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `TECNICOID` | int | 0% |
| 3 | `TECNICONOMBRE` | varchar | 0% |
| 4 | `TECNICOCEL` | varchar | 0% |
| 5 | `TECNICOEMAIL` | varchar | 0% |
| 6 | `TECNICOSMSHAB` | int | 0% |
| 7 | `TECNICORECEPTOR` | varchar | 0% |
| 8 | `TECNICOSTS` | varchar | 0% |
| 9 | `TECNICOUSUARIO` | varchar | 0% |
| 10 | `TECNICOTPO` | varchar | 0% |
| 11 | `TECNICOPADRE` | int | 0% |
| 12 | `TECNICOEMPLEADONRO` | int | 0% |
| 13 | `TECNICOCI` | varchar | 0% |
| 14 | `TECNICOCITPO` | varchar | 0% |
| 15 | `TECNICOPERTENECEID` | int | 48% |
| 16 | `TECNICOCENTROOPERATIVO` | int | 72% |
| 17 | `TECNICOCODEXT` | varchar | 100% |
| 18 | `TECNICOFUNCION` | int | 100% |
| 19 | `TECNICOCONSUMERED` | int | 100% |
| 20 | `TECNICOAUTOINSTALABLE` | int | 100% |
| 21 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 22 | `TECNICODISPATCHER` | int | 99% |
| 23 | `PIPELINERUNID` | varchar | 0% |
| 24 | `PKTECNICOID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TECNICOID` (int) → [[clave-TECNICOID]]
- `TECNICOEMPLEADONRO` (int) → [[clave-TECNICOEMPLEADONRO]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.ORDENSRV]] · `TECNICO.EMPRESAID = ORDENSRV.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.ORDENSRV]] · `TECNICO.TECNICOID = ORDENSRV.TECNICOIDCIERRE` — view_join (DW_ORDENES_TECNICAS_V5), alta

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.DW_ORDENES_TECNICAS_ORDINAL_V1]]
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.V_ORDENESPENDIENTES]]
