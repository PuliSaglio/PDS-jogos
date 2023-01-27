from django.shortcuts import render
from .models import *
from .forms import *

def cadastrarEspaco(request):
    form = EspacosForm(request.POST or None)
    
    if form.is_valid():
        form.save()

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

# Create your views here.
