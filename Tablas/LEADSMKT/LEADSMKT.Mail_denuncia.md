---
esquema: LEADSMKT
tabla: Mail_denuncia
objeto: LEADSMKT.Mail_denuncia
tipo_objeto: BASE TABLE
dominio: Marketing / Leads
canonico: true
grain: grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `mail`
n_columnas: 1
tags:
  - esquema/LEADSMKT
  - dominio/marketing-leads
  - tipo/tabla-base
  - canonico
---

# LEADSMKT.Mail_denuncia

> **BASE TABLE** · Dominio: **Marketing / Leads** · 1 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** grano fino / posible tabla de hechos — sin clave única en muestra; más identificadoras: `mail`

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `mail` | nvarchar | 0% |

## Claves de join presentes
_(sin claves detectadas)_

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
_(ninguna)_
