---
esquema: SIGASC
tabla: CLIENTENATURALEZA
objeto: SIGASC.CLIENTENATURALEZA
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `CLIENTENATURALEZAID` (único en muestra de 9)
n_columnas: 3
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.CLIENTENATURALEZA

> **BASE TABLE** · Dominio: **Core SIGA** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CLIENTENATURALEZAID` (único en muestra de 9)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CLIENTENATURALEZAID` | int | 0% |
| 2 | `CLIENTENATURALEZANOM` | varchar | 0% |
| 3 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `CLIENTENATURALEZAID` (int) → [[clave-CLIENTENATURALEZAID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.VM_CLIENTE]] · `CLIENTENATURALEZA.CLIENTENATURALEZAID = VM_CLIENTE.CLIENTENATURALEZAID` — view_join (BI_FACTURA_ENCABEZADO_ALL), alta

## Reglas de negocio conocidas

**Derivaciones (CASE)**
- _de_ [[dbo.V_CATEGORIACLIENTE]]:
  ```sql
  CASE WHEN c.clientenaturalezaid IN ('1','2','6') THEN 'CATV' WHEN c.clientenaturalezaid IN ('4','5','7') THEN 'DUPLO' WHEN c.clientenaturalezaid IN ('3') THEN 'INTERNET' ELSE 'SIN CATEGORIA' END
  ```

## Vistas que la consumen (referencia)
- [[dbo.BI_FACTURA_ENCABEZADO_ALL]]
- [[dbo.V_CATEGORIACLIENTE]]
