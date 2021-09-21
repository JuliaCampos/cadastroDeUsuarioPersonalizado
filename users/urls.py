from django.urls import path

from .views import UsuarioCreate
from .views import UsuarioUpdate
from .views import UsuarioDelete
from .views import UsuarioList

#urls referentes as operações de usuario
urlpatterns = [
    path('cadastrar/usuario/', UsuarioCreate.as_view(), name='cadastrar-usuario'),
    path('editar/usuario/<int:pk>/', UsuarioUpdate.as_view(), name='editar-usuario'),
    path('excluir/usuario/<int:pk>/', UsuarioDelete.as_view(), name='excluir-usuario'),
    path('listar/usuario/', UsuarioList.as_view(), name='listar-usuario'),
]