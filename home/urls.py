from django.urls import path, include
from . import views

urlpatterns = [
    # CRUD
    # acceso por defecto
    path('', views.home),
    path('create', views.create),
    path('update', views.update, name='update'),
    #path('getServicio', views.getMove, name='getmove'),
    path('read', views.read),
    path('delete', views.delete),
    
]