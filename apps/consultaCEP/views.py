import requests
from django.shortcuts import render
from .forms import EnderecoForm
from .models import Endereco


"""crie uma view para consultar os dados da sua api"""
def buscar_cep(request):
    form = EnderecoForm(request.GET or None) 
    endereco = None

    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/') #defina a api a ser utilizada
        
        if response.status_code == 200: #valide os dados de acordo com os que serão consultados
            dados_endereco = response.json()
            endereco = Endereco.objects.create(
                cep=cep,
                logradouro=dados_endereco.get('logradouro'),
                bairro=dados_endereco.get('bairro'),
                localidade=dados_endereco.get('localidade'),
                uf=dados_endereco.get('uf')
            )

    return render(request, 'consultaCEP.html', {'form': form, 'endereco': endereco}) #retorne a consulta utilizando seu modelo e form já criado