---
esquema: dbo
tabla: v_HistoricoCliente
objeto: dbo.v_HistoricoCliente
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 5
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.v_HistoricoCliente

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
| 5 | `Fecha` | date | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.v_HistoricoCliente
-- Extraida: 2026-08-07T15:27:58.492639+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[v_HistoricoCliente]
AS with clientes_fixeados as(
SELECT C.[EMPRESAID]
      ,C.[CLIENTENRO]
      ,C.[CLIENTESTS]
	  ,C.[PKCLIENTENRO]
	  ,C.[NEGOCIOSEGMENTO]
      ,c.[CLIENTENATURALEZAID]
      ,CASE
		when C.[BDMODIFIEDDATE] > '1990-01-01' THEN C.[BDMODIFIEDDATE] 
        WHEN C.[BDMODIFIEDDATE] <= '1990-01-01' and C.[CLIENTESTS] = 'C' THEN '2022-09-01'
        ELSE null
    END AS BDMODIFIEDDATE
  FROM [SIGASC].[H_VM_CLIENTE] C
  where (C.[CLIENTESTS] = 'C' or C.[BDMODIFIEDDATE] > '1900-01-01')
and clientenaturalezaid <> 8

),
-- clientes_con_lag as(
-- SELECT clientenro, empresaid, clientests, bdmodifieddate, pkclientenro,NEGOCIOSEGMENTO,CLIENTENATURALEZAID
-- FROM (
--   SELECT 
--     clientenro, 
--     empresaid, 
--     clientests, 
--     bdmodifieddate, 
-- 	pkclientenro,
--     CLIENTENATURALEZAID,
-- 	NEGOCIOSEGMENTO,
--     LAG(clientests) OVER (PARTITION BY clientenro, empresaid ORDER BY bdmodifieddate) AS prev_clientests
--   FROM clientes_fixeados
--   where BDMODIFIEDDATE is not null
-- ) t
clientes_con_lag as(
SELECT clientenro, empresaid, clientests, bdmodifieddate, pkclientenro,NEGOCIOSEGMENTO,CLIENTENATURALEZAID
FROM (
  SELECT 
    clientenro, 
    empresaid, 
    clientests, 
    bdmodifieddate, 
	pkclientenro,
    CLIENTENATURALEZAID,
	NEGOCIOSEGMENTO,
    LAG(clientests) OVER (PARTITION BY clientenro, empresaid ORDER BY bdmodifieddate) AS prev_clientests,
    LAG(CLIENTENATURALEZAID) OVER (PARTITION BY clientenro, empresaid ORDER BY bdmodifieddate) AS prev_clientenat
  FROM clientes_fixeados
  where BDMODIFIEDDATE is not null
) t
WHERE (clientests != prev_clientests OR prev_clientests IS NULL)
or (CLIENTENATURALEZAID != prev_clientenat OR prev_clientenat IS NULL))
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
               ROW_NUMBER() OVER (PARTITION BY clientenro ORDER BY bdmodifieddate DESC) AS rn
        FROM clientes_con_lag
        WHERE dateadd(day, 1, eomonth(BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
    ) AS subquery
    WHERE rn = 1
and clientenro not in (
select c.clientenro
FROM [SIGASC].h_contrato c
left join [SIGASC].producto p
on c.pkproductoid = p.pkproductoid
WHERE dateadd(day, 1, eomonth(c.BDMODIFIEDDATE, -1)) <= DATEADD(month,1,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1))))
and p.productotpo = 'T'
group by c.clientenro)
--------------------------------------
union
----------------------------------------
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,2,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,3,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,4,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,5,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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

    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,6,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,7,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,8,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,9,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,10,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,11,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
    SELECT clientenro, clientests,CLIENTENATURALEZAID,empresaid,DATEADD(month,12,DATEADD(year, -1,dateadd(day, 1, eomonth(GETDATE(), -1)))) as Fecha
    FROM (
        SELECT clientenro, clientests, bdmodifieddate,empresaid,CLIENTENATURALEZAID,
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
