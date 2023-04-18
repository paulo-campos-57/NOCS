from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField(max_length=355)
    senha = models.TextField(max_length=100)

class Mensagem(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=355)
    endereco = models.TextField(default='-')
    texto = models.TextField(max_length=1000)

class Pergunta(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField(max_length=355)
    texto = models.TextField(max_length=3000)
