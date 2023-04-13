from django.db import models

class moedas(models.Model):
    id = models.AutoField(primary_key=True)
    qtd = models.IntegerField(default=500)
