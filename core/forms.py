from django.forms import ModelForm
from .models import Espaco, Atividade, Nivel, Status, Modalidades

class EspacosForm(ModelForm):
    class Meta:
        model = Espaco
        fields = ['nome_espaco']

class AtividadeForm(ModelForm):
    class Meta:
        model =  Atividade
        fields = ['data_hora_inicio', 'data_hora_fim', 'responsavel', 'quantidade', 'turma' ]

class NivelForm(ModelForm):
    class Meta:
        model = Nivel
        fields = ['Nivel']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['Status']

class ModalidadeForm(ModelForm):
    class Meta:
        model = Modalidades
        fields = ['Nome_Modalidade']