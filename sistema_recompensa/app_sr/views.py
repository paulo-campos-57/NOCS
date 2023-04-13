from django.shortcuts import render
from .models import moedas

def home(request):
    pontos = moedas()
    return render(request, 'sr/home.html')#, pontos)
""""
    pontos.qtd = 800
    
    pontos.save()
    
    pontos = {
        'pontos':moedas.objects.all()
    }
"""

def descr(request):
    return render(request, 'sr/descr.html')
