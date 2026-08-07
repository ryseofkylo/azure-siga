# FASE 3 — Recuperación (implementación)

Retrieval en **dos niveles** con **schema-linking** (sin vector DB; ver la
justificación en `_retrieval/FASE3-diseno-retrieval.md`).

## Piezas
- `system_prompt.md` — instrucciones para el LLM (tabla-first, reglas de negocio,
  protocolo de dos niveles). Va como *system prompt*.
- `_data/catalogo_compacto.md` — **nivel 1**: una línea por tabla base. Va **siempre**
  en contexto junto al system prompt (~33 KB).
- `armar_contexto.py` — **nivel 2**, determinista: dado el conjunto de tablas que el
  LLM nombró, materializa el bundle de contexto (notas completas + reglas +
  relaciones + vecinos por JOIN). No llama a ningún LLM.

## Flujo
1. **System prompt** + **catálogo compacto** → contexto base del modelo.
2. El modelo lee la pregunta y **nombra** las tablas base relevantes.
3. Corrés el ensamblador con esas tablas:
   ```
   python _retrieval/armar_contexto.py contexto SIGASC.H_CONTRATO_CLIENTE SIGASC.PRODUCTO
   ```
   (agregá `--vecinos` para traer también las notas completas de los vecinos 1-hop).
4. Pegás ese bundle como contexto y el modelo genera el SQL **tabla-first**.

### Ayudas
- `python _retrieval/armar_contexto.py catalogo` — imprime el nivel 1.
- `python _retrieval/armar_contexto.py sugerir cobranza cliente` — filtra líneas del
  catálogo que matcheen esas palabras (apoyo al paso 2).

## Pendiente (cuando quieras)
Wiring a un LLM concreto (API de Claude, endpoint local, etc.): un script que tome la
pregunta, deje que el modelo nombre tablas, invoque `armar_contexto.py` y devuelva el
SQL. Se deja fuera a propósito para no atarlo a un proveedor.
