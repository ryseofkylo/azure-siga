---
esquema: dbo
tabla: FACT_TVE_AUTHORIZATION_EVENTS
objeto: dbo.FACT_TVE_AUTHORIZATION_EVENTS
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: 1 fila = 1 `authorization_event_id` (único en muestra de 200)
n_columnas: 12
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.FACT_TVE_AUTHORIZATION_EVENTS

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 12 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `authorization_event_id` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `authorization_event_id` | bigint | 0% |
| 2 | `subscriber_id` | bigint | 0% |
| 3 | `resource_urn` | nvarchar | 0% |
| 4 | `event_created_at_art` | datetime2 | 0% |
| 5 | `event_created_at_utc` | datetime2 | 0% |
| 6 | `event_date_art` | date | 0% |
| 7 | `source_updated_at_art` | datetime2 | 0% |
| 8 | `access_ok` | tinyint | 0% |
| 9 | `access_class` | varchar | 0% |
| 10 | `source_high_watermark` | bigint | 0% |
| 11 | `ingestion_batch_id` | varchar | 0% |
| 12 | `ingested_at_utc` | datetime2 | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
