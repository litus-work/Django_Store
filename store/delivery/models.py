from django.db import models
from django.contrib.auth.models import User

class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deliveries")
    city_name = models.CharField(max_length=255)
    city_ref = models.CharField(max_length=255)
    warehouse_name = models.CharField(max_length=255)
    warehouse_ref = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city_name} - {self.warehouse_name}"
