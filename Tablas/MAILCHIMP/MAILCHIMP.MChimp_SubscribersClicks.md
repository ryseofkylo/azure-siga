---
esquema: MAILCHIMP
tabla: MChimp_SubscribersClicks
objeto: MAILCHIMP.MChimp_SubscribersClicks
tipo_objeto: BASE TABLE
dominio: Email marketing
canonico: true
grain: 1 fila ≈ 1 combinación de (`EmailId`) — compuesto, tentativo (muestra 10)
n_columnas: 6
tags:
  - esquema/MAILCHIMP
  - dominio/email-marketing
  - tipo/tabla-base
  - canonico
---

# MAILCHIMP.MChimp_SubscribersClicks

> **BASE TABLE** · Dominio: **Email marketing** · 6 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila ≈ 1 combinación de (`EmailId`) — compuesto, tentativo (muestra 10)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `CampaignId` | nvarchar | 0% |
| 2 | `Clicks` | nvarchar | 0% |
| 3 | `Email` | nvarchar | 0% |
| 4 | `EmailId` | nvarchar | 0% |
| 5 | `ListId` | nvarchar | 0% |
| 6 | `UrlId` | nvarchar | 0% |

## Claves de join presentes
- `CampaignId` (nvarchar) → [[clave-CAMPAIGNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
