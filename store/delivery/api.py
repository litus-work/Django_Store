import requests
import json
from django.conf import settings

API_KEY = "b332f5cbfdea90daf7f876e3bdcf7534"
URL = "https://api.novaposhta.ua/v2.0/json/"

def get_cities(search: str):
    payload = {
        "apiKey": API_KEY,
        "modelName": "Address",
        "calledMethod": "getCities",
        "methodProperties": {"FindByString": search}
    }
    r = requests.post(URL, json=payload)
    return r.json().get("data", [])

def get_warehouses(city_ref: str):
    payload = {
        "apiKey": API_KEY,
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {"CityRef": city_ref}
    }
    r = requests.post(URL, json=payload)
    return r.json().get("data", [])
