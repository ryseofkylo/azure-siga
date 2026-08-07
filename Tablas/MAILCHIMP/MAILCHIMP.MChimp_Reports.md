---
esquema: MAILCHIMP
tabla: MChimp_Reports
objeto: MAILCHIMP.MChimp_Reports
tipo_objeto: BASE TABLE
dominio: Email marketing
canonico: true
grain: 1 fila = 1 `CampaignId` (único en muestra de 200)
n_columnas: 14
tags:
  - esquema/MAILCHIMP
  - dominio/email-marketing
  - tipo/tabla-base
  - canonico
---

# MAILCHIMP.MChimp_Reports

> **BASE TABLE** · Dominio: **Email marketing** · 14 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CampaignId` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CampaignId` | nvarchar | 0% |
| 2 | `CampaignTitle` | nvarchar | 0% |
| 3 | `EmailsSent` | int | 0% |
| 4 | `OpenRate` | decimal | 0% |
| 5 | `OpenTotal` | int | 0% |
| 6 | `UniqueOpens` | int | 0% |
| 7 | `ClickRate` | decimal | 0% |
| 8 | `ClickTotal` | int | 0% |
| 9 | `UniqueClicks` | int | 0% |
| 10 | `UniqueSubscriberClicks` | int | 0% |
| 11 | `Unsubscribed` | int | 0% |
| 12 | `HardBounces` | int | 0% |
| 13 | `SoftBounces` | int | 0% |
| 14 | `SyntaxErrors` | int | 0% |

## Claves de join presentes
- `CampaignId` (nvarchar) → [[clave-CAMPAIGNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
