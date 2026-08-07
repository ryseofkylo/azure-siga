---
esquema: MAILCHIMP
tabla: MChimp_OngoingCampaigns
objeto: MAILCHIMP.MChimp_OngoingCampaigns
tipo_objeto: BASE TABLE
dominio: Email marketing
canonico: true
grain: TODO (muestra vacía)
n_columnas: 5
tags:
  - esquema/MAILCHIMP
  - dominio/email-marketing
  - tipo/tabla-base
  - canonico
---

# MAILCHIMP.MChimp_OngoingCampaigns

> **BASE TABLE** · Dominio: **Email marketing** · 5 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** TODO (muestra vacía)

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
