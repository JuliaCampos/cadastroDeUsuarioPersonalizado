from cpf_field.models import CPFField
from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UsuarioForm(UserCreationForm):
    nome = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    pais = forms.CharField(max_length=255)
    estado = forms.CharField(max_length=255)
    municipio = forms.CharField(max_length=255)
    cep = forms.CharField(max_length=9)
    rua = forms.CharField(max_length=255)
    numero = forms.CharField(max_length=255)
    complemento = forms.CharField(max_length=255)
    cpf = CPFField('cpf')
    pis = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
