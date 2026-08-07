---
esquema: dbo
tabla: v_HistoricoClientexy
objeto: dbo.v_HistoricoClientexy
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 10
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_HistoricoClientexy

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGASC.H_CONTRATO]]
- [[SIGASC.H_VM_CLIENTE]]
- [[SIGASC.PRODUCTO]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `clientenro` | int | 0% |
| 2 | `clientests` | nvarchar | 0% |
| 3 | `CLIENTENATURALEZAID` | int | 0% |
| 4 | `empresaid` | int | 0% |
| 5 | `GEODIV1ID` | int | 0% |
| 6 | `GEODIV2ID` | int | 0% |
| 7 | `GEOMANID` | int | 0% |
| 8 | `clientecordx` | float | 2% |
| 9 | `clientecordy` | float | 2% |
| 10 | `Fecha` | date | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_HistoricoClientexy
-- Extraida: 2026-08-07T15:27:58.828264+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_HistoricoClientexy]
AS with clientes_fixeados as(
SELECT C.[EMPRESAID]
      ,C.[CLIENTENRO]
      ,C.[CLIENTESTS]
	  ,C.[PKCLIENTENRO]
	  ,C.[NEGOCIOSEGMENTO]
      ,c.[CLIENTENATURALEZAID]
      ,c.[GEODIV1ID]
      ,c.[GEODIV2ID]
      ,c.[GEOMANID]
      ,case when isnumeric (c.clientecordx)=1 then round(convert  ( float ,c.clientecordx  ),6) else null end as clientecordx 
	  ,case when isnumeric (c.clientecordy)=1 then round(convert  ( float ,c.clientecordy  ),6) else null end as clientecordy 
      ,CASE
		when C.[BDMODIFIEDDATE] > '1990-01-01' THEN C.[BDMODIFIEDDATE] 
        WHEN C.[BDMODIFIEDDATE] <= '1990-01-01' and C.[CLIENTESTS] = 'C' THEN '2022-09-01'
        ELSE null
    END AS BDMODIFIEDDATE
  FROM [SIGASC].[H_VM_CLIENTE] C
  where (C.[CLIENTESTS] = 'C' or C.[BDMODIFIEDDATE] > '1900-01-01')
and clientenaturalezaid <> 8 
--and clientenro =5664349

),

clientes_con_lag as(
SELECT clientenro, empresaid, clientests, bdmodifieddate, pkclientenro,NEGOCIOSEGMENTO,CLIENTENATURALEZAID,  
[GEODIV1ID]    ,[GEODIV2ID]      , GEOMANID ,clientecordx	  ,clientecordy
FROM (
  SELECT 
    clientenro, 
    empresaid, 
    clientests, 
    bdmodifieddate, 
	pkclientenro,
    CLIENTENATURALEZAID,
	NEGOCIOSEGMENTO,
    [GEODIV1ID],
    [GEODIV2ID],
    GEOMANID,
    clientecordx,
	clientecordy,
    LAG(clientests) OVER (PARTITION BY clientenro, empresaid ORDER BY bdmodifieddate) AS prev_clientests,
    LAG(CLIENTENATURALEZAID) OVER (PARTITION BY clientenro, empresaid ORDER BY bdmodifieddate) AS prev_clientenat,
	LAG(clientecordx) OVER (PARTITION BY clientenro, empresaid ORDER BY bdmodifieddate) AS prev_clientecordx,
	LAG(clientecordy) OVER (PARTITION BY clientenro, empresaid ORDER BY bdmodifieddate) AS prev_clientecordy,
    LAG(GEOMANID) OVER (PARTITION BY clientenro, empresaid ORDER BY bdmodifieddate) AS prev_GEOMANID
  FROM clientes_fixeados
  where BDMODIFIEDDATE is not null
) t
WHERE (clientests != prev_clientests OR prev_clientests IS NULL)
or (CLIENTENATURALEZAID != prev_clientenat OR prev_clientenat IS NULL)
or (clientecordx != prev_clientecordx OR prev_clientecordx IS NULL)
or (clientecordy != prev_clientecordy OR prev_clientecordy IS NULL)
or (GEOMANID != prev_GEOMANID OR prev_GEOMANID IS NULL))

---------------
SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid, [GEODIV1ID]  ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy, DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
        ) AS subquery
    WHERE rn = 1 
    and clientenro not in (
                            select c.clientenro
                            FROM [SIGASC].h_contrato c
                            left join [SIGASC].producto p on c.pkproductoid = p.pkproductoid
                            WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
                            and p.productotpo = 'T'
                            group by c.clientenro
                            )
                            
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,[GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,[GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------

    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,[GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,[GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,[GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,[GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],CLIENTENATURALEZAID,clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,[GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)

--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,[GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID], clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)

--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID, [GEODIV1ID]
      ,[GEODIV2ID]
      ,[GEOMANID],clientecordx, clientecordy,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1

and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro);
```
