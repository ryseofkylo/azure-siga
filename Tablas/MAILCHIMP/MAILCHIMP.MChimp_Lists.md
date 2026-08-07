---
esquema: MAILCHIMP
tabla: MChimp_Lists
objeto: MAILCHIMP.MChimp_Lists
tipo_objeto: BASE TABLE
dominio: Email marketing
canonico: true
grain: 1 fila = 1 `ListID` (único en muestra de 14)
n_columnas: 3
tags:
  - esquema/MAILCHIMP
  - dominio/email-marketing
  - tipo/tabla-base
  - canonico
---

# MAILCHIMP.MChimp_Lists

> **BASE TABLE** · Dominio: **Email marketing** · 3 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `ListID` (único en muestra de 14)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `ListID` | nvarchar | 0% |
| 2 | `Name` | nvarchar | 0% |
| 3 | `MemberCount` | int | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
