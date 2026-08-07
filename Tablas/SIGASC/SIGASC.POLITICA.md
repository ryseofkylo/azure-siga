---
esquema: SIGASC
tabla: POLITICA
objeto: SIGASC.POLITICA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPOLITICAID` (único en muestra de 200)
n_columnas: 26
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.POLITICA

> **BASE TABLE** · Dominio: **Core SIGA** · 26 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPOLITICAID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `POLITICAID` | int | 0% |
| 3 | `POLITICANOMBRE` | varchar | 0% |
| 4 | `POLITICASTS` | varchar | 0% |
| 5 | `POLITICAREQAUT` | int | 0% |
| 6 | `POLITICAMESVIG` | int | 0% |
| 7 | `POLITICAPORZONA` | int | 0% |
| 8 | `POLITICAULTLIN` | int | 0% |
| 9 | `POLITICATPOCLIENTE` | int | 0% |
| 10 | `POLITICADIASPRORRATEO` | varchar | 0% |
| 11 | `MONEDAPOL` | int | 0% |
| 12 | `POLITICATPO` | varchar | 0% |
| 13 | `POLITICACOMBO` | int | 0% |
| 14 | `MONEDAFAC` | int | 0% |
| 15 | `POLITICAREQDEBITO` | int | 0% |
| 16 | `POLITICAFACTURACOMBO` | int | 0% |
| 17 | `POLITICACONSUCURSAL` | int | 0% |
| 18 | `POLITICAREQEFECTIVO` | int | 0% |
| 19 | `POLITICAPERMITECNTPREVENTA` | int | 0% |
| 20 | `POLITICATPOSERVICIO` | varchar | 0% |
| 21 | `POLITICACARTELERAACTIVA` | int | 99% |
| 22 | `POLITICACARTELERANOMBRE` | varchar | 99% |
| 23 | `POLITICAREQPLAN` | int | 0% |
| 24 | `POLITICAREQPROMOTOR` | int | 0% |
| 25 | `PIPELINERUNID` | varchar | 0% |
| 26 | `PKPOLITICAID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPOLITICAID` (varchar) → [[clave-PKPOLITICAID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.FACTURA]] · `POLITICA.EMPRESAID = FACTURA.EMPRESAID` — view_join (BI_FACTURA_DETALLE_ALL), alta

## Reglas de negocio conocidas
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]]

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_DETALLE_ALL]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
