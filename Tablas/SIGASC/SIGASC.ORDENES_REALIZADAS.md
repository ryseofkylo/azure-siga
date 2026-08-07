---
esquema: SIGASC
tabla: ORDENES_REALIZADAS
objeto: SIGASC.ORDENES_REALIZADAS
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `TAREAID` (único en muestra de 200)
n_columnas: 52
tags:
  - esquema/SIGASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGASC.ORDENES_REALIZADAS

> **BASE TABLE** · Dominio: **Core SIGA** · 52 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `TAREAID` (único en muestra de 200)

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
| 15 | `FECHAFINALIZADA` | datetime2 | 0% |
| 16 | `HORAFINALIZADA` | datetime2 | 100% |
| 17 | `FECHAPROCESADA` | datetime2 | 0% |
| 18 | `HORAPROCESADA` | datetime2 | 100% |
| 19 | `FECHAAGENDADA` | datetime2 | 30% |
| 20 | `TURNOID` | varchar | 28% |
| 21 | `TECNICOID` | int | 0% |
| 22 | `DEMORATOTAL` | int | 0% |
| 23 | `TECNICOEMPLEADONRO` | int | 2% |
| 24 | `ORDENTRBRED` | int | 0% |
| 25 | `TIPOPRODUCTO` | varchar | 0% |
| 26 | `PRODUCTOPPAL` | varchar | 0% |
| 27 | `MOTIVOSOLUCION` | varchar | 0% |
| 28 | `USUARIOINGRESO` | varchar | 0% |
| 29 | `USUARIOCIERRE` | varchar | 0% |
| 30 | `ZONAHABID` | varchar | 14% |
| 31 | `ZONAPELID` | varchar | 96% |
| 32 | `CORTE` | date | 83% |
| 33 | `PKCONTRATONRO` | varchar | 0% |
| 34 | `PKPROMOTORID` | varchar | 0% |
| 35 | `PROMOTORGRUPOID` | varchar | 0% |
| 36 | `ORDENFCHCONEXIONFUTURA` | datetime2 | 100% |
| 37 | `ORDENTIPOCONEXION` | varchar | 0% |
| 38 | `COD_MZN` | varchar | 0% |
| 39 | `TIPOCIERRE` | varchar | 0% |
| 40 | `CONTRATOFING` | datetime2 | 0% |
| 41 | `FACTURATOTAL` | float | 41% |
| 42 | `FACTURAPERIODO` | int | 41% |
| 43 | `CUOTASADEUDADAS` | int | 65% |
| 44 | `TECNICOID2` | int | 0% |
| 45 | `MOVILES` | varchar | 0% |
| 46 | `PRODUCTOTPOLISTA` | varchar | 47% |
| 47 | `DERIVADOS` | int | 0% |
| 48 | `DECODERS` | int | 0% |
| 49 | `EXTENSORES` | int | 0% |
| 50 | `CATEGORIACLIENTE` | int | 1% |
| 51 | `CATEGORIAAGRUPACION` | varchar | 1% |
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
- [[SIGASC.PRODUCTOTPO]] · `ORDENES_REALIZADAS.TIPOPRODUCTO = PRODUCTOTPO.PRODUCTOTPO` — view_join (V_TAREAS_REALIZADAS), alta
- [[dbo.V_ORD_REALIZADAS_INDICADORES]] · `ORDENES_REALIZADAS.TAREAID = V_ORD_REALIZADAS_INDICADORES.TAREAID` — view_join (V_TAREAS_REALIZADAS), alta
- [[dbo.V_ORD_REALIZADAS_INDIC_2]] · `ORDENES_REALIZADAS.TAREAID = V_ORD_REALIZADAS_INDIC_2.TAREAID` — view_join (V_TAREAS_REALIZADAS), alta

## Reglas de negocio conocidas
**Filtros**
- `p.tipoproducto = 'R'` — _de_ [[dbo.V_TAREAS_REALIZADAS]]
- `p.tipoproducto = 'D'` — _de_ [[dbo.V_TAREAS_REALIZADAS]]
- `p.tareaid <> '-I-C'` — _de_ [[dbo.V_TAREAS_REALIZADAS]]
- `( (p.tipoorden = 'I' AND p.tipoproducto IN ('R', 'D', 'C', 'B', 'L', 'Z', 'E', 'W')) OR (p.tipoorden = 'D' AND p.tipoproducto IN ('B', 'W')) OR (p.tipoorden = 'R') )` — _de_ [[dbo.V_TAREAS_REALIZADAS]]
- `p.clientenro IS NOT NULL` — _de_ [[dbo.V_TAREAS_REALIZADAS]]
- 🚦 `p.estadoorden IN ('F','C')` — _de_ [[dbo.V_TAREAS_REALIZADAS]]
- ♻️ dedup: vistas que deduplican esta tabla → [[dbo.V_ORD_REALIZADAS_FECHAS]], [[dbo.V_ORD_REALIZADAS_INDICADORES]], [[dbo.V_ORD_REALIZADAS_INDIC_2]], [[dbo.V_TAREAS_REALIZADAS]]

## Vistas que la consumen (referencia)
- [[dbo.V_ORD_REALIZADAS_FECHAS]]
- [[dbo.V_ORD_REALIZADAS_INDICADORES]]
- [[dbo.V_ORD_REALIZADAS_INDIC_2]]
- [[dbo.V_TAREAS_REALIZADAS]]
