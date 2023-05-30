from django.db import models

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

class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=255)
    email = models.TextField(max_length=355)
    password1 = models.TextField(max_length=100)
    bairro = models.TextField(default='-')
    rua = models.TextField(default='')
    numero = models.IntegerField(default=0)
    complemento = models.TextField(default='-')

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    endereco = models.TextField(default='-')
    data = models.DateField()
    hora = models.TimeField()

class Coletor(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.IntegerField(default=0)
    username = models.TextField(max_length=255)
    email = models.TextField(max_length=355)
    password = models.TextField(max_length=100)

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    bairro_hora = models.TextField(default='-')
    day = models.IntegerField(default=1, null=False)
    mes = models.IntegerField(default=1)
    horario = models.TextField(max_length=10)

class Rotas(models.Model):
    id = models.AutoField(primary_key=True)
    nome_coletor = models.TextField(max_length=255)
    rua_problema = models.TextField(default='')
    rota_alternativa = models.TextField(default='-')

class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    coment_trabalho = models.TextField(max_length=10000)
    coment_plataforma = models.TextField(max_length=10000)

# perfil = Cadastro()
