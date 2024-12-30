from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('add/', views.add_reservation, name='add_reservation'),
    path('<int:pk>/edit/', views.edit_reservation, name='edit_reservation'),
    path('<int:pk>/assign/', views.assign_vehicle, name='assign_vehicle'),
]
