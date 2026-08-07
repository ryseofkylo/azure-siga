---
esquema: SIGASC
tabla: ORDENES_PENDIENTES
objeto: SIGASC.ORDENES_PENDIENTES
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `NUMEROORDEN` (único en muestra de 200)
n_columnas: 52
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ORDENES_PENDIENTES

> **BASE TABLE** · Dominio: **Core SIGA** · 52 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `NUMEROORDEN` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `EMPRESAID` | int | 0% |
| 2 | `SUCURSALID` | int | 0% |
| 3 | `NUMEROORDEN` | varchar | 0% |
| 4 | `TIPOORDEN` | varchar | 0% |
| 5 | `ESTADOORDEN` | varchar | 0% |
| 6 | `PRODUCTOID` | varchar | 0% |
| 7 | `MOTIVOINGRESO` | int | 0% |
| 8 | `MOTIVOID` | int | 0% |
| 9 | `FORMAGENERADA` | varchar | 0% |
| 10 | `CENTROOPERATIVOID` | varchar | 0% |
| 11 | `CLIENTENRO` | varchar | 0% |
| 12 | `ESTADOCLIENTE` | varchar | 0% |
| 13 | `FECHAINGRESO` | datetime2 | 0% |
| 14 | `HORAINGRESO` | datetime2 | 100% |
| 15 | `FECHAFINALIZADA` | datetime2 | 76% |
| 16 | `HORAFINALIZADA` | datetime2 | 99% |
| 17 | `FECHAPROCESADA` | datetime2 | 64% |
| 18 | `HORAPROCESADA` | datetime2 | 100% |
| 19 | `FECHAAGENDADA` | datetime2 | 63% |
| 20 | `TURNOID` | varchar | 68% |
| 21 | `TECNICOID` | int | 0% |
| 22 | `DEMORATOTAL` | int | 64% |
| 23 | `TECNICOEMPLEADONRO` | int | 66% |
| 24 | `ORDENTRBRED` | int | 0% |
| 25 | `TIPOPRODUCTO` | varchar | 0% |
| 26 | `PRODUCTOPPAL` | varchar | 0% |
| 27 | `MOTIVOSOLUCION` | varchar | 0% |
| 28 | `USUARIOINGRESO` | varchar | 0% |
| 29 | `USUARIOCIERRE` | varchar | 0% |
| 30 | `ZONAHABID` | varchar | 12% |
| 31 | `ZONAPELID` | varchar | 94% |
| 32 | `CORTE` | date | 72% |
| 33 | `PKCONTRATONRO` | varchar | 0% |
| 34 | `PKPROMOTORID` | varchar | 0% |
| 35 | `PROMOTORGRUPOID` | varchar | 0% |
| 36 | `ORDENFCHCONEXIONFUTURA` | datetime2 | 100% |
| 37 | `ORDENTIPOCONEXION` | varchar | 14% |
| 38 | `COD_MZN` | varchar | 0% |
| 39 | `TIPOCIERRE` | varchar | 0% |
| 40 | `CONTRATOFING` | datetime2 | 0% |
| 41 | `FACTURATOTAL` | float | 56% |
| 42 | `FACTURAPERIODO` | int | 56% |
| 43 | `CUOTASADEUDADAS` | int | 66% |
| 44 | `TECNICOID2` | int | 1% |
| 45 | `MOVILES` | varchar | 0% |
| 46 | `PRODUCTOTPOLISTA` | varchar | 46% |
| 47 | `DERIVADOS` | int | 0% |
| 48 | `DECODERS` | int | 0% |
| 49 | `EXTENSORES` | int | 0% |
| 50 | `CATEGORIACLIENTE` | int | 2% |
| 51 | `CATEGORIAAGRUPACION` | varchar | 2% |
| 52 | `TAREAID` | varchar | 0% |

