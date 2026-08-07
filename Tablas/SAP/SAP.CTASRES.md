---
esquema: SAP
tabla: CTASRES
objeto: SAP.CTASRES
tipo_objeto: BASE TABLE
dominio: Compras y Finanzas (SAP)
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `Importe_ML2`, `Texto`, `Nro_doc`
n_columnas: 31
tags:
  - esquema/SAP
  - dominio/compras-y-finanzas-_sap_
  - tipo/tabla-base
  - canonico
---

# SAP.CTASRES

> **BASE TABLE** · Dominio: **Compras y Finanzas (SAP)** · 31 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `Importe_ML2`, `Texto`, `Nro_doc`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Div` | varchar | 0% |
| 2 | `Nombre_division` | varchar | 0% |
| 3 | `Soc` | varchar | 0% |
| 4 | `Lib_mayor` | varchar | 0% |
| 5 | `Nombre_cuenta_contable` | varchar | 0% |
| 6 | `Nro_doc` | varchar | 36% |
| 7 | `Referencia` | varchar | 0% |
| 8 | `Ejerc_mes` | varchar | 0% |
| 9 | `Fecha_doc` | date | 0% |
| 10 | `Registrado` | date | 0% |
| 11 | `Fe_contab` | date | 0% |
| 12 | `Clase` | varchar | 0% |
| 13 | `CPCon` | varchar | 68% |
| 14 | `ImpteML` | decimal | 66% |
| 15 | `Mon` | varchar | 0% |
| 16 | `Importe_ML2` | decimal | 29% |
| 17 | `ML2` | varchar | 0% |
| 18 | `Texto` | varchar | 0% |
| 19 | `CtaCP` | varchar | 2% |
| 20 | `Descripcion_Acreedor` | varchar | 0% |
| 21 | `Texto_cab_documento` | varchar | 0% |
| 22 | `Asignacion` | varchar | 0% |
| 23 | `I` | varchar | 0% |
| 24 | `Doc_comp` | varchar | 0% |
| 25 | `St` | varchar | 0% |
| 26 | `Area_funcional` | varchar | 0% |
| 27 | `CeBe` | varchar | 0% |
| 28 | `Ce_coste` | varchar | 0% |
| 29 | `Area_func` | varchar | 0% |
| 30 | `Usuario` | varchar | 0% |
| 31 | `Elemento_PEP` | varchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
