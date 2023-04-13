from django.contrib import admin
from django.urls import path
from app_sr import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #sr.com
    path('', views.home, name='home'),
    #sr/
    path('sr/', views.descr, name='descr')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
