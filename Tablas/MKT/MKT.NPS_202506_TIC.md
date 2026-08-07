---
esquema: MKT
tabla: NPS_202506_TIC
objeto: MKT.NPS_202506_TIC
tipo_objeto: BASE TABLE
dominio: Marketing
canonico: true
grain: 1 fila = 1 `Clientenro` (único en muestra de 154)
n_columnas: 35
tags:
  - esquema/MKT
  - dominio/marketing
  - tipo/tabla-base
  - canonico
---

# MKT.NPS_202506_TIC

> **BASE TABLE** · Dominio: **Marketing** · 35 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `Clientenro` (único en muestra de 154)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `respondent_id` | bigint | 0% |
| 2 | `collector_id` | int | 0% |
| 3 | `date_created` | datetime2 | 0% |
| 4 | `date_modified` | datetime2 | 0% |
| 5 | `ip_address` | nvarchar | 0% |
| 6 | `email_address` | nvarchar | 0% |
| 7 | `first_name` | nvarchar | 1% |
| 8 | `last_name` | nvarchar | 0% |
| 9 | `Clientenro` | int | 0% |
| 10 | `Empresa` | nvarchar | 0% |
| 11 | `Categoria` | nvarchar | 0% |
| 12 | `Segmento` | nvarchar | 0% |
| 13 | `Recomendacion` | int | 0% |
| 14 | `Mas_Satisfecho_Precio` | int | 83% |
| 15 | `Mas_Satisfecho_Producto` | int | 80% |
| 16 | `Mas_Satisfecho_Atención_al_cliente` | int | 88% |
| 17 | `Mas_Satisfecho_Servicio_Técnico` | int | 88% |
| 18 | `Qué_debemos_mejorar` | int | 49% |
| 19 | `Aspectos_precio_mejora_Aumentos` | int | 92% |
| 20 | `Aspectos_precio_mejora_Precio_no_coincide` | int | 96% |
| 21 | `Aspectos_precio_mejora_FinPromo_Precio_MuyAlto` | int | 84% |
| 22 | `Aspectos_precio_mejora_alternativas_economicas` | int | 84% |
| 23 | `Aspectos_producto_mejora_veloc_internet` | int | 88% |
| 24 | `Aspectos_producto_mejora_corte_internet` | int | 92% |
| 25 | `Aspectos_producto_mejora_Senial_TV` | int | 94% |
| 26 | `Aspectos_producto_mejora_Cantidad_Senial_TV` | int | 94% |
| 27 | `Mejora_Atencion_Cliente_Comuniación_con_Atención_al_cliente` | int | 98% |
| 28 | `Mejora_Atencion_Cliente_Resolución_de_problemas_durante_la_consulta` | int | 97% |
| 29 | `Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal` | int | 99% |
| 30 | `Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center` | int | 99% |
| 31 | `Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_hora_pactada_para_la_visita` | int | 98% |
| 32 | `Mejora_Servicio_Tecnico_Solución_de_inconveniente` | int | 100% |
| 33 | `Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_de_Servicio_Técnico` | int | 100% |
| 34 | `Mejora_Servicio_Tecnico_Prolijidad_y_limpieza_al_finalizar_el_trabajo` | int | 100% |
| 35 | `Te_gustaría_dejarnos_algún_cometario_adicional` | nvarchar | 48% |

## Claves de join presentes
- `respondent_id` (bigint) → [[clave-RESPONDENT_ID]]
- `collector_id` (int) → [[clave-COLLECTOR_ID]]
- `Clientenro` (int) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_NPS_TIC]]
