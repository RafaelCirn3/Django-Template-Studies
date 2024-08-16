from django.core.exceptions import ValidationError
from django.db import models
import requests

class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    altura = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)

    def clean(self):
        # Verifica se o nome do Pokémon existe na PokeAPI
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.nome.lower()}/')

        if response.status_code != 200:
            raise ValidationError(f'O Pokémon "{self.nome}" não foi encontrado. Verifique a ortografia ou tente outro nome.')

    def __str__(self):
        return self.nome
