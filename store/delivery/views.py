from django.shortcuts import render
from django.http import JsonResponse
from .api import get_cities, get_warehouses

def select_city(request):
    query = request.GET.get("q", "")
    data = get_cities(query)
    return JsonResponse(data, safe=False)

def select_warehouse(request):
    city_ref = request.GET.get("ref", "")
    data = get_warehouses(city_ref)
    return JsonResponse(data, safe=False)
