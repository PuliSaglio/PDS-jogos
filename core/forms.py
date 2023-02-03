from django.forms import ModelForm
from django import forms
from .models import Usuario, Modalidade, Espaco, Nivel, Status, Turma
from django.contrib.auth.forms import UserCreationForm

class ModalidadeForm(ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome']

class EspacoForm(ModelForm):
    class Meta:
        model = Espaco
        fields = ['nome']

class NivelForm(ModelForm):
    class Meta:
        model = Nivel
        fields = ['nome']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['nome']

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = ['nome']

#class AtividadeForm(ModelForm):
#    class Meta:
#        model = Atividade
#        fields = ['data_inicio', 'data_fim', 'quantidade_limite', 'turma','usuario', 'espaco', 'status', 'nivel','modalidade']
#        widgets = {
#           'turma':forms.RadioSelect(),
#           'espaco':forms.RadioSelect(),
#           'nivel':forms.RadioSelect(),
#           'modalidade':forms.RadioSelect(),
#            'status':forms.RadioSelect(),
#        } 

