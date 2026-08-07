---
esquema: SIGAMSASC
tabla: USUARIO
objeto: SIGAMSASC.USUARIO
tipo_objeto: BASE TABLE
dominio: Core SIGA
canonico: true
grain: 1 fila = 1 `USUARIOID` (único en muestra de 200)
n_columnas: 27
tags:
  - esquema/SIGAMSASC
  - dominio/core-siga
  - tipo/tabla-base
  - canonico
---

# SIGAMSASC.USUARIO

> **BASE TABLE** · Dominio: **Core SIGA** · 27 columnas · Consultá esta tabla directamente (**tabla-first**).
> **Grain (inferido):** 1 fila = 1 `USUARIOID` (único en muestra de 200)

## Columnas
| # | Columna | Tipo | %null (m) |
|--:|---|---|--:|
| 1 | `USUARIOID` | int | 0% |
| 2 | `USUARIONOMBRE` | varchar | 0% |
| 3 | `USUARIOEMAIL` | varchar | 0% |
| 4 | `USUARIOLGN` | varchar | 0% |
| 5 | `USUARIOPSW` | varchar | 60% |
| 6 | `ORGANIZACIONID` | int | 0% |
| 7 | `USUARIOEMAILLGN` | varchar | 0% |
| 8 | `USUARIOEMAILPSW` | varchar | 0% |
| 9 | `USUARIOIMG` | varbinary |  |
| 10 | `USUARIOPSWFCH` | datetime2 | 14% |
| 11 | `USUARIOPSWEXPIRA` | int | 0% |
| 12 | `USUARIOBLOQUEADO` | int | 0% |
| 13 | `USUARIOFCHEXPIRACIONCTA` | datetime2 | 100% |
| 14 | `USUARIOMOVIL` | varchar | 48% |
| 15 | `USUARIOFCHINGRESO` | datetime2 | 29% |
| 16 | `USUARIOSUPERVISOR` | int | 48% |
| 17 | `USUARIOSEXO` | varchar | 20% |
| 18 | `USUARIOPSWDEFAULT` | int | 0% |
| 19 | `USUARIOPSWHASH` | varchar | 38% |
| 20 | `USUARIOLEGAJO` | varchar | 14% |
| 21 | `USUARIOSTS` | varchar | 0% |
| 22 | `ADACTIVO` | int | 50% |
| 23 | `ADUSERNAME` | varchar | 46% |
| 24 | `ADID` | int | 48% |
| 25 | `PIPELINERUNID` | varchar | 0% |
| 26 | `ADFECHAEXPIRACIONPSW` | datetime2 | 54% |
| 27 | `ADUSERPRINCIPALNAME` | varchar | 50% |

## Claves de join presentes
- `USUARIOID` (int) → [[clave-USUARIOID]]
- `ORGANIZACIONID` (int) → [[clave-ORGANIZACIONID]]
- `PIPELINERUNID` (varchar) → [[clave-PIPELINERUNID]]

## Relaciones (derivadas de JOINs de vistas)
_(ninguna relación explícita hallada en vistas)_

## Reglas de negocio conocidas
_(ninguna regla derivada de vistas)_

## Vistas que la consumen (referencia)
- [[dbo.V_USUARIO]]
