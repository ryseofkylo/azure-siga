---
esquema: dbo
tabla: Estado_Agentes
objeto: dbo.Estado_Agentes
tipo_objeto: BASE TABLE
dominio: Data Warehouse / BI
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `Inicio_intervalo`, `Fin_intervalo`, `ID_agente`
n_columnas: 20
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/tabla-base
  - canonico
---

# dbo.Estado_Agentes

> **BASE TABLE** · Dominio: **Data Warehouse / BI** · 20 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `Inicio_intervalo`, `Fin_intervalo`, `ID_agente`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Inicio_intervalo` | datetime2 | 0% |
| 2 | `Fin_intervalo` | datetime2 | 0% |
| 3 | `Intervalo_completo` | nvarchar | 0% |
| 4 | `Filtros` | nvarchar | 100% |
| 5 | `ID_agente` | nvarchar | 0% |
| 6 | `Nombre` | nvarchar | 0% |
| 7 | `Aptitudes` | nvarchar | 100% |
| 8 | `Conectado` | nvarchar | 86% |
| 9 | `Cola` | nvarchar | 88% |
| 10 | `Inactivo` | nvarchar | 88% |
| 11 | `Disponible` | nvarchar | 86% |
| 12 | `Ocupado` | nvarchar | 94% |
| 13 | `Ausente` | nvarchar | 93% |
| 14 | `Descanso` | nvarchar | 90% |
| 15 | `Comida` | nvarchar | 100% |
| 16 | `No_responde` | nvarchar | 99% |
| 17 | `Fuera_cola` | nvarchar | 86% |
| 18 | `Interactuando` | nvarchar | 91% |
| 19 | `Inactivo2` | nvarchar | 88% |
| 20 | `Ocupacion` | nvarchar | 88% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
