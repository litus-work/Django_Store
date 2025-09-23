

API_KEY = "bfdcfc48f5fbe8dabf2e67a7723143c8"

# test_novapost_stage.py
import os, sys, requests

BASE = "https://api-stage.novapost.pl/v.1.0"               # stage: .pl + v.1.0

def get_jwt():
    url = f"{BASE}/clients/authorization"  # ВАЖНО: clients, и v.1.0
    r = requests.get(url, params={"apiKey": API_KEY}, timeout=15)
    r.raise_for_status()
    data = r.json()
    jwt = data.get("jwt") or data.get("token")
    if not jwt:
        raise RuntimeError(f"Нет jwt/token в ответе: {data}")
    return jwt

def test_divisions(jwt):
    url = f"{BASE}/divisions"
    headers = {"Authorization": f"Bearer {jwt}"}
    params = {
        "countryCodes[]": "UA",
        "divisionCategories[]": "PostBranch",  # PostBranch | CargoBranch | Postomat | PUDO
        "name": "*Kyiv*",                      # маска поиска
        "limit": 5,
    }
    r = requests.get(url, headers=headers, params=params, timeout=20)
    print("GET", r.url, "→", r.status_code)
    if not r.ok:
        print("Ответ:", r.text[:800])
        r.raise_for_status()
    data = r.json()
    items = data if isinstance(data, list) else data.get("items", [])
    for i, d in enumerate(items, 1):
        print(f"{i}. {d.get('name')} — {d.get('address')} (id={d.get('id')})")

def main():
    if not API_KEY or API_KEY == "ВАШ_API_КЛЮЧ":
        print("✖ Укажи API-ключ в NOVAPOST_API_KEY или прямо в файле.")
        sys.exit(1)
    jwt = get_jwt()
    print("✓ JWT получен (первые 30):", jwt[:30], "...")
    test_divisions(jwt)

if __name__ == "__main__":
    main()
