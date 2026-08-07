---
esquema: MAILCHIMP
tabla: MChimp_LinkClicks
objeto: MAILCHIMP.MChimp_LinkClicks
tipo_objeto: BASE TABLE
dominio: Email marketing
canonico: true
grain: 1 fila = 1 `LinkId` (único en muestra de 200)
n_columnas: 7
tags:
  - esquema/MAILCHIMP
  - dominio/email-marketing
  - tipo/tabla-base
  - canonico
---

# MAILCHIMP.MChimp_LinkClicks

> **BASE TABLE** · Dominio: **Email marketing** · 7 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `LinkId` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ReportId` | nvarchar | 0% |
| 2 | `CampaignId` | nvarchar | 0% |
| 3 | `LinkUrl` | nvarchar | 0% |
| 4 | `LinkId` | nvarchar | 0% |
| 5 | `ClickRate` | decimal | 0% |
| 6 | `ClickTotal` | int | 0% |
| 7 | `UniqueClicks` | int | 0% |

## Claves de join presentes
- `CampaignId` (nvarchar) → [[clave-CAMPAIGNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
