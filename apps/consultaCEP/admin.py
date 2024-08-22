# meu_app/admin.py
from django.contrib import admin
from .models import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'bairro', 'localidade', 'uf')
    search_fields = ('cep', 'logradouro', 'bairro', 'localidade', 'uf')
    list_filter = ('uf', 'localidade')
    ordering = ('cep',)
