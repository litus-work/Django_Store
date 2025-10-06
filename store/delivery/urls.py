from django.urls import path
from . import views

app_name = 'delivery'

urlpatterns = [
    path('cities/', views.select_city, name='select_city'),
    path('warehouses/', views.select_warehouse, name='select_warehouse'),
]
