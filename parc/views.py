from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from reservations.models import Reservation
from vehicles.models import Vehicle
from datetime import datetime


def parc_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'parc/parc_list.html', {'vehicles': vehicles})

def parc_info(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    # Vérifier que le véhicule est "Indisponible" ou "Réservé"
    if vehicle.availability not in ['indisponible', 'réservé']:
        return HttpResponse("Vous ne pouvez consulter les informations que pour les véhicules indisponibles ou réservés.")

    reservation = Reservation.objects.filter(
        assigned_vehicle=vehicle,
        is_assigned=True
        ).first()
    context = {
        'vehicle': vehicle,
        'reservation': reservation,
        }
    return render(request, 'parc/parc_info.html', context)

def parc_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    reservation = Reservation.objects.filter(assigned_vehicle=vehicle, is_assigned=True).first()
    available_vehicles = Vehicle.objects.filter(availability="disponible")

    if not reservation:
        return HttpResponse("Aucune réservation associée ou vous n'êtes pas le responsable de cette réservation.")

    if request.method == 'POST':
        action = request.POST.get('action')  # Bouton cliqué
        if action == "update":
            # Enregistrer les modifications
            reservation.client_name = request.POST.get('client_name')
            reservation.criticality = request.POST.get('criticality')
            reservation.reasons = request.POST.get('reasons')
            new_vehicle_id = request.POST.get('assigned_vehicle')

            if new_vehicle_id and str(vehicle.pk) != new_vehicle_id:
                # Libérer l'ancien véhicule
                vehicle.availability = "disponible"
                vehicle.save()

                # Assigner un nouveau véhicule
                new_vehicle = get_object_or_404(Vehicle, pk=new_vehicle_id)
                reservation.assigned_vehicle = new_vehicle
                new_vehicle.availability = "réservé"
                new_vehicle.save()

            # Récupérer et valider la date de retour
            return_date = request.POST.get('return_date')
            if return_date:  # Vérifiez que la date est fournie
                try:
                    reservation.end_date = datetime.strptime(return_date, '%Y-%m-%d').date()
                except ValueError:
                    messages.error(request, "Le format de la date est invalide.")
                    return redirect('parc_update', pk=pk)
            # Gestion conditionnelle des fichiers
            if request.FILES.get('driving_license_front'):
                reservation.driving_license_front = request.FILES.get('driving_license_front')
            if request.FILES.get('driving_license_back'):
                reservation.driving_license_back = request.FILES.get('driving_license_back')
            if request.FILES.get('id_card_front'):
                reservation.id_card_front = request.FILES.get('id_card_front')
            if request.FILES.get('id_card_back'):
                reservation.id_card_back = request.FILES.get('id_card_back')
            reservation.save()
            messages.success(request, "Réservation mise à jour avec succès.")
            return redirect('parc_list')

        elif action == "confirm_delivery":
            # Confirmer la livraison
            # Confirmer la livraison avec gestion conditionnelle des fichiers
            if request.FILES.get('driving_license_front'):
                reservation.driving_license_front = request.FILES.get('driving_license_front')
            if request.FILES.get('driving_license_back'):
                reservation.driving_license_back = request.FILES.get('driving_license_back')
            if request.FILES.get('id_card_front'):
                reservation.id_card_front = request.FILES.get('id_card_front')
            if request.FILES.get('id_card_back'):
                reservation.id_card_back = request.FILES.get('id_card_back')
            vehicle.availability = "indisponible"
            reservation.start_date = datetime.now()
            reservation.save()
            vehicle.save()
            messages.success(request, "Livraison confirmée.")
            return redirect('parc_list')

        elif action == "confirm_return":
            # Confirmer le retour
            # Confirmer le retour avec gestion conditionnelle des fichiers
            if request.FILES.get('driving_license_front'):
                reservation.driving_license_front = request.FILES.get('driving_license_front')
            if request.FILES.get('driving_license_back'):
                reservation.driving_license_back = request.FILES.get('driving_license_back')
            if request.FILES.get('id_card_front'):
                reservation.id_card_front = request.FILES.get('id_card_front')
            if request.FILES.get('id_card_back'):
                reservation.id_card_back = request.FILES.get('id_card_back')
            vehicle.availability = "disponible"
            reservation.end_date = datetime.now()
            reservation.is_assigned = False
            reservation.is_active = False
            reservation.save()
            vehicle.save()
            messages.success(request, "Retour confirmé.")
            return redirect('parc_list')

        elif action == "cancel_reservation":
            # Annuler la réservation
            cancellation_reason = request.POST.get('cancellation_reason')
            vehicle.availability = "disponible"
            vehicle.save()
            reservation.deleted = True
            reservation.reasons = f"Annulé : {cancellation_reason}"
            reservation.save()
            messages.success(request, "Réservation annulée.")
            return redirect('parc_list')

    context = {
        'vehicle': vehicle,
        'reservation': reservation,
        'available_vehicles': available_vehicles,
    }
    return render(request, 'parc/parc_update.html', context)




def update_vehicle_status(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    reservation = Reservation.objects.filter(assigned_vehicle=vehicle, is_assigned=True).first()

    if request.method == 'POST':
        # Récupération des données du formulaire
        client_name = request.POST.get('client_name')
        criticality = request.POST.get('criticality')
        new_vehicle_id = request.POST.get('new_vehicle')
        reasons = request.POST.get('reasons')
        status = request.POST.get('status')
        delivery_date = request.POST.get('delivery_date')

        if client_name:
            reservation.client_name = client_name
        if criticality:
            reservation.criticality = criticality
        if new_vehicle_id and new_vehicle_id != str(vehicle.id):
            new_vehicle = get_object_or_404(Vehicle, pk=new_vehicle_id)
            reservation.assigned_vehicle = new_vehicle
            new_vehicle.availability = 'Réservé'
            new_vehicle.save()
            vehicle.availability = 'disponible'
        if reasons:
            reservation.reasons = reasons
        if status == 'livré':
            delivery_date = request.POST.get('delivery_date')
            if delivery_date:
                try:
                    reservation.start_date = datetime.strptime(delivery_date, '%Y-%m-%d').date()
                    vehicle.availability = 'indisponible'
                except ValueError:
                    messages.error(request, "Le format de la date de livraison est invalide.")
                    return redirect('update_vehicle_status', pk=pk)

        elif status == 'annulé':
            reservation.deleted = True
            vehicle.availability = 'disponible'

        reservation.save()
        vehicle.save()
        return redirect('parc_list')

    available_vehicles = Vehicle.objects.filter(availability='disponible')

    context = {
        'vehicle': vehicle,
        'reservation': reservation,
        'available_vehicles': available_vehicles,
    }
    return render(request, 'parc/update_vehicle.html', context)

