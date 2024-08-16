from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_pokemon, name='buscar_pokemon'),
]
