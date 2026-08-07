---
objeto: MKT.NPS_YYYYMM
tipo_objeto: FAMILIA (particiones por período)
esquema: MKT
dominio: Marketing
canonico: true
familia: true
n_miembros: 29
tags:
  - esquema/MKT
  - dominio/marketing
  - tipo/familia
  - canonico
---

# Familia: MKT.NPS_YYYYMM

> Serie de **29 objetos** con esquema (casi) idéntico, particionados por período. Consultá el **miembro del período** que necesites; el esquema común es el de abajo.

## Esquema común (según NPS_202202)
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `respondent_id` | bigint | 0% |
| 2 | `collector_id` | int | 0% |
| 3 | `date_created` | datetime2 | 0% |
| 4 | `date_modified` | datetime2 | 0% |
| 5 | `ip_address` | nvarchar | 0% |
| 6 | `email_address` | nvarchar | 0% |
| 7 | `first_name` | nvarchar | 2% |
| 8 | `last_name` | nvarchar | 0% |
| 9 | `clientenro` | bigint | 0% |
| 10 | `empresa` | nvarchar | 0% |
| 11 | `categoria` | nvarchar | 0% |
| 12 | `segmento` | nvarchar | 0% |
| 13 | `nps` | int | 0% |
| 14 | `Cantidad_de_canales` | nvarchar | 21% |
| 15 | `Variedad_de_canales` | nvarchar | 26% |
| 16 | `Calidad_de_la_señal_de_tv` | nvarchar | 26% |
| 17 | `Disponibilidad_de_canales_locales` | nvarchar | 28% |
| 18 | `Atención_al_clienteTV` | nvarchar | 26% |
| 19 | `Servicio_técnicoTV` | nvarchar | 26% |
| 20 | `PrecioTV` | nvarchar | 24% |
| 21 | `Velocidad` | nvarchar | 40% |
| 22 | `Estabilidad` | nvarchar | 44% |
| 23 | `Atención_al_clienteINT` | nvarchar | 42% |
| 24 | `Servicio_técnicoINT` | nvarchar | 46% |
| 25 | `PrecioINT` | nvarchar | 43% |
| 26 | `Estoy_conforme_con_el_servicio_que_tengoTV` | nvarchar | 96% |
| 27 | `Estoy_evaluando_cambiar_a_un_plan_con_menos_prestaciones_pero_más_económicoTV` | nvarchar | 90% |
| 28 | `Estoy_evaluando_cambiar_a_un_plan_superior_aunque_tenga_un_precio_mayorTV` | nvarchar | 99% |
| 29 | `Estoy_evaluando_cambiar_de_proveedorTV` | nvarchar | 81% |
| 30 | `Estoy_evaluando_dar_de_baja_y_no_contratar_otro_proveedorTV` | nvarchar | 90% |
| 31 | `Estoy_conforme_con_el_servicio_que_tengoINT` | nvarchar | 98% |
| 32 | `Estoy_evaluando_cambiar_a_un_plan_con_menos_prestaciones_pero_más_económicoINT` | nvarchar | 94% |
| 33 | `Estoy_evaluando_cambiar_a_un_plan_superior_aunque_tenga_un_precio_mayorINT` | nvarchar | 100% |
| 34 | `Estoy_evaluando_cambiar_de_proveedorINT` | nvarchar | 80% |
| 35 | `Estoy_evaluando_dar_de_baja_y_no_contratar_otro_proveedorINT` | nvarchar | 94% |
| 36 | `En_los_últimos_30_dias_tuviste_algún_inconveniente_con_el_servicio` | nvarchar | 50% |
| 37 | `Clasif_NPS` | nvarchar | 0% |

## Miembros disponibles
- `MKT.NPS_20200612` (17 col)
- `MKT.NPS_202106` (26 col)
- `MKT.NPS_202108` (28 col)
- `MKT.NPS_202111` (34 col)
- `MKT.NPS_202202` (37 col)
- `MKT.NPS_202205` (29 col)
- `MKT.NPS_202207` (29 col)
- `MKT.NPS_202209` (35 col)
- `MKT.NPS_202211` (35 col)
- `MKT.NPS_202302` (35 col)
- `MKT.NPS_202304` (35 col)
- `MKT.NPS_202307` (35 col)
- `MKT.NPS_202308` (35 col)
- `MKT.NPS_202310` (35 col)
- `MKT.NPS_202402` (35 col)
- `MKT.NPS_202404` (35 col)
- `MKT.NPS_202406` (35 col)
- `MKT.NPS_202408` (35 col)
- `MKT.NPS_202410` (35 col)
- `MKT.NPS_202412` (35 col)
- `MKT.NPS_202502` (35 col)
- `MKT.NPS_202504` (35 col)
- `MKT.NPS_202506` (35 col)
- `MKT.NPS_202508` (35 col)
- `MKT.NPS_202510` (35 col)
- `MKT.NPS_202512` (35 col)
- `MKT.NPS_202602` (35 col)
- `MKT.NPS_202604` (35 col)
- `MKT.NPS_202606` (35 col)