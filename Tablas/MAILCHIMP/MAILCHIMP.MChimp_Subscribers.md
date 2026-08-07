---
esquema: MAILCHIMP
tabla: MChimp_Subscribers
objeto: MAILCHIMP.MChimp_Subscribers
tipo_objeto: BASE TABLE
dominio: Email marketing
canonico: true
grain: 1 fila = 1 `ContactId` (único en muestra de 200)
n_columnas: 11
tags:
  - esquema/MAILCHIMP
  - dominio/email-marketing
  - tipo/tabla-base
  - canonico
---

# MAILCHIMP.MChimp_Subscribers

> **BASE TABLE** · Dominio: **Email marketing** · 11 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ContactId` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ListId` | nvarchar | 0% |
| 2 | `ContactId` | nvarchar | 0% |
| 3 | `clientenro` | int | 0% |
| 4 | `Email` | nvarchar | 0% |
| 5 | `FullName` | nvarchar | 0% |
| 6 | `EmailClient` | nvarchar | 0% |
| 7 | `Status` | nvarchar | 0% |
| 8 | `IP` | nvarchar | 0% |
| 9 | `MemberRating` | int | 0% |
| 10 | `Source` | nvarchar | 0% |
| 11 | `UnsubscribeReason` | nvarchar | 98% |

## Claves de join presentes
- `clientenro` (int) → [[clave-CLIENTENRO]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
