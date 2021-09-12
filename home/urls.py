from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    # CRUD
    # acceso por defecto
    path('', views.home, name='home'),
    path('create', views.create,name='create'),
    path('update', views.update, name='update'),
    path('edit/<int:id>/employee', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/employee', views.delete_employee, name='delete_employee'),
    path('edit/<int:id>/tools', views.edit_tools, name='edit_tools'),
    path('delete/<int:id>/tools', views.delete_tools, name='delete_tools'),
    #path('getServicio', views.getMove, name='getmove'),
    path('read', views.read,name='read'),
    path('delete', views.delete,name='delete'),
    path('employees',views.employees,name='employees'),
    path('tools',views.tools,name='tools'),
    path('moves',views.moves,name='moves'),
    path('movetype',views.movetype,name='movetype'),
    path('inform',views.inform,name='inform'),
    
]