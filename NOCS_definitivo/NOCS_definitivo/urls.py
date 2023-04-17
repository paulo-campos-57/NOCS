from django.contrib import admin
from django.urls import path
from NOCS_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nocs/', views.logged, name='logged'),
    path('nocs/indice', views.indice, name='indice'),
    path('nocs/descarte_p', views.descarte_perigoso, name='descarte_perigoso'),
    path('nocs/descarte_p/mensagem', views.mensagem, name='mensagem'),
    path('nocs/descarte_p/mensagem/coletor', views.coletor, name='coletor'),
    path('nocs/loja', views.loja, name='loja'),
    path('nocs/loja/descr', views.descr, name='descr'),
    path('nocs/info', views.info, name='info'),
    path('nocs/info/info_descarte', views.info_descarte, name='info_descarte'),
    path('nocs/info/info_descarte/enviado', views.enviado, name='enviado')
]
