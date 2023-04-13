from django.contrib import admin
from django.urls import path
from app_dp import views

urlpatterns = [
    #dp.com
    path('', views.home, name='home'),
    #dp.com/enviado
    path('dp/', views.mensagens, name='mensagens'),
    #dp.com/coletor
    path('dp/coletor', views.coletor, name='coletor')
]
