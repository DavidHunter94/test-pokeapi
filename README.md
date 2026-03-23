# PokéAPI – Script de verificación con Python

Proyecto de pruebas de API contra la **PokéAPI** (https://pokeapi.co), desarrollado como práctica de testing de APIs públicas.

Ejecuta 10 verificaciones y muestra un resumen `X/10 OK` al finalizar, validando tanto respuestas exitosas como manejo de errores 404.

---

## 🧪 Casos de prueba

### Casos positivos (200)
| ID | Endpoint | Validaciones |
|---|---|---|
| TC-001 | `GET /pokemon/pikachu` | nombre, id, tipo eléctrico, sprites, habilidades, stats, movimientos |
| TC-002 | `GET /type/water` | status 200, nombre correcto |
| TC-003 | `GET /type/fire` | status 200, nombre correcto |
| TC-004 | `GET /type/5` | status 200, id y nombre válidos |
| TC-005 | `GET /pokemon-species/132` | nombre "ditto", cadena evolutiva, nombres localizados |

### Casos negativos (404)
| ID | Endpoint | Validación |
|---|---|---|
| TC-006 | `GET /type/earth` | tipo inexistente → 404 |
| TC-007 | `GET /pokemon/pikachuu` | typo en nombre → 404 |
| TC-008 | `GET /generation/10` | generación inexistente → 404 |
| TC-009 | `GET /pokemon-species/1026` | species inexistente → 404 |
| TC-010 | `GET /pokemon-color/11` | color inexistente → 404 |

---

## ⚙️ Tecnologías utilizadas

- **Lenguaje:** Python 3.x
- **Dependencia:** requests
- **API:** PokéAPI v2 (https://pokeapi.co/api/v2)

---

## 🏗️ Estructura del proyecto

```
project/
│
├── test_pokeapi.py    ← Script principal con los 10 casos de prueba
├── requirements.txt   ← Dependencias
└── README.md
```

---

## ▶️ Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone https://github.com/DavidHunter94/test-pokeapi.git
cd test-pokeapi

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar los tests
python test_pokeapi.py
```

Al finalizar verás algo así:

```
[OK] test_tc001_pikachu_por_nombre
[OK] test_tc002_tipo_water
[OK] test_tc003_tipo_fire
[OK] test_tc004_tipo_por_id_5
[OK] test_tc005_species_132_ditto
[OK] test_tc006_tipo_earth_no_existe
[OK] test_tc007_pokemon_pikachuu_no_existe
[OK] test_tc008_generacion_10_no_existe
[OK] test_tc009_species_1026_no_existe
[OK] test_tc010_color_11_no_existe

RESULTADO FINAL: 10/10 OK
```

---

## 🔍 Detalles de implementación

- Cada función de prueba es independiente y autocontenida
- El bloque principal ejecuta las 10 funciones en orden y reporta resultados
- Termina con `sys.exit(0)` si todas pasan, `sys.exit(1)` si alguna falla
- No requiere pytest — corre directamente con `python`

---

## 🚀 Autor

**Victor David Martínez Matías**
QA Engineer con experiencia en pruebas manuales, automatización UI y pruebas de API.
