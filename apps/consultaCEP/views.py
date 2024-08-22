import requests
from django.shortcuts import render
from .forms import EnderecoForm
from .models import Endereco
from django.shortcuts import get_object_or_404, render, redirect

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

def endereco_list(request):
    enderecos = Endereco.objects.all()
    return render(request, 'endereco_list.html', {'enderecos': enderecos})

def endereco_detail(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)
    return render(request, 'endereco_detail.html', {'endereco': endereco})

def endereco_edit(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)
    
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
            return redirect('endereco_detail', pk=endereco.pk)
    else:
        form = EnderecoForm(instance=endereco)
    
    return render(request, 'endereco_form.html', {'form': form})

def endereco_delete(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)
    
    if request.method == 'POST':
        endereco.delete()
        return redirect('endereco_list')
    
    return render(request, 'endereco_confirm_delete.html', {'endereco': endereco})