# meu_app/urls.py
from django.urls import path
from .views import buscar_cep, endereco_list, endereco_detail, endereco_edit, endereco_delete


urlpatterns = [
    path('buscar-cep/', buscar_cep, name='buscar_cep'),
    path('enderecos/', endereco_list, name='endereco_list'),
    path('enderecos/<int:pk>/', endereco_detail, name='endereco_detail'),
    path('enderecos/<int:pk>/editar/', endereco_edit, name='endereco_edit'),
    path('enderecos/<int:pk>/deletar/', endereco_delete, name='endereco_delete'),
]
