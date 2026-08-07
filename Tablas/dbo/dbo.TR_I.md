---
esquema: dbo
tabla: TR_I
objeto: dbo.TR_I
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `TAREAID_I`, `CONTRATO`, `CLIENTENRO`
n_columnas: 12
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.TR_I

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `TAREAID_I`, `CONTRATO`, `CLIENTENRO`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ID` | varchar | 0% |
| 2 | `CLIENTENRO` | varchar | 0% |
| 3 | `TAREAID_I` | varchar | 0% |
| 4 | `FECHAPROCESADA_I` | datetime2 | 0% |
| 5 | `TIPOORDEN` | varchar | 0% |
| 6 | `TIPOPRODUCTO` | varchar | 0% |
| 7 | `EMPRESAID` | int | 0% |
| 8 | `TECNICOID` | int | 0% |
| 9 | `TECNICOID2` | int | 0% |
| 10 | `TECNICOR1` | varchar | 0% |
| 11 | `TECNICOR2` | varchar | 0% |
| 12 | `CONTRATO` | varchar | 0% |

## Claves de join presentes
- `ID` (varchar) → [[clave-ID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]
- `TIPOPRODUCTO` (varchar) → [[clave-TIPOPRODUCTO]]
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `TECNICOID` (int) → [[clave-TECNICOID]]
- `CONTRATO` (varchar) → [[clave-CONTRATO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
