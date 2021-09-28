from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioRegister

urlpatterns = [
  #  path('admin/', admin.site.urls, nome=''),
    path('login/', auth_views.LoginView.as_view(
        template_name='autenticacao/login.html'
         ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioRegister.as_view(), name='registrar'),
]
