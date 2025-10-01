# QA PokéAPI — Script de verificación (Python)

Script en **Python** que realiza **10 verificaciones** contra la PokéAPI y muestra un **resumen `X/Y OK`** al finalizar.

---

## Estructura del archivo

**Nombre del archivo:** `test_pokeapi.py`

- **Importaciones**
  - `requests` — para realizar solicitudes HTTP.

- **Constantes**
  - `BASE = "https://pokeapi.co/api/v2"` — URL base usada para construir cada endpoint.

- **Funciones de verificación (10)**
  - `test_tc001_pikachu_por_nombre()`
  - `test_tc002_tipo_water()`
  - `test_tc003_tipo_fire()`
  - `test_tc004_tipo_por_id_5()`
  - `test_tc005_species_132_ditto()`
  - `test_tc006_tipo_earth_no_existe()`
  - `test_tc007_pokemon_pikachuu_no_existe()`
  - `test_tc008_generacion_10_no_existe()`
  - `test_tc009_species_1026_no_existe()`
  - `test_tc010_color_11_no_existe()`

- **Bloque de ejecución**
  - `if __name__ == "__main__":`
    - Declara la lista `tests` con las 10 funciones anteriores.
    - Ejecuta cada función en orden.
    - Imprime `[OK] nombre_de_la_función` si pasa sin lanzar excepción.
    - Imprime `[FAIL]` o `[ERROR]` con detalle si ocurre una excepción.
    - Muestra `RESULTADO FINAL: X/10 OK`.
    - Finaliza con `sys.exit(0)` cuando todas pasan, o `sys.exit(1)` en caso contrario.

---

## Verificaciones realizadas (detalle por prueba)

### TC-001 — `GET /pokemon/pikachu` (200)
- `r.status_code == 200`
- `j["name"] == "pikachu"`
- `j["id"] == 25`
- `any(t["type"]["name"] == "electric" for t in j["types"])`
- `isinstance(j["sprites"]["front_default"], str)` y comienza con `"http"`
- `len(j["abilities"]) >= 1`
- `len(j["stats"]) == 6`
- `len(j["moves"]) >= 1`

### TC-002 — `GET /type/water` (200)
- `r.status_code == 200`
- `j["name"] == "water"`

### TC-003 — `GET /type/fire` (200)
- `r.status_code == 200`
- `j["name"] == "fire"`

### TC-004 — `GET /type/5` (200)
- `r.status_code == 200`
- `isinstance(j["id"], int)` y `j["id"] > 0`
- `isinstance(j["name"], str)` y `j["name"] != ""`

### TC-005 — `GET /pokemon-species/132` (200)
- `r.status_code == 200`
- `j["name"] == "ditto"`
- `isinstance(j["evolution_chain"]["url"], str)` y comienza con `"http"`
- `any(n["language"]["name"] == "en" for n in j["names"])`

### TC-006 — `GET /type/earth` (404)
- `r.status_code == 404`

### TC-007 — `GET /pokemon/pikachuu` (404)
- `r.status_code == 404`

### TC-008 — `GET /generation/10` (404)
- `r.status_code == 404`

### TC-009 — `GET /pokemon-species/1026` (404)
- `r.status_code == 404`

### TC-010 — `GET /pokemon-color/11` (404)
- `r.status_code == 404`

---

## Flujo de salida

Durante la ejecución, el script imprime una línea por función:
```
[OK] test_tc001_pikachu_por_nombre
[OK] test_tc002_tipo_water
...
```
Al final imprime:
```
RESULTADO FINAL: X/10 OK
```
y termina con código de salida **0** cuando `X == 10`, o **1** en caso contrario.

---

## Dependencias observadas en el código

- `requests`

---

## Ejecución

```
python test_pokeapi.py
```

---

## Autor y fuente original de los casos

- **Autor**: Nicolas Benegas
- **Página original**: APIMON RIVEIRA en Scribd — https://es.scribd.com/document/878211357/APIMON-RIVEIRA
- **Documentación de los casos de prueba**: https://docs.google.com/spreadsheets/d/13jylpctWsb19tyo2FvaAidWQtY0Df3MLBDqTYJwicSU/edit?usp=sharing