---
esquema: MIO
tabla: TBX_Activities
objeto: MIO.TBX_Activities
tipo_objeto: BASE TABLE
dominio: MIO
canonico: true
grain: 1 fila = 1 `PKGUID` (único en muestra de 200)
n_columnas: 16
tags:
  - esquema/MIO
  - dominio/mio
  - tipo/tabla-base
  - canonico
---

# MIO.TBX_Activities

> **BASE TABLE** · Dominio: **MIO** · 16 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKGUID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Date` | datetime2 | 0% |
| 2 | `Urn` | nvarchar | 0% |
| 3 | `Action` | nvarchar | 0% |
| 4 | `CountryCode` | nvarchar | 0% |
| 5 | `SubscriberID` | numeric | 0% |
| 6 | `Status` | nvarchar | 0% |
| 7 | `Reason` | nvarchar | 0% |
| 8 | `IDP` | nvarchar | 0% |
| 9 | `IDPShortName` | nvarchar | 0% |
| 10 | `ContentProviderName` | nvarchar | 0% |
| 11 | `ContentProviderShortName` | nvarchar | 0% |
| 12 | `Devicetype` | nvarchar | 0% |
| 13 | `Ip` | nvarchar | 0% |
| 14 | `DeviceId` | nvarchar | 0% |
| 15 | `DeviceDescription` | nvarchar | 0% |
| 16 | `PKGUID` | nvarchar | 0% |

## Claves de join presentes
- `SubscriberID` (numeric) → [[clave-SUBSCRIBERID]]
- `DeviceId` (nvarchar) → [[clave-DEVICEID]]
- `PKGUID` (nvarchar) → [[clave-PKGUID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