## Claves de join presentes
- `EMPRESAID` (int) → [[clave-EMPRESAID]]
- `SUCURSALID` (int) → [[clave-SUCURSALID]]
- `PRODUCTOID` (varchar) → [[clave-PRODUCTOID]]
- `MOTIVOID` (int) → [[clave-MOTIVOID]]
- `CENTROOPERATIVOID` (varchar) → [[clave-CENTROOPERATIVOID]]
- `CLIENTENRO` (varchar) → [[clave-CLIENTENRO]]
- `TURNOID` (varchar) → [[clave-TURNOID]]
- `TECNICOID` (int) → [[clave-TECNICOID]]
- `TECNICOEMPLEADONRO` (int) → [[clave-TECNICOEMPLEADONRO]]
- `TIPOPRODUCTO` (varchar) → [[clave-TIPOPRODUCTO]]
- `ZONAHABID` (varchar) → [[clave-ZONAHABID]]
- `ZONAPELID` (varchar) → [[clave-ZONAPELID]]
- `PKCONTRATONRO` (varchar) → [[clave-PKCONTRATONRO]]
- `PKPROMOTORID` (varchar) → [[clave-PKPROMOTORID]]
- `PROMOTORGRUPOID` (varchar) → [[clave-PROMOTORGRUPOID]]
- `TAREAID` (varchar) → [[clave-TAREAID]]

## Relaciones (derivadas de JOINs de vistas)
- [[SIGASC.PRODUCTOTPO]] · `ORDENES_PENDIENTES.TIPOPRODUCTO = PRODUCTOTPO.PRODUCTOTPO` — view_join (V_TAREAS_PENDIENTES), alta
- [[dbo.V_ORD_PENDIENTES_INDICADORES]] · `ORDENES_PENDIENTES.TAREAID = V_ORD_PENDIENTES_INDICADORES.TAREAID` — view_join (V_TAREAS_PENDIENTES), alta
- [[dbo.V_ORD_PENDIENTES_INDIC_2]] · `ORDENES_PENDIENTES.TAREAID = V_ORD_PENDIENTES_INDIC_2.TAREAID` — view_join (V_TAREAS_PENDIENTES), alta

## Reglas de negocio conocidas
**Filtros**
- `p.tipoproducto IN ('B','W','Z')` — _de_ [[dbo.V_ORD_PENDIENTES_INDIC_2]]
- `p.tipoproducto IN ('E','C','I','N','L')` — _de_ [[dbo.V_ORD_PENDIENTES_INDIC_2]]
- `p.tipoproducto = 'R'` — _de_ [[dbo.V_TAREAS_PENDIENTES]]
- `p.tipoproducto = 'D'` — _de_ [[dbo.V_TAREAS_PENDIENTES]]
- `( (p.tipoorden = 'I' AND p.tipoproducto IN ('R', 'D', 'C', 'B', 'L', 'Z', 'E', 'W', 'T', 'N', 'I', 'S')) OR (p.tipoorden = 'D' AND p.tipoproducto IN ('B', 'W', 'T', 'N', 'I', 'S')) OR (p.tipoorden = 'R') )` — _de_ [[dbo.V_TAREAS_PENDIENTES]]
- `p.clientenro IS NOT NULL` — _de_ [[dbo.V_TAREAS_PENDIENTES]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_ORD_PENDIENTES_INDICADORES]], [[dbo.V_ORD_PENDIENTES_INDIC_2]], [[dbo.V_TAREAS_PENDIENTES]]

**Derivaciones (CASE)**
- _de_ [[dbo.V_TAREAS_PENDIENTES]]:
  ```sql
  CASE WHEN p.ordentipoconexion IS NULL OR p.ordentipoconexion='' OR p.ordentipoconexion=' ' THEN 'P' ELSE p.ordentipoconexion END
  ```

## Vistas que la consumen (referencia)
- [[dbo.V_ORD_PENDIENTES_INDICADORES]]
- [[dbo.V_ORD_PENDIENTES_INDIC_2]]
- [[dbo.V_TAREAS_PENDIENTES]]
