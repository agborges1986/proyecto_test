from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    
    # acceso por defecto
    path('', views.home, name='home'),
    path('create', views.create,name='create'),
    path('update', views.update, name='update'),

    #Employees CRUD
    path('edit/<int:id>/employee', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/employee', views.delete_employee, name='delete_employee'),
    path('view/<int:id>/employee', views.view_employee, name='view_employee'),
    path('create/emp', views.create_employee,name='create_employee'),
    path('create/employee_add', views.employee_add,name='employee_add'),

    #Tools CRUD
    path('edit/<int:id>/tools', views.edit_tools, name='edit_tools'),
    path('delete/<int:id>/tools', views.delete_tools, name='delete_tools'),
    path('view/<int:id>/tools', views.view_tools, name='view_tools'),
    path('create/tool', views.create_tools,name='create_tools'),
    path('create/tool_add', views.tool_add,name='tool_add'),

    #Moves CRUD
    path('edit/<int:id>/move', views.edit_moves, name='edit_move'),
    path('delete/<int:id>/move', views.delete_moves, name='delete_move'),
    path('view/<int:id>/move', views.view_moves, name='view_move'),
    path('create/move', views.create_moves,name='create_move'),
    path('create/move_add', views.move_add,name='move_add'),
    
    #path('getServicio', views.getMove, name='getmove'),
    path('read', views.read,name='read'),
    path('delete', views.delete,name='delete'),
    path('employees',views.employees,name='employees'),
    path('tools',views.tools,name='tools'),
    path('moves',views.moves,name='moves'),
    path('movetype',views.movetype,name='movetype'),
    path('inform',views.inform,name='inform'),
    
]