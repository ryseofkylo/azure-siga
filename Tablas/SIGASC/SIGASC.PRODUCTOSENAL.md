---
esquema: SIGASC
tabla: PRODUCTOSENAL
objeto: SIGASC.PRODUCTOSENAL
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `SKPRODUCTOSENAL` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTOSENAL

> **BASE TABLE** · Dominio: **Core SIGA** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `SKPRODUCTOSENAL` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `SKPRODUCTOSENAL` | varchar | 0% |
| 2 | `EMPRESAID` | int | 0% |
| 3 | `PRODUCTOID` | int | 0% |
| 4 | `SENALID` | int | 0% |
| 5 | `PIPELINERUNID` | varchar | 0% |
| 6 | `PKPRODUCTOID` | varchar | 0% |
| 7 | `PKSENALID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `SENALID` (int) → [[clave-SENALID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.SENAL]] · `PRODUCTOSENAL.SENALID = SENAL.SENALID` — view_join (vSENAL_PROYECCION), alta

## Reglas de negocio conocidas

**Derivaciones (CASE)**
- _de_ [[dbo.vSENAL_PROYECCION]]:
  ```sql
  CASE WHEN p.senalid IN ('4','25','80', '1073') THEN 'HBO' WHEN p.senalid IN ('6','83','1075') THEN 'ADULTOS' WHEN ( p.senalid IN ('46','75','1077') )THEN 'FUTBOL' WHEN ( p.senalid IN ('2','3','15','42','72','1016','1019','1054','1069') ) THEN 'DIGITALES' WHEN ( p.senalid IN ('10','11','32','43','73','1018','1056','1070','1071') ) THEN 'D. ADICIONALES' END
  ```
- _de_ [[dbo.V_PRODUCTOSENAL]]:
  ```sql
  CASE WHEN ( p.senalid IN ('2','3','15','42','72','1016','1019','1054','1069') ) THEN 'DIGITALES' WHEN ( p.senalid IN ('10','11','32','43','73','1018','1056','1070','1071') ) THEN 'D. ADICIONALES' WHEN ( p.senalid IN ('4','6','25','45','46','74','75','80','83','1063','1073','1074','1075','1076','1077') ) THEN 'PREMIUM' WHEN ( p.senalid IN ('1093') ) THEN 'PLATAFORMA' END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_PRODUCTOSENAL]]
- [[dbo.vSENAL_PROYECCION]]
