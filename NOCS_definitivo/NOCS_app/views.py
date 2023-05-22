from django.shortcuts import render, redirect
from .models import Mensagem
from .models import Pergunta
from .models import Cadastro
from .models import Coletor
from .models import Horario
from .models import Rotas

def home(request):
    novo_usuario = Cadastro()
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            if (email == Cadastro.objects.get(email = email).email):
                if (senha == Cadastro.objects.get(email = email).password1):
                    return render(request, 'nocs/logged.html')
        except:
            return render(request, 'nocs/nao_cadastrado.html')
    return render(request, 'nocs/home.html')

def home_coletor(request):
    usuario = Coletor()
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if (email == Coletor.objects.get(email = email).email):
                if (password == Coletor.objects.get(email = email).password):
                    return render(request, 'nocs/confirmado_coletor.html')
        except:
            return render(request, 'nocs/nao_cadastrado_coletor.html')
    return render(request, 'nocs/home_coletor.html')

def logged(request):
    return render(request, 'nocs/logged.html')

def nao_cadastrado(request):
    return render(request, 'nocs/nao_cadastrado.html')

def nao_cadastrado_coletor(request):
    return render(request, 'nocs/nao_cadastrado_coletor.html')

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

def cadastro_coletor(request):
    return render(request, 'nocs/cadastro_coletor.html')

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

def confirmado_coletor(request):
    novo_coletor = Coletor()

    novo_coletor.cpf = request.POST.get('cpf')
    novo_coletor.username = request.POST.get('username')
    novo_coletor.email = request.POST.get('email')
    novo_coletor.password = request.POST.get('password')

    novo_coletor.save()
    return render(request, 'nocs/confirmado_coletor.html')

def indice_coletor(request):
    return render(request, 'nocs/indice_coletor.html')

def informar_coleta(request):
    novo_horario = Horario()
    if request.method == 'POST':
        novo_horario.bairro_hora = request.POST.get('bairro')
        novo_horario.day = request.POST.get('dia')
        novo_horario.mes = request.POST.get('mes')
        novo_horario.horario = request.POST.get('horario')

        novo_horario.save()
        return render(request, 'nocs/horario_marcado.html')
    return render(request, 'nocs/informar_coleta.html')

def horario_marcado(request):
    return render(request, 'nocs/horario_marcado.html')

def rotas(request):
    rotas = {
        'rotas': Rotas.objects.all()
    }
    return render(request, 'nocs/rotas.html', rotas)

def nova_rota(request):
    nova_rota = Rotas()
    if request.method == 'POST':
        nova_rota.nome_coletor = request.POST.get('name')
        nova_rota.rua_problema = request.POST.get('rua')
        nova_rota.rota_alternativa = request.POST.get('alternativa')

        nova_rota.save()
        return render(request, 'nocs/rota_confirmada.html')
    return render(request, 'nocs/nova_rota.html')

def rota_confirmada(request):
    return render(request, 'nocs/rota_confirmada.html')

def sobre(request):
    return render(request, 'nocs/sobre.html')
