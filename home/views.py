from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from vehicles.models import Vehicle
from reservations.models import Reservation

@login_required
def home(request):
    available_vehicles_count = Vehicle.objects.filter(availability=True).count()
    pending_reservations_count = Reservation.objects.filter(is_assigned=False).count()

    return render(request, 'home/home.html', {
        'user': request.user,
        'available_vehicles_count': available_vehicles_count,
        'pending_reservations_count': pending_reservations_count,
    })
