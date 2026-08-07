---
objeto: MOC-INDICE
tipo_objeto: MOC-raiz
tags:
  - tipo/moc
  - indice
---

# Catálogo SIGA — Índice

- Tablas base canónicas: **389**
- Vistas (referencia): **188**
- Familias (particiones): **7**
- Claves de join (hubs): **182**
- Relaciones (view_join): **285**
- Reglas de negocio: **934**
- Deprecated (fuera de corpus): **150**

## MOCs por esquema
- [[MOC-ACTIVITY]]
- [[MOC-BIGDATA]]
- [[MOC-COMPRAS]]
- [[MOC-LEADS]]
- [[MOC-LEADSMKT]]
- [[MOC-MAILCHIMP]]
- [[MOC-MAPPING]]
- [[MOC-MIO]]
- [[MOC-MKT]]
- [[MOC-SAP]]
- [[MOC-SAP_COMPRAS]]
- [[MOC-SIGAMSASC]]
- [[MOC-SIGASC]]
- [[MOC-TEMP]]
- [[MOC-VISMA]]
- [[MOC-dbo]]

## Cómo usar
- **Tabla-first**: consultá las tablas base; las vistas son *referencia* de cómo se armó cada cosa.
- Las **reglas de negocio** (tombstone 1900-01-01, filtros de estado, dedup) están en cada nota de tabla base.
- **Grain** inferido en cada nota de tabla (qué representa 1 fila).
- Recuperación (FASE 3) en `_retrieval/` (system prompt + ensamblador de contexto).