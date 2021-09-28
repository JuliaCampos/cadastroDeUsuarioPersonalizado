from asyncio import exceptions

from django.db import models
from cpf_field.models import CPFField

# Create your models here.
from pycep_correios import get_address_from_cep, WebService, exceptions

from users import forms


class UsuarioAutenticacao(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome:")
    email = models.EmailField(max_length=255, verbose_name="e-mail:", unique=True)
    pais = models.CharField(max_length=255, verbose_name="País:")
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255, verbose_name="Município:")
    cep =  models.CharField(max_length=9, verbose_name="CEP:")
    rua = models.CharField(max_length=255, verbose_name="Rua:")
    numero = models.CharField(max_length=255, verbose_name="Número:")
    complemento = models.CharField(max_length=255, verbose_name="Complemento:", null=True)
    cpf = CPFField('cpf')
    pis = models.CharField(max_length=255, verbose_name="PIS:", unique=True, null=True)

    class Meta:
        # o cpf deve ser unico para cada pessoa, pis ou e-mail
        unique_together = [
            ['nome', 'cpf',],
            ['nome', 'pis',],
            ['nome', 'email',],
        ]

    def __str__(self):
        return self.nome, self.email, self.cpf, self.pis

