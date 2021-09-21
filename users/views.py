from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Usuario

from django.urls import reverse_lazy

#controle de acesso
from django.contrib.auth.mixins import LoginRequiredMixin

######################################
# Criacao de Usuario                 #
####################################
class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['nome', 'email', 'pais', 'estado', 'municipio', 'cep', 'rua', 'numero', 'complemento', 'cpf', 'pis']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('login')

######################################
# Update de Usuario                 #
####################################

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ['nome', 'email', 'pais', 'estado', 'municipio', 'cep', 'rua', 'numero', 'complemento', 'cpf', 'pis']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-usuario')

######################################
# Delete de Usuario                 #
####################################

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('excluir-usuario')

######################################
# Listar Usuarios                 #
####################################

class UsuarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/listas/usuario.html'
