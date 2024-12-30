from django.db import models
from vehicles.models import Vehicle  # Assurez-vous que l'application vehicles existe
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    client_name = models.CharField(max_length=100)
    client_license_plate = models.CharField(max_length=20)
    client_vehicle_date = models.DateField()
    commercial_advisor = models.CharField(max_length=100)
    service_advisor = models.CharField(max_length=100)
    criticality = models.CharField(max_length=20, choices=[('low', 'Faible'), ('medium', 'Moyen'), ('high', 'Critique')])
    reservation_date = models.DateField()
    reservation_duration = models.PositiveIntegerField(help_text="Durée en jours")
    reasons = models.TextField()
    assigned_vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    is_assigned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client_name} - {self.reservation_date}"
