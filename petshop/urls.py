from django.contrib import admin
from django.urls import path
from base.views import inicio, contato

urlpatterns = [
    path('', inicio),
    path('contato/', contato),
    path('admin/', admin.site.urls),
]
