---
esquema: MKT
tabla: NPS_2020_12
objeto: MKT.NPS_2020_12
tipo_objeto: BASE TABLE
dominio: Marketing
canonico: true
grain: 1 fila = 1 `clientenro` (único en muestra de 200)
n_columnas: 26
tags:
  - esquema/MKT
  - dominio/marketing
  - tipo/tabla-base
  - canonico
---

# MKT.NPS_2020_12

> **BASE TABLE** · Dominio: **Marketing** · 26 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `clientenro` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `respondent_id` | float | 0% |
| 2 | `collector_id` | int | 0% |
| 3 | `date_created` | datetime2 | 0% |
| 4 | `date_modified` | datetime2 | 0% |
| 5 | `ip_address` | float | 0% |
| 6 | `email_address` | nvarchar | 0% |
| 7 | `first_name` | nvarchar | 0% |
| 8 | `last_name` | nvarchar | 0% |
| 9 | `clientenro` | int | 0% |
| 10 | `empresa` | nvarchar | 0% |
| 11 | `Categoria` | nvarchar | 0% |
| 12 | `Segmento` | nvarchar | 0% |
| 13 | `NPS` | nvarchar | 0% |
| 14 | `Cantidad_de_canales` | nvarchar | 28% |
| 15 | `Variedad_de_canales` | nvarchar | 30% |
| 16 | `Calidad_de_la_se_al_de_tv` | nvarchar | 28% |
| 17 | `Disponibilidad_de_canales_locales` | nvarchar | 30% |
| 18 | `Atenci_n_al_clienteTV` | nvarchar | 29% |
| 19 | `Servicio_t_cnicoTV` | nvarchar | 30% |
| 20 | `PrecioTV` | nvarchar | 30% |
| 21 | `Velocidad` | nvarchar | 35% |
| 22 | `Estabilidad` | nvarchar | 35% |
| 23 | `Atenci_n_al_clienteINT` | nvarchar | 36% |
| 24 | `Servicio_t_cnicoINT` | nvarchar | 36% |
| 25 | `PrecioINT` | nvarchar | 35% |
| 26 | `Clasif_NPS` | nvarchar | 0% |

## Claves de join presentes
- `respondent_id` (float) → [[clave-RESPONDENT_ID]]
- `collector_id` (int) → [[clave-COLLECTOR_ID]]
- `clientenro` (int) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
