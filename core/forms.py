from django.forms import ModelForm
from .models import Espaco

class EspacosForm(ModelForm):
    class Meta:
        model = Espaco
        fields = ['nome_espaco']