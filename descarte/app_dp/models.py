from django.db import models

class Mensagens(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=355)
    endereco = models.TextField(default='-')
    texto = models.TextField(max_length=1000)
