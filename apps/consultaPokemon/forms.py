from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome']
        labels = {
            'nome': 'Nome do Pokémon',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do Pokémon'}),
        }
