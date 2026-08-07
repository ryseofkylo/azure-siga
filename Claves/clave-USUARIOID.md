---
objeto: clave-USUARIOID
tipo_objeto: CLAVE DE JOIN
columna: USUARIOID
tipos:
  - int
  - varchar
n_tablas: 5
confidence: baja
tags:
  - tipo/clave-join
  - clave/USUARIOID
---

# Clave de join: `USUARIOID`

> Columna homónima (tipo int, varchar) presente en **5 tablas canónicas**. Candidata de JOIN — confidence **baja** (por nombre+tipo, no declarada).

**SIGAMSASC**
- [[SIGAMSASC.USUARIO]]

**SIGASC**
- [[SIGASC.COBRADOR]]
- [[SIGASC.PROMOTOR]]

**dbo**
- [[dbo.V_USUARIO]]
- [[dbo.V_USUARIO_ORGANIZACION]]
