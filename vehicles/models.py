from django.db import models

# Create your models here.

class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    mileage = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    last_service_km = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"
