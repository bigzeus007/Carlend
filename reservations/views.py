from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm
from vehicles.models import Vehicle
from django.contrib.auth.decorators import login_required

# Liste des réservations
def reservation_list(request):
    reservations = Reservation.objects.filter(is_active=True, is_assigned=False)
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

# Ajouter une réservation
@login_required
def add_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)  # Inclure les fichiers
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Associer l'utilisateur connecté
            reservation.driving_license_front = request.FILES.get('driving_license_front')
            reservation.driving_license_back = request.FILES.get('driving_license_back')
            reservation.id_card_front = request.FILES.get('id_card_front')
            reservation.id_card_back = request.FILES.get('id_card_back')
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/add_reservation.html', {'form': form})

# Modifier une réservation
def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES, instance=reservation)  # Inclure request.FILES
        if form.is_valid():
            # Vérifiez si de nouveaux fichiers ont été soumis
            if 'driving_license_front' in request.FILES:
                reservation.driving_license_front = request.FILES['driving_license_front']
            if 'driving_license_back' in request.FILES:
                reservation.driving_license_back = request.FILES['driving_license_back']
            if 'id_card_front' in request.FILES:
                reservation.id_card_front = request.FILES['id_card_front']
            if 'id_card_back' in request.FILES:
                reservation.id_card_back = request.FILES['id_card_back']

            reservation.save()  # Sauvegarder les modifications
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/edit_reservation.html', {'form': form, 'reservation': reservation})

# Affecter un véhicule
def assign_vehicle(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    available_vehicles = Vehicle.objects.filter(availability='disponible')

    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
        reservation.assigned_vehicle = vehicle
        reservation.is_assigned = True
        reservation.save()

        vehicle.availability = 'réservé'  # Marquer le véhicule comme réservé
        vehicle.save()

        return redirect('reservation_list')

    return render(request, 'reservations/assign_vehicle.html', {
        'reservation': reservation,
        'vehicles': available_vehicles,
    })

def reservation_history(request):
    reservations = Reservation.objects.filter(deleted=False).order_by('-reservation_date')
    return render(request, 'reservations/reservation_history.html', {
        'reservations': reservations,
    })