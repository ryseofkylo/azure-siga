---
esquema: dbo
tabla: V_NPS_TIC
objeto: dbo.V_NPS_TIC
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 36
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_NPS_TIC

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[MKT.NPS_202504_TIC]]
- [[MKT.NPS_202506_TIC]]
- [[MKT.NPS_202508_TIC]]
- [[MKT.NPS_202510_TIC]]
- [[MKT.NPS_202512_TIC]]
- [[MKT.NPS_202602_TIC]]
- [[MKT.NPS_202604_TIC]]
- [[MKT.NPS_202606_TIC]]

## Columnas expuestas
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
| 9 | `Clientenro` | int | 0% |
| 10 | `Empresa` | nvarchar | 0% |
| 11 | `Categoria` | nvarchar | 0% |
| 12 | `Segmento` | nvarchar | 0% |
| 13 | `Recomendacion` | int | 0% |
| 14 | `Mas_Satisfecho_Precio` | int | 84% |
| 15 | `Mas_Satisfecho_Producto` | int | 80% |
| 16 | `Mas_Satisfecho_Atención_al_cliente` | int | 88% |
| 17 | `Mas_Satisfecho_Servicio_Técnico` | int | 90% |
| 18 | `Qué_debemos_mejorar` | int | 53% |
| 19 | `Aspectos_precio_mejora_Aumentos` | int | 92% |
| 20 | `Aspectos_precio_mejora_Precio_no_coincide` | int | 98% |
| 21 | `Aspectos_precio_mejora_FinPromo_Precio_MuyAlto` | int | 87% |
| 22 | `Aspectos_precio_mejora_alternativas_economicas` | int | 88% |
| 23 | `Aspectos_producto_mejora_veloc_internet` | int | 87% |
| 24 | `Aspectos_producto_mejora_corte_internet` | int | 88% |
| 25 | `Aspectos_producto_mejora_Senial_TV` | int | 97% |
| 26 | `Aspectos_producto_mejora_Cantidad_Senial_TV` | int | 95% |
| 27 | `Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente` | int | 98% |
| 28 | `Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta` | int | 97% |
| 29 | `Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal` | int | 99% |
| 30 | `Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center` | int | 99% |
| 31 | `Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita` | int | 98% |
| 32 | `Mejora_Servicio_Tecnico_Solución_de_inconveniente` | int | 98% |
| 33 | `Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico` | int | 99% |
| 34 | `Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo` | int | 100% |
| 35 | `Te_gustaría_dejarnos_algún_cometario_adicional` | nvarchar | 50% |
| 36 | `PERIODO` | varchar | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_NPS_TIC
-- Extraida: 2026-08-07T15:28:05.173818+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_NPS_TIC]
AS SELECT  [respondent_id]
,[collector_id]
,[date_created]
,[date_modified]
,[ip_address]
,[email_address]
,[first_name]
,[last_name]
,[Clientenro]
,[Empresa]
,[Categoria]
,[Segmento]
,[Recomendacion]
,[Mas_Satisfecho_Precio]
,[Mas_Satisfecho_Producto]
,[Mas_Satisfecho_Atención_al_cliente]
,[Mas_Satisfecho_Servicio_Técnico]
,[Qué_debemos_mejorar]
,[Aspectos_precio_mejora_Aumentos]
,[Aspectos_precio_mejora_Precio_no_coincide]
,[Aspectos_precio_mejora_FinPromo_Precio_MuyAlto]
,[Aspectos_precio_mejora_alternativas_economicas]
,[Aspectos_producto_mejora_veloc_internet]
,[Aspectos_producto_mejora_corte_internet]
,[Aspectos_producto_mejora_Senial_TV]
,[Aspectos_producto_mejora_Cantidad_Senial_TV]
,[Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente]
,[Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center]
,[Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita]
,[Mejora_Servicio_Tecnico_Solución_de_inconveniente]
,[Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico]
,[Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo]
,[Te_gustaría_dejarnos_algún_cometario_adicional]
,'202504' as PERIODO
 FROM MKT.NPS_202504_TIC
 
 UNION ALL
 
