---
esquema: SIGASC
tabla: PRODUCTO
objeto: SIGASC.PRODUCTO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `PKPRODUCTOID` (único en muestra de 200)
n_columnas: 39
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.PRODUCTO

> **BASE TABLE** · Dominio: **Core SIGA** · 39 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKPRODUCTOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `PRODUCTOID` | int | 0% |
| 3 | `PRODUCTONOMBRE` | varchar | 0% |
| 4 | `PRODUCTOTPO` | varchar | 0% |
| 5 | `PRODUCTOPPL` | varchar | 0% |
| 6 | `PRODUCTOSTS` | varchar | 0% |
| 7 | `PRODUCTOPPV` | int | 0% |
| 8 | `PRODUCTOAPROVISIONAR` | varchar | 0% |
| 9 | `PRODUCTOCONADICIONAL` | int | 0% |
| 10 | `PRODUCTOPRNFORMULARIO` | varchar | 0% |
| 11 | `NEGOCIOID` | varchar | 0% |
| 12 | `PRODUCTOINGPREVENTA` | int | 0% |
| 13 | `PRODUCTOHPP` | int | 0% |
| 14 | `PRODUCTONOMPEQ` | varchar | 0% |
| 15 | `PRODUCTOCONCAMBIO` | int | 0% |
| 16 | `PRODUCTOCONMUDANZA` | int | 0% |
| 17 | `PRODUCTODETALLE` | varchar | 0% |
| 18 | `PRODUCTOCARTELERAID` | int | 0% |
| 19 | `PRODUCTOCARTELERANOMBRE` | varchar | 0% |
| 20 | `PRODUCTOCARTELERAACTIVO` | int | 0% |
| 21 | `PRODUCTOCONSUCURSAL` | int | 0% |
| 22 | `PRODUCTOCARTELERAIMAGEN` | int | 0% |
| 23 | `PRODUCTOCONFACTORCONTEO` | int | 0% |
| 24 | `MOROSIDADCRITERIOID` | int | 4% |
| 25 | `PRODUCTOCONMUDANZADSC` | int | 0% |
| 26 | `PRODUCTOCONDERIVADO` | int | 0% |
| 27 | `PRODUCTOCONCAMBIOCANTIDAD` | int | 0% |
| 28 | `PRODUCTOUNICO` | int | 90% |
| 29 | `PRODUCTOPPLID` | int | 82% |
| 30 | `PRODUCTOPRGIMPRESION` | varchar | 82% |
| 31 | `FORMID` | int | 17% |
| 32 | `PRODUCTOGENCORTEFISICO` | int | 0% |
| 33 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 34 | `PRODUCTOSKEELOPRODUCTOTIPOID` | varchar | 0% |
| 35 | `PRODUCTOIMG` | varchar | 100% |
| 36 | `PRODUCTOCARTELERAULTLIN` | int | 100% |
| 37 | `PIPELINERUNID` | varchar | 0% |
| 38 | `PKPRODUCTOID` | varchar | 0% |
| 39 | `PRODUCTOPRMPORTALDSC` | varchar | 100% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `PRODUCTOTPO` (varchar) → [[clave-PRODUCTOTPO]]
- `NEGOCIOID` (varchar) → [[clave-NEGOCIOID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]
- `PKPRODUCTOID` (varchar) → [[clave-PKPRODUCTOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.CONTRATO]] · `PRODUCTO.EMPRESAID = CONTRATO.EMPRESAID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.CONTRATO]] · `PRODUCTO.PRODUCTOID = CONTRATO.PRODUCTOID` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.PRODUCTOTPO]] · `PRODUCTO.PRODUCTOTPO = PRODUCTOTPO.PRODUCTOTPO` — view_join (DW_ORDENES_TECNICAS_V5), alta
- [[SIGASC.H_CONTRATO]] · `PRODUCTO.PKPRODUCTOID = H_CONTRATO.PKPRODUCTOID` — view_join (V_BAJAS_CARTERA_AI), alta
- [[SIGASC.H_CONTRATO]] · `PRODUCTO.EMPRESAID = H_CONTRATO.EMPRESAID` — view_join (V_BAJAS_CARTERA_AI), alta
- [[SIGASC.H_CONTRATO_CLIENTE]] · `PRODUCTO.PKPRODUCTOID = H_CONTRATO_CLIENTE.PKPRODUCTOID` — view_join (V_CLIENTEDATOS_SINFILTRO), alta

## Reglas de negocio conocidas
**Filtros**
- `p.PRODUCTOPPL = 'P'` — _de_ [[dbo.vContratos_MF_Cuota1]]
- `p.productoppl = 'P'` — _de_ [[dbo.vFACTURACION_DETALLE_202305_cp]]
- `P.productoid in (6402,6409,6418,70048,70049,70050,70061,70062,70063,70044,70074) OR ( P.productoid in (8552,8555,8556) and p.empresaid=23)` — _de_ [[dbo.V_BAJAS_CARTERA_MIO]]
- `(P.productoid in (6407,70052,6394, 70083, 6393) or ( P.productoid in (8554,6393,8790) and p.empresaid=23))` — _de_ [[dbo.V_BAJAS_CARTERA_PARAMOUNT]]
- `p.productotpo = 'T'` — _de_ [[dbo.V_CLIENTESPRODDATOS]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro )` — _de_ [[dbo.v_HistoricoClientexy]]
- `p.PRODUCTOTPO IN ('B','Z','W','R')` — _de_ [[SIGASC.V_CONTRATOS_EXTENDIDOS]]
- ♻️ dedup: vistas que deduplican esta tabla → [[SIGASC.V_CONTRATOS_EXTENDIDOS]], [[dbo.V_BAJAS_CARTERA_AI]], [[dbo.V_BAJAS_CARTERA_MIO]], [[dbo.V_BAJAS_CARTERA_PARAMOUNT]], [[dbo.V_BAJAS_CARTERA_UNIVERSAL]], [[dbo.V_BAJAS_CARTERA_skeelo]], [[dbo.V_CARTERA_CONTRATOS_PPALES]], [[dbo.V_CARTERA_SKEELO]], [[dbo.V_CARTERA_TIPO_CONTRATO]], [[dbo.V_CARTERA_TIPO_CONTRATO1]], [[dbo.V_CLIENTEDATOS_SINFILTRO]], [[dbo.V_FACTURACLIENTE]], [[dbo.V_NPS_TECNOLOGIA]], [[dbo.vFACTURACION_DETALLE_202305_cp]], [[dbo.vFACTURACION_DETALLE_202306_cp]], [[dbo.vFACTURACION_DETALLE_202307_cp]], [[dbo.vFACTURACION_DETALLE_202308_cp]], [[dbo.vFACTURACION_DETALLE_202309_cp]], [[dbo.vFACTURACION_DETALLE_202310_cp]], [[dbo.v_HistoricoCliente]], [[dbo.v_HistoricoClientexy]], [[dbo.v_Segmentacion]]

**Derivaciones (CASE)**
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and P.PRODUCTOTPO = 'B' and P.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and P.PRODUCTOTPO = 'B' and P.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and P.PRODUCTOTPO = 'L' and P.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and P.PRODUCTOTPO = 'Z' and P.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and P.PRODUCTOTPO = 'R' and P.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE when O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' and P.PRODUCTOTPO = 'D' and P.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END
  ```
- _de_ [[dbo.DW_OT_PENDIENTES_V2]]:
  ```sql
  CASE WHEN O.ORDENGEN <> 'R' AND O.ORDENTPO = 'I' AND P.PRODUCTOTPO IN('C','I') and P.PRODUCTOPPL = 'P' then 1 ELSE 0 END
  ```
- _de_ [[dbo.v_Segmentacion]]:
  ```sql
  case when p.productotpo = 'Q' then 1 else 0 end
  ```

## Vistas que la consumen (referencia)
- [[SIGASC.V_CONTRATOS_EXTENDIDOS]]
- [[dbo.BI_FACTURA_DETALLE_ALL]]
- [[dbo.DW_ORDENES_TECNICAS_V5]]
- [[dbo.DW_OT_PENDIENTES_V2]]
- [[dbo.V_BAJAS_CARTERA_AI]]
- [[dbo.V_BAJAS_CARTERA_MIO]]
- [[dbo.V_BAJAS_CARTERA_PARAMOUNT]]
- [[dbo.V_BAJAS_CARTERA_UNIVERSAL]]
- [[dbo.V_BAJAS_CARTERA_skeelo]]
- [[dbo.V_CARTERA_CONTRATOS_PPALES]]
- [[dbo.V_CARTERA_SKEELO]]
- [[dbo.V_CARTERA_TIPO_CONTRATO]]
- [[dbo.V_CARTERA_TIPO_CONTRATO1]]
- [[dbo.V_CLIENTEDATOS_SINFILTRO]]
- [[dbo.V_CLIENTESPRODDATOS]]
- [[dbo.V_COBRANZAS_BASE]]
- [[dbo.V_CONTRATOS_BDDD]]
- [[dbo.V_FACTURACLIENTE]]
- [[dbo.V_NPS_TECNOLOGIA]]
- [[dbo.V_ORDENESPENDIENTES]]
- [[dbo.V_ORDENSRV_DESCONEX]]
- [[dbo.V_ORDENSRV_INST]]
- [[dbo.V_ORDENSRV_RECLAMOS]]
- [[dbo.V_RECLAMOS_BDDD]]
- [[dbo.vContratos_MF_Cuota1]]
- [[dbo.vFACTURACION_DETALLE_202305_cp]]
- [[dbo.vFACTURACION_DETALLE_202306_cp]]
- [[dbo.vFACTURACION_DETALLE_202307_cp]]
- [[dbo.vFACTURACION_DETALLE_202308_cp]]
- [[dbo.vFACTURACION_DETALLE_202309_cp]]
- [[dbo.vFACTURACION_DETALLE_202310_cp]]
- [[dbo.v_HistoricoCliente]]
- [[dbo.v_HistoricoClientexy]]
- [[dbo.v_Segmentacion]]
