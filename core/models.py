from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField("Usuario", max_length=20)
    email = models.EmailField("email")
    senha =models.CharField("Senha", max_length=30)

class Modalidades(models.Model):
    nome_modalidade = models.CharField("NomeModalidade", max_length=100, default="Modalidade")

class Espaco(models.Model):
    nome_espaco = models.CharField("NomeEspaco", max_length=100, default="Ginasio")

class Nivel(models.Model):
    nivel = models.CharField("Nivel", max_length=100, default="Nivel")

class Status(models.Model):
    status = models.CharField("Status", max_length=100, default="status")

class Atividade(models.Model):
    data_hora_inicio = models.DateField('data_hora_inicio', auto_now=True)
    data_hora_fim = models.DateField('data_hora_fim', auto_now=True)
    responsavel = models.CharField('responsavel', max_length=100)
    quantidade = models.IntegerField('quantidade')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    modalidade = models.ForeignKey(Modalidades, on_delete=models.CASCADE)
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    turma=models.CharField('turma', max_length=100) 
# Create your models here.
