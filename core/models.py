from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class Usuario(models.Model):
    nome_usuario = models.CharField("Usuario", max_length=20)
    email = models.EmailField("email")
    senha =models.CharField("Senha", max_length=30)
 

class Modalidade(models.Model):
    nome = models.CharField('Nome', max_length=100, default='a')

    def __str__(self):
        return self.nome

class Espaco(models.Model):
    nomeEspaco = models.CharField('nomeEspaco', max_length=100, default='a')

    def __str__(self):
        return self.nomeEspaco

class Nivel(models.Model):
    nome = models.CharField('Nome', max_length=100, default='a')

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField('Nome', max_length=100, default='a')

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField('Nome', max_length=100, default='a')
    turma = models.IntegerField('Ano', default='a')

    def __str__(self):
        return self.nome



