from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login,name='login'),
    path('registrar', views.registrar),
    path('inicio', views.inicio),
    path('registro', views.registro),
    path('logout', views.logout),
]