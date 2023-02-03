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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        novoUsuario = User.objects.create_user(username=username, email=email, password=password)
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
    form = EspacoForm(request.POST or None)
    
    contexto = {
        'todas_atividade' : atividade
    }
    return render(request,'atividade.html', contexto)

def Atividade_listar(request):
    atividade = Atividade.objects.all()
    
    contexto = {
        'todos_modalidade' : atividade
    }
    return render(request, contexto, 'atividade.html')


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


def Espaco_listar(request):
    espaco = Espaco.objects.all()
    
    contexto = {
        'todos_espaco' : espaco
    }
    return render(request, 'espaco.html', contexto)

def Espaco_cadastro(request):
    form = EspacoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('espaco_listar')

    contexto = {
       'form_espaco': form
    }
    return render(request,'gerenciar_espacos.html',contexto)


def Espaco_editar(request, id):
    meus_espaco = Espaco.objects.get(pk=id)
    
    form = EspacoForm(request.POST or None, instance = meus_espaco)
    
    if form.is_valid():
        form.save()
        return redirect('espaco_listar')
   
    contexto = {
        'form_espaco': form
    }
    return render(request, 'gerenciar_espacos.html', contexto )  

def Espaco_remover(request, id):
    meus_espaco = Espaco.objects.get(pk=id)
    meus_espaco.delete()
    return redirect ('espaco_listar')  


def Modalidade_listar(request):
    modalidade = Modalidade.objects.all()
    
    contexto = {
        'todos_modalidade' : modalidade
    }
    return render(request,'modalidade.html', contexto)

def Modalidade_cadastro(request):
    form = ModalidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('modalidade_listar')

    contexto = {
       'form_modalidade': form
    }
    return render(request,'gerenciar_modalidades.html', contexto)

def Modalidade_editar(request, id):
    meus_modalidade = Modalidade.objects.get(pk=id)
    
    form = ModalidadeForm(request.POST or None, instance = meus_modalidade)
    
    if form.is_valid():
         form.save()
         return redirect('modalidade_listar')
   
    contexto = {
        'form_modalidade': form
    }
    return render(request, 'gerenciar_modalidades.html', contexto )  

def Modalidade_remover(request, id):
    meus_modalidade = Modalidade.objects.get(pk=id)
    meus_modalidade.delete()
    return redirect ('modalidade_listar')  

def Nivel_listar(request):
    nivel = Nivel.objects.all()
    
    contexto = {
        'todos_nivel' : nivel
    }
    return render(contexto, 'niveis.html', request)

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

@login_required    
def perfil (request):
    return render(request, 'perfil.html',)

# Create your views here.
