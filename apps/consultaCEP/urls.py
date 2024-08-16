from django.urls import path
from . import views

"""defina as urls utilizadas para sua aplicação"""
urlpatterns = [
    path('', views.buscar_cep, name='buscar_cep'),
]
