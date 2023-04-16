from django.db import models

class Pergunta(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField(max_length=355)
    texto = models.TextField(max_length=3000)
