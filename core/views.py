from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from .models import *
from .forms import *

@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            return render(request, 'index.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

    except User.DoesNotExist:
        nome_usuario = request.POST['username']
        email = request.POST['email']
        senha = request.POST['password']

        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()

@require_POST
def entrar(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username, password=request.POST["password"])
    if usuario is not None:
        auth_login(request, usuario)
        return redirect('perfil')

    return redirect('home')

@login_required
def sair(request):
    logout(request)
    return redirect('home')

def cadastrarEspaco(request):
    form = EspacosForm(request.POST or None)
    
    contexto = {
        'todas_atividade' : atividade
    }
    return render(request,'atividade.html', contexto)

def Atividade_listar(request, redirect):
    atividade = Atividade.objects.all()
    
    contexto = {
        'todos_modalidade' : atividade
    }
    return redirect(contexto, 'atividade.html', request)


def Atividade_cadastro(request, redirect):
    form = AtividadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Atividade_listar')

    contexto = {
       'form_atividade': form
    }
    return render(request,'gerenciar_atv.html', contexto)

def Atividade_editar(request, id, redirect):
    meus_atividades = Atividade.objects.get(pk=id)
    
    form = AtividadeForm(request.POST or None, instance = meus_atividades)
    
    if form.is_valid():
         form.save()
         return redirect('Atividade_listar')
   
    contexto = {
        'form_atividade': form
    }
    return render(request, 'gerenciar_atv.html', contexto )      

def Atividade_remover(id, redirect):
    meus_atividades = Atividade.objects.get(pk=id)
    meus_atividades.delete()
    return redirect('Atividade_listar')


def Espaco_listar(request, redirect):
    espaco = Espaco.objects.all()
    
    contexto = {
        'todos_espaco' : espaco
    }
    return redirect(contexto, 'espaco.html', request)

def Espaco_cadastro(request, redirect):
    form = EspacosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Espaco_listar')

    contexto = {
       'form_espaco': form
    }
    return render(request,'gerenciar_espacos.html', contexto)


def Espaco_editar(request, id, redirect):
    meus_espaco = Espaco.objects.get(pk=id)
    
    form = EspacosForm(request.POST or None, instance = meus_espaco)
    
    if form.is_valid():
         form.save()
         return redirect('Espaco_listar')
   
    contexto = {
        'form_espaco': form
    }
    return render(request, 'gerenciar_espacos.html', contexto )  

def Espaco_remover(id, redirect):
    meus_espaco = Espaco.objects.get(pk=id)
    meus_espaco.delete()
    return redirect ('Espaco_listar')  


def Modalidade_listar(request, redirect):
    modalidade = Modalidades.objects.all()
    
    contexto = {
        'todos_modalidade' : modalidade
    }
    return redirect(contexto, 'modalidade.html', request)

def Modalidade_cadastro(request, redirect):
    form = ModalidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Modalidade_listar')

    contexto = {
       'form_modalidade': form
    }
    return render(request,'gerenciar_modalidades.html', contexto)

def Modalidade_editar(request, id, redirect):
    meus_modalidade = Modalidades.objects.get(pk=id)
    
    form = ModalidadeForm(request.POST or None, instance = meus_modalidade)
    
    if form.is_valid():
         form.save()
         return redirect('Modalidade_listar')
   
    contexto = {
        'form_modalidade': form
    }
    return render(request, 'gerenciar_modalidades.html', contexto )  

def Modalidade_remover(id, redirect):
    meus_modalidade = Modalidades.objects.get(pk=id)
    meus_modalidade.delete()
    return redirect ('Modalidade_listar')  

def Nivel_listar(request, redirect):
    nivel = Nivel.objects.all()
    
    contexto = {
        'todos_nivel' : nivel
    }
    return redirect(contexto, 'niveis.html', request)

def Nivel_cadastro(request, redirect):
    form = NivelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Nivel_listar')

    contexto = {
       'form_nivel': form
    }
    return render(request,'gerenciar_niveis.html', contexto)


def Nivel_editar(request, id, redirect):
    meus_nivel = Nivel.objects.get(pk=id)
    
    form = NivelForm(request.POST or None, instance = meus_nivel)
    
    if form.is_valid():
         form.save()
         return redirect('Nivel_listar')
   
    contexto = {
        'form_nivel': form
    }
    return render(request, 'gerenciar_niveis.html', contexto )  

def Nivel_remover(id, redirect):
    meus_nivel = Nivel.objects.get(pk=id)
    meus_nivel.delete()
    return redirect ('Nivel_listar')

    








def home (request):
    return render(request, 'index.html')

def cadastro (request):
    return render(request, 'cadastro.html')

def login (request):
    return render(request, 'login.html')

def atividade (request):
    return render(request, 'atividade.html')

def form (request):
    return render(request, 'form.html')
    
def espacos (request):
    return render(request, 'gerenciar_espacos.html')
    
def perfil (request):
    return render(request, 'perfil.html')

# Create your views here.
