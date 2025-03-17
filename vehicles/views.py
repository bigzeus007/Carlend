from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Vehicle
from .forms import VehicleForm
# Create your views here.

def index(request):
    return HttpResponse("Bienvenue sur la gestion des véhicules de CarLend!")

@staff_member_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

@staff_member_required
def add_vehicle(request):
    if request.method == 'POST':
        print("Données POST reçues :", request.POST)  # Debug
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.fuel_level = int(request.POST.get('fuel_level', 50))  # Conversion en entier
            print("Niveau de carburant enregistré :", vehicle.fuel_level)  # Debug
            vehicle.save()
            return redirect('vehicle_list')  
    else:
        form = VehicleForm()
    return render(request, 'vehicles/add_vehicle.html', {'form': form})


@staff_member_required
def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.fuel_level = int(request.POST.get('fuel_level', vehicle.fuel_level))  # Assure la conversion en entier
            vehicle.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/edit_vehicle.html', {'form': form})

@staff_member_required
def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    vehicle.delete()
    return redirect('vehicle_list')