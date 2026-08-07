---
esquema: SIGASC
tabla: MEDIOCOBRO
objeto: SIGASC.MEDIOCOBRO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `MEDCOBROID` (único en muestra de 200)
n_columnas: 19
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.MEDIOCOBRO

> **BASE TABLE** · Dominio: **Core SIGA** · 19 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `MEDCOBROID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `MEDCOBROID` | int | 0% |
| 2 | `MEDCOBRONOMBRE` | varchar | 0% |
| 3 | `MEDCOBROTPO` | varchar | 0% |
| 4 | `MEDCOBROPGMCHK` | varchar | 0% |
| 5 | `MEDCOBROPGMDEBENVIO` | varchar | 0% |
| 6 | `MEDCOBROPGMDEBRETORNO` | varchar | 0% |
| 7 | `MEDCOBROPGMDEBPADRON` | varchar | 0% |
| 8 | `MEDCOBROUSUARIO` | varchar | 0% |
| 9 | `MEDCOBROPGMDEBCARGA` | varchar | 0% |
| 10 | `MEDCOBROPGMDEBCONCILIA` | varchar | 0% |
| 11 | `MEDCOBROPGMDEBNOVEDADES` | varchar | 0% |
| 12 | `MEDCOBRORESTRINGEUNIDAD` | int | 0% |
| 13 | `MEDCOBROFORMATO` | varchar | 86% |
| 14 | `MEDCOBRODIGITOMAX` | int | 14% |
| 15 | `MEDCOBRODIGITOMIN` | int | 14% |
| 16 | `MEDCOBROFCHALTA` | datetime2 | 0% |
| 17 | `MEDCOBROMULTIEMPRESA` | int | 98% |
| 18 | `MEDCOBROCICLOID` | int | 100% |
| 19 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `MEDCOBROID` (int) → [[clave-MEDCOBROID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.VM_CLIENTE]] · `MEDIOCOBRO.MEDCOBROID = VM_CLIENTE.MEDCOBROID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta
- [[BIGDATA.AGRUPACIONMEDCOBROBD]] · `MEDIOCOBRO.MEDCOBROID = AGRUPACIONMEDCOBROBD.MEDIOCOBROIDBD` — view_join (V_MEDIOCOBRO), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_MEDIOCOBRO]]

**Derivaciones (CASE)**
- _de_ [[dbo.BI_FACTURA_ENCABEZADO_ALL]]:
  ```sql
  case mcob.medcobrotpo when 'B' then 'ADHERIDO' when 'T' then 'ADHERIDO' when 'N' then 'ADHERIDO' else 'NO ADHERIDO' End
  ```

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_ENCABEZADO_ALL]]
- [[dbo.V_MEDIOCOBRO]]
