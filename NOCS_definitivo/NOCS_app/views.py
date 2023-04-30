from django.shortcuts import render, redirect
from .models import Mensagem
from .models import Pergunta
from .models import Cadastro
# from .models import perfil

def home(request):
    novo_usuario = Cadastro()
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # print(email)
        # print(senha)$$$$$
        # print(Cadastro.objects.get(email))
        try:
            if (email == Cadastro.objects.get(email = email).email):
                if (senha == Cadastro.objects.get(email = email).password1):
                    # perfil = Cadastro.objects.get(email = email)
                    # print(perfil.email)
                    return render(request, 'nocs/logged.html')
        except:
            return render(request, 'nocs/nao_cadastrado.html')
    return render(request, 'nocs/home.html')

def logged(request):
    # context = {
        # 'perfil': perfil,
    # }
    return render(request, 'nocs/logged.html')# , context)

def nao_cadastrado(request):
    return render(request, 'nocs/nao_cadastrado.html')

def indice(request):
    return render(request, 'nocs/indice.html')

def descarte_perigoso(request):
    return render(request, 'nocs/descarte_perigoso.html')

def mensagem(request):
    nova_mensagem = Mensagem()

    nova_mensagem.nome = request.POST.get('nome')
    nova_mensagem.email = request.POST.get('email')
    nova_mensagem.endereco = request.POST.get('endereco')
    nova_mensagem.texto = request.POST.get('texto')
    nova_mensagem.save()

    return render(request,'nocs/mensagem.html')

def coletor(request):
    mensagens = {
        'mensagens': Mensagem.objects.all()
    }
    return render(request,'nocs/coletor.html', mensagens)

def loja(request):
    return render(request, 'nocs/loja.html')

def descr(request):
    return render(request, 'nocs/descr.html')

def info(request):
    return render(request, 'nocs/info.html')

def info_descarte(request):
    return render(request, 'nocs/info_descarte.html')

def enviado(request):
    nova_pergunta = Pergunta()

    nova_pergunta.email = request.POST.get('email')
    nova_pergunta.texto = request.POST.get('mensagem')
    nova_pergunta.save()

    return render(request, 'nocs/enviado.html')

def cadastro(request):
    return render(request, 'nocs/cadastro.html')

def confirmado(request):
    novo_cadastro = Cadastro()

    novo_cadastro.username = request.POST.get('username')
    novo_cadastro.email = request.POST.get('email')
    novo_cadastro.password1 = request.POST.get('password1')
    novo_cadastro.bairro = request.POST.get('bairro')
    novo_cadastro.rua = request.POST.get('rua')
    novo_cadastro.numero = request.POST.get('numero')
    novo_cadastro.complemento = request.POST.get('complemento')
    novo_cadastro.save()

    return render(request, 'nocs/confirmado.html')

def sobre(request):
    return render(request, 'nocs/sobre.html')
