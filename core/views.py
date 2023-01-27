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
    
    if form.is_valid():
        form.save()
        return redirect('home')

    contexto = {
    'form_espaco' : form
    }

    return render(request, 'gerenciar_espacos.html', contexto)

def listarAtividades(request):
    atividade = Atividade.objects.all()
    contexto ={
        'lista_atividades': atividade
    }
    return render(request, 'index.html', contexto)


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
