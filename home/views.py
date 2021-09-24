from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from login.models import User
from home.models import *
from django.contrib.auth.decorators import login_required


#Funcion para validar la session en cada una de las views
def validate_session(session):
    if 'id' in session:
        return True
    else:
        return False

# Página de home
def home(request):
    if validate_session(request.session):
        reg_user = User.objects.get(id=request.session['id'])
        employees=Employee.objects.all()
        tools=Tool.objects.all()
        context = {
            'active_user': reg_user,
            'employees': employees,
            'tools': tools,
        }
        return render(request, 'home/home.html', context)
    else:
        return redirect('/')

@login_required
def create(request):
    return redirect('/home/')

@login_required
def read(request):
    return HttpResponse("read")

@login_required
def update(request):
    return redirect('/home/')

@login_required
def delete(request):
    return redirect('/home/')


def employees(request):
    if validate_session(request.session):
        employees=Employee.objects.all()
        context = {
            'employees': employees,
        }
        return render(request, 'home/employees.html', context)
    else:
        return redirect('/')


def tools(request):
    if validate_session(request.session):
        tools=Tool.objects.all()
        context = {
            'tools': tools,
        }
        return render(request, 'home/tools.html', context)
    else:
        return redirect('/')

#@login_required
def moves(request):
    if validate_session(request.session):
        tools=Tool.objects.all()
        moves=Move.objects.all().order_by('created_at')
        context = {
            'tools': tools,
            'moves':moves,
        }
        return render(request, 'home/moves.html', context)
    else:
        return redirect('/')


@login_required
def movetype(request):
    pass

@login_required
def inform(request):
    pass

#Utilizo el decorador para evitar que entre a las páginas sin estar logueado
#se debe cambiar en settings settings.LOGIN_URL='/' The URL or named URL pattern where requests are redirected 
# for login when using the login_required() decorator

#@login_required

# Controladores para CRUD de Empleados
def edit_employee(request,id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Employee.objects.filter(id=id).exists():
        employee = Employee.objects.get(id=id)
        return HttpResponse(f'Editando a Employee: {employee}')
    else:
        return redirect('/home/')

def delete_employee(request,id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Employee.objects.filter(id=id).exists():
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect('/home/employees')
    else:
        return redirect('/home/employees')

def view_employee(request,id):
    return HttpResponse(f"Vista de Empleado Detalles {id}")

def create_employee(request):
    return render(request, 'home/create_emp.html')

def employee_add(request):
    #employee = Employee.objects.create(name=request.POST[''])
    print(request.POST)
    return HttpResponse(f"Creado")

# Controladores para CRUD de Herramientas
def edit_tools(request,id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Tool.objects.filter(id=id).exists():
        tool = Tool.objects.get(id=id)
        return HttpResponse(f'Editando a Tools: {tool}')
    else:
        return redirect('/home/')

def delete_tools(request,id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Tool.objects.filter(id=id).exists():
        tool = Tool.objects.get(id=id)
        tool.delete()
        return redirect('/home/') 
    else:
        return redirect('/home/')

def create_tools(request):
    pass

def view_tools(request,id):
    return HttpResponse(f"Visualizar detalles de herramienta {id} ")

# Controladores para CRUD de Movimientos
def edit_moves(request,id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Move.objects.filter(id=id).exists():
        move = Move.objects.get(id=id)
        return HttpResponse(f'Editando a Moves: {move}')
    else:
        return redirect('/home/')

def delete_moves(request,id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Move.objects.filter(id=id).exists():
        move = Move.objects.get(id=id)
        move.delete()
        #Visualizar mensaje para indicar que fue efectiva la acción
        return redirect('/home/') 
    else:
        return redirect('/home/')

def create_moves(request):
    pass

def view_moves(request,id):
    return HttpResponse(f"Visualizar el movimiento {id} ")