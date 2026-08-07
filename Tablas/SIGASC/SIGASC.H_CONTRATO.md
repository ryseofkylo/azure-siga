---
esquema: SIGASC
tabla: H_CONTRATO
objeto: SIGASC.H_CONTRATO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 versión de `PKCONTRATONRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)
n_columnas: 16
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.H_CONTRATO

> **BASE TABLE** · Dominio: **Core SIGA** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 versión de `PKCONTRATONRO` por `BDMODIFIEDDATE` — histórica/versionada (inferido de muestra)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `CONTRATONRO` | int | 0% |
| 3 | `CLIENTENRO` | int | 0% |
| 4 | `POLITICAID` | int | 0% |
| 5 | `PRODUCTOID` | int | 0% |
| 6 | `CONTRATOSTS` | nvarchar | 0% |
| 7 | `PLANCOMERCIALCLIENTEITEM` | int | 21% |
| 8 | `PLANCOMERCIALGESTIONID` | int | 21% |
| 9 | `PLANCOMERCIALCLIENTEID` | int | 21% |
| 10 | `PIPELINERUNID` | nvarchar | 0% |
| 11 | `BDMODIFIEDDATE` | datetime2 | 0% |
| 12 | `hash` | nvarchar | 0% |
| 13 | `PKCONTRATONRO` | nvarchar | 0% |
| 14 | `PKCLIENTENRO` | nvarchar | 0% |
| 15 | `PKPOLITICAID` | nvarchar | 0% |
| 16 | `PKPRODUCTOID` | nvarchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `CONTRATONRO` (int) → [[clave-CONTRATONRO]]
- `CLIENTENRO` (int) → [[clave-CLIENTENRO]]
- `POLITICAID` (int) → [[clave-POLITICAID]]
- `PRODUCTOID` (int) → [[clave-PRODUCTOID]]
- `PLANCOMERCIALGESTIONID` (int) → [[clave-PLANCOMERCIALGESTIONID]]
- `PLANCOMERCIALCLIENTEID` (int) → [[clave-PLANCOMERCIALCLIENTEID]]
- `PIPELINERUNID` (nvarchar) → [[clave-PIPELINERUNID]]
- `PKCONTRATONRO` (nvarchar) → [[clave-PKCONTRATONRO]]
- `PKCLIENTENRO` (nvarchar) → [[clave-PKCLIENTENRO]]
- `PKPOLITICAID` (nvarchar) → [[clave-PKPOLITICAID]]
- `PKPRODUCTOID` (nvarchar) → [[clave-PKPRODUCTOID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PRODUCTO]] · `H_CONTRATO.PKPRODUCTOID = PRODUCTO.PKPRODUCTOID` — view_join (V_BAJAS_CARTERA_AI), alta
- [[SIGASC.PRODUCTO]] · `H_CONTRATO.EMPRESAID = PRODUCTO.EMPRESAID` — view_join (V_BAJAS_CARTERA_AI), alta

## Reglas de negocio conocidas
**Filtros**
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro)` — _de_ [[dbo.v_HistoricoCliente]]
- `dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))` — _de_ [[dbo.v_HistoricoCliente]]
- `clientenro not in ( select c.clientenro FROM [SIGASC].h_contrato c left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) and p.productotpo = 'T' group by c.clientenro )` — _de_ [[dbo.v_HistoricoClientexy]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_BAJAS_CARTERA_AI]], [[dbo.V_BAJAS_CARTERA_MIO]], [[dbo.V_BAJAS_CARTERA_PARAMOUNT]], [[dbo.V_BAJAS_CARTERA_UNIVERSAL]], [[dbo.V_BAJAS_CARTERA_skeelo]], [[dbo.V_CARTERA_CONTRATOS_PPALES]], [[dbo.V_CARTERA_SKEELO]], [[dbo.V_CARTERA_TIPO_CONTRATO]], [[dbo.V_CARTERA_TIPO_CONTRATO1]], [[dbo.V_NPS_TECNOLOGIA]], [[dbo.v_HistoricoCliente]], [[dbo.v_HistoricoClientexy]]

**Derivaciones (CASE)**
- _de_ [[dbo.v_HistoricoClientexy]]:
  ```sql
  case when isnumeric (c.clientecordx)=1 then round(convert ( float ,c.clientecordx ),6) else null end
  ```
- _de_ [[dbo.v_HistoricoClientexy]]:
  ```sql
  case when isnumeric (c.clientecordy)=1 then round(convert ( float ,c.clientecordy ),6) else null end
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_BAJAS_CARTERA_AI]]
- [[dbo.V_BAJAS_CARTERA_MIO]]
- [[dbo.V_BAJAS_CARTERA_PARAMOUNT]]
- [[dbo.V_BAJAS_CARTERA_UNIVERSAL]]
- [[dbo.V_BAJAS_CARTERA_skeelo]]
- [[dbo.V_CARTERA_CONTRATOS_PPALES]]
- [[dbo.V_CARTERA_SKEELO]]
- [[dbo.V_CARTERA_TIPO_CONTRATO]]
- [[dbo.V_CARTERA_TIPO_CONTRATO1]]
- [[dbo.V_CONTRATOS_BDDD]]
- [[dbo.V_NPS_TECNOLOGIA]]
- [[dbo.v_HistoricoCliente]]
- [[dbo.v_HistoricoClientexy]]
- [[dbo.v_HistoricoContrato]]
