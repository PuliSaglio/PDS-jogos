from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=10)
    idade = models.IntegerField('Idade')
    email = models.EmailField('Email')
    matricula = models.CharField('Matricula', max_length=14, unique=True)

    USERNAME_FILED = 'matricula' 

class Modalidade(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Espaco(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Nivel(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField('Nome', max_length=100)
    turma = models.IntegerField('Ano')

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    data_inicio = models.DateTimeField('Data e hora de Início ')
    data_fim = models.DateTimeField('Data e hora do Fim')
    quantidade_limite = models.IntegerField('Quantidade e Limite')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
