---
esquema: SIGASC
tabla: FACTURARESUMENCOMPLE
objeto: SIGASC.FACTURARESUMENCOMPLE
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTENRO` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.FACTURARESUMENCOMPLE

> **BASE TABLE** · Dominio: **Core SIGA** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTENRO` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `PERIODO` | int | 0% |
| 4 | `CONTRATOS` | int | 0% |
| 5 | `SUMA_CONTRATOS` | bigint | 0% |
| 6 | `SUMA_POLITICAS` | bigint | 0% |
| 7 | `SUMA_PROMOCIONES` | bigint | 0% |
| 8 | `CLASEPRODUCTO` | int | 0% |
| 9 | `FACTURACION` | float | 0% |
| 10 | `PERIODOANTERIOR` | int | 0% |
| 11 | `IMPORTE_POL` | float | 0% |
| 12 | `IMPORTE_PRM` | float | 0% |
| 13 | `ESCALON` | int | 0% |
| 14 | `ESBAJA` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas

**Derivaciones (CASE)**
- _de_ [[dbo.V_ANALISISFAC_CONBAJAS_COMPLE]]:
  ```sql
  CASE WHEN ( f.suma_contratos <> c.suma_contratos ) THEN 'Y' ELSE 'N' END
  ```
- _de_ [[dbo.V_ANALISISFAC_CONBAJAS_COMPLE]]:
  ```sql
  CASE WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) > ROUND(ISNULL(c.facturacion,0),0,1) ) THEN 'Aumenta' WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) < ROUND(ISNULL(c.facturacion,0),0,1) ) THEN 'Disminuye' ELSE 'No varia' END
  ```
- _de_ [[dbo.V_ANALISISFAC_CONBAJAS_COMPLE]]:
  ```sql
  CASE WHEN ( ROUND(ISNULL(f.facturacion,0),0,1) = 0 ) THEN 'Facturacion en cero' END
  ```
- _de_ [[dbo.V_ANALISISFAC_CONBAJAS_COMPLE]]:
  ```sql
  CASE WHEN ( f.suma_politicas <> c.suma_politicas ) THEN 'Y' ELSE 'N' END
  ```
- _de_ [[dbo.V_ANALISISFAC_CONBAJAS_COMPLE]]:
  ```sql
  CASE WHEN ( ( c.clientenro IS NULL ) OR ( c.esbaja = 'Y' ) ) THEN 'Alta' WHEN ( f.esbaja = 'Y' ) THEN 'Baja' END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_ANALISISFAC_CONBAJAS_COMPLE]]
