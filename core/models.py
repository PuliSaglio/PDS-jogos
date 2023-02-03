from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class Usuario(models.Model):
    nome_usuario = models.CharField("Usuario", max_length=20)
    email = models.EmailField("email")
    senha =models.CharField("Senha", max_length=30)
 

class Modalidade(models.Model):
    nome = models.CharField('Nome', max_length=100, default='')

    def __str__(self):
        return self.nome

class Espaco(models.Model):
    nome = models.CharField('Nome', max_length=100, default='')

    def __str__(self):
        return self.nome

class Nivel(models.Model):
    nome = models.CharField('Nome', max_length=100, default='')

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField('Nome', max_length=100, default='')

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField('Nome', max_length=100, default='')
    turma = models.IntegerField('Ano', default='')

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    data_inicio = models.DateTimeField('Data e hora de Início', default=now)
    data_fim = models.DateTimeField('Data e hora do Fim', default=now)
    quantidade_limite = models.IntegerField('Quantidade e Limite', default='')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, default='')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default='')
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE, default='espaco')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='')
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, default='')
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, default='')
