import requests

BASE = "https://pokeapi.co/api/v2"

# ---------- POSITIVOS (200) ----------

def test_tc001_pikachu_por_nombre():
    r = requests.get(f"{BASE}/pokemon/pikachu")
    assert r.status_code == 200
    j = r.json()
    assert j["name"] == "pikachu"
    assert j["id"] == 25
    assert any(t["type"]["name"] == "electric" for t in j["types"])
    assert isinstance(j["sprites"]["front_default"], str) and j["sprites"]["front_default"].startswith("http")
    assert len(j["abilities"]) >= 1
    assert len(j["stats"]) == 6
    assert len(j["moves"]) >= 1

def test_tc002_tipo_water():
    r = requests.get(f"{BASE}/type/water")
    assert r.status_code == 200
    j = r.json()
    assert j["name"] == "water"

def test_tc003_tipo_fire():
    r = requests.get(f"{BASE}/type/fire")
    assert r.status_code == 200
    j = r.json()
    assert j["name"] == "fire"

def test_tc004_tipo_por_id_5():
    r = requests.get(f"{BASE}/type/5")
    assert r.status_code == 200
    j = r.json()
    assert isinstance(j["id"], int) and j["id"] > 0
    assert isinstance(j["name"], str) and j["name"] != ""

def test_tc005_species_132_ditto():
    r = requests.get(f"{BASE}/pokemon-species/132")
    assert r.status_code == 200
    j = r.json()
    assert j["name"] == "ditto"
    assert isinstance(j["evolution_chain"]["url"], str) and j["evolution_chain"]["url"].startswith("http")
    assert any(n["language"]["name"] == "en" for n in j["names"])

# ---------- NEGATIVOS (404) ----------

def test_tc006_tipo_earth_no_existe():
    r = requests.get(f"{BASE}/type/earth")
    assert r.status_code == 404

def test_tc007_pokemon_pikachuu_no_existe():
    r = requests.get(f"{BASE}/pokemon/pikachuu")
    assert r.status_code == 404

def test_tc008_generacion_10_no_existe():
    r = requests.get(f"{BASE}/generation/10")
    assert r.status_code == 404

def test_tc009_species_1026_no_existe():
    r = requests.get(f"{BASE}/pokemon-species/1026")
    assert r.status_code == 404

def test_tc010_color_11_no_existe():
    r = requests.get(f"{BASE}/pokemon-color/11")
    assert r.status_code == 404


# --- MODO RESUMEN: ejecuta y muestra "X/Y OK" si corres con `python archivo.py` ---
if __name__ == "__main__":
    tests = [
        test_tc001_pikachu_por_nombre,
        test_tc002_tipo_water,
        test_tc003_tipo_fire,
        test_tc004_tipo_por_id_5,
        test_tc005_species_132_ditto,
        test_tc006_tipo_earth_no_existe,
        test_tc007_pokemon_pikachuu_no_existe,
        test_tc008_generacion_10_no_existe,
        test_tc009_species_1026_no_existe,
        test_tc010_color_11_no_existe,
    ]
    ok = 0
    for t in tests:
        try:
            t()
            print(f"[OK] {t.__name__}")
            ok += 1
        except AssertionError as e:
            print(f"[FAIL] {t.__name__} -> {e}")
        except Exception as e:
            print(f"[ERROR] {t.__name__} -> {e}")

    total = len(tests)
    print(f"RESULTADO FINAL: {ok}/{total} OK")
    import sys
    sys.exit(0 if ok == total else 1)
