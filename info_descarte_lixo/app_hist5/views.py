from django.shortcuts import render
from .models import Pergunta

def home(request):
    return render(request, 'usuarios/home.html')

def info(request):
    return render(request, 'usuarios/info.html')

def enviado(request):
    nova_pergunta = Pergunta()

    nova_pergunta.email = request.POST.get('email')
    nova_pergunta.texto = request.POST.get('mensagem')
    nova_pergunta.save()

    return render(request, 'usuarios/enviado.html')
