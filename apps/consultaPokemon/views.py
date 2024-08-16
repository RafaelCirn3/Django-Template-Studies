from django.shortcuts import render
from .forms import PokemonForm
from .models import Pokemon
import requests

"""crie uma view para consultar os dados da sua api"""
def buscar_pokemon(request):
    form = PokemonForm(request.GET or None)
    pokemon = None

    if form.is_valid(): #valide os dados de acordo com os que serão consultados
            nome = form.cleaned_data['nome'].lower()
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome}/')
            
            if response.status_code == 200:
                dados_pokemon = response.json()
                pokemon = Pokemon(
                    nome=nome.capitalize(),
                    altura=dados_pokemon['height'] / 10, # Convertendo para metros
                    peso=dados_pokemon['weight'] / 10,  # Convertendo para quilogramas
                    tipo=', '.join([t['type']['name'] for t in dados_pokemon['types']])
                )
                pokemon.full_clean() # Valida o modelo antes de salvar
                pokemon.save()


    return render(request, 'consultaPokemon.html', {'form': form, 'pokemon': pokemon})  #retorne a consulta utilizando seu modelo e form já criado
