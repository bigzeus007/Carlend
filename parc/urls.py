from django.urls import path
from . import views

urlpatterns = [
    path('', views.parc_list, name='parc_list'),
    path('<int:pk>/info/', views.parc_info, name='parc_info'),
    path('<int:pk>/update-status/', views.parc_update, name='parc_update')
]
