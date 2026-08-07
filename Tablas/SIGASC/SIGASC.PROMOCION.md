---
esquema: SIGASC
tabla: PROMOCION
objeto: SIGASC.PROMOCION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPROMOCIONID` (único en muestra de 200)
n_columnas: 31
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PROMOCION

> **BASE TABLE** · Dominio: **Core SIGA** · 31 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPROMOCIONID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PROMOCIONID` | int | 0% |
| 3 | `PROMOCIONNOMBRE` | varchar | 0% |
| 4 | `PROMOCIONSTS` | varchar | 0% |
| 5 | `PROMOCIONAPLCPTO` | varchar | 0% |
| 6 | `CPTOFACID` | int | 0% |
| 7 | `PROMOCIONCOMBO` | int | 0% |
| 8 | `PROMOCIONTPODTO` | varchar | 0% |
| 9 | `PROMOCIONPERMANENTE` | int | 0% |
| 10 | `PROMOCIONSIMULTANEA` | int | 0% |
| 11 | `PROMOCIONDEBITO` | int | 0% |
| 12 | `PROMOCIONCONSUCURSAL` | int | 0% |
| 13 | `PROMOCIONPRORRATEO` | int | 0% |
| 14 | `PROMOCIONTPODTOPRIORIDAD` | int | 0% |
| 15 | `PROMOCIONCLASE` | varchar | 0% |
| 16 | `PROMOCIONANTIGMIN` | int | 0% |
| 17 | `PROMOCIONREQAUT` | int | 0% |
| 18 | `PROMOCIONEFECTIVO` | int | 0% |
| 19 | `PROMOCIONENFACTURA` | int | 2% |
| 20 | `PROMOCIONNOMBREFAC` | varchar | 85% |
| 21 | `PROMOCIONCARTELERAACTIVA` | int | 100% |
| 22 | `PROMOCIONCARTELERANOMBRE` | varchar | 100% |
| 23 | `PROMOCIONANTIGMAX` | int | 99% |
| 24 | `PROMOCIONTPO` | varchar | 100% |
| 25 | `PROMOCIONREQPLAN` | int | 0% |
| 26 | `PROMOCIONREQPROMOTOR` | int | 0% |
| 27 | `PROMOCIONCARTELERADETALLE` | varchar | 100% |
| 28 | `PIPELINERUNID` | varchar | 0% |
| 29 | `PKPROMOCIONID` | varchar | 0% |
| 30 | `PORTALMIOSEGMENTOID` | int | 0% |
| 31 | `PROMOCIONPORTALDSC` | varchar | 100% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PROMOCIONID` (int) → [[clave-PROMOCIONID]]
- `CPTOFACID` (int) → [[clave-CPTOFACID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPROMOCIONID` (varchar) → [[clave-PKPROMOCIONID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PROMOCIONMES]] · `PROMOCION.PROMOCIONID = PROMOCIONMES.PROMOCIONID` — view_join (v_EscalonPromo), alta
- [[SIGASC.PROMOCIONMES]] · `PROMOCION.EMPRESAID = PROMOCIONMES.EMPRESAID` — view_join (v_EscalonPromo), alta

## Reglas de negocio conocidas
**Filtros**
- `pr.PROMOCIONTPODTO = 'F'` — _de_ [[dbo.vContratos_MF_Cuota1]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_INDICEPROMOCIONMES]], [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]]

**Derivaciones (CASE)**
- _de_ [[dbo.vProyeccion]]:
  ```sql
  CASE when p.PROMOCIONTPODTO = 'F' and d.PRODUCTOTPO in ('B','Z','W') and d.facturatpo = 'F' and d.PROMOID > 0 then 2 when PROMOCIONTPODTO = 'P' and d.PRODUCTOTPO in ('B','Z','W') and d.facturatpo = 'F' and d.PROMOID > 0 then 1 else 0 end
  ```
- _de_ [[dbo.vProyeccion]]:
  ```sql
  CASE when p.promocionclase = 'R' and d.PRODUCTOTPO in ('B','Z','W') and d.facturatpo = 'F' and d.PROMOID > 0 then 2 when p.promocionclase = 'N' and d.PRODUCTOTPO in ('B','Z','W') and d.facturatpo = 'F' and d.PROMOID > 0 then 1 else 0 end
  ```
- _de_ [[dbo.vProyeccion]]:
  ```sql
  CASE when p.PROMOCIONTPODTO = 'F' and d.PRODUCTOTPO in ('C','I','L','E') and d.facturatpo = 'F' and d.PROMOID > 0 then 2 when p.PROMOCIONTPODTO = 'P' and d.PRODUCTOTPO in ('C','I','L','E') and d.facturatpo = 'F' and d.PROMOID > 0 then 1 else 0 end
  ```
- _de_ [[dbo.vProyeccion]]:
  ```sql
  CASE when p.promocionclase = 'R' and d.PRODUCTOTPO in ('C','I','L','E') and d.facturatpo = 'F' and d.PROMOID > 0 then 2 when p.promocionclase = 'N' and d.PRODUCTOTPO in ('C','I','L','E') and d.facturatpo = 'F' and d.PROMOID > 0 then 1 else 0 end
  ```
- _de_ [[dbo.vProyeccion]]:
  ```sql
  CASE when p.PROMOCIONTPODTO = 'F' and d.PRODUCTOTPO in ('N') and d.facturatpo = 'F' and d.PROMOID > 0 then 2 when p.PROMOCIONTPODTO = 'P' and d.PRODUCTOTPO in ('N') and d.facturatpo = 'F' and d.PROMOID > 0 then 1 else 0 end
  ```
- _de_ [[dbo.vProyeccion]]:
  ```sql
  CASE when p.promocionclase = 'R' and d.PRODUCTOTPO in ('N') and d.facturatpo = 'F' and d.PROMOID > 0 then 2 when p.promocionclase = 'N' and d.PRODUCTOTPO in ('N') and d.facturatpo = 'F' and d.PROMOID > 0 then 1 else 0 end
  ```
- _de_ [[dbo.V_PROMOCION]]:
  ```sql
  CASE p.PROMOCIONTPODTO WHEN 'F' THEN 'Monto Fijo' WHEN 'I' THEN 'Importe' WHEN 'P' THEN 'Porcentaje' END
  ```

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_DETALLE_ALL]]
- [[dbo.V_INDICEPROMOCIONMES]]
- [[dbo.V_PROMOCION]]
- [[dbo.vContratos_MF_Cuota1]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
- [[dbo.vProyeccion]]
- [[dbo.v_EscalonPromo]]
- [[dbo.v_promomes]]
