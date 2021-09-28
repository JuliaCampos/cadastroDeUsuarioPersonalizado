#tela para criar usuarios
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import UsuarioAutenticacao
from .forms import UsuarioForm
# Create your views here.
######################################
# Criacao de Usuario                 #
####################################
class UsuarioRegister(CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm

    success_url = reverse_lazy('inicio')
