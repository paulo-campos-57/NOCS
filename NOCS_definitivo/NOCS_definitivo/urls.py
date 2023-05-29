from django.contrib import admin
from django.urls import path
from NOCS_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nocs/home_coletor', views.home_coletor, name='home_coletor'),
    path('nocs/cadastro', views.cadastro, name='cadastro'),
    path('nocs/cadastro_coletor', views.cadastro_coletor, name='cadastro_coletor'),
    path('nocs/rotas', views.rotas, name='rotas'),
    path('nocs/nova_rota', views.nova_rota, name='nova_rota'),
    path('nocs/rota_confirmada', views.rota_confirmada, name='rota_confirmada'),
    path('nocs/sobre', views.sobre, name='sobre'),
    path('nocs/nao_cadastrado', views.nao_cadastrado, name='nao_cadastrado'),
    path('nocs/nao_cadastrado_coletor', views.nao_cadastrado_coletor, name='nao_cadastrado_coletor'),
    path('nocs/informar_coleta', views.informar_coleta, name='informar_coleta'),
    path('nocs/informar_coleta/horario_marcado', views.horario_marcado, name='horario_marcado'),
    path('nocs/avaliacao', views.avaliacao, name='avaliacao'),
    path('nocs/avaliacao_confirmada', views.avaliacao_confirmada, name='avaliacao_confirmada'),
    path('nocs/logged', views.logged, name='logged'),
    path('nocs/cadastro/confirmado', views.confirmado, name='confirmado'),
    path('nocs/confirmado_coletor', views.confirmado_coletor, name='confirmado_coletor'),
    path('nocs/indice', views.indice, name='indice'),
    path('nocs/indice_coletor', views.indice_coletor, name='indice_coletor'),
    path('nocs/descarte_p', views.descarte_perigoso, name='descarte_perigoso'),
    path('nocs/descarte_p/mensagem', views.mensagem, name='mensagem'),
    path('nocs/descarte_p/mensagem/coletor', views.coletor, name='coletor'),
    path('nocs/loja', views.loja, name='loja'),
    path('nocs/loja/descr', views.descr, name='descr'),
    path('nocs/info', views.info, name='info'),
    path('nocs/info/info_descarte', views.info_descarte, name='info_descarte'),
    path('nocs/info/info_descarte/enviado', views.enviado, name='enviado')
]
