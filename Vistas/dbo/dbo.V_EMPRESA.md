---
esquema: dbo
tabla: V_EMPRESA
objeto: dbo.V_EMPRESA
tipo_objeto: VIEW
dominio: Data Warehouse / BI
canonico: true
referencia: true
grain: N/A (vista)
n_columnas: 7
tags:
  - esquema/dbo
  - dominio/data-warehouse-bi
  - tipo/vista
  - referencia
---

# dbo.V_EMPRESA

> ⚠️ **VISTA — REFERENCIA, no target de consulta.** Mostrá *cómo se armó* esta info; para consultar, andá a las tablas base de abajo.

## Tablas base que consume
- [[SIGAMSASC.EMPRESA]]

## Columnas expuestas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `EMPRESAORIGEN` | varchar | 0% |
| 3 | `EMPRESADEVENGAVTO` | int | 0% |
| 4 | `EMPRESANOMBRE` | varchar | 0% |
| 5 | `EMPRESAZONA` | varchar | 4% |
| 6 | `EMPRESAGRUPO` | varchar | 0% |
| 7 | `EMPRESAORDEN` | int | 0% |

## Definición (CREATE VIEW)
```sql
-- Vista: dbo.V_EMPRESA
-- Extraida: 2026-08-07T15:27:52.409308+00:00
-- Fuente: sys.sql_modules / OBJECT_DEFINITION

CREATE VIEW [V_EMPRESA]
AS SELECT a.*,
	   CASE --WHEN empresaid IN ('4','21')  THEN 'CATAMARCA'
			WHEN empresaid IN ('11','28') THEN 'BARILOCHE'
			WHEN empresaid IN ('1','27')  THEN 'MENDOZA'
			WHEN empresaid IN ('2','29')  THEN 'SAN JUAN'
			ELSE empresanombre
	   END AS EMPRESAGRUPO,
	   CASE empresanombre
	   WHEN 'TUCUMAN'			  THEN 1
	   WHEN 'TV CATAMARCA'		  THEN 2
	   WHEN 'TVCA'				  THEN 3
	   WHEN 'SANTIAGO DEL ESTERO' THEN 4
	   WHEN 'LA RIOJA'			  THEN 5
	   WHEN 'RECONQUISTA'		  THEN 6
	   WHEN 'SAN JUAN'			  THEN 7
	   WHEN 'SION SAN JUAN'		  THEN 7
	   WHEN 'VILLA MERCEDES'	  THEN 8
	   WHEN 'MENDOZA'			  THEN 9
	   WHEN 'TCC MENDOZA'		  THEN 9
	   WHEN 'LABOULAYE'			  THEN 10
	   WHEN 'LEVALLE'			  THEN 11
	   WHEN 'RIO CUARTO'		  THEN 12
	   WHEN 'VICUÑA MAKENNA'	  THEN 13
	   WHEN 'VILLA DOLORES'		  THEN 14
	   WHEN 'SAN MARTIN DE LOS ANDES' THEN 15
	   WHEN 'VIEDMA'			  THEN 16
	   WHEN 'BARILOCHE'			  THEN 17
	   WHEN 'GCGROUP'			  THEN 17
	   WHEN 'PUERTO MADRYN'		  THEN 18
	   WHEN 'TRELEW'			  THEN 19
	   WHEN 'COMODORO RIVADAVIA'  THEN 20
	   WHEN 'RIO GALLEGOS'		  THEN 21
	   WHEN 'USHUAIA'			  THEN 22
	   ELSE 23
	   END AS EMPRESAORDEN	    
FROM ( SELECT EMPRESAID, 
				empresanom AS EMPRESAORIGEN,
				EMPRESADEVENGAVTO,
				CASE WHEN empresanom = 'SUPERCANAL MENDOZA'				    THEN 'MENDOZA'
					 WHEN empresanom = 'SUPERCANAL SAN JUAN'			    THEN 'SAN JUAN'
					 WHEN empresanom = 'SUPERCANAL TUCUMAN'				    THEN 'TUCUMAN'
					 WHEN empresanom = 'SUPERCANAL CATAMARCA'			    THEN 'TV CATAMARCA'
					 WHEN empresanom = 'SUPERCANAL SANTA CRUZ'			    THEN 'RIO GALLEGOS'
					 WHEN empresanom = 'SUPERCANAL SAN LUIS'			    THEN 'VILLA MERCEDES'
					 WHEN empresanom = 'SUPERCANAL TIERRA DEL FUEGO'	    THEN 'USHUAIA'
					 WHEN empresanom = 'SUPERCANAL COMODORO RIVADAVIA'	    THEN 'COMODORO RIVADAVIA'
					 WHEN empresanom = 'SUPERCANAL PUERTO MADRYN'		    THEN 'PUERTO MADRYN'
					 WHEN empresanom = 'SUPERCANAL TRELEW'				    THEN 'TRELEW'
					 WHEN empresanom = 'SUPERCANAL BARILOCHE'		        THEN 'BARILOCHE'
					 WHEN empresanom = 'SUPERCANAL VIEDMA - PATAGONES'	    THEN 'VIEDMA'
					 WHEN empresanom = 'SUPERCANAL SAN MARTIN DE LOS ANDES' THEN 'SAN MARTIN DE LOS ANDES'
					 WHEN empresanom = 'TAJAMAR - MUNDO TV'				    THEN 'ALTA GRACIA'
					 WHEN empresanom = 'SUPERCANAL LA RIOJA - CHILECITO'	THEN 'LA RIOJA'
					 WHEN empresanom = 'FIBRA IMAGEN RIO CUARTO'		    THEN 'RIO CUARTO'
					 WHEN empresanom = 'SUPERCANAL LABOULAYE'		        THEN 'LABOULAYE'
					 WHEN empresanom = 'SUPERCANAL CORDOBA'				    THEN 'CORDOBA'
					 WHEN empresanom = 'RTC RECONQUISTA'					THEN 'RECONQUISTA'
					 WHEN empresanom = 'TVCAT CATAMARCA'					THEN 'TVCA'
					 WHEN empresanom = 'TIC S.A.'						    THEN 'SANTIAGO DEL ESTERO'
					 WHEN empresanom = 'VICUNA MACKENNA'					THEN 'VICUÑA MAKENNA'
					 WHEN empresanom = 'GENERAL LEVALLE'					THEN 'LEVALLE'
					 WHEN empresanom = 'VILLA DOLORES'					    THEN 'VILLA DOLORES'
					 WHEN empresanom = 'TCC MENDOZA'						THEN 'TCC MENDOZA'
					 WHEN empresanom = 'GCGROUP BARILOCHE'					THEN 'GCGROUP'
					 WHEN empresanom = 'SION SAN JUAN'						THEN 'SION SAN JUAN'
					 ELSE empresanom
				END AS EMPRESANOMBRE,
				CASE WHEN empresaid IN ('1','2','6','15','17','18','19','24','25','26','27','29') THEN 'ZONA CENTRO'
					 WHEN empresaid IN ('3','4','16','20','21','23')						 THEN 'ZONA NORTE'
					 WHEN empresaid IN ('5','7','8','9','10','11','12','14','28')			 THEN 'ZONA SUR'
				END AS EMPRESAZONA
	   FROM SIGAMSASC.EMPRESA
	   WHERE empresaid <> '22'
	 ) a;
```
