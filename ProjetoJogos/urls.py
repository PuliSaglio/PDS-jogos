"""ProjetoJogos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, atividade, cadastro, login, form, cadastrarEspaco, cadastrar_usuario, entrar, perfil

urlpatterns = [
    path('' , home, name="home"),
    path('perfil/', perfil, name="perfil"),
    path('cadastro/', cadastro, name="cadastro"),
    path('login/', login, name="login"),
    path('atividade/', atividade, name="atividade"),
    path('form/', form, name="form"),
    path('gerenciar_espacos/', cadastrarEspaco, name="espacos"),
    path('admin/', admin.site.urls),
    path('cadastrar/', cadastrar_usuario),
    path('entrar/', entrar),
]
