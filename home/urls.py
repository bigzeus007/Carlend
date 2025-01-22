from django.urls import path, include  # Ajout de `include` pour inclure d'autres applications
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Vue principale du tableau de bord
    path('reservations/', include('reservations.urls')),  # Inclure les URLs de l'application reservations
    path('vehicles/', include('vehicles.urls')),  # Inclure les URLs de l'application vehicles
    path('parc/', include('parc.urls')),  # Inclure les URLs de l'application parc (si besoin)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
