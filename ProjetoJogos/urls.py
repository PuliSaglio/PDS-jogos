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
from core.views import home, atividade, cadastro, login, sair, form, cadastrarEspaco, cadastrar_usuario, entrar, perfil, Modalidade_listar, Modalidade_editar, Modalidade_remover, Modalidade_cadastro, Nivel_cadastro, Nivel_editar, Nivel_listar, Nivel_remover, Atividade_cadastro, Atividade_editar, Atividade_remover,Atividade_listar, Espaco_cadastro, Espaco_editar, Espaco_listar, Espaco_remover

urlpatterns = [
    path('' , home, name="home"),
    path('perfil/', perfil, name="perfil"),
    path('cadastro/', cadastro, name="cadastro"),
    path('login/', login, name="login"),
    path('sair/', sair, name="sair"),
    path('atividade/', atividade, name="atividade"),
    path('form/', form, name="form"),
    path('gerenciar_espacos/', cadastrarEspaco, name="espacos"),
    path('admin/', admin.site.urls),
    path('cadastrar/', cadastrar_usuario),
    path('entrar/', entrar),
    path('atividade_listar/', Atividade_listar, name='atividade_listar'),
    path('atividade_editar/<int:id>/', Atividade_editar, name='atividade_editar'),
    path('atividade_cadastro/', Atividade_cadastro, name='atividade_cadastro'),
    path('atividade_remover/<int:id>/', Atividade_remover, name='atividade_remover'),
    path('modalidade_listar/', Modalidade_listar, name='modalidade_listar'),
    path('modalidade_editar/<int:id>/', Modalidade_editar, name='modalidade_editar'),
    path('modalidade_cadastro/', Modalidade_cadastro, name='modalidade_cadastro'),
    path('modalidade_remover<int:id>/', Modalidade_remover, name='modalidade_remover'),
    path('espaco_listar/', Espaco_listar, name='espaco_listar'),
    path('espaco_editar/<int:id>/', Espaco_editar, name='espaco_editar'),
    path('espaco_cadastro/', Espaco_cadastro, name='espaco_cadastro'),
    path('espaco_remover/<int:id>/', Espaco_remover, name='espaco_remover'),
    path('nivel_listar', Nivel_listar, name='nivel_listar'),
    path('nivel_editar/<int:id>/', Nivel_editar, name='nivel_editar'),
    path('nivel_cadstro', Nivel_cadastro, name='nivel_cadstro'),
    path('nivel_remover/<int:id>/', Nivel_remover, name='nivel_remover'),





]
