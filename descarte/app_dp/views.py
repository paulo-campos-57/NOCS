from django.shortcuts import render
from .models import Mensagens

def home(request):
    return render(request,'dp/home.html')

def mensagens(request):
    nova_mensagem = Mensagens()

    nova_mensagem.nome = request.POST.get('nome')
    nova_mensagem.email = request.POST.get('email')
    nova_mensagem.endereco = request.POST.get('endereco')
    nova_mensagem.texto = request.POST.get('texto')
    nova_mensagem.save()

    return render(request,'dp/mensagem.html')

def coletor(request):
    mensagens = {
        'mensagens': Mensagens.objects.all()
    }
    return render(request,'dp/coletor.html', mensagens)
