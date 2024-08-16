from django import forms
from .models import Endereco

"""formularize os dados a ser utilizados pela sua consulta"""
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep']
        labels = {
            'cep': 'CEP',
        }
        widgets = {
            'cep': forms.TextInput(attrs={'placeholder': 'Digite o CEP', 'maxlength': '8'}), #personalização
        }
