from django.urls import path
from app_hist5 import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # Acesso à informação sobre descarte de lixo
    path('',views.home,name='home'),
    path('usuarios/',views.info,name='info'),
    path('usuarios/info',views.enviado,name='enviado')
]
