import requests
import json

API_KEY = "b332f5cbfdea90daf7f876e3bdcf7534"
URL = "https://api.novaposhta.ua/v2.0/json/"

payload = {
    "apiKey": API_KEY,
    "modelName": "Address",
    "calledMethod": "getWarehouses",
    "methodProperties": {
        "CityName": "Київ"
    }
}

response = requests.post(URL, json=payload)
print("📦 Код ответа:", response.status_code)
print("Ответ:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
