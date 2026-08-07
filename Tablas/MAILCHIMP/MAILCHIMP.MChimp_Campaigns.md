---
esquema: MAILCHIMP
tabla: MChimp_Campaigns
objeto: MAILCHIMP.MChimp_Campaigns
tipo_objeto: BASE TABLE
dominio: Email marketing
canonico: true
grain: 1 fila = 1 `CampaignID` (único en muestra de 200)
n_columnas: 5
tags:
  - esquema/MAILCHIMP
  - dominio/email-marketing
  - tipo/tabla-base
  - canonico
---

# MAILCHIMP.MChimp_Campaigns

> **BASE TABLE** · Dominio: **Email marketing** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `CampaignID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CampaignID` | nvarchar | 0% |
| 2 | `Title` | nvarchar | 0% |
| 3 | `Type` | nvarchar | 0% |
| 4 | `Status` | nvarchar | 0% |
| 5 | `SendTime` | datetime | 0% |

## Claves de join presentes
- `CampaignID` (nvarchar) → [[clave-CAMPAIGNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
