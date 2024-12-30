from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm
# Create your views here.

def index(request):
    return HttpResponse("Bienvenue sur la gestion des véhicules de CarLend!")

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  # Redirige vers la liste des véhicules
    else:
        form = VehicleForm()
    return render(request, 'vehicles/add_vehicle.html', {'form': form})

def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/edit_vehicle.html', {'form': form})

def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    vehicle.delete()
    return redirect('vehicle_list')