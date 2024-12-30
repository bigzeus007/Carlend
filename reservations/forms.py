from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['client_name', 'client_license_plate', 'client_vehicle_date', 
                  'commercial_advisor', 'service_advisor', 'criticality', 
                  'reservation_date', 'reservation_duration', 'reasons']
