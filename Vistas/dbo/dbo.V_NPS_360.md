---
esquema: dbo
tabla: V_NPS_360
objeto: dbo.V_NPS_360
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 38
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_NPS_360

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[dbo.V_NPS]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `respondent_id` | bigint | 0% |
| 2 | `collector_id` | int | 0% |
| 3 | `PERIODO` | varchar | 0% |
| 4 | `date_created` | datetime2 | 0% |
| 5 | `date_modified` | datetime2 | 0% |
| 6 | `ip_address` | nvarchar | 0% |
| 7 | `email_address` | nvarchar | 0% |
| 8 | `first_name` | nvarchar | 0% |
| 9 | `last_name` | nvarchar | 0% |
| 10 | `Clientenro` | bigint | 0% |
| 11 | `Empresa` | nvarchar | 0% |
| 12 | `Categoria` | nvarchar | 0% |
| 13 | `Segmento` | nvarchar | 0% |
| 14 | `Recomendacion` | int | 0% |
| 15 | `Mas_Satisfecho_Precio` | int | 78% |
| 16 | `Mas_Satisfecho_Producto` | int | 84% |
| 17 | `Mas_Satisfecho_Atencion_al_cliente` | int | 84% |
| 18 | `Mas_Satisfecho_Servicio_Tecnico` | int | 87% |
| 19 | `Que_debemos_mejorar` | int | 60% |
| 20 | `Aspectos_precio_mejora_Aumentos` | int | 95% |
| 21 | `Aspectos_precio_mejora_Precio_no_coincide` | int | 97% |
| 22 | `Aspectos_precio_mejora_FinPromo_Precio_MuyAlto` | int | 93% |
| 23 | `Aspectos_precio_mejora_alternativas_economicas` | int | 92% |
| 24 | `Aspectos_producto_mejora_veloc_internet` | int | 94% |
| 25 | `Aspectos_producto_mejora_corte_internet` | int | 95% |
| 26 | `Aspectos_producto_mejora_Senial_TV` | int | 94% |
| 27 | `Aspectos_producto_mejora_Cantidad_Senial_TV` | int | 97% |
| 28 | `Mejora_Atencion_Cliente_Comuniacion` | int | 96% |
| 29 | `Mejora_Atencion_Cliente_Resolucion_de_problemas` | int | 97% |
| 30 | `Mejora_Atencion_Cliente_Trato_por_parte_del_personal_de_la_Sucursal` | int | 99% |
| 31 | `Mejora_Atencion_Cliente_Trato_por_parte_del_personal_del_Call_Center` | int | 99% |
| 32 | `Mejora_Servicio_Tecnico_Cumplimiento_con_fecha_pactada` | int | 97% |
| 33 | `Mejora_Servicio_Tecnico_Solucion_de_inconveniente` | int | 95% |
| 34 | `Mejora_Servicio_Tecnico_Trato_por_parte_del_personal_Tecnico` | int | 99% |
| 35 | `Mejora_Servicio_Tecnico_Prolijidad_y_limpieza` | int | 100% |
| 36 | `Cometario_adicional` | nvarchar | 44% |
| 37 | `PKPREVENTANRO` | varchar | 0% |
| 38 | `RowNum` | bigint | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_NPS_360
-- Extraida: 2026-08-07T15:28:03.818300+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[V_NPS_360]
AS WITH CTE AS (
  SELECT
    n.*,
    pf.PKPREVENTANRO,
    ROW_NUMBER() OVER (PARTITION BY n.CLIENTENRO, n.PERIODO ORDER BY pf.PREVENTAFCHING ASC) AS RowNum
  FROM
    V_NPS n
    LEFT JOIN V_PREVENTAS_FINAL pf ON n.CLIENTENRO = pf.CLIENTENROPREVENTA AND n.PERIODO >= FORMAT(pf.PREVENTAFCHING, 'yyyymm')
  WHERE
    EXISTS (
      SELECT 1
      FROM V_PREVENTAS_FINAL p
      WHERE n.CLIENTENRO = p.CLIENTENROPREVENTA AND n.PERIODO >= FORMAT(p.PREVENTAFCHING, 'yyyymm')
    )
)
SELECT * FROM CTE WHERE RowNum = 1;
```
