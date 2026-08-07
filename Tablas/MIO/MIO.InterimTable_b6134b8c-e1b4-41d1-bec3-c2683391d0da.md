---
esquema: MIO
tabla: InterimTable_b6134b8c-e1b4-41d1-bec3-c2683391d0da
objeto: MIO.InterimTable_b6134b8c-e1b4-41d1-bec3-c2683391d0da
tipo_objeto: BASE TABLE
dominio: MIO
canonico: true
grain: 1 fila = 1 `PKGUID` (único en muestra de 200)
n_columnas: 38
tags:
  - esquema/MIO
  - dominio/mio
  - tipo/tabla-base
  - canonico
---

# MIO.InterimTable_b6134b8c-e1b4-41d1-bec3-c2683391d0da

> **BASE TABLE** · Dominio: **MIO** · 38 columnas · Consultá esta tabla directamente (**tabla-first**).
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
| 10 | `ContentProviderName` | nvarchar | 0% |
| 11 | `ContentProviderShortName` | nvarchar | 0% |
| 12 | `Source` | nvarchar | 0% |
| 13 | `Provider` | nvarchar | 0% |
| 14 | `DeviceType` | nvarchar | 0% |
| 15 | `PlatformType` | nvarchar | 0% |
| 16 | `TypeEvent` | nvarchar | 0% |
| 17 | `Position` | nvarchar | 0% |
| 18 | `FormatType` | nvarchar | 98% |
| 19 | `DRMType` | nvarchar | 99% |
| 20 | `Language` | nvarchar | 0% |
| 21 | `BitRate` | nvarchar | 0% |
| 22 | `BufferTime` | nvarchar | 100% |
| 23 | `PlaybackNetTime` | nvarchar | 0% |
| 24 | `ExternalId` | nvarchar | 0% |
| 25 | `DeviceDescription` | nvarchar | 0% |
| 26 | `DeviceId` | nvarchar | 0% |
| 27 | `ProfileId` | nvarchar | 0% |
| 28 | `PKGUID` | nvarchar | 0% |
| 29 | `Title` | nvarchar | 0% |
| 30 | `Episode` | nvarchar | 100% |
| 31 | `SeriesTitle` | nvarchar | 100% |
| 32 | `AlternativeTitle` | nvarchar | 100% |
| 33 | `ReleaseYear` | nvarchar | 100% |
| 34 | `Duration` | nvarchar | 0% |
| 35 | `Season` | nvarchar | 100% |
| 36 | `Genres` | nvarchar | 2% |
| 37 | `ContentType` | nvarchar | 0% |
| 38 | `BatchIdentifier` | bigint | 0% |

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
