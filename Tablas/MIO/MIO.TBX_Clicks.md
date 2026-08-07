---
esquema: MIO
tabla: TBX_Clicks
objeto: MIO.TBX_Clicks
tipo_objeto: BASE TABLE
dominio: MIO
canonico: true
grain: 1 fila = 1 `PKGUID` (único en muestra de 200)
n_columnas: 35
tags:
  - esquema/MIO
  - dominio/mio
  - tipo/tabla-base
  - canonico
---

# MIO.TBX_Clicks

> **BASE TABLE** · Dominio: **MIO** · 35 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `PKGUID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `Date` | datetime2 | 0% |
| 2 | `CountryCode` | nvarchar | 0% |
| 3 | `Network` | nvarchar | 0% |
| 4 | `Id` | nvarchar | 0% |
| 5 | `SubscriberId` | numeric | 0% |
| 6 | `CustomerId` | nvarchar | 0% |
| 7 | `Ratings` | nvarchar | 0% |
| 8 | `IDP` | nvarchar | 0% |
| 9 | `IDPShortName` | nvarchar | 0% |
| 10 | `ContentProviderShortName` | nvarchar | 0% |
| 11 | `ContentProviderName` | nvarchar | 0% |
| 12 | `Description` | nvarchar | 64% |
| 13 | `Source` | nvarchar | 0% |
| 14 | `Provider` | nvarchar | 0% |
| 15 | `PlatformType` | nvarchar | 0% |
| 16 | `DeviceType` | nvarchar | 0% |
| 17 | `URN` | nvarchar | 0% |
| 18 | `BillingId` | nvarchar | 87% |
| 19 | `ViewCondition` | nvarchar | 0% |
| 20 | `IsClip` | nvarchar | 0% |
| 21 | `ExternalId` | nvarchar | 0% |
| 22 | `DeviceDescription` | nvarchar | 0% |
| 23 | `XforwardedFor` | nvarchar | 0% |
| 24 | `DeviceId` | nvarchar | 0% |
| 25 | `ProfileId` | nvarchar | 0% |
| 26 | `PKGUID` | nvarchar | 0% |
| 27 | `Title` | nvarchar | 3% |
| 28 | `Episode` | nvarchar | 90% |
| 29 | `SeriesTitle` | nvarchar | 90% |
| 30 | `AlternativeTitle` | nvarchar | 90% |
| 31 | `ReleaseYear` | nvarchar | 88% |
| 32 | `Duration` | nvarchar | 3% |
| 33 | `Season` | nvarchar | 90% |
| 34 | `Genres` | nvarchar | 20% |
| 35 | `ContentType` | nvarchar | 3% |

## Claves de join presentes
- `Id` (nvarchar) → [[clave-ID]]
- `SubscriberId` (numeric) → [[clave-SUBSCRIBERID]]
- `DeviceId` (nvarchar) → [[clave-DEVICEID]]
- `PKGUID` (nvarchar) → [[clave-PKGUID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
