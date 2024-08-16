from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    localidade = models.CharField(max_length=255, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    
    def __str__(self):
        return f'{self.cep} - {self.localidade}, {self.uf}'