SELECT  [respondent_id]
,[collector_id]
,[date_created]
,[date_modified]
,[ip_address]
,[email_address]
,[first_name]
,[last_name]
,[Clientenro]
,[Empresa]
,[Categoria]
,[Segmento]
,[Recomendacion]
,[Mas_Satisfecho_Precio]
,[Mas_Satisfecho_Producto]
,[Mas_Satisfecho_Atención_al_cliente]
,[Mas_Satisfecho_Servicio_Técnico]
,[Qué_debemos_mejorar]
,[Aspectos_precio_mejora_Aumentos]
,[Aspectos_precio_mejora_Precio_no_coincide]
,[Aspectos_precio_mejora_FinPromo_Precio_MuyAlto]
,[Aspectos_precio_mejora_alternativas_economicas]
,[Aspectos_producto_mejora_veloc_internet]
,[Aspectos_producto_mejora_corte_internet]
,[Aspectos_producto_mejora_Senial_TV]
,[Aspectos_producto_mejora_Cantidad_Senial_TV]
,[Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente]
,[Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center]
,[Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita]
,[Mejora_Servicio_Tecnico_Solución_de_inconveniente]
,[Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico]
,[Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo]
,[Te_gustaría_dejarnos_algún_cometario_adicional]
,'202506' as PERIODO
 FROM MKT.NPS_202506_TIC
 
 
 UNION ALL
 
SELECT  [respondent_id]
,[collector_id]
,[date_created]
,[date_modified]
,[ip_address]
,[email_address]
,[first_name]
,[last_name]
,[Clientenro]
,[Empresa]
,[Categoria]
,[Segmento]
,[Recomendacion]
,[Mas_Satisfecho_Precio]
,[Mas_Satisfecho_Producto]
,[Mas_Satisfecho_Atención_al_cliente]
,[Mas_Satisfecho_Servicio_Técnico]
,[Qué_debemos_mejorar]
,[Aspectos_precio_mejora_Aumentos]
,[Aspectos_precio_mejora_Precio_no_coincide]
,[Aspectos_precio_mejora_FinPromo_Precio_MuyAlto]
,[Aspectos_precio_mejora_alternativas_economicas]
,[Aspectos_producto_mejora_veloc_internet]
,[Aspectos_producto_mejora_corte_internet]
,[Aspectos_producto_mejora_Senial_TV]
,[Aspectos_producto_mejora_Cantidad_Senial_TV]
,[Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente]
,[Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center]
,[Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita]
,[Mejora_Servicio_Tecnico_Solución_de_inconveniente]
,[Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico]
,[Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo]
,[Te_gustaría_dejarnos_algún_cometario_adicional]
,'202508' as PERIODO
 FROM MKT.NPS_202508_TIC
 
 
 UNION ALL
 
SELECT  [respondent_id]
,[collector_id]
,[date_created]
,[date_modified]
,[ip_address]
,[email_address]
,[first_name]
,[last_name]
,[Clientenro]
,[Empresa]
,[Categoria]
,[Segmento]
,[Recomendacion]
,[Mas_Satisfecho_Precio]
,[Mas_Satisfecho_Producto]
,[Mas_Satisfecho_Atención_al_cliente]
,[Mas_Satisfecho_Servicio_Técnico]
,[Qué_debemos_mejorar]
,[Aspectos_precio_mejora_Aumentos]
,[Aspectos_precio_mejora_Precio_no_coincide]
,[Aspectos_precio_mejora_FinPromo_Precio_MuyAlto]
,[Aspectos_precio_mejora_alternativas_economicas]
,[Aspectos_producto_mejora_veloc_internet]
,[Aspectos_producto_mejora_corte_internet]
,[Aspectos_producto_mejora_Senial_TV]
,[Aspectos_producto_mejora_Cantidad_Senial_TV]
,[Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente]
,[Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center]
,[Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita]
,[Mejora_Servicio_Tecnico_Solución_de_inconveniente]
,[Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico]
,[Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo]
,[Te_gustaría_dejarnos_algún_cometario_adicional]
,'202510' as PERIODO
 FROM MKT.NPS_202510_TIC
 
 
 UNION ALL
 
SELECT  [respondent_id]
,[collector_id]
,[date_created]
,[date_modified]
,[ip_address]
,[email_address]
,[first_name]
,[last_name]
,[Clientenro]
,[Empresa]
,[Categoria]
,[Segmento]
,[Recomendacion]
,[Mas_Satisfecho_Precio]
,[Mas_Satisfecho_Producto]
,[Mas_Satisfecho_Atención_al_cliente]
,[Mas_Satisfecho_Servicio_Técnico]
,[Qué_debemos_mejorar]
,[Aspectos_precio_mejora_Aumentos]
,[Aspectos_precio_mejora_Precio_no_coincide]
,[Aspectos_precio_mejora_FinPromo_Precio_MuyAlto]
,[Aspectos_precio_mejora_alternativas_economicas]
,[Aspectos_producto_mejora_veloc_internet]
,[Aspectos_producto_mejora_corte_internet]
,[Aspectos_producto_mejora_Senial_TV]
,[Aspectos_producto_mejora_Cantidad_Senial_TV]
,[Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente]
,[Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center]
,[Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita]
,[Mejora_Servicio_Tecnico_Solución_de_inconveniente]
,[Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico]
,[Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo]
,[Te_gustaría_dejarnos_algún_cometario_adicional]
,'202512' as PERIODO
 FROM MKT.NPS_202512_TIC
 
  UNION ALL
 
