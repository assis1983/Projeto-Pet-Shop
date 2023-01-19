from django.contrib import admin
from django.urls import path, include
from base.views import inicio, contato

urlpatterns = [
    path('', inicio),
    path('contato/', contato),
    path('reserva/', include('reserva.urls', namespace = 'reserva')),
    path('admin/', admin.site.urls),
]
