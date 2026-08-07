---
esquema: dbo
tabla: DW_ORDENES_TECNICAS_V5
objeto: dbo.DW_ORDENES_TECNICAS_V5
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 55
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.DW_ORDENES_TECNICAS_V5

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.EMPRESA]]
- [[SIGASC.CENTROOPERATIVO]]
- [[SIGASC.CODIGO_TAREAS]]
- [[SIGASC.CONTRATO]]
- [[SIGASC.EMPRESASMULTI]]
- [[SIGASC.ORDENSRV]]
- [[SIGASC.PRODUCTO]]
- [[SIGASC.PRODUCTOTPO]]
- [[SIGASC.TECNICO]]
- [[SIGASC.VM_CLIENTE]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESA` | int | 0% |
| 2 | `EMPRESA_NOM` | varchar | 0% |
| 3 | `CentroProductivo` | varchar | 0% |
| 4 | `FECHA` | datetime2 | 0% |
| 5 | `CLIENTE` | int | 0% |
| 6 | `ID_TECNICO1` | int | 0% |
| 7 | `TECNICO1_EMPLEADONRO` | int | 0% |
| 8 | `TECNICO1_TIPO` | varchar | 0% |
| 9 | `TECNICO1` | varchar | 0% |
| 10 | `ID_TECNICO2` | int | 16% |
| 11 | `TECNICO2_TIPO` | varchar | 22% |
| 12 | `TECNICO2_EMPLEADONRO` | int | 22% |
| 13 | `TECNICO2` | varchar | 22% |
| 14 | `TOTAL` | int | 0% |
| 15 | `DETALLE` | nvarchar | 0% |
| 16 | `INSTALACION_BASICO` | int | 0% |
| 17 | `BASICO_ADICIONAL` | int | 0% |
| 18 | `INSTALACION_FTTH` | int | 0% |
| 19 | `CATV_FTTH` | int | 0% |
| 20 | `DERIVADO` | int | 0% |
| 21 | `INSTALACION_DIGITAL` | int | 0% |
| 22 | `DIGITAL_ADICIONAL` | int | 0% |
| 23 | `INSTALACION_MODEM` | int | 0% |
| 24 | `INSTALACION_EOC` | int | 0% |
| 25 | `INSTALACION_CORPORATIVO` | int | 0% |
| 26 | `BASICO_CATV_EOC` | int | 0% |
| 27 | `UPGRADE_CATV_FTTH` | int | 0% |
| 28 | `UPGRADE_DECO` | int | 0% |
| 29 | `RECONEXION_BASICO` | int | 0% |
| 30 | `RECONEXION_CATV_FTTH` | int | 0% |
| 31 | `RECONEXION_FTTH` | int | 0% |
| 32 | `RECONEXION_MODEM` | int | 0% |
| 33 | `RECONEXION_EOC` | int | 0% |
| 34 | `RECONEXION_CATV_EOC` | int | 0% |
| 35 | `DESCONEXION_BASICO` | int | 0% |
| 36 | `DESCONEXION_DIGITAL` | int | 0% |
| 37 | `DESCONEXION_MODEM` | int | 0% |
| 38 | `DESCONEXION_EOC` | int | 0% |
| 39 | `DESCONEXION_DERIVADOS` | int | 0% |
| 40 | `DESCONEXION_DECO_ANALOGICO` | int | 0% |
| 41 | `DESCONEXION_FTTH` | int | 0% |
| 42 | `DESCONEXION_FTTH_CATV` | int | 0% |
| 43 | `DESCONEXION_BASICO_EOC` | int | 0% |
| 44 | `DESCONEXION_CORPORATIVO` | int | 0% |
| 45 | `RECLAMO` | int | 0% |
| 46 | `RECLAMO_CORPORTATIVO` | int | 0% |
| 47 | `CODIGO_INSTALACION` | varchar | 0% |
| 48 | `CODIGO_AT` | varchar | 0% |
| 49 | `CODIGO_DERIVADOS` | varchar | 0% |
| 50 | `CODIGO_DESCONEXION` | varchar | 0% |
| 51 | `Coef_Instalacion` | decimal | 94% |
| 52 | `Coef_AT` | decimal | 60% |
| 53 | `Coef_Desconexion` | decimal | 76% |
| 54 | `Coef_Derivado` | decimal | 92% |
| 55 | `Coef_Total` | decimal | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.DW_ORDENES_TECNICAS_V5
-- Extraida: 2026-08-07T15:27:33.217675+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [dbo].[DW_ORDENES_TECNICAS_V5]
AS with estados as (
--    select 'E' Estado, 'Emitita' Descripcion from dual -- emitida
--        union all 
--    select 'A' Estado, 'Agendada' Descripcion from dual -- Agendada
--        union all 
--    select 'P' Estado, 'Pendiente' Descripcion from dual -- Pendiente
--        union all 
--    select 'R' Estado, 'Re-Agendada' Descripcion from dual -- reAgendada
--        union all 
--    select 'S' Estado, 'Suspendida' Descripcion from dual -- Suspendida
----        union all 
    select 'F' Estado, 'Finalizada' Descripcion  
)
,ordenes as (
SELECT case O.EMPRESAID 
				WHEN 21 THEN 4 -- Si es TVCA -> Que regrese UDN Catamarca. 
			ELSE O.EMPRESAID 
        END EMPRESAID, 
        case O.EMPRESAID 
				WHEN 21 THEN 'SUPERCANAL CATAMARCA' -- Si es TVCA -> Que regrese UDN Catamarca. 
			ELSE TRIM(EMP.EMPRESANOM) 
        END EMPRESA_nom, 
        O.CLIENTENROORD, 
        O.TECNICOIDCIERRE TECNICO,
        t.TECNICOEMPLEADONRO, 
        O.TECNICOIDCIERREAUX  ID_TECNICO2,
        Tec2.TECNICOTPO TECNICO2_TIPO,
        Tec2.TECNICOEMPLEADONRO TECNICO2_EMPLEADONRO,
        trim (Tec2.TECNICONOMBRE) TECNICO2,
        O.ORDENFPROCESO FECHA, 
        t.TECNICOTPO TECNICO1_TIPO,
        trim (T.TECNICONOMBRE) TECNICO1,
        case t.EMPRESAID 
            when  1 then	
                case COP.CENTROOPERATIVOID when  3 then --'C.O. SAN MARTIN'	
                    'CP. SAN MARTIN MZA'
                else
                    'CP. MENDOZA'
                end 
            when  16 then	
                case COP.CENTROOPERATIVOID when  2 then -- 'C.O. CHILECITO'	
                    'CP. CHILECITO'
                else
                    'CP. LA RIOJA'
                end
            when 3 then 
                'CP. TUCUMAN'
            when 21 then  -- TVCA
                'CP. CATAMARCA'
        else 
            REPLACE(CENTROOPERATIVONOMBRE,'C.O.','CP.')
        end CentroProductivo,
        O.ORDENNRO,
        o.ORDENTPO,
        o.ordensts,
        P.PRODUCTOTPO,
        P.PRODUCTOPPL,
        O.ORDENTRBRED, 
        o.ORDENGEN
    FROM SIGASC.ORDENSRV O
        inner join sigasc.empresasmulti em
            on O.EMPRESAID = em.empresaid
        left join SIGASC.CENTROOPERATIVO cop
            on em.empresaid = cop.empresaid
            and O.CENTROOPERATIVOID = COP.CENTROOPERATIVOID
        inner join SIGASC.TECNICO T
            on O.EMPRESAID = T.EMPRESAID
            and O.TECNICOIDCIERRE = T.TECNICOID  -- Se cambio al tecnico de cierre 19/04/23
        inner join SIGAMSASC.EMPRESA EMP
            on o.EMPRESAID = EMP.EMPRESAID
		INNER JOIN SIGASC.VM_CLIENTE cli
                on O.EMPRESAID = CLI.empresaid 
                and O.CLIENTENROORD = CLI.CLIENTENRO
        INNER JOIN estados est
                on o.ordensts = est.Estado
        inner join SIGASC.CONTRATO CO
                on O.EMPRESAID = CO.EMPRESAID 
                    AND O.CONTRATONRO = CO.CONTRATONRO 
                    AND O.CLIENTENROORD = CO.CLIENTENRO 
        inner join SIGASC.PRODUCTO P
                on CO.EMPRESAID = P.EMPRESAID  
                    AND CO.PRODUCTOID = P.PRODUCTOID
        inner join sigasc.productotpo PTO
                ON PTO.PRODUCTOTPO = P.PRODUCTOTPO 
        LEFT join SIGASC.TECNICO Tec2
            on o.EMPRESAID = Tec2.EMPRESAID
            and o.TECNICOIDCIERREAUX = Tec2.TECNICOID -- Se cambio al tecnico de cierre 19/04/23
    WHERE O.TECNICOIDCIERRE > 0 
        -- AND O.ORDENFPROCESO between to_date ('01/05/2022','DD/MM/RRRR') AND TO_DATE ('02/05/2022','DD/MM/RRRR')
    )
	--select top 1 * from ordenes
	,datos_calculados as (
        SELECT 
        o.EMPRESAID,
        EMPRESA_nom,
        o.CentroProductivo,
        FECHA,  
        clientenroord CLIENTE,  
        TECNICO ID_TECNICO1,
        o.TECNICOEMPLEADONRO TECNICO1_EMPLEADONRO,
        TECNICO1_TIPO,
        TECNICO1, 
        ID_TECNICO2,
        TECNICO2_TIPO,
        TECNICO2_EMPLEADONRO,
        TECNICO2,
        ORDENTPO,
--        PRODUCTOTPO,
        ORDENGEN,
--        PRODUCTOPPL,
        ORDENNRO,
        --TOTAL,
        --DETALLE DE ORDENES    
        --DETALLE,
        --LISTAGG (O.ORDENNRO, ',') WITHIN GROUP (ORDER BY O.ORDENNRO) DETALLE,
        --LISTAGG (O.PRODUCTOTPO, ',') WITHIN GROUP (ORDER BY O.PRODUCTOTPO) DETALLE_PRODUCTOTPO,
--        COUNT (*) TOTAL,
        SUM( CASE when O.ORDENGEN <> 'R' 
                     AND O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'B' 
                     and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo, o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2 ) 
        AS INSTALACION_BASICO
        , SUM( CASE when O.ORDENGEN <> 'R' 
                     AND O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'B' 
                     and O.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END ) -- A REVISAR
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS BASICO_ADICIONAL
        , SUM( CASE when 
                     O.ORDENGEN <> 'R' AND 
                     O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'L' 
                     and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS INSTALACION_FTTH
        , SUM( CASE when 
                     O.ORDENGEN <> 'R'  AND 
                     O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'Z' 
                     and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS CATV_FTTH
        , SUM( CASE when O.ORDENGEN <> 'R' 
                     AND O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'R' 
                     and O.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS DERIVADO
        , SUM( CASE when O.ORDENGEN <> 'R' 
                     AND O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'D' 
                     and O.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS INSTALACION_DIGITAL
        , SUM( CASE when O.ORDENGEN <> 'R' 
                     AND O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'D' 
                     and O.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)
            - 1 -- Resta 1 Para no incluir el DIGITAL Anterior 
        AS DIGITAL_ADICIONAL
        , SUM( CASE WHEN 
                    O.ORDENGEN <> 'R' AND 
                    O.ORDENTPO = 'I'
                    AND o.PRODUCTOTPO IN('C','I')
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS INSTALACION_MODEM
        , SUM( CASE WHEN 
                    O.ORDENGEN <> 'R' AND  
                    O.ORDENTPO = 'I'
                    AND o.PRODUCTOTPO = 'E'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS INSTALACION_EOC
        , SUM( CASE WHEN O.ORDENTPO = 'I'
                    AND o.PRODUCTOTPO = 'N'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END )   
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS INSTALACION_CORPORATIVO
        , SUM( CASE WHEN O.ORDENGEN <> 'R' AND  
                    O.ORDENTPO = 'I'
                    AND o.PRODUCTOTPO = 'W'
                    and o.PRODUCTOPPL = 'P' then 1 ELSE 0 END )   
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, o.TECNICO, ID_TECNICO2) 
        AS BASICO_CATV_EOC
        ----- RECONEXIONES ----------------------------------------------------------
        , SUM( CASE when O.ORDENGEN = 'R' 
                     AND O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'B' 
                     and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS RECONEXION_BASICO
        , SUM( CASE when 
                     O.ORDENGEN = 'R'  AND 
                     O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'Z' 
                     and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS RECONEXION_CATV_FTTH
        , SUM( CASE when 
                     O.ORDENGEN = 'R' AND 
                     O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'L' 
                     and O.PRODUCTOPPL = 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS RECONEXION_FTTH
        , SUM( CASE WHEN 
                    O.ORDENGEN = 'R' AND 
                    O.ORDENTPO = 'I'
                    AND o.PRODUCTOTPO IN('C','I')
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS RECONEXION_MODEM
        , SUM( CASE WHEN 
                    O.ORDENGEN = 'R' AND  
                    O.ORDENTPO = 'I'
                    AND o.PRODUCTOTPO = 'E'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS RECONEXION_EOC
        , SUM( CASE WHEN O.ORDENGEN = 'R' AND  
                    O.ORDENTPO = 'I'
                    AND o.PRODUCTOTPO = 'W'
                    and o.PRODUCTOPPL = 'P' then 1 ELSE 0 END )   
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, o.TECNICO, ID_TECNICO2) 
        AS RECONEXION_CATV_EOC
        , SUM( CASE when O.ORDENGEN <> 'R' 
                     AND O.ORDENTPO = 'I' 
                     and o.PRODUCTOTPO = 'R' 
                     and O.PRODUCTOPPL <> 'P' THEN 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2) 
        AS RECONEXION_DERIVADO
        -- DESCONEXIONES -------------------------------------------------------------------
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'B'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_BASICO
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'D'
                    and O.PRODUCTOPPL <> 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_DIGITAL
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO IN ('C','I' )
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_MODEM
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'E'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_EOC
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'R'
                    and O.PRODUCTOPPL <> 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_DERIVADOS
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'J'
                    and O.PRODUCTOPPL <> 'P' then 1 ELSE 0 END )  
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_DECO_ANALOGICO
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'L'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_FTTH
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'Z'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_FTTH_CATV
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'N'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END )  
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_CORPORATIVO
        , SUM( CASE WHEN O.ORDENTPO = 'D'
                    AND o.PRODUCTOTPO = 'W'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS DESCONEXION_BASICO_EOC
        --- RECLAMOS -------------------------------------------------------------------------
        , SUM( CASE WHEN O.ORDENTPO = 'R'
                    AND o.PRODUCTOTPO <> 'N'
                    and O.ORDENTRBRED = 0 then 1 ELSE 0 END )  
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS RECLAMO
        , SUM( CASE WHEN O.ORDENTPO = 'R'
                    AND o.PRODUCTOTPO = 'N' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS RECLAMO_CORPORTATIVO
        --- SERVICIOS -------------------------------------------------------------------------
        , SUM( CASE WHEN O.ORDENGEN = 'S' AND  
                    O.ORDENTPO = 'S'
                    AND o.PRODUCTOTPO = 'L'
                    and O.PRODUCTOPPL = 'P' then 1 ELSE 0 END  )  
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS UPGRADE_CATV_FTTH
        , SUM( CASE WHEN O.ORDENGEN = 'S' AND  
                    O.ORDENTPO = 'S'
                    AND o.PRODUCTOTPO = 'D'
                    and O.PRODUCTOPPL <> 'P' then 1 ELSE 0 END ) 
            OVER ( PARTITION BY o.empresaid, o.CentroProductivo,  o.clientenroord,o.fecha,ORDENNRO, TECNICO, ID_TECNICO2)  
        AS UPGRADE_DECO
        FROM ordenes o
    )
    , Agrupados as (
    SELECT
        EMPRESAID,
        EMPRESA_nom,
        CentroProductivo,
        FECHA,  
        CLIENTE,  
        ID_TECNICO1,
        TECNICO1_EMPLEADONRO,
        TECNICO1_TIPO,
        TECNICO1, 
        ID_TECNICO2,
        TECNICO2_TIPO,
        TECNICO2_EMPLEADONRO,
        TECNICO2,
        string_agg(O.ORDENNRO, ',') WITHIN GROUP (ORDER BY O.ORDENNRO) DETALLE,
        COUNT (*) TOTAL,
        sum(INSTALACION_BASICO) INSTALACION_BASICO,
        sum(BASICO_ADICIONAL) BASICO_ADICIONAL, 
        sum(INSTALACION_FTTH) INSTALACION_FTTH,
        sum(CATV_FTTH) CATV_FTTH,
        sum(INSTALACION_MODEM) INSTALACION_MODEM,
        sum(INSTALACION_EOC) INSTALACION_EOC,
        sum(INSTALACION_CORPORATIVO) INSTALACION_CORPORATIVO,
        sum(BASICO_CATV_EOC) BASICO_CATV_EOC,
        sum(DERIVADO) DERIVADO,
        sum(INSTALACION_DIGITAL) INSTALACION_DIGITAL,
        sum(case when DIGITAL_ADICIONAL= -1 then 0 else DIGITAL_ADICIONAL end) DIGITAL_ADICIONAL,
        --- RECONEXIONES -------------
        sum(RECONEXION_BASICO) RECONEXION_BASICO,
        sum(RECONEXION_CATV_FTTH) RECONEXION_CATV_FTTH,
		sum(RECONEXION_FTTH) RECONEXION_FTTH,
		sum(RECONEXION_MODEM) RECONEXION_MODEM,
		sum(RECONEXION_EOC) RECONEXION_EOC,
		sum(RECONEXION_CATV_EOC) RECONEXION_CATV_EOC,
		sum(RECONEXION_DERIVADO) RECONEXION_DERIVADO,
        --- DESCONEXIONES -------------
        sum(DESCONEXION_BASICO) DESCONEXION_BASICO,
        sum(DESCONEXION_DIGITAL) DESCONEXION_DIGITAL,
        sum(DESCONEXION_MODEM) DESCONEXION_MODEM,
        sum(DESCONEXION_EOC) DESCONEXION_EOC,
        sum(DESCONEXION_DERIVADOS) DESCONEXION_DERIVADOS,
        sum(DESCONEXION_DECO_ANALOGICO) DESCONEXION_DECO_ANALOGICO,
        sum(DESCONEXION_FTTH) DESCONEXION_FTTH, 
        sum(DESCONEXION_FTTH_CATV) DESCONEXION_FTTH_CATV,
        sum(DESCONEXION_BASICO_EOC ) DESCONEXION_BASICO_EOC,
        sum(DESCONEXION_CORPORATIVO) DESCONEXION_CORPORATIVO,
        --- RECLAMOS -------------
        sum(RECLAMO) RECLAMO,
        sum(RECLAMO_CORPORTATIVO) RECLAMO_CORPORTATIVO,
        -- SERVICIOS ----
        sum(UPGRADE_CATV_FTTH) UPGRADE_CATV_FTTH,
        sum(UPGRADE_DECO) UPGRADE_DECO
    FROM datos_calculados o
    GROUP BY EMPRESAID,
        EMPRESA_nom,
        CentroProductivo,
        FECHA,  
        CLIENTE ,  
        ID_TECNICO1 ,
        TECNICO1_EMPLEADONRO,
        TECNICO1_TIPO,
        TECNICO1, 
        ID_TECNICO2,
        TECNICO2_TIPO,
        TECNICO2_EMPLEADONRO,
        TECNICO2
    )
    ,datos_codigos as (
        Select D.*,concat(
            CASE WHEN INSTALACION_BASICO           > 0 THEN '|HFC_BAS' ELSE '' END           ,
            CASE WHEN BASICO_ADICIONAL             > 0 THEN '|BAS_ADIC' ELSE '' END          ,
            CASE WHEN INSTALACION_FTTH             > 0 THEN '|FTTH_INT' ELSE '' END          ,
            CASE WHEN CATV_FTTH                    > 0 THEN '|FTTH_CATV' ELSE '' END         ,
            CASE WHEN INSTALACION_MODEM            > 0 THEN '|HFC_INT' ELSE '' END           ,
            CASE WHEN INSTALACION_EOC              > 0 THEN '|EOC_INT' ELSE '' END           ,
            CASE WHEN INSTALACION_CORPORATIVO      > 0 THEN '|INST_CORP' ELSE '' END         ,
            CASE WHEN BASICO_CATV_EOC              > 0 THEN '|EOC_CATV' ELSE '' END          ,
            CASE WHEN RECONEXION_BASICO            > 0 THEN '|RECO_BAS' ELSE '' END			 ,
            CASE WHEN RECONEXION_CATV_FTTH         > 0 THEN '|RECO_CATV_FTTH' ELSE '' END	 ,
            CASE WHEN RECONEXION_FTTH              > 0 THEN '|RECO_FTTH' ELSE '' END		 ,
            CASE WHEN RECONEXION_MODEM             > 0 THEN '|RECO_MODEM' ELSE '' END		 ,
            CASE WHEN RECONEXION_EOC               > 0 THEN '|RECO_EOC' ELSE '' END			 ,
            CASE WHEN RECONEXION_CATV_EOC          > 0 THEN '|RECO_CATV_EOC' ELSE '' END	 ,
            CASE WHEN UPGRADE_CATV_FTTH            > 0 THEN '|UPGRADE_FTTH' ELSE '' END		 ,
            CASE WHEN UPGRADE_DECO                 > 0 THEN '|UPGRADE_DECO' ELSE '' END		 ,
            case when (INSTALACION_BASICO  
                        + BASICO_ADICIONAL 
                        + INSTALACION_FTTH + CATV_FTTH 
                        + INSTALACION_MODEM 
                        + INSTALACION_EOC 
                        + INSTALACION_CORPORATIVO 
                        + BASICO_CATV_EOC
                        + RECONEXION_BASICO
                        + RECONEXION_CATV_FTTH
                        + RECONEXION_FTTH
                        + RECONEXION_MODEM
                        + RECONEXION_EOC
                        + RECONEXION_CATV_EOC
                        + UPGRADE_CATV_FTTH
                        + UPGRADE_DECO)>0 then '|' else NULL end)  
            AS codigo_instalacion,
            CONCAT (CASE WHEN RECLAMO                      > 0 THEN '|AT' ELSE '' END		,  
					CASE WHEN RECLAMO_CORPORTATIVO         > 0 THEN '|AT_CORP' ELSE '' END	,   
					CASE WHEN (RECLAMO + RECLAMO_CORPORTATIVO)> 0 THEN '|' ELSE NULL END)
            AS codigo_at,        
			-- CONCAT 1-
            CONCAT(CASE WHEN DERIVADO                     > 0 THEN -- Valida si es un solo derivado o varios.
						-- CONCAT 2
						CONCAT(
						CASE WHEN (INSTALACION_BASICO  + BASICO_ADICIONAL + INSTALACION_FTTH + CATV_FTTH + INSTALACION_MODEM 
							+ INSTALACION_EOC + INSTALACION_CORPORATIVO + BASICO_CATV_EOC+ RECONEXION_BASICO + RECONEXION_CATV_FTTH
							+ RECONEXION_FTTH + RECONEXION_MODEM + RECONEXION_EOC + RECONEXION_CATV_EOC) = 0
                        then 
                            '|DERIV_PRINCIPAL'
                        else
                            ''
						end , 
						case WHEN (INSTALACION_BASICO  + BASICO_ADICIONAL + INSTALACION_FTTH + CATV_FTTH + INSTALACION_MODEM 
							+ INSTALACION_EOC + INSTALACION_CORPORATIVO + BASICO_CATV_EOC + RECONEXION_BASICO + RECONEXION_CATV_FTTH
							+ RECONEXION_FTTH + RECONEXION_MODEM + RECONEXION_EOC + RECONEXION_CATV_EOC) = 0
							AND DERIVADO = 1  THEN
							''
							ELSE 
							'|DERIV' 
						END) -- FIN CONCAT 2
					END ,
				CASE WHEN INSTALACION_DIGITAL                     > 0 THEN -- Valida si es un solo INSTALACION_DIGITAL o varios.
					-- CONCAT 3
					CONCAT(
						CASE WHEN (INSTALACION_BASICO  
							+ BASICO_ADICIONAL 
							+ INSTALACION_FTTH + CATV_FTTH 
							+ INSTALACION_MODEM 
							+ INSTALACION_EOC 
							+ INSTALACION_CORPORATIVO 
							+ BASICO_CATV_EOC
							+ RECONEXION_BASICO
							+ RECONEXION_CATV_FTTH
							+ RECONEXION_FTTH
							+ RECONEXION_MODEM
							+ RECONEXION_EOC
							+ RECONEXION_CATV_EOC + DERIVADO) = 0
							then 
								'|DECO_PRINCIPAL'
							else
								''
						end , 
						case 
							WHEN (INSTALACION_BASICO  
								+ BASICO_ADICIONAL 
								+ INSTALACION_FTTH + CATV_FTTH 
								+ INSTALACION_MODEM 
								+ INSTALACION_EOC 
								+ INSTALACION_CORPORATIVO 
								+ BASICO_CATV_EOC
								+ RECONEXION_BASICO
								+ RECONEXION_CATV_FTTH
								+ RECONEXION_FTTH
								+ RECONEXION_MODEM
								+ RECONEXION_EOC
								+ RECONEXION_CATV_EOC + DERIVADO) = 0
								AND INSTALACION_DIGITAL = 1  THEN
								''
							ELSE 
								'|DECO' 
						END) -- FIN CONCAT 3
					END ,
            CASE WHEN DIGITAL_ADICIONAL            > 0 THEN '|DECO' ELSE '' END              , 
            CASE WHEN (DERIVADO + INSTALACION_DIGITAL + DIGITAL_ADICIONAL)> 0 THEN '|' ELSE NULL END) 
            AS codigo_derivados,
			CONCAT(
				CASE WHEN DESCONEXION_CORPORATIVO      > 0 THEN '|RETIRO_EQUIPO' ELSE '' END     ,
				CASE WHEN DESCONEXION_BASICO           > 0 THEN '|DESC_BASICO' ELSE '' END       ,
				CASE WHEN DESCONEXION_DIGITAL          > 0 THEN '|RETIRO_EQUIPO' ELSE '' END     ,
				CASE WHEN DESCONEXION_MODEM            > 0 THEN '|RETIRO_EQUIPO' ELSE '' END     ,
				CASE WHEN DESCONEXION_EOC              > 0 THEN '|RETIRO_EQUIPO' ELSE '' END     ,
				CASE WHEN DESCONEXION_BASICO_EOC       > 0 THEN '|DESC_BASICO' ELSE '' END       ,
				CASE WHEN DESCONEXION_DERIVADOS        > 0 THEN '|DESC_DERIV' ELSE '' END        ,
				CASE WHEN DESCONEXION_DECO_ANALOGICO   > 0 THEN '|RETIRO_EQUIPO' ELSE '' END     ,
				CASE WHEN DESCONEXION_FTTH             > 0 THEN '|RETIRO_EQUIPO' ELSE '' END     ,
				CASE WHEN DESCONEXION_FTTH_CATV        > 0 THEN '|RETIRO_EQUIPO' ELSE '' END     , 
				CASE WHEN (DESCONEXION_CORPORATIVO + DESCONEXION_BASICO
                        + DESCONEXION_DIGITAL +  DESCONEXION_MODEM
                        + DESCONEXION_EOC + DESCONEXION_BASICO_EOC + DESCONEXION_DERIVADOS
                        + DESCONEXION_DECO_ANALOGICO + DESCONEXION_FTTH 
                        + DESCONEXION_FTTH_CATV)> 0 THEN '|' ELSE NULL END) 
            AS codigo_desconexion,
            case 
                when CLI.CLIENTESTS in ('A','I','P','E') then 'N'
                when CLI.CLIENTESTS in ('C','X','B','M','J') then 'E'
                else 'ERROR'
            End GRUPO_CLIENTE    
        from Agrupados d
            inner join SIGASC.VM_CLIENTE cli
                on d.cliente = cli.clientenro
					--  and d.Empresaid = cli.Empresaid (se quita por cambio de empresa para productividad 19/04/2023)
     ),
 datos_finales as (
     Select 
        r.EMPRESAID EMPRESA
        ,r.EMPRESA_NOM
        ,r.CentroProductivo
        ,r.FECHA
        ,r.CLIENTE
        ,r.ID_TECNICO1
        ,r.TECNICO1_EMPLEADONRO
        ,r.TECNICO1_TIPO
        ,r.TECNICO1
        ,r.ID_TECNICO2
        ,r.TECNICO2_TIPO
        ,r.TECNICO2_EMPLEADONRO
        ,r.TECNICO2
        ,r.TOTAL
        ,r.DETALLE
        --- INSTALACION
        ,r.INSTALACION_BASICO
        ,r.BASICO_ADICIONAL
        ,r.INSTALACION_FTTH
        ,r.CATV_FTTH
        ,r.DERIVADO
        ,r.INSTALACION_DIGITAL
        ,r.DIGITAL_ADICIONAL
        ,r.INSTALACION_MODEM
        ,r.INSTALACION_EOC
        ,r.INSTALACION_CORPORATIVO
        ,r.BASICO_CATV_EOC
        ,r.UPGRADE_CATV_FTTH
        ,r.UPGRADE_DECO
        -- RECONEXIONES
        ,r.RECONEXION_BASICO
        ,r.RECONEXION_CATV_FTTH
        ,r.RECONEXION_FTTH
        ,r.RECONEXION_MODEM
        ,r.RECONEXION_EOC
        ,r.RECONEXION_CATV_EOC
        -- DESCONEXIONES
        ,r.DESCONEXION_BASICO
        ,r.DESCONEXION_DIGITAL
        ,r.DESCONEXION_MODEM
        ,r.DESCONEXION_EOC
        ,r.DESCONEXION_DERIVADOS
        ,r.DESCONEXION_DECO_ANALOGICO
        ,r.DESCONEXION_FTTH
        ,r.DESCONEXION_FTTH_CATV
        ,r.DESCONEXION_BASICO_EOC
        ,r.DESCONEXION_CORPORATIVO
        -- RECLAMOS
        ,r.RECLAMO
        ,r.RECLAMO_CORPORTATIVO
        --- CODIGOS
        ,r.CODIGO_INSTALACION
        ,r.CODIGO_AT
        ,r.CODIGO_DERIVADOS
        ,r.CODIGO_DESCONEXION,
        cti.Coeficiente Coef_Instalacion, 
        ctat.Coeficiente Coef_AT,
        ctd.Coeficiente Coef_Desconexion,
        ctde.Coeficiente Coef_Derivado,
        ISNULL(cti.Coeficiente,0) +
        ISNULL(ctat.Coeficiente,0) +
        ISNULL(ctd.Coeficiente,0) +
        ISNULL(ctde.Coeficiente,0) Coef_Total
     from datos_codigos r
			LEFT JOIN SIGASC.CODIGO_TAREAS CTI
			      ON R.codigo_instalacion = CTI.codigo
                      and r.grupo_cliente = CTI.grupo_cliente
			      and cti.Grupo = 'Instalación'
			LEFT JOIN SIGASC.CODIGO_TAREAS CTAT
			      ON R.codigo_at = CTAT.codigo
			      and r.grupo_cliente = CTAT.grupo_cliente
			      and ctAT.Grupo = 'Atencion Tecnica'
			LEFT JOIN SIGASC.CODIGO_TAREAS CTD
			      ON R.CODIGO_DESCONEXION = CTD.codigo
			      and r.grupo_cliente = CTD.grupo_cliente
			      and ctd.Grupo = 'Desconexion'
			LEFT JOIN SIGASC.CODIGO_TAREAS CTDE
			      ON R.codigo_derivados = CTDE.codigo
			      and r.grupo_cliente = CTDE.grupo_cliente
			      and CTDE.Grupo = 'Derivados'
     )
     Select * 
     from datos_finales r;
```