SELECT  [respondent_id]
,[collector_id]
,[date_created]
,[date_modified]
,[ip_address]
,[email_address]
,[first_name]
,[last_name]
,[Clientenro]
,[Empresa]
,[Categoria]
,[Segmento]
,[Recomendacion]
,[Mas_Satisfecho_Precio]
,[Mas_Satisfecho_Producto]
,[Mas_Satisfecho_Atención_al_cliente]
,[Mas_Satisfecho_Servicio_Técnico]
,[Qué_debemos_mejorar]
,[Aspectos_precio_mejora_Aumentos]
,[Aspectos_precio_mejora_Precio_no_coincide]
,[Aspectos_precio_mejora_FinPromo_Precio_MuyAlto]
,[Aspectos_precio_mejora_alternativas_economicas]
,[Aspectos_producto_mejora_veloc_internet]
,[Aspectos_producto_mejora_corte_internet]
,[Aspectos_producto_mejora_Senial_TV]
,[Aspectos_producto_mejora_Cantidad_Senial_TV]
,[Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente]
,[Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center]
,[Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita]
,[Mejora_Servicio_Tecnico_Solución_de_inconveniente]
,[Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico]
,[Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo]
,[Te_gustaría_dejarnos_algún_cometario_adicional]
,'202602' as PERIODO
 FROM MKT.NPS_202602_TIC
 
 
  
  UNION ALL
 
SELECT  [respondent_id]
,[collector_id]
,[date_created]
,[date_modified]
,[ip_address]
,[email_address]
,[first_name]
,[last_name]
,[Clientenro]
,[Empresa]
,[Categoria]
,[Segmento]
,[Recomendacion]
,[Mas_Satisfecho_Precio]
,[Mas_Satisfecho_Producto]
,[Mas_Satisfecho_Atención_al_cliente]
,[Mas_Satisfecho_Servicio_Técnico]
,[Qué_debemos_mejorar]
,[Aspectos_precio_mejora_Aumentos]
,[Aspectos_precio_mejora_Precio_no_coincide]
,[Aspectos_precio_mejora_FinPromo_Precio_MuyAlto]
,[Aspectos_precio_mejora_alternativas_economicas]
,[Aspectos_producto_mejora_veloc_internet]
,[Aspectos_producto_mejora_corte_internet]
,[Aspectos_producto_mejora_Senial_TV]
,[Aspectos_producto_mejora_Cantidad_Senial_TV]
,[Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente]
,[Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center]
,[Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita]
,[Mejora_Servicio_Tecnico_Solución_de_inconveniente]
,[Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico]
,[Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo]
,[Te_gustaría_dejarnos_algún_cometario_adicional]
,'202604' as PERIODO
 FROM MKT.NPS_202604_TIC
 
 
 
 
  
  UNION ALL
 
SELECT  [respondent_id]
,[collector_id]
,[date_created]
,[date_modified]
,[ip_address]
,[email_address]
,[first_name]
,[last_name]
,[Clientenro]
,[Empresa]
,[Categoria]
,[Segmento]
,[Recomendacion]
,[Mas_Satisfecho_Precio]
,[Mas_Satisfecho_Producto]
,[Mas_Satisfecho_Atención_al_cliente]
,[Mas_Satisfecho_Servicio_Técnico]
,[Qué_debemos_mejorar]
,[Aspectos_precio_mejora_Aumentos]
,[Aspectos_precio_mejora_Precio_no_coincide]
,[Aspectos_precio_mejora_FinPromo_Precio_MuyAlto]
,[Aspectos_precio_mejora_alternativas_economicas]
,[Aspectos_producto_mejora_veloc_internet]
,[Aspectos_producto_mejora_corte_internet]
,[Aspectos_producto_mejora_Senial_TV]
,[Aspectos_producto_mejora_Cantidad_Senial_TV]
,[Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente]
,[Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal]
,[Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center]
,[Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita]
,[Mejora_Servicio_Tecnico_Solución_de_inconveniente]
,[Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico]
,[Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo]
,[Te_gustaría_dejarnos_algún_cometario_adicional]
,'202606' as PERIODO
 FROM MKT.NPS_202606_TIC;
```
