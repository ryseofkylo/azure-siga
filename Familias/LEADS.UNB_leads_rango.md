---
objeto: LEADS.UNB_leads_rango
tipo_objeto: FAMILIA (particiones por período)
esquema: LEADS
dominio: Marketing / Leads
canonico: true
familia: true
n_miembros: 6
tags:
  - esquema/LEADS
  - dominio/marketing-leads
  - tipo/familia
  - canonico
---

# Familia: LEADS.UNB_leads_rango

> Serie de **6 objetos** con esquema (casi) idéntico, particionados por período. Consultá el **miembro del período** que necesites; el esquema común es el de abajo.

## Esquema común (según UNB_leads_20201101_20201130)
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `date_submitted` | datetime2 | 0% |
| 2 | `time_submitted` | nvarchar | 0% |
| 3 | `ip_address` | nvarchar | 0% |
| 4 | `variant` | nvarchar | 0% |
| 5 | `page_uuid` | nvarchar | 0% |
| 6 | `page_url` | nvarchar | 0% |
| 7 | `provincia` | nvarchar | 0% |
| 8 | `email` | nvarchar | 0% |
| 9 | `numero_de_contacto` | nvarchar | 90% |
| 10 | `dni_del_titular` | nvarchar | 90% |
| 11 | `utm_source` | nvarchar | 2% |
| 12 | `page_name` | nvarchar | 0% |
| 13 | `page_variant_name` | nvarchar | 0% |
| 14 | `Date_Submitted2` | nvarchar | 0% |
| 15 | `utm_campaign` | nvarchar | 2% |
| 16 | `utm_medium` | nvarchar | 2% |
| 17 | `nombre_y_apellido` | nvarchar | 0% |
| 18 | `dni` | nvarchar | 10% |
| 19 | `telefono_de_contacto` | nvarchar | 10% |
| 20 | `sos_cliente` | nvarchar | 100% |
| 21 | `nro_cliente` | nvarchar | 100% |
| 22 | `long` | nvarchar | 100% |
| 23 | `nro_celular` | nvarchar | 100% |
| 24 | `lead_id` | nvarchar | 100% |
| 25 | `date_lead` | nvarchar | 100% |
| 26 | `producto` | nvarchar | 100% |
| 27 | `lat` | nvarchar | 100% |
| 28 | `nombre_cliente` | nvarchar | 100% |
| 29 | `PREG_1` | nvarchar | 100% |
| 30 | `PREG_2` | nvarchar | 100% |
| 31 | `PREG_3` | nvarchar | 100% |
| 32 | `nro_de_cliente` | nvarchar | 100% |
| 33 | `correo_electrónico` | nvarchar | 100% |
| 34 | `telefono_de_contacto2` | nvarchar | 100% |

## Miembros disponibles
- `LEADS.UNB_leads_20200101_20200831` (31 col)
- `LEADS.UNB_leads_20200901_20200930` (26 col)
- `LEADS.UNB_leads_20201001_20201031` (28 col)
- `LEADS.UNB_leads_20201101_20201130` (34 col)
- `LEADS.UNB_leads_20201201_20201231` (30 col)
- `LEADS.UNB_leads_20210101_20210131` (27 col)