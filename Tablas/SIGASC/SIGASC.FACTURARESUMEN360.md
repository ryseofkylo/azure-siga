---
esquema: SIGASC
tabla: FACTURARESUMEN360
objeto: SIGASC.FACTURARESUMEN360
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila ≈ 1 combinación de (`CONTRATONRO`) — compuesto, tentativo (muestra 10)
n_columnas: 18
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURARESUMEN360

> **BASE TABLE** · Dominio: **Core SIGA** · 18 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`CONTRATONRO`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `CONTRATONRO` | int | 0% |
| 4 | `PREVENTAFCHING` | datetime2 | 0% |
| 5 | `PREVENTAFCHFIN` | datetime2 | 0% |
| 6 | `PREVENTAPRODUCTO` | int | 0% |
| 7 | `PERIODO` | int | 0% |
| 8 | `CONTRATOS` | int | 0% |
| 9 | `SUMA_CONTRATOS` | bigint | 0% |
| 10 | `SUMA_POLITICAS` | bigint | 0% |
| 11 | `SUMA_PROMOCIONES` | bigint | 0% |
| 12 | `CLASEPRODUCTO` | int | 0% |
| 13 | `FACTURACION` | float | 0% |
| 14 | `PERIODOANTERIOR` | int | 0% |
| 15 | `IMPORTE_POL` | float | 0% |
| 16 | `IMPORTE_PRM` | float | 0% |
| 17 | `ESCALON` | int | 0% |
| 18 | `ESBAJA` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas

**Derivaciones (CASE)**
- _de_ [[dbo.V_ANALISIS_FAC360]]:
  ```sql
  CASE WHEN ( f.suma_contratos <> c.suma_contratos ) THEN 'Y' ELSE 'N' END
  ```
- _de_ [[dbo.V_ANALISIS_FAC360]]:
  ```sql
  CASE WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) > ROUND(ISNULL(c.facturacion,0),0,1) ) THEN 'Aumenta' WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) < ROUND(ISNULL(c.facturacion,0),0,1) ) THEN 'Disminuye' WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) = 0 ) THEN 'Facturacion en cero' ELSE 'No varia' END
  ```
- _de_ [[dbo.V_ANALISIS_FAC360]]:
  ```sql
  CASE WHEN ( f.suma_politicas <> c.suma_politicas ) THEN 'Y' ELSE 'N' END
  ```
- _de_ [[dbo.V_ANALISIS_FAC360]]:
  ```sql
  CASE WHEN ( ( c.clientenro IS NULL ) OR ( c.esbaja = 'Y' ) ) THEN 'Alta' WHEN ( f.esbaja = 'Y' ) THEN 'Baja' END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_ANALISIS_FAC360]]
