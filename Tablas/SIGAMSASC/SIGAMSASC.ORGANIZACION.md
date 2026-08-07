---
esquema: SIGAMSASC
tabla: ORGANIZACION
objeto: SIGAMSASC.ORGANIZACION
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `ORGANIZACIONID` (único en muestra de 67)
n_columnas: 3
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.ORGANIZACION

> **BASE TABLE** · Dominio: **Core SIGA** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ORGANIZACIONID` (único en muestra de 67)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ORGANIZACIONID` | int | 0% |
| 2 | `ORGANIZACIONNOMBRE` | varchar | 0% |
| 3 | `PIPELINERUNID` | varchar | 0% |

## Claves de join presentes
- `ORGANIZACIONID` (int) → [[clave-ORGANIZACIONID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas

**Derivaciones (CASE)**
- _de_ [[dbo.V_ORGANIZACION]]:
  ```sql
  CASE WHEN o.organizacionid = '4' THEN 'TELEPERFORMANCE' WHEN o.organizacionid IN ('2','6','7','14','16','17','18','19','52') THEN 'OFICINA' WHEN o.organizacionid IN ('27','36','46','26','28','34','35','41','48', '37','32','42','31','11','33','22','40','49','39','43','15','29','38','47','20','53','55') THEN 'OTROS' ELSE 'OTROS' END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_ORGANIZACION]]
